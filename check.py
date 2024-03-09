import requests 
import os
import subprocess
import time



bareer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im14dGZka3BweHlmbG1tZ2x1bGxmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDgwNDI1ODEsImV4cCI6MjAyMzYxODU4MX0.mNkDiJaCBB5twRNypzThEKl-s8d5VjasNyJj1l9BK9o"
auth_url = "https://id.io.net/auth/v1/token?grant_type=refresh_token"
api = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im14dGZka3BweHlmbG1tZ2x1bGxmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDgwNDI1ODEsImV4cCI6MjAyMzYxODU4MX0.mNkDiJaCBB5twRNypzThEKl-s8d5VjasNyJj1l9BK9o"
acces_token = "eyJhbGciOiJIUzI1NiIsImtpZCI6IlNFUGRXMkpHWXlzc0ZqU3ciLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzA5OTg0OTAwLCJpYXQiOjE3MDk5ODEzMDAsImlzcyI6Imh0dHBzOi8vbXh0ZmRrcHB4eWZsbW1nbHVsbGYuc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6ImMxZTZjZDNhLTNhNjktNGYxOS04Yjc3LWMyYWQ2NWFlNDc4NCIsImVtYWlsIjoibWVybGluMjI4bW9yZG9yQGdtYWlsLmNvbSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZ29vZ2xlIiwicHJvdmlkZXJzIjpbImdvb2dsZSJdfSwidXNlcl9tZXRhZGF0YSI6eyJhdmF0YXJfdXJsIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jSXV4bklVNXN2SGhxdFBJRzFSVHAtRkZQNTBENGpmazhhT0ViZW50RDgxNVE9czk2LWMiLCJlbWFpbCI6Im1lcmxpbjIyOG1vcmRvckBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZnVsbF9uYW1lIjoiZGF6YXkiLCJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYW1lIjoiZGF6YXkiLCJwaG9uZV92ZXJpZmllZCI6ZmFsc2UsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NJdXhuSVU1c3ZIaHF0UElHMVJUcC1GRlA1MEQ0amZrOGFPRWJlbnREODE1UT1zOTYtYyIsInByb3ZpZGVyX2lkIjoiMTEyMTg1NzQ0MTU1MDI5MTczODUxIiwic3ViIjoiMTEyMTg1NzQ0MTU1MDI5MTczODUxIn0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoib2F1dGgiLCJ0aW1lc3RhbXAiOjE3MDk3OTcxNzh9XSwic2Vzc2lvbl9pZCI6IjEzMzMzMDU5LTZmMmItNDFmNy05MjRlLWEyNjU0NTA0MGU0MyJ9.8MkZ4WVfSpzlM7QdKl6rMdjCnUmJwQ-5G4kIgsbKkMo"
def access_token():
    response = requests.post(auth_url, headers={
        "Authorization": "Bearer" + f"{bareer_token}",
        "Apikey": f"{api}"
    })
    data = response.json()
    
    return data


def check(delay = 2):
    time.sleep(delay)
    url = "https://production.io.systems/v1/io-worker/devices/16d63c38-4270-405d-ad5a-1ff73f305d9a/details"
    response = requests.get(url, headers={"Token": acc})

    data = response.json()
    status = data.get("data").get("status")
    if status == "up":
        return True


    else:
            return False
    return data    
        
def main():   
    
    if check():
        pass
    else:
        command = "./launch_binary_linux --device_id=16d63c38-4270-405d-ad5a-1ff73f305d9a --user_id=c1e6cd3a-3a69-4f19-8b77-c2ad65ae4784 --operating_system=Linux --usegpus=false --device_name=worker"
        result = subprocess.run(command, shell=True)
        print(result)




if __name__ == "__main__":
    main()