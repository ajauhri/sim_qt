require('events').EventEmitter

var http = require('http');
server = http.createServer(function (req, res) {
      res.writeHead(200, {'Content-Type': 'text/plain'});
        now = new Date().getTime();  
        //while(new Date().getTime() < now + 5000) {    } 
        res.end('Welcome to Performance Modeling!\n');
        console.log('Request came ' + new Date() + req.url);
        }).listen(3000, '127.0.0.1');
console.log('Server running at http://127.0.0.1:3000/');


server.on('connection', function (stream) {
      console.log('someone connected!');
    
});

