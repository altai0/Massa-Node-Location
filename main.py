import requests
import json
from beautifultable import BeautifulTable

# It shows the locations and other information of the nodes your node is connected to.
# Port 33035 needs to be open.

headers = {
    'Content-type': 'application/json',
}
nodeIp = 'http://141.94.218.103:33035/'
response = requests.post(nodeIp,
                         headers=headers, data='{"jsonrpc": "2.0", "method": "get_status", "id": 123 }')
data = response.json()

network_stats = data["result"]["network_stats"]
connected_nodes = data["result"]["connected_nodes"]
location = []

for node in connected_nodes:
    strChange = connected_nodes[node].split(':')
    ipUrl = f"https://ipinfo.io/{strChange[-1]}/json"
    res = requests.get(ipUrl)
    data = res.json()
    item = {
        "ip": strChange[-1],
        "country": data["country"],
        "provider": data["org"],
        "city": data["city"],
        "node_id": node
    }
    location.append(item)


table = BeautifulTable()
table.columns.header = ["country", "provider", "city", "node_id", "ip"]

for loc in location:
    table.rows.append([loc["country"], loc["provider"],
                      loc["city"], loc["node_id"], loc["ip"]])

print(table)

with open('sonuc.txt', 'w') as w:
    w.write(str(table))
