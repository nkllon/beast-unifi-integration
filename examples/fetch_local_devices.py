#!/usr/bin/env python3
"""Fetch all devices and clients from local UniFi controller."""

import sys
from pathlib import Path

# Add src to path for development
sys.path.insert(0, str(Path(__file__).parent.parent))

from beast_unifi.api.local_controller import LocalControllerClient
from beast_unifi.credentials import load_credentials_from_env, load_credentials_from_1password
import pandas as pd


def main():
    """Fetch devices and clients from local controller."""
    print("="*70)
    print("FETCHING DEVICES & CLIENTS FROM LOCAL CONTROLLER")
    print("="*70)
    
    # Load credentials
    print("\n1. Loading credentials...")
    
    # Try 1Password first
    creds = load_credentials_from_1password(vault_name="Beastmaster")
    
    # Fall back to env
    if not creds.get('UNIFI_LOCAL_TOKEN'):
        env_creds = load_credentials_from_env()
        creds.update(env_creds)
    
    local_token = creds.get('UNIFI_LOCAL_TOKEN')
    
    if not local_token:
        print("❌ UNIFI_LOCAL_TOKEN not found!")
        print("\n💡 To get device/client data:")
        print("   1. Create API token in UniFi OS:")
        print("      • Log in at https://192.168.1.1")
        print("      • Settings → API Tokens")
        print("      • Create new token")
        print("   2. Add to ~/.env as UNIFI_LOCAL_TOKEN=your_token")
        print("      OR add to 1Password Beastmaster vault")
        return
    
    print(f"  ✓ Local API token found ({len(local_token)} chars)")
    
    # Connect to local controller
    print("\n2. Connecting to local controller...")
    
    # Try common IPs
    base_urls = [
        "https://192.168.1.1:443",
        "https://10.0.0.1:443",
        "http://192.168.1.1:8080",
    ]
    
    client = None
    for base_url in base_urls:
        try:
            print(f"   Trying {base_url}...")
            client = LocalControllerClient(
                base_url=base_url,
                api_token=local_token,
                site="default"
            )
            # Test connection
            sites = client.get_sites()
            if sites:
                print(f"  ✓ Connected to {base_url}")
                print(f"  ✓ Found {len(sites)} site(s)")
                break
        except Exception as e:
            print(f"  ✗ Failed: {e}")
            continue
    
    if not client:
        print("\n❌ Could not connect to local controller")
        print("   Check that:")
        print("   • Controller is accessible")
        print("   • API token is valid")
        print("   • Token has correct permissions")
        return
    
    # Fetch devices
    print("\n3. Fetching UniFi devices (APs, switches, etc.)...")
    try:
        devices = client.get_devices()
        print(f"  ✓ Found {len(devices)} device(s)")
        
        if devices:
            print("\n   Devices:")
            for device in devices[:10]:
                name = device.get('name', 'Unknown')
                model = device.get('model', 'N/A')
                ip = device.get('ip', 'N/A')
                mac = device.get('mac', 'N/A')
                print(f"     • {name} ({model}) - IP: {ip}, MAC: {mac}")
            
            if len(devices) > 10:
                print(f"\n     ... and {len(devices) - 10} more devices")
    except Exception as e:
        print(f"  ✗ Error fetching devices: {e}")
        devices = []
    
    # Fetch clients
    print("\n4. Fetching connected clients (thermostats, TVs, computers, etc.)...")
    try:
        clients = client.get_clients()
        print(f"  ✓ Found {len(clients)} client(s)")
        
        if clients:
            print("\n   Clients:")
            for client_data in clients[:20]:
                hostname = client_data.get('hostname', 'Unknown')
                ip = client_data.get('ip', 'N/A')
                mac = client_data.get('mac', 'N/A')
                device_type = client_data.get('device_type', 'N/A')
                essid = client_data.get('essid', 'N/A')
                
                # Show interesting devices
                if any(keyword in hostname.lower() for keyword in ['thermostat', 'tv', 'tv-', 'computer', 'pc', 'laptop', 'iphone', 'ipad']):
                    print(f"     ⭐ {hostname} ({device_type}) - IP: {ip}")
                else:
                    print(f"     • {hostname} ({device_type}) - IP: {ip}")
            
            if len(clients) > 20:
                print(f"\n     ... and {len(clients) - 20} more clients")
    except Exception as e:
        print(f"  ✗ Error fetching clients: {e}")
        clients = []
    
    # Create DataFrames and save
    if devices or clients:
        print("\n5. Saving data...")
        output_dir = Path("unifi_local_data")
        output_dir.mkdir(exist_ok=True)
        
        if devices:
            df_devices = pd.DataFrame(devices)
            devices_file = output_dir / "devices.csv"
            df_devices.to_csv(devices_file, index=False)
            print(f"  ✓ Saved {len(devices)} devices to {devices_file}")
        
        if clients:
            df_clients = pd.DataFrame(clients)
            clients_file = output_dir / "clients.csv"
            df_clients.to_csv(clients_file, index=False)
            print(f"  ✓ Saved {len(clients)} clients to {clients_file}")
    
    print("\n" + "="*70)
    print("✅ Complete!")
    if devices:
        print(f"   • UniFi devices: {len(devices)}")
    if clients:
        print(f"   • Network clients: {len(clients)}")
    print("="*70)


if __name__ == '__main__':
    main()

