#!/usr/bin/env python3
"""Basic example: Fetch UniFi data and display."""

from beast_unifi import SiteManagerClient
from beast_unifi.credentials import load_credentials_from_env


def main():
    """Example usage of UniFi API client."""
    # Load credentials from ~/.env
    creds = load_credentials_from_env()
    
    # Initialize client
    client = SiteManagerClient(api_key=creds.get('UNIFI_API_KEY'))
    
    # Fetch data
    print("Fetching UniFi data...")
    hosts = client.get_hosts()
    sites = client.get_sites()
    devices = client.get_devices()
    
    # Display summary
    print(f"\n✓ Found {len(hosts)} host(s)")
    print(f"✓ Found {len(sites)} site(s)")
    print(f"✓ Found {len(devices)} device(s)")
    
    # Display hosts
    if hosts:
        print("\nHosts:")
        for host in hosts:
            host_id = host.get('id', 'N/A')[:8]
            host_type = host.get('type', 'N/A')
            ip = host.get('ipAddress', 'N/A')
            print(f"  • {host_type} ({ip}) - ID: {host_id}...")


if __name__ == '__main__':
    main()

