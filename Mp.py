import os      # to do operations on directory
from tkinter.filedialog import askdirectory

import pygame    # music playing
from tkinter import*    # to make the basic gui for the app
from mutagen.id3 import ID3 # it is an open source python module to extract the meta data of a file

root=Tk()
root.minsize(300,300)
listofsongs =[]
realnames=[]

v=StringVar()
songlabel=Label(root,textvariable=v,width=35)

index=0

def nextsong(event):
    global index
    index+=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

def prevsong(event):
    global index
    index-=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
    return songname

def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    return songname

def directorychooser():
    directory= askdirectory()
    os.chdir(directory)

    for files in os.listdir():
        if files.endswith(".mp3"):

            realdir=os.path.realpath(files)
            audio=ID3(realdir)
            realnames.append(audio["TIT2"].text[0])

            listofsongs.append(files)
            print(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    #pygame.mixer.music.play()


Label= Label(root,text='Music Player')
Label.pack()

#listofsongs.reverse()


listbox=Listbox(root)
listbox.pack()

realnames.reverse()
#listofsongs.reverse()

for items in realnames:
    listofsongs.insert(0,items)

realnames.reverse()

nextbutton=Button(root,text='Next Song')
nextbutton.pack()
previousbutton=Button(root,text='Previous Song')
previousbutton.pack()
stopbutton=Button(root,text='Stop Song')
stopbutton.pack()

nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)

directorychooser()

songlabel.pack()

root.mainloop()

