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
    res.write('Job id:' + count + '\n');
    setTimeout(function() {
         res.end('Job ended\n');
         count -= 1;
         process.stdout.write(count +'\n');
    }, 2000);
  });
  count += 1; 
  process.stdout.write('Requests active now: ' + count + '\n');
  
   while (requestPool.length) {
      requestPool.shift()();
    }
}).listen(httpServerPort);

util.puts('http proxy server started on port ' + httpProxyServerPort);
util.puts('http server started on port ' + httpServerPort);

