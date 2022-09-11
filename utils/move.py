import os
from pathlib import Path
from time import strftime
from tkinter import END


def move(file_manager, whitelist, blacklist):
    file_manager.whitelist = whitelist.get("1.0", END)[:-1].split(";")
    file_manager.blacklist = blacklist.get("1.0", END)[:-1].split(";")
    index = 1
    original_to_remove, new_to_remove = set(), set()
    record_file = f'{file_manager.path}\\zaznam programu FileSort - {str(strftime("%Y-%m-%d, %H-%M-%S"))}.txt'
    record = ""
    for original, new in zip(file_manager.original_files, file_manager.file_paths):
        record += str(original)
        record += f"\n -> {str(new)}\n\n"
        if Path(new).suffix in file_manager.whitelist and str(Path(new).suffix):
            if os.path.exists(new):
                while True:
                    current_suffix = Path(original).suffix
                    new_1 = str(new).split(str(Path(new).suffix))
                    new_path = str(f"{Path(new_1[0])}\\{current_suffix}{Path(new_1[1])}({index}){current_suffix}")
                    index += 1
                    if not os.path.exists(new_path):
                        index = 1
                        break
            else:
                new_path = new
            original_to_remove.add(original)
            new_to_remove.add(new)

            os.replace(original, new_path)
    try:
        with open(record_file, "wt") as file:

            file.write(record)
            file.close()
    except Exception:
        print(Exception)
    for original, new in zip(original_to_remove, new_to_remove):
        file_manager.original_files.remove(original)
        file_manager.file_paths.remove(new)
    print(file_manager.original_files)
