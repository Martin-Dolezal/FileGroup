from tkinter import END
from pathlib import Path
import os
from time import strftime


def move(file_manager, whitelist, blacklist):
    file_manager.whitelist = whitelist.get("1.0", END)[:-1].split(";")
    file_manager.blacklist = blacklist.get("1.0", END)[:-1].split(";")
    index=1
    original_to_remove, new_to_remove = set(), set()
    zaznamovysoubor = f'{file_manager.path}\\zaznam programu FileSort - {str(strftime("%Y-%m-%d, %H-%M-%S"))}.txt'
    zaznam = ""
    for original, new in zip(file_manager.original_files, file_manager.file_paths):
        zaznam += str(original)
        zaznam += "\n -> " + str(new) + "\n\n"
        if Path(new).suffix in file_manager.whitelist and str(Path(new).suffix):
            if os.path.exists(new):
                while True:
                    current_suffix = Path(original).suffix
                    new_1 = str(new).split(str(Path(new).suffix))
                    new_path = str(f"{Path(new_1[0])}\\{current_suffix}{Path(new_1[1])}({index}){current_suffix}")
                    index += 1
                    if not os.path.exists(new_path):
                        index=1
                        break
            else:
                new_path = new
            original_to_remove.add(original)
            new_to_remove.add(new)

            os.replace(original, new_path)
    try:
        with open(zaznamovysoubor, "wt") as file:

            file.write(zaznam)
            file.close()
    except Exception:
        print(Exception)
    for original, new in zip(original_to_remove, new_to_remove):
        file_manager.original_files.remove(original)
        file_manager.file_paths.remove(new)
    print(file_manager.original_files)

