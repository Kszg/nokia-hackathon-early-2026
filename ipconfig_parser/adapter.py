class Adapter:
    PROPERTY_NAMES = {
        "Description": "description",
        "Physical Address": "physical_address",
        "DHCP Enabled": "dhcp_enabled",
        "IPv4 Address": "ipv4_address",
        "Subnet Mask": "subnet_mask",
        "Default Gateway": "default_gateway",
        "DNS Servers": "dns_servers"
    }

    def __init__(self,
                 adapter_name: str = "",
                 description: str = "",
                 physical_address: str = "",
                 dhcp_enabled: str = "",
                 ipv4_address: str = "",
                 subnet_mask: str = "",
                 default_gateway: str = "",
                 dns_servers: list[str] = []):
        self.adapter_name = adapter_name
        self.description = description
        self.physical_address = physical_address
        self.dhcp_enabled = dhcp_enabled
        self.ipv4_address = ipv4_address
        self.subnet_mask = subnet_mask
        self.default_gateway = default_gateway
        self.dns_servers = dns_servers

    def to_dict():
        return {
            
        }
