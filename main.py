from tkinter import *
import pygame
from tkinter import filedialog
from extract_features import FeatureExtractor

root = Tk()
root.title("Codemy.com")
pygame.mixer.init()
root.geometry("500x400")

def upload_song():
    song = filedialog.askopenfilename(initialdir="audio/" , title="sarki sec" , filetypes=(("wav Files" , "*.wav"), ))
    #features = FeatureExtractor.extract_features(song)
    #print(features)
    song_list.insert(END , song)

def play_song():
    song = song_list.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0) 

def stop_song():
    pygame.mixer.music.stop()
    song_list.selection_clear(ACTIVE)

song_list = Listbox(root , bg = "black" , fg="green" ,width=60)
song_list.pack(pady=20)


#Menu
my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Upload Song" , menu=add_song_menu)
add_song_menu.add_command(label="Upload One Song", command=upload_song)


play_btn_img = PhotoImage(file="img/play50.png")
stop_btn_img = PhotoImage(file="img/stop50.png")

controls_frame = Frame(root)
controls_frame.pack()

play_btn = Button(controls_frame , image= play_btn_img , borderwidth=0 , command=play_song)
stop_btn = Button(controls_frame , image= stop_btn_img, borderwidth=0 , command=stop_song)

play_btn.grid(row=0,column=2)
stop_btn.grid(row=0 , column=3)





root.mainloop()