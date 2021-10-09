var fs = require("fs")
var http = require("http");
var ip = require('ip')
var os = require("os")

function getuptime() {
  serverTime = os.uptime();

  return serverTime
}

function getCPUCores(){
const numOfCpus = os.cpus().length;
return numOfCpus;
}

function getTotalMemory(){
  totalMem = os.totalmem
  return totalMem
}

function getFreeMemory(){
  freeMem = os.freemem
  return freeMem;
}

var server = http.createServer(function (req, res) {
  if (req.url === "/") {
    res.writeHead(200, { "content-Type": "text/html" });
    fs.readFile("./public/index.html", "UTF-8", function (err, body) {
      res.writeHead(200, { "Content-Type": "text/html" });
      res.end(body);
    });
  }
  else if (req.url.match("/sysinfo")) {
    myHostname = os.hostname();
    html = `
          <!DOCTYPE html>
            <html>
              <head>
                <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostname}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${getuptime()}</p>
            <p>Total Memory: ${getTotalMemory()}</p>
            <p>Free Memory: ${getFreeMemory()}</p>
            <p>Number of CPUs: ${getCPUCores()}</p>
          </body>
          </html>`

    res.writeHead(200, { "Content-Type": "text/html" });
    res.end(html);
  }
  else {
    res.writeHead(404, { "Content-Type": "text/html" });
    res.end(`404 file not found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");