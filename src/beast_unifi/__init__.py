"""UniFi API client library for Beastmaster framework."""

__version__ = "0.1.0"

# Lazy imports to avoid circular dependencies
def __getattr__(name: str):
    if name == "SiteManagerClient":
        from beast_unifi.api.site_manager import SiteManagerClient
        return SiteManagerClient
    elif name == "LocalControllerClient":
        from beast_unifi.api.local_controller import LocalControllerClient
        return LocalControllerClient
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = [
    "SiteManagerClient",
    "LocalControllerClient",
]

