from tkinter import *
import tkinter as tk
from pytube import YouTube
import threading
from tkinter import filedialog
from random import randint
from moviepy.editor import VideoFileClip, AudioFileClip
import os


root = tk.Tk()
root.title("YouTube video downloader")
root.geometry("800x900")
root.geometry("+{}+{}".format(root.winfo_screenwidth()-900, 20))
root.resizable(0, 0)
root.configure(bg='cyan')
root.iconbitmap('iconAI.ico')

cv = ">скачивание видео со звуком(1)"
vc = ">скачивание аудио из видео запущено"
ki = ">скачивание видео со звуком запущено(2)"
an = "|_название видео_|=>"
kl = "<в скором времени будет завершено"
lk = "<аудио файл будет сохранён под названием(пример названия: audioYouTube896.mp3)"
ik = "<видео файл будет сохранён под названием(пример названия: YouTubeVideoWithSound56.mp4)"
warning = "!рекомендуем каждый раз очищать обозраватель данных!"
error = "!ЕСЛИ ВИДЕО ДОЛГО НЕ СКАЧИВАЕТСЯ, ТО ПРОИЗОШЛА ОШИБКА ФИЛЬТРАЦИИ ПОТОКОВ!"

def clear_listbox():
    g.delete(0, 'end')

def paste_text():
    text = root.clipboard_get()
    a.insert(tk.END, text)

def paste_text_two():
    text = root.clipboard_get()
    b.insert(tk.END, text)

def Destroy_WINDOW():
    root.destroy()

def Download_from_YouTube():
    video_url = a.get()
    save_path = filedialog.askdirectory()
    t = threading.Thread(target=download_video, args=(video_url, save_path,))
    t.start()


def download_video(video_url, save_path):
    yt = YouTube(video_url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    title = yt.title
    g.insert(1, cv + an + title)
    g.insert(2, kl)
    g.insert(3, warning)
    g.insert(4, error)
    gg.insert(1, title)
    stream.download(output_path=save_path)
    

def Download_AUdio():
    vid_url = b.get()
    save_path = filedialog.askdirectory()
    p = threading.Thread(target=download_audio, args=(vid_url, save_path,))
    p.start()

def download_audio(vid_url, save_path):
    ty = YouTube(vid_url)
    ream = ty.streams.filter(only_audio=True).first()
    ream.download(output_path=save_path, filename = f'audioYouTube{randint(0, 1000)}.mp3')
    tItle = ty.title
    g.insert(1, vc + an + tItle)
    g.insert(2, lk)
    g.insert(3, warning)
    g.insert(4, error)
    gg.insert(1, tItle)
    


Label(root, text="YouTube video downloader", font="Impact", bg="white").place(x=350, y=0)
Label(root, text="Обозреватель процессов:", bg="white").place(x=320, y=35)
g = Listbox(root, width=132, height=6)
g.place(x=0, y=60)
gg = Listbox(root, width=132, height=15)
gg.place(x=0, y=650)
Label(root, text="Скачивание видео со звуком(обычное качество)", bg="white").place(x=0, y=180)
Label(root, text="Скачивание аудио из видео", bg="white").place(x=0, y=480)
Button(root, text="Выйти", bg="red", width=5, command=Destroy_WINDOW).place(x=750, y=0)
a = Entry(root, width=90)
a.place(x=10, y=200)
b = Entry(root, width=90)
b.place(x=10, y=500)
Button(root, text="скачать видео со звуком", width=21, bg="yellow", command=Download_from_YouTube).place(x=600, y=200)
Button(root, text="скачать аудио", width=20, bg="yellow", command=Download_AUdio).place(x=600, y=500)
Button(root, text="Вставить из буфера обмена", width=25, bg="orange", command=paste_text).place(x=600, y=240)
Button(root, text="Вставить из буфера обмена", width=25, bg="orange", command=paste_text_two).place(x=600, y=540)
Button(root, text="очистить", width=15, bg="red", command=clear_listbox).place(x=500, y=30)
Label(root, text="version 1.0").place(x=0, y=0)
Label(root, text="скачанные видео и аудио:", bg='white').place(x=320, y=625)

root.mainloop()
