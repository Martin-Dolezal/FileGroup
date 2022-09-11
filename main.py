import logging
import tkinter as tk
from tkinter import END
from tkinter import ttk

from utils.find_suffixes import find_all_suffixes
from utils.group import group_files
from utils.move import move
from utils.settings import FileManager

file_manager = FileManager(set(), set(), "")
logging.basicConfig(filename="filegroup.log", format='%(levelname)s:%(message)s', level=logging.INFO)
window = tk.Tk()
window.title("FileSort")
mainframe = ttk.Frame(window)

mainframe.pack()
buttonframe = ttk.Frame(window)
buttonframe.pack()
suffix_group = ttk.Frame(window)
suffix_group.pack()


def swap():
    suffix_whitelist = file_manager.whitelist
    suffix_blacklist = file_manager.blacklist
    file_manager.whitelist = suffix_blacklist
    file_manager.blacklist = suffix_whitelist
    whitelist.replace(1.0, END, ";".join(file_manager.whitelist))
    blacklist.replace(1.0, END, ";".join(file_manager.blacklist))


find_suffixes = tk.Button(buttonframe, text="Find file suffixes in file folder", command=lambda:
find_all_suffixes(file_manager, whitelist, blacklist, swap_lists))
find_suffixes.grid(column=0, row=0, sticky=tk.NSEW)

whitelist_label = tk.Label(mainframe, text="Whitelist:")
whitelist_label.grid(row=0, column=0)

blacklist_label = tk.Label(mainframe, text="Blacklist:")
blacklist_label.grid(row=2, column=0)

whitelist = tk.Text(mainframe, width=100, height=3)
whitelist.grid(column=0, row=1, columnspan=2)

blacklist = tk.Text(mainframe, width=100, height=3)
blacklist.grid(column=0, row=3, columnspan=2)

swap_lists = tk.Button(mainframe, width=114, height=3, text="Swap", state="disabled", command=swap)
swap_lists.grid(column=0, row=5)

move_button = tk.Button(buttonframe, text="Move files to folders",
                        command=lambda: move(file_manager, whitelist, blacklist))
move_button.grid(column=1, row=0, columnspan=6, sticky=tk.NSEW)

group_files_by_type_button = tk.Button(buttonframe, text="Group files by type",
                                       command=lambda: group_files(file_manager))
group_files_by_type_button.grid(column=0, row=1)
allow: bool = True

window.mainloop()
