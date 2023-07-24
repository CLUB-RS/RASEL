import requests

def get_ip_info(ip_address):
    api_url = f"https://ipinfo.io/{ip_address}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        ip_data = response.json()
        return ip_data
    else:
        print(f"Failed to fetch data for IP: {ip_address}")
        return None

if __name__ == "__main__":
    ip_address = input("Enter an IP address: ")
    ip_info = get_ip_info(ip_address)

    if ip_info:
        print("IP Information:")
        print(f"IP Address: {ip_info.get('ip')}")
        print(f"Hostname: {ip_info.get('hostname')}")
        print(f"City: {ip_info.get('city')}")
        print(f"Region: {ip_info.get('region')}")
        print(f"Country: {ip_info.get('country')}")
        print(f"Postal Code: {ip_info.get('postal')}")
        print(f"Location: {ip_info.get('loc')}")
    else:
        print("No information available.")
