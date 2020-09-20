from tkinter import * #tkinter is easy and understandable - gui
import PIL.ImageTk, PIL.Image
from PIL import Image
from tkinter import filedialog
import os
import pafy
import threading
from tkinter import messagebox
from threading import *

def mycb(total, recvd, ratio, rate, eta):
	download_button["state"] = "disabled"
	clear_button["state"] = "disabled"
	browse_button["state"] = "disabled"
	download_button["text"] = "PLEASE WAIT..."

def change():
	download_button["state"] = "normal"
	clear_button["state"] = "normal"
	browse_button["state"] = "normal"
	download_button["text"] = "START DOWNLOAD"

def clear_fun():
	add_url_entry.delete(0,END)

def browse_button():
	global folder_path # string variable - 
	filename = filedialog.askdirectory()
	folder_path.set(filename)  # filename is the path and set puts the path in the entry bpx

def Download(): # command=lambda::func_name(parameter)
	try:
		URL = add_url_entry.get() # add_url entry represents dabba - jo value user type kra lekr aayo
		PATH = add_path_entry.get() # to get the value
		if len(URL)!=0 and len(PATH)!=0: # if not empty string then only run
			os.chdir(PATH) # change directory path
			global select_video_type # check value 1 or 2
			global select_media_type 
			value_video = select_video_type.get()
			value_media = select_media_type.get()
			if (value_video!=0) and (value_media!=0): # if 1 or 2 go inside
				if 'playlist' in URL and value_video==1:
					playlist = pafy.get_playlist(URL) #pafy is library that sends request on yt-it is validated- downloadable link
					if(value_media==1): # 1=audio
						for x in range(0,len(playlist['items'])): # 1st video selected
							filename = playlist['items'][x]['pafy'].getbestaudio().download(quiet=False, callback=mycb)
						messagebox.showinfo("You Tube Downloader", "SuccessFully Download! Your Audio Playlist")
					else:
						for x in range(0,len(playlist['items'])):
							filename = playlist['items'][x]['pafy'].getbest().download(quiet=False, callback=mycb) # callback is used to recieve download process
						messagebox.showinfo("You Tube Downloader", "SuccessFully Download! Your Video Playlist")
					change()
				elif 'playlist' not in URL and value_video==2: # 2 means single video
					yt_object = pafy.new(URL) # new will give single video
					if(value_media==1): # audeo
						filename = yt_object.getbestaudio().download(quiet=True, callback=mycb)
						messagebox.showinfo("You Tube Downloader", "SuccessFully Download Your Audio file!")
					else:
						filename = yt_object.getbest().download(quiet=False, callback=mycb)
						messagebox.showinfo("You Tube Downloader", "SuccessFully Download Your Video file!")
					change()
				elif 'playlist' in URL and value_video==2:
					messagebox.showerror("You Tube Downloader","This is a playlist but you have select a other option")
				else:
					messagebox.showerror("You Tube Downloader", "This is a single but you have select a playlist option")  
			else:
				messagebox.showerror("You Tube Downloader", "You have forgot to select Options what you have to download") 
		else:
			messagebox.showerror("You Tube Downloader", "You have forgot to enter either the path or URL") 
	except Exception as e:
		print(e)


yt = Tk() # empty gui crteaed
yt.title("Apoorv's YouTube Downloader"); # by defalut TK
yt.iconbitmap('icon.ico') # by default flower
yt.configure(background="#263d42") #blue
yt.geometry('500x500')
yt.resizable(0, 0) # better visualzation 

folder_path = StringVar() # as no datatyps in python- to force that we want string as varaible so our folder path wil be string
img = Image.open("kids.png") # youtube logo
img = img.resize((500,150), Image.ANTIALIAS) # filter to remove the noise
img = PIL.ImageTk.PhotoImage(img) # python encoding to use this image with python library - to get height width
panel = Label(yt, image=img) # label is used to insert the image on the window yt
panel.place(x=0,y=0) # image has placted at x,y cordintaes 0,0 and it will got till size

add_url = Label(yt,text="Add Url",bg='#263d42',font=('Arial 12'))
add_url.place(x=30,y=200)

add_url_entry = Entry(yt,bd=3,width=33) # user input
add_url_entry.place(x=110,y=200)

clear_button = Button(yt,text="CLEAR",bg="DeepSkyBlue4",font=('Arial 10'),command=clear_fun) # clear the content - button is mapped with url entry
clear_button.place(x=335,y=200)

select_video_type = IntVar() # if first clicked then value 1 if next then 2 and so on
playlist_button = Radiobutton(yt, text='Playlist', bg="DeepSkyBlue4",font=('Arial 10'),variable=select_video_type, value=1) 
single_button = Radiobutton(yt, text='Single Link', bg="DeepSkyBlue4",font=('Arial 10'),variable=select_video_type, value=2)

playlist_button.place(x=110,y=250) # coordinates
single_button.place(x=210,y=250)


add_path = Label(yt,text="Add Path",bg='#263d42',font=('Arial 12'))
add_path.place(x=30,y=300)

add_path_entry = Entry(yt,textvariable=folder_path,bd=3,width=33) # textvariable will show the value of folder_path
add_path_entry.place(x=110,y=300)

browse_button = Button(yt,text="BROWSE",bg="DeepSkyBlue4",font=('Arial 10'),command=browse_button)
browse_button.place(x=335,y=300)

select_media_type = IntVar()
audio_button = Radiobutton(yt, text='Audio', bg="DeepSkyBlue4",font=('Arial 10'),variable=select_media_type, value=1)  # put value in variable
video_button = Radiobutton(yt, text='Video', bg="DeepSkyBlue4",font=('Arial 10'),variable=select_media_type, value=2)

audio_button.place(x=110,y=350)
video_button.place(x=210,y=350)

download_button = Button(yt,text="START DOWNLOAD",bg="DeepSkyBlue4",font=('Arial 10'),command=Download)
download_button.place(x=130,y=410)

yt.mainloop() # until you crosss the function will run