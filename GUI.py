from pytube import YouTube
import shutil
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image
import urllib.request
from pytube import Playlist
window = Tk()
window.title('YouTube Video Downloader')
window.geometry("980x600")
fileSizeInBytes = 0
Link = StringVar()
LinkI = Entry(window, textvariable = Link, width = 50)
LinkI.place(x = 230, y = 85, width=220, height=48)
LinkI.insert(0, 'Enter YouTube Link')
def openDirectory():
        global FolderName
        FolderName =  filedialog.askdirectory()
        if(len(FolderName) > 1):
            fileLocationLabel.config(text=FolderName,fg="green")
        else:
            fileLocationLabel.config(text="Please choose folder!",fg="red")
Directory = Button(window,width=20,bg="Blue",fg="white",text="Choose folder",command=openDirectory)
Directory.place(x = 550, y = 0)
fileLocationLabel = Label(window,text="")
fileLocationLabel.place(x = 550, y = 50)
def VideoDownloader():
    url =YouTube(str(Link.get()))
    video = url.streams.first()
    video.streams.filter(progressive=True,res="720p").download()
    video.streams.filter(progressive=True,res="360p").download()
    fileSizeInBytes = video.filesize
    complete()
    return url, fileSizeInBytes
def PlaylistDownloader():
    PlUrl =str(Link.get())
    try:
       p = Playlist(PlUrl)
    except VideoUnavailable:
       print("There is no such link for a YouTube playlist{}".format(PlUrl))
    else:
       for video in p.videos:
          video.streams.filter(progressive=True).download(output_path=" ",filename="")
          video.register_on_progress_callback(complete())
    complete()
LoadingLabel = Label(window,text="")
LoadingLabel.place(x = 550, y = 150)
def complete():
    LoadingLabel.config(text=("Download Complete"))
def progress(fileSizeInBytes, remaining):
    percent = (100 * (fileSizeInBytes - remaining)) / fileSizeInBytes
progressbar = ttk.Progressbar(window,orient="horizontal", length=220, mode='determinate')
progressbar.place(x = 230, y = 250)
def details(url):
    return f"The video title is :\n{url.title}\n---------\n"+f"The video views are :\n{url.views}\n---------\n"+ f"The video rating is :\n{url.rating}\n---------\n"
def preview(url):
    PicUrl = url.thumbnail_url
    urllib.request.urlretrieve(PicUrl,"pic.png")
    img = Image.open("pic.png")
    img.show()
    return img
with open('details.txt', 'w') as d:
    d.write(details(YouTube(str(Link.get()))))
    d.close()
shutil.move("C:\\Users\\EGYPT\\Desktop\\details.txt", str(filedialog.askdirectory()))
def captions_extraction(url):
    caption = url.captions.get_by_language_code('en').generate_srt_captions()
    return caption
with open('captions.txt', 'w') as f:
    f.write(captions_extraction(YouTube(str(Link.get()))))
    f.close()
shutil.move("C:\\Users\\EGYPT\\Desktop\\captions.txt", str(filedialog.askdirectory()))
photo = PhotoImage(file = "psi (1).png")
window.iconphoto(False, photo)
photo1 = PhotoImage(file = r"532.png")
photoimage1 = photo1.subsample(25, 25)
photo2 = PhotoImage(file = r"533.png")
photoimage2 = photo2.subsample(25, 25)
photo3 = PhotoImage(file = r"534.png")
photoimage3 = photo3.subsample(25, 25)
User = Button(window, text='User', padx = 10, pady = 10)
User.place(x = 0, y = 0, width=120, height=50)
FavoritesList = Button(window, text='Favorites List', padx = 10, pady = 10)
FavoritesList.place(x = 120, y = 0, width=120, height=50)
Download = Button(window, text='Vi Download', image = photoimage1, compound = RIGHT, bg = 'blue', command = VideoDownloader)
Download.place(x = 450, y = 85, width=100, height=48)
Download = Button(window, text='Pl Download', image = photoimage1, compound = RIGHT, bg = 'blue', command = PlaylistDownloader)
Download.place(x = 450, y = 133, width=100, height=48)
Filter = Button(window, text='Filter', image = photoimage2, compound = RIGHT, bg = 'blue')
Filter.place(x = 550, y = 85, width=100, height=48)
Search = Button(window, text='Search', image = photoimage3, compound = RIGHT, bg = 'blue')
Search.place(x = 650, y = 85, width=100, height=48)
Preview = Button(window, text='Preview', bg = 'blue')
Preview.place(x = 750, y = 85, width=100, height=48)
Favorites = Button(window, text='Favorites', bg = 'blue')
Favorites.place(x = 850, y = 85, width=100, height=48)
ImgLabel = Label(window, image = "")
ImgLabel.place(x = 50, y = 350,height=200)
DetailsLabel = Label(window, text = "")
DetailsLabel.place(x = 550, y = 350,height=200)
Preview.config(command = lambda: ImgLabel.config(image=preview(YouTube(str(Link.get())))))
Search.config(command = lambda: DetailsLabel.config(text=details(YouTube(str(Link.get())))))
users=[]
favorites=[]
def CheckUser():
    if x in users:
        # open the program
    else:
        print("the user is not inculded")
    #register function
    # button register is pressed
    users.append()
with open("program_data.txt","w") as k:
    k.write(users)
    k.write(favorites)
    k.close
with open("program_data.txt","r") as t:
    def user_detection(x):
    for i in range(users):
        if users[i]==x:
            return i
    #register function
    # button register is pressed
    users.append('the entered name')
x=input("ENter the user:")
#def Favorites():
    # if favorites is pressed
    ##favorites[i].append(Link)
    #show favorites
    #favorites[i]
window.mainloop()






