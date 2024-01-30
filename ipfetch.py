import requests
from os import system, name
from version import getVersion as gv
import json


# URLs for IPv4 and IPv6 APIs
ipv4_url = 'https://4.myip.is/'
ipv6_url = 'https://6.myip.is/'

def clear_screen():
    '''Clears the screen.'''
    if name == "nt":
        _ = system("cls")
    elif name == "posix":
        _ = system("clear")

def get_ip_info(url):
    '''Calls the specified URL and parses the JSON data.

    Args:
        url (str): The URL to call.

    Returns:
        dict: Parsed JSON data.

    Raises:
        requests.RequestException: If an error occurs during the request.
    '''
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error on request: {e}")
        print("Please check your internet connection.")

def print_ip_info(ip_data, protocol):
    '''Prints IP information.'''
    nl(1)
    print(f"IPv{protocol}")
    print("=" * 4)
    nl(1)
    print(f"IP-Address   : {ip_data['ip']}")
    print(f"Host         : {ip_data['host']}")
    print(f"Timestamp    : {ip_data['timestamp']}")

def nl(count):
    '''Prints specified number of new lines.'''
    if count > 0:
        try:
            for _ in range(count):
                print()
        except TypeError as e:
            print(f"{count} is not a valid value! Use integers!")
            print(f"Error: {e}")
            raise

def main():
    clear_screen()
    # Welcome Message
    print(f"Welcome to ipfetch, Version {gv()}")
    nl(1)

    # Getting and parsing Data of IPv4-API
    ipv4_data = get_ip_info(ipv4_url)
    if ipv4_data:
        print_ip_info(ipv4_data, 4)

    # Getting and parsing Data of IPv6-API
    ipv6_data = get_ip_info(ipv6_url)
    if ipv6_data:
        print_ip_info(ipv6_data, 6)

if __name__ == "__main__":
    main()