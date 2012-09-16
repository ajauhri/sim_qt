var util = require('util'),
    http = require('http'),    
    httpProxy = require('./node_modules/http-proxy/lib/node-http-proxy');

var httpServerPort = 3001;
var httpProxyServerPort = 3000;
httpProxy.createServer(httpServerPort, 'localhost').listen(httpProxyServerPort);

//
// To simulate First Scheduled First Server scheduling policy
//

var requestPool = [],
    count = 0;

http.createServer(function (req, res) {
  requestPool.push(function () {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Sample of First Scheduled First Served(FSFS) strategy' + '\n' + 'Request size: ' + req.url);
  });
  count += 1; 
  process.stdout.write('Requests received till now: ' + count + '\n');
  
   while (requestPool.length) {
      requestPool.shift()();
    }
}).listen(httpServerPort);

util.puts('http proxy server started on port ' + httpProxyServerPort);
util.puts('http server started on port ' + httpServerPort);
