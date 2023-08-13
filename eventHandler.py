import time
import random
import shutil
import os 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/drsba/Downloads"

class FileEventhandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"Hi,{event.src_path} has been created")
    def on_deleted (self,event):
        print(f"Oops,{event.src_path} has been deleted")
    def on_moved(self,event):
        print(f"Hi,{event.src_path} has been moved")
    def on_modified(self,event):
        print(f"Congrats,{event.src_path} has been modified")
    
eventHandler = FileEventhandler()

observer = Observer()
observer.schedule(eventHandler,from_dir,recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("Running...")
except KeyboardInterrupt:
    print("Stop")
    observer.stop()
