from tkinter import *
import pygame
from tkinter import filedialog
from get_recommendations import Recommender

root = Tk()
root.title("Music Recommender")
pygame.mixer.init()
root.geometry("500x400")

def upload_song():
    song = filedialog.askopenfilename(initialdir="audio/" , title="sarki sec" , filetypes=(("wav Files" , "*.wav"),("mp3 Files" , "*.mp3"), ))
    rec_list = Recommender.get_recommendations(song=song)
    print(rec_list)

    for rec in rec_list:
        label = rec.split(sep = ".")[0]
        recommendation = f"genres_original/{label}/{rec}"
        recommendations_list.insert(END,recommendation)
    
    song_list.insert(END , song)

def play_song():
    if song_list.get(ACTIVE):
        song = song_list.get(ACTIVE)
    if recommendations_list.get(ACTIVE):
        song = recommendations_list.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0) 

def stop_song():
    pygame.mixer.music.stop()
    if song_list.get(ACTIVE):
        song_list.selection_clear(ACTIVE)
    if recommendations_list.get(ACTIVE):
        recommendations_list.selection_clear(ACTIVE)

song_list = Listbox(root, bg="LightBlue3", fg="green", width=60)
recommendations_list = Listbox(root, bg="LightBlue3", fg="green", width=60)


song_list.grid(row=0, column=0, padx=5)
recommendations_list.grid(row=0, column=1, padx=5)


my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Upload Song", menu=add_song_menu)
add_song_menu.add_command(label="Upload One Song", command=upload_song)


play_btn_img = PhotoImage(file="img/play50.png")
stop_btn_img = PhotoImage(file="img/stop50.png")


controls_frame = Frame(root)
controls_frame.grid(row=1, columnspan=2)  


play_btn = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play_song)
stop_btn = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop_song)


play_btn.grid(row=0, column=0, padx=5)
stop_btn.grid(row=0, column=1, padx=5)

root.mainloop()



