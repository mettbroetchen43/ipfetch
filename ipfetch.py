import requests
import json

# URL für die IPv4 API (4.myip.is)
ipv4_url = 'https://4.myip.is/'

# URL für die IPv6 API (6.myip.is)
ipv6_url = 'https://6.myip.is/'

# Funktion zum Abrufen und Parsen der JSON-Daten von der URL
def get_ip_info(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            parsed_json = response.json()
            return parsed_json
        else:
            print(f"Fehler beim Abrufen der Daten. Statuscode: {response.status_code}")
    except requests.RequestException as e:
        print(f"Fehler bei der Anfrage: {e}")

def nl():
    print()

# Abrufen und Parsen der Daten von der IPv4-API
ipv4_data = get_ip_info(ipv4_url)
if ipv4_data:
    print("Daten von IPv4-API")
    print("==================")
    nl()
    print(f"IP-Adresse : {ipv4_data['ip']}")
    print(f"Host       : {ipv4_data['host']}")
    print(f"Timestamp  : {ipv4_data['timestamp']}")

# Abrufen und Parsen der Daten von der IPv6-API
ipv6_data = get_ip_info(ipv6_url)
if ipv6_data:
    nl()
    print("Daten von IPv6-API")
    print("==================")
    nl()
    print(f"IP-Adresse : {ipv6_data['ip']}")
    print(f"Host       : {ipv6_data['host']}")
    print(f"Timestamp  : {ipv6_data['timestamp']}")
