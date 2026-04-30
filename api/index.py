import os
from http.server import BaseHTTPRequestHandler
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Start a session to handle cookies automatically
        session = requests.Session()
        
        # 2. Get credentials from secure environment variables defined in Vercel
        username = os.environ.get("PORTAL_USER")
        password = os.environ.get("PORTAL_PASS")
        
        # 3. Perform login
        # NOTE: Check your portal's HTML "name" attributes if login fails.
        # These keys (txtUserName, txtPassword, btnLogin) must match the portal's form inputs.
        login_url = "http://fgtbanas.fortiddns.com:8080/OnlineOrder/Login.aspx"
        payload = {
            "txtUserName": username,
            "txtPassword": password,
            "btnLogin": "Login"
        }
        
        try:
            # Send login request
            session.post(login_url, data=payload)
            
            # 4. Fetch the target page after login
            # Once logged in, the session keeps your cookies/login state.
            invoice_url = "http://fgtbanas.fortiddns.com:8080/OnlineOrder/Invoice.aspx?FromDate=01/04/2026&ToDate=29/04/2026"
            resp = session.get(invoice_url)
            
            # 5. Return the result to your browser
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(resp.text.encode())
            
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Error: {str(e)}".encode())