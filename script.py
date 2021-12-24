import os,shutil,time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from variables import *


class Handler(FileSystemEventHandler) :

    def on_created(self, event):
        # switch to organisedfiles dir
        os.chdir(trackfolder + '\\organisedfiles')
        listFiles = os.listdir(trackfolder)
        # loop files in trackfolder directory
        for files in listFiles :
            ext = os.path.splitext(files)
            if(ext[1] == '.html'):
                if(os.path.isdir(trackfolder + '\\organisedfiles\\html') == False) :
                    os.system('mkdir html')
                shutil.move(trackfolder + '\\' + files , trackfolder + '\\organisedfiles\\html' )
            elif(ext[1] == '.jpg' or ext[1] == '.png' ) :
                if(os.path.isdir(trackfolder + '\\organisedfiles\\images') == False) :
                    os.system('mkdir images')
                shutil.move(trackfolder + '\\' + files , trackfolder + '\\organisedfiles\\images' )
           

# watching folders
trackfolder = mainpath
downloads_folder = secondarypath

# List
folder_lists = ((trackfolder),(downloads_folder))

observer = Observer()
event_handler = Handler()
observer.schedule(event_handler , trackfolder , recursive = True)

observer.start()
try :
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

