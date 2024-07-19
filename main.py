# import os
# from os import scandir, rename
# from os.path import splitext, exists, join
# from shutil import move
# from time import sleep
#
# import logging
#
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
#
# # ? folder to track e.g. Windows: "C:\\Users\\UserName\\Downloads"
# source_dir = "C:/Users/hp/Downloads/Telegram Desktop"
# dest_dir_music = "C:/Users/hp/Downloads/Telegram Desktop/musics"
# dest_dir_video = "C:/Users/hp/Downloads/Telegram Desktop/video"
# dest_dir_image = "C:/Users/hp/Downloads/Telegram Desktop/imgs"
# dest_dir_documents = "C:/Users/hp/Downloads/Telegram Desktop/docs"
#
# # ? supported image types
# image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
#                     ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# # ? supported Video types
# video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
#                     ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# # ? supported Audio types
# audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
# # ? supported Document types
# document_extensions = [".doc", ".docx", ".odt",
#                        ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]
#
#
# def make_unique(dest, name):
#     filename, extension = splitext(name)
#     counter = 1
#     # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
#     while exists(f"{dest}/{name}"):
#         name = f"{filename}({str(counter)}){extension}"
#         counter += 1
#
#     return name
#
#
# def move_file(dest, entry, name):
#     if not exists(dest):
#         os.makedirs(dest)
#         logging.info(f"Created directory: {dest}")
#     if exists(f"{dest}/{name}"):
#         unique_name = make_unique(dest, name)
#         old_name = join(dest, name)
#         new_name = join(dest, unique_name)
#         logging.info(f"Renaming file from {old_name} to {new_name}")
#         rename(old_name, new_name)
#     move(entry, dest)
#
#
# class MoverHandler(FileSystemEventHandler):
#     # ? THIS FUNCTION WILL RUN WHENEVER THERE IS A CHANGE IN "source_dir"
#     # ? .upper is for not missing out on files with uppercase extensions
#     def on_modified(self, event):
#         with scandir(source_dir) as entries:
#             for entry in entries:
#                 name = entry.name
#                 self.check_audio_files(entry, name)
#                 self.check_video_files(entry, name)
#                 self.check_image_files(entry, name)
#                 self.check_document_files(entry, name)
#
#     def check_audio_files(self, entry, name):  # * Checks all Audio Files
#         for audio_extension in audio_extensions:
#             if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
#                 if entry.stat().st_size < 10_000_000 or "SFX" in name:  # ? 10Megabytes
#                     dest = dest_dir_sfx
#                 else:
#                     dest = dest_dir_music
#                 move_file(dest, entry, name)
#                 logging.info(f"Moved audio file: {name}")
#
#     def check_video_files(self, entry, name):  # * Checks all Video Files
#         for video_extension in video_extensions:
#             if name.endswith(video_extension) or name.endswith(video_extension.upper()):
#                 move_file(dest_dir_video, entry, name)
#                 logging.info(f"Moved video file: {name}")
#
#     def check_image_files(self, entry, name):  # * Checks all Image Files
#         for image_extension in image_extensions:
#             if name.endswith(image_extension) or name.endswith(image_extension.upper()):
#                 move_file(dest_dir_image, entry, name)
#                 logging.info(f"Moved image file: {name}")
#
#     def check_document_files(self, entry, name):  # * Checks all Document Files
#         for documents_extension in document_extensions:
#             if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
#                 move_file(dest_dir_documents, entry, name)
#                 logging.info(f"Moved document file: {name}")
#
#
# # ! NO NEED TO CHANGE BELOW CODE
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s - %(message)s',
#                         datefmt='%Y-%m-%d %H:%M:%S')
#     path = source_dir
#     event_handler = MoverHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path, recursive=True)
#     observer.start()
#     try:
#         while True:
#             sleep(10)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()
#
import os
from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Directories to track
source_dir = "C:/Users/hp/Downloads/Telegram Desktop"
dest_dir_music = "C:/Users/hp/Downloads/Telegram Desktop/musics"
dest_dir_video = "C:/Users/hp/Downloads/Telegram Desktop/video"
dest_dir_image = "C:/Users/hp/Downloads/Telegram Desktop/imgs"
dest_dir_documents = "C:/Users/hp/Downloads/Telegram Desktop/docs"

# Supported file types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd",
                    ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf",
                    ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
audio_extensions = [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"]
document_extensions = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]


def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # If file exists, add number to the end of the filename
    while exists(join(dest, name)):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name


def move_file(dest, entry, name):
    if not exists(dest):
        os.makedirs(dest)
        logging.info(f"Created directory: {dest}")

    # Renaming file if it already exists in the destination
    if exists(join(dest, name)):
        unique_name = make_unique(dest, name)
        old_name = join(dest, name)
        new_name = join(dest, unique_name)
        logging.info(f"Renaming file from {old_name} to {new_name}")
        rename(old_name, new_name)

    # Moving file
    move(entry, dest)
    logging.info(f"Moved file: {name}")


class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        logging.info(f"Directory modified: {source_dir}")
        with scandir(source_dir) as entries:
            for entry in entries:
                if entry.is_file():
                    name = entry.name
                    self.check_audio_files(entry, name)
                    self.check_video_files(entry, name)
                    self.check_image_files(entry, name)
                    self.check_document_files(entry, name)

    def check_audio_files(self, entry, name):
        for audio_extension in audio_extensions:
            if name.lower().endswith(audio_extension):
                dest = dest_dir_music if entry.stat().st_size >= 10_000_000 and "SFX" not in name else dest_dir_sfx
                move_file(dest, entry, name)
                logging.info(f"Moved audio file: {name}")

    def check_video_files(self, entry, name):
        for video_extension in video_extensions:
            if name.lower().endswith(video_extension):
                move_file(dest_dir_video, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_image_files(self, entry, name):
        for image_extension in image_extensions:
            if name.lower().endswith(image_extension):
                move_file(dest_dir_image, entry, name)
                logging.info(f"Moved image file: {name}")

    def check_document_files(self, entry, name):
        for document_extension in document_extensions:
            if name.lower().endswith(document_extension):
                move_file(dest_dir_documents, entry, name)
                logging.info(f"Moved document file: {name}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    logging.info(f"Observer started on directory: {path}")

    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        logging.info("Stopping observer...")
        observer.stop()
    observer.join()
    logging.info("Observer stopped.")

