var util = require('util'),
    http = require('http'),    
    httpProxy = require('./node_modules/http-proxy/lib/node-http-proxy');

var httpServerPort = 3001;
var httpProxyServerPort = 3000;
var threshold = 1;
httpProxy.createServer(httpServerPort, 'localhost').listen(httpProxyServerPort);

//
// To simulate Shortest Job First scheduling policy
//

var requestPool = [],
    count = 0;

function compare (val1, val2) {
    if (val1.size > val2.size)
        return 1;
    else if (val1.size < val2.size)
        return -1;
    return 0;
    }

http.createServer(function (req, res) {
    requestPool.push({fn: function () {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Sample of Shortest Job First (SJF) strategy' + '\n' + 'Request size: ' + req.url);
    }, size: req.url.substring(1)});
  count += 1; 
  process.stdout.write('Requests received till now: ' + count + '\n');

  requestPool.sort(compare);

  if (requestPool.length > threshold) {
    while (requestPool.length) {
        requestPool.shift().fn();
        }
    }
}).listen(httpServerPort);

util.puts('http proxy server started on port ' + httpProxyServerPort);
util.puts('http server started on port ' + httpServerPort);
