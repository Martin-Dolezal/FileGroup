class FileManager:
    def __init__(self, whitelist: set, blacklist:set, path: str):
        self.whitelist = whitelist
        self.blacklist = blacklist
        self.file_paths = set()
        self.original_files = set()
        self.path = path