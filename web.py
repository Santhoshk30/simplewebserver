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