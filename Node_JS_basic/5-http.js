const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
    const databasePath = process.argv[2];

    if(req.url === '/') {
        req.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end('Hello Holberton School!');
    } else if(req.url === '/students') {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');

        countStudents(databasePath)
            .then(() => {
                res.end('This is the list of our students\n');
            })
            .catch((err) => {
                res.end(err.message);
            });
    } else {
        res.statusCode = 404;
        res.end('Not found');
    }
});
app.listen(1245, () => {
    console.log('Server listening at port 1245');
});
module.exports = app;
