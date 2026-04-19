class ParsedFile:
    def __init__(self, file_name: str, adapters: list):
        self.file_name = file_name
        self.adapters = []
        for adapter in adapters:
            self.adapters.append(adapter.__dict__)
