import tkinter as tk
import tkinter.filedialog
from os import replace
from pathlib import Path
from time import strftime
import logging


def find_all_suffixes(settings, whitelist, find_suffixes, swap_lists):
    """
    vstupnipromenna = Path(entry.get())
    if os.path.exists(vstupnipromenna):
        cesta = vstupnipromenna
    else:
        return"""
    path = Path(tk.filedialog.askdirectory())
    print(path)
    listcest = []
    allowed_suffixes = []
    zaznam = ""
    for child in path.iterdir():
        if (child.is_file()) and "zaznam programu FileSort" not in str(child) and ".py" not in str(child):
            zaznam += str(child)
            logging.info(str(child))
            if child.suffix not in listcest:
                listcest.append(child.suffix)
            slozka = f"{str(path)}\\{child.suffix}"
            cestaslozky = Path(slozka)
            try:
                if not (cestaslozky.exists()):
                    cestaslozky.mkdir()
            except Exception:
                print(Exception)
            cestanovehosouboru = str(Path(path)) + "\\" + str(child.suffix) + "\\" + str(child.stem)
            print(cestanovehosouboru)
            print(allowed_suffixes)
            settings.file_paths.append(cestanovehosouboru + child.suffix)
            settings.original_files.append(child)
            if child.suffix in allowed_suffixes:
                zaznam += "\n -> " + str(cestanovehosouboru) + str(child.suffix) + "\n\n"
                replace(str(child), str(cestanovehosouboru) + str(child.suffix))

    zaznamovysoubor = f'{str(path)}\\zaznam programu FileSort - {str(strftime("%Y-%m-%d, %H-%M-%S"))}.txt'
    try:
        with open(zaznamovysoubor, "wt") as file:
            file.write(zaznam)
            file.close()
    except Exception:
        print(Exception)
    whitelist.insert(tk.INSERT, ";".join(listcest))

    settings.whitelist = listcest
    settings.blacklist = []
    swap_lists.configure(state="active")
    print(listcest)
