import requests

url = "http://localhost:8000/mcp"
headers = {
    "Accept": "application/json, text/event-stream",
}
body = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/list",
    "params": {}
}

response = requests.post(url, headers=headers, json=body, stream=True)

for line in response.iter_lines():
    if line:
        print(line.decode('utf-8'))

