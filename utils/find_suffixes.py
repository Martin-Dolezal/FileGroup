import logging
import tkinter as tk
import tkinter.filedialog
from pathlib import Path
from tkinter import END


def find_all_suffixes(file_manager, whitelist, blacklist, swap_lists):
    path = Path(tk.filedialog.askdirectory())
    file_manager.path = str(path)
    print(path)
    suffixes = set()
    allowed_suffixes = []
    file_record = ""
    for child in path.iterdir():
        if (child.is_file()) and "zaznam programu FileSort" not in str(child) and ".py" not in str(child):
            file_record += str(child)
            logging.info(str(child))
            if child.suffix:
                suffixes.add(child.suffix)
            directory_path = Path(f"{str(path)}\\{child.suffix}")
            try:
                if not (directory_path.exists()):
                    directory_path.mkdir()
            except Exception:
                print(Exception)
            new_file_path = str(Path(path)) + "\\" + str(child.suffix) + "\\" + str(child.stem)
            print(new_file_path)
            print(allowed_suffixes)
            file_manager.file_paths.add(new_file_path + child.suffix)
            file_manager.original_files.add(child)
    whitelist.delete("1.0", END)
    whitelist.insert(tk.INSERT, ";".join(suffixes))

    file_manager.whitelist = suffixes
    file_manager.blacklist = {}
    swap_lists.configure(state="active")
    blacklist.delete("1.0", END)
