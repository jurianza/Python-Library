'''
Youtube Downloader
'''
from tkinter import *
import pytube



#Functions
def download():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first()
        video.download("C:\Youtube Videos")
        notif.config(fg= "green", text="Download Complete")
    except Exception as e:
        print(e)
        notif.config(fg="red",txt= "Video Could Not Be Downloaded")

#Main Screen
master = Tk()
master.title("Youtube Video Downloader")

#Labels
Label(master, text= "Youtube Video Converter", fg= "red", font=("Times New Roman",15)).grid(sticky=N,padx=100,row=0) #padx makes row amount
Label(master, text= "Please enter the link to your video below: ", font=("Times New Roman",12)).grid(sticky=N,row=1,pady=50)  #pady give some space. 
notif = Label(master,font=("Times New Roman",12))
notif.grid(sticky=N,pady=1,row=4)

#VARS
url=StringVar()


#Entry
Entry(master,width=50,textvariable=url).grid(sticky=N,row=2)

#Button
Button(master,width=20,text="Download",font=("Times New Roman",12),command=download).grid(sticky=N,row=3,pady=15)



master.mainloop()

