# Requirements: UniFi API Client

**Feature:** unifi-api-client  
**Status:** Delivered  
**Created:** 2025-11-03

## Requirements (EARS Format)

### WHEN the user initializes SiteManagerClient THEN the system SHALL authenticate using Site Manager API key.

**Rationale:** Cloud API requires API key authentication.

**Acceptance:**
- Client accepts API key via constructor parameter
- Falls back to `UNIFI_API_KEY` environment variable
- Raises `ValueError` if no key provided

---

### WHEN the user calls `get_hosts()` THEN the system SHALL return list of gateway devices.

**Rationale:** Site Manager API provides gateway/host devices (limited devices).

**Acceptance:**
- Returns list of dictionaries with host data
- Handles API errors appropriately
- Returns empty list if no hosts found

---

### WHEN the user calls `get_sites()` THEN the system SHALL return list of UniFi sites.

**Rationale:** Sites are organizational units in UniFi.

**Acceptance:**
- Returns list of site dictionaries
- Includes site metadata (name, id, etc.)

---

### WHEN the user calls `get_devices()` THEN the system SHALL return list of UniFi devices.

**Rationale:** Devices are network equipment managed by UniFi.

**Acceptance:**
- Returns list of device dictionaries
- Includes device metadata (model, MAC, IP, etc.)

---

### WHEN the user initializes LocalControllerClient THEN the system SHALL authenticate using Local API token.

**Rationale:** Local controllers require API token (2FA required for UniFi OS).

**Acceptance:**
- Client accepts base_url, api_token, site, verify_ssl parameters
- Falls back to `UNIFI_LOCAL_TOKEN` environment variable
- Raises `ValueError` with helpful message if token missing
- Disables SSL verification by default (for local self-signed certs)

---

### WHEN the user calls local client `get_devices()` THEN the system SHALL return all network devices.

**Rationale:** Local API provides comprehensive device data (more than Site Manager).

**Acceptance:**
- Returns list of all network devices
- Includes access points, switches, gateways, clients
- More comprehensive than Site Manager API

---

### WHEN the user calls local client `get_clients()` THEN the system SHALL return all network clients.

**Rationale:** Local API provides client device data (thermostats, TVs, computers, phones).

**Acceptance:**
- Returns list of client devices
- Includes hostname, IP, MAC address
- Supports discovery of interesting devices (thermostats, TVs, etc.)

---

### IF API request fails THEN the system SHALL raise appropriate exception with error details.

**Rationale:** Clear error handling improves debugging.

**Acceptance:**
- HTTP errors raise `requests.HTTPError`
- Network errors raise `requests.RequestException`
- Includes error details in exception message

---

### WHERE credentials are needed THEN the system SHALL support 1Password CLI and environment variable fallback.

**Rationale:** Secure credential management without hardcoding.

**Acceptance:**
- Tries 1Password CLI first (Beastmaster vault)
- Falls back to environment variables (~/.env)
- Never hardcodes credentials in code

