var http = require('http');
http.createServer(function (req, res) {
            res.end('Hello, World.');
            }).listen(8080, '127.0.0.1');
console.log('Server running at http://127.0.0.1:8080/');
