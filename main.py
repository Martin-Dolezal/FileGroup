import tkinter as tk
import tkinter.filedialog
from os import replace
from pathlib import Path
from time import strftime
from tkinter import ttk
import tkinter.simpledialog
import docx
import os
from tkinter import messagebox
import logging
from settings import FileSortSettings
from tkinter import END

settings = FileSortSettings([],[])
def find_all_suffixes():
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
            print (allowed_suffixes)
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
    global settings
    settings = FileSortSettings(whitelist=listcest, blacklist=[])
    swap_lists.configure(state="active")
    spustit.configure(state="disabled")
    print(listcest)



logging.basicConfig(filename="filegroup.log", format='%(levelname)s:%(message)s', level=logging.INFO)
window = tk.Tk()
window.title("FileSort")
mainframe = ttk.Frame(window, padding="10 10 10 10")

mainframe.grid(column=0, row=0, sticky="N, W, E, S")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
def swap():
    print(settings.whitelist)
    print(settings.blacklist)
    suffix_whitelist = settings.whitelist
    suffix_blacklist = settings.blacklist
    settings.whitelist = suffix_blacklist
    settings.blacklist = suffix_whitelist
    whitelist.replace(1.0, END, ";".join(settings.whitelist))
    blacklist.replace(1.0, END, ";".join(settings.blacklist))

spustit = tk.Button(mainframe, text="Najít koncovky souborů ve složce", command=find_all_suffixes, height=3)
spustit.grid(column=3, row=0)
whitelist = tk.Text(mainframe, width=100, height=3)
whitelist.grid(column=0, row=0, columnspan=2)
blacklist = tk.Text(mainframe, width=100, height=3)
blacklist.grid(column=0, row=1, columnspan=2)
swap_lists = tk.Button(mainframe, width=110, height=3, text="Swap", state="disabled", command=swap)
swap_lists.grid(column=0, row=2)
allow: bool = True




window.mainloop()
