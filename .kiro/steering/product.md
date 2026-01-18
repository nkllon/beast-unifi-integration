# Product Vision: beast-unifi-integration

**Project:** beast-unifi-integration  
**Purpose:** Demonstration project showcasing Beastmaster framework integration with ServiceNow for network infrastructure management  
**Status:** Active development

## Product Overview

beast-unifi-integration provides a Python-based integration between UniFi network controllers and ServiceNow CMDB, enabling automated discovery and synchronization of network infrastructure data.

## Core Value Propositions

1. **Network Discovery:** Automatically discover and catalog UniFi network devices, sites, and clients
2. **ServiceNow Integration:** Sync network data to ServiceNow CMDB via MID server
3. **Automated Credentials:** Secure credential management via 1Password integration
4. **Local + Cloud API Support:** Support both UniFi Site Manager (cloud) and Local Controller APIs

## Target Users

- **Network Administrators:** Need visibility into UniFi network infrastructure
- **ServiceNow Administrators:** Want to populate CMDB with network device data
- **DevOps Engineers:** Need programmatic access to network data

## Key Features (Delivered)

1. **UniFi API Clients**
   - Site Manager API client (cloud/remote)
   - Local Controller API client (on-premises)

2. **Credential Management**
   - 1Password CLI integration
   - Environment variable fallback
   - Secure token storage

3. **ServiceNow Integration Framework**
   - MID server Docker configuration
   - Data transformation pipeline
   - Sync orchestration (partial)

4. **Discovery & Analysis Tools**
   - Jupyter notebooks for API exploration
   - Data analysis and schema inference
   - Automated token setup

## Product Principles

- **Security First:** Credentials never in code, always via 1Password or env vars
- **Portable:** Works with both cloud and on-premises UniFi deployments
- **Demonstration Quality:** Clean, documented code showcasing Beastmaster patterns

