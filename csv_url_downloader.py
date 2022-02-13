import urllib.request
import concurrent.futures
from pathlib import Path
import socket

socket.setdefaulttimeout(10)  # timeout for all connections for 10 sec


class Downloader:

    def __init__(self, file):
        """gets absolute file path and downloads all the links of pictures inside to the same folder creating
         a sub folder inside with a same name as file"""
        self.file_name = file
        self.file_folder = Path(file).parent.absolute()
        self.destination = self.file_name.replace(".csv", "")
        print(self.file_name)
        print(self.file_folder.parent.absolute())

    def __enter__(self):
        with open(self.file_name) as file:
            self.link_list = [line.strip() for line in file.readlines()]
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.link_list = None

    def create_folder(self):
        """creates a folder without exceptions raise if exist"""
        Path(self.destination).mkdir(parents=True, exist_ok=True)

    def download_image(self,url,path):
        """get a single image"""
        urllib.request.urlretrieve(url,path)

    def download_all_from_csv(self):
        self.create_folder()
        print(self.link_list)
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future = {executor.submit(self.download_image, url=row, path=self.destination+"/"+str(index)+".jpg")
                      : row for index, row in enumerate(self.link_list)}



