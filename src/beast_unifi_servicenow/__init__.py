"""ServiceNow integration for UniFi network data."""

__version__ = "0.1.0"

# Lazy imports
def __getattr__(name: str):
    if name == "UniFiServiceNowSync":
        from beast_unifi_servicenow.integration.unifi_sync import UniFiServiceNowSync
        return UniFiServiceNowSync
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = [
    "UniFiServiceNowSync",
]

