import requests
import json

from version import getVersion as gv 

# URL for IPv4 API (4.myip.is)
ipv4_url = 'https://4.myip.is/'

# URL for IPv6 API (6.myip.is)
ipv6_url = 'https://6.myip.is/'

# Method for calling and parsing JSON-data of given URL
def get_ip_info(url):
     """Calls the specified URL and parses the JSON data.

    Args:
        url (str): The URL to call.

    Returns:
        dict: Parsed JSON data.

    Raises:
        requests.RequestException: If an error occurs during the request.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            parsed_json = response.json()
            return parsed_json
        else:
            print(f"Error while getting Data. Statuscode: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error on request: {e}")
        print("Please check your internet connection.")

def nl(count):
    '''Prints specified number of new lines.
       You should use Integer Values.'''
    if count > 0:
        try:
            for i in range(count):
                print()
        except TypeError as e:
            print(f"{count} is not a valid value! Use integers!")
            print(f"Error: {e}")
            raise
    else:
        pass
    

#Welcome Message
print (f"Welcome to ipfetch, Version {gv()}")
nl(1)

# Getting and parsing Data of IPv4-API
ipv4_data = get_ip_info(ipv4_url)
if ipv4_data:
    print("IPv4")
    print("====")
    nl(1)
    print(f"IP-Adress  : {ipv4_data['ip']}")
    print(f"Host       : {ipv4_data['host']}")
    print(f"Timestamp  : {ipv4_data['timestamp']}")

# Getting and parsing Data of IPv6-API
ipv6_data = get_ip_info(ipv6_url)
if ipv6_data:
    nl(1)
    print("IPv6")
    print("====")
    nl(1)
    print(f"IP-Adress  : {ipv6_data['ip']}")
    print(f"Host       : {ipv6_data['host']}")
    print(f"Timestamp  : {ipv6_data['timestamp']}")
