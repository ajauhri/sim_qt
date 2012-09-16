var util = require('util'),
    http = require('http'),    
    httpProxy = require('./node_modules/http-proxy/lib/node-http-proxy');

var httpServerPort = 3001;
var httpProxyServerPort = 3000;
httpProxy.createServer(httpServerPort, 'localhost').listen(httpProxyServerPort);

//
// Target Http Server
//
// to check apparent problems with concurrent connections
// make a server which only responds when there is a given nubmer on connections
//


var connections = [],
    count = 0;

http.createServer(function (req, res) {
  connections.push(function () {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Sample of First Scheduled First Served(FSFS) strategy' + '\n' + 'Request size: ' + req.url);
  });
   
  process.stdout.write('Connections received till now: ' + count);
  
   while (connections.length) {
      connections.shift()();
    }
}).listen(httpProxyServerPort);

util.puts('http proxy server'+ ' started '+ 'on port '+ httpProxyServerPort);
util.puts('http server '+ 'started '+ 'on port '+ httpServerPort);
