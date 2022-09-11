import os
import pathlib


def group_files(file_manager):
    print(file_manager.path)
    image_extensions = (".webp", ".jpg", ".jpeg", ".gif", ".jfif", ".png", ".bmp", ".svg", ".apng", ".avif")
    video_extensions = (".avi", ".mp4", ".mkv")
    ms_office_extensions = (".doc", ".docx", ".ppt", ".pptx", ".ppsx", ".pdf", ".xls", ".xlsx")
    archives = (".gz", ".zip", ".rar", ".7z")
    executables = (".exe", ".msi")
    iterate_through_files(file_manager, image_extensions, "Images")
    iterate_through_files(file_manager, video_extensions, "Videos")
    iterate_through_files(file_manager, ms_office_extensions, "MS Office Documents, pdf")
    iterate_through_files(file_manager, archives, "Archives")
    iterate_through_files(file_manager, executables, "executables")


def iterate_through_files(file_manager, image_extensions: tuple, file_type: str):
    file_type_folder = f"{file_manager.path}\\{file_type}"
    if not os.path.exists(file_type_folder):
        os.mkdir(file_type_folder)
    for extension in image_extensions:
        path = f"{file_manager.path}\\{extension}"
        if os.path.exists(path):
            for item in pathlib.Path(path).iterdir():
                new_item_path = f"{file_manager.path}\\{file_type}\\{item.stem}{item.suffix}"
                os.replace(item, new_item_path)
        folder = f"{file_manager.path}\\{extension}"
        if os.path.exists(folder):
            os.removedirs(folder)
