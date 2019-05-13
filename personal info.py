import json
import socket
import getpass
from urllib.request import urlopen
username = getpass.getuser()
print("\n username : ", username)
hostname = socket.gethostname()
print("\n hostname : ", hostname)
machineIP = socket.gethostbyname(hostname)
print("\n IP address : ", machineIP)
url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

print("\n public IP : ",data['ip'])
print("\n city : ", data['city'])
print("\n state : ", data['region'])
print("\n country : ", data['country'])
