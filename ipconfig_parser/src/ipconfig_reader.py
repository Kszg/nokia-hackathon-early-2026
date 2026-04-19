from .models.adapter import Adapter

class IpConfigReader:
    @staticmethod
    def get_adapters(input_lines: list[str]) -> list[Adapter]:
        adapters = []
        current_adapter = None
        current_list_property_name = None

        for line in input_lines:
            line_stripped = line.strip()

            if (len(line_stripped) == 0): continue

            is_name_line = not line.startswith(("   ", "\t"))
            if (is_name_line):
                current_list_property_name = None

                if (current_adapter is not None): adapters.append(current_adapter)

                name = line.strip().removesuffix(":")
                if (name == "Windows IP Configuration"): continue

                current_adapter = Adapter(adapter_name=name, dns_servers=[])
            else:
                property = IpConfigReader.get_adapter_property(line)

                is_kvp = (property is not None)
                if (is_kvp):
                    current_list_property_name = None

                    if (property[0] in Adapter.PROPERTY_NAMES):
                        var_name = Adapter.PROPERTY_NAMES[property[0]]

                        if (isinstance(getattr(current_adapter, var_name), list)):
                            current_list_property_name = var_name
                            getattr(current_adapter, var_name).append(property[1])
                        else:
                            setattr(current_adapter, Adapter.PROPERTY_NAMES[property[0]], property[1])
                elif (current_list_property_name is not None):
                    getattr(current_adapter, current_list_property_name).append(line.strip())

        adapters.append(current_adapter)
        return adapters

    @staticmethod
    def get_adapter_property(line: str) -> tuple[str, str]:
        line_data = line.strip().split(": ", 1)
        
        if (len(line_data) < 2): return None

        key = line_data[0].strip(" \t.")
        value = line_data[1].strip()

        return key, value