class FileManager:
    def __init__(self, whitelist: list, blacklist:list):
        self.whitelist = whitelist
        self.blacklist = blacklist
        self.file_paths = []
        self.original_files = []