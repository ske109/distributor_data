import requests
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        session = requests.Session()
        
        # 1. Login (Replace these field names with what you find in your portal's Inspect Element)
        login_url = "http://fgtbanas.fortiddns.com:8080/OnlineOrder/Login.aspx"
        payload = {
            "txtUserName": "YOUR_USERNAME",  # Replace with actual field name
            "txtPassword": "YOUR_PASSWORD",  # Replace with actual field name
            "btnLogin": "Login"              # Replace with button name/value
        }
        session.post(login_url, data=payload)
        
        # 2. Fetch the invoices
        invoice_url = "http://fgtbanas.fortiddns.com:8080/OnlineOrder/Invoice.aspx?FromDate=01/04/2026&ToDate=29/04/2026"
        resp = session.get(invoice_url)
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(resp.text.encode())
