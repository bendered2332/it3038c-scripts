var fs = require("fs")
var http = require("http");
var ip = require('ip')
var os = require("os")

function getuptime() {
  serverTime = os.uptime();
    var d = Math.floor(serverTime / (3600*24));
    var h = Math.floor(serverTime % (3600*24) / 3600);
    var m = Math.floor(serverTime % 3600 / 60);
    var s = Math.floor(serverTime % 60);

    var dDisplay = d > 0 ? d + (d == 1 ? " day, " : " days, ") : "";
    var hDisplay = h > 0 ? h + (h == 1 ? " hour, " : " hours, ") : "";
    var mDisplay = m > 0 ? m + (m == 1 ? " minute, " : " minutes, ") : "";
    var sDisplay = s > 0 ? s + (s == 1 ? " second" : " seconds") : "";
      return dDisplay + hDisplay + mDisplay + sDisplay;
}

function getCPUCores(){
const numOfCpus = os.cpus().length;
return numOfCpus;
}

function getTotalMemory(){
  totalMem = os.totalmem
  totalMBMem = totalMem / 1000000;
  var totalMBDisplay = totalMBMem + "MB";
  return totalMBDisplay
}

function getFreeMemory(){
  freeMem = os.freemem
  freeMBMem = freeMem / 1000000;
  var freeMBDisplay = freeMBMem + "MB"
  return freeMBDisplay;
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