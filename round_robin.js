var httpProxy = require('./node_modules/http-proxy/lib/node-http-proxy');

var addresses = [
  {
    host: 'localhost',
    port: 3001 
  }];

httpProxy.createServer(function (req, res, proxy) {
  var target = addresses.shift();

  //
  // ...then proxy to the server whose 'turn' it is...
  //
  console.log('balancing request to: ', target);
  proxy.proxyRequest(req, res, target);

  //
  // ...and then the server you just used becomes the last item in the list.
  //
  addresses.push(target);
}).listen(3000);

// Rinse; repeat; enjoy.

