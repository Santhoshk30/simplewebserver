# EX01 Developing a Simple Webserver
## Date:28.09.2026

## AIM:
To develop a simple webserver to serve html pages and display the Windows Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
web.py
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<body>

<h2>SANTHOSH K (26016599)</h2>

<h3>Laptop Configuration</h3>

<table border="1">
    <tr>
        <th>Specification</th>
        <th>Details</th>
    </tr>

    <tr>
        <td>Device Name</td>
        <td>Santhosh</td>
    </tr>

    <tr>
        <td>Processor</td>
        <td>Intel Core 5 210H (2.20 GHz)</td>
    </tr>

    <tr>
        <td>RAM</td>
        <td>16 GB (15.7 GB usable)</td>
    </tr>

    <tr>
        <td>Graphics Card</td>
        <td>Intel Graphics (128 MB)</td>
    </tr>

    <tr>
        <td>Storage</td>
        <td>112 GB of 477 GB used</td>
    </tr>

    <tr>
        <td>System Type</td>
        <td>64-bit OS, x64-based processor</td>
    </tr>

    <tr>
        <td>Pen & Touch</td>
        <td>No pen or touch input</td>
    </tr>

</table>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()
```

## OUTPUT:
Webpage
![alt text](image.png)
Server page
![alt text](image-1.png)
## RESULT:
The program for implementing simple webserver is executed successfully.
