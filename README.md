# Cloud_LFI

 Python script that allows you to scan IP addresses within specific subnets of popular cloud providers (AWS, Azure, and GCP) for Local File Inclusion (LFI) vulnerabilities. It sends GET requests to each IP address and checks if the response contains the string "root:".
Features

    Select a cloud provider (AWS, Azure, or GCP).
    Get the subnets associated with the selected cloud provider.
    Perform LFI vulnerability scanning on each IP address within the subnets.
    Save the IP addresses with the "root:" string in the response to a file.

Prerequisites

    Python 3.x
    requests library (Install using pip install requests)

Usage

    Run the script: python cloud_lfi.py
    Select the cloud provider.
    The script will scan each IP address within the selected cloud provider's subnets.
    The IP addresses with the "root:" string in the response will be saved to a file named matching_ips_<cloud_provider>.txt.
