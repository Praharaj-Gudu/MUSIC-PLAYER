import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from PIL import Image, ImageTk

root = Tk()
root.title("Clause Music Player")
root.geometry("485x700")
root.configure(background='#333333')
root.resizable(False, False)
mixer.init()

# Create a function to open a folder and add music to the playlist


def AddMusic():
    folder_path = filedialog.askdirectory()
    if folder_path:
        songs = []
        for file in os.listdir(folder_path):
            if file.endswith(".mp3"):
                songs.append(file)
        if songs:
            Playlist.delete(0, END)
            for song in songs:
                Playlist.insert(END, song)
                PlaylistPath.insert(END, os.path.join(folder_path, song))


def PlayMusic():
    path = PlaylistPath.get(ACTIVE)
    mixer.music.load(path)
    mixer.music.play()


# Icon
image_icon = PhotoImage(file="logo png.png")
root.iconphoto(False, image_icon)

# Display animated GIF
gif_path = 'aa1.gif'
gif = Image.open(gif_path)
frames = []
frame_count = 0

try:
    while True:
        frames.append(ImageTk.PhotoImage(gif.copy()))
        frame_count += 1
        gif.seek(frame_count)
except EOFError:
    pass

label = Label(root)
label.pack()


def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frame_count:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)


# Buttons
button_frame = Frame(root, bg="#333333")
button_frame.pack(pady=10)

ButtonPlay = PhotoImage(file="play1.png")
Button(button_frame, image=ButtonPlay, bg="#333333",
       bd=0, command=PlayMusic).pack(side=LEFT, padx=5)

ButtonStop = PhotoImage(file="stop1.png")
Button(button_frame, image=ButtonStop, bg="#333333", bd=0,
       command=mixer.music.stop).pack(side=LEFT, padx=5)

ButtonBrowse = PhotoImage(file="browse.png")
Button(button_frame, image=ButtonBrowse, bg="#333333",
       bd=0, command=AddMusic).pack(side=LEFT, padx=5)

# Playlist
playlist_frame = Frame(root, bg="#333333")
playlist_frame.pack(padx=10, pady=10)

Scroll = Scrollbar(playlist_frame)
Playlist = Listbox(playlist_frame, width=50, font=("Times New Roman", 10), bg="#333333",
                   fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Playlist.pack(side=LEFT, fill=BOTH)

Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)

PlaylistPath = Listbox(root, width=0, height=0, bd=0)
PlaylistPath.pack()

# Execute Tkinter
root.after(0, update, 0)
root.mainloop()
