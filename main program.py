from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from pytube import YouTube
from tkinter import messagebox
from threading import Thread
from PIL import ImageTk,Image
import urllib.request, io
from tkinter.ttk import *
import threading
from youtupe_sound import down_sound
from youtube_playlist import youtube_list
#all libraries here.....

root=tk.Tk()
root.title("full downloader app (version 1.0)")
root.geometry("800x470+400+200")
root.iconbitmap("images/download.ico")
img=PhotoImage(file="images/youtube.png")
root.resizable(0,0)
# root.attributes("-topmost",True)
Label1=Label(root,image=img)
Label1.place(x=10,y=0)

youtupe_lable=Label(root,text="Youtube Video Downloader",font=("calibre ",20,"bold"))
youtupe_lable.place(x=70,y=10)

img200=PhotoImage(file="images/earth.png")
world_img=Label(root,image=img200)
world_img.place(x=730,y=50)

hello_world=Label(root,text="Hello World!!",foreground="black",font=("SF Arabic",20,"bold"))
hello_world.place(x=550,y=60)

program_d=Label(root,text="Made By:AHMED RAMADAN®",foreground="black",font=("SF Arabic",15,"bold"))
program_d.place(x=510,y=16)



def stop():
    root.quit()
    


Menubar=Menu(root)
root.config(menu=Menubar)
organise_menue=Menu(Menubar,tearoff=False)
def develober():
    messagebox.showinfo("Ahmed Ramadan Abd Elnaser","Contact Me On\nAhmed-Ramadan-Abd-Elnaser@protonmail.com")
    

    
    
Menubar.add_command(label="Devoleped By",command=develober,font=('Technolog', 3, ' bold '))  
Menubar.add_command(label="Youtube Sound",command=down_sound,font=('Technolog', 3, ' bold ')) 
Menubar.add_command(label="Youtube List",command=youtube_list,font=('Technolog', 3, ' bold '))
Menubar.add_command(label="Exit",command=stop,font=('Technolog', 3, ' bold '))  






def locate():
    locate_entry.delete(0,1000)
    global file_location
    file_location=filedialog.askdirectory(initialdir=os.getcwd(),title="select location")
    locate_entry.insert(END,file_location)




def download_youtube_ved():
    try:
     global tilte_v
     global v_itle_lable
     global v_author1_lable
     global v_views1_lable
     global v_date1_lable
     
     
     url =link_entry.get()
     my_video = YouTube(url,on_complete_callback=finish_down)
     tilte_v=my_video.title
     views_v=my_video.views
     date_v=my_video.publish_date.strftime("%Y/%m/%d")
     author_v=my_video.author
     
     
     v_itle_lable=tk.Label(root,text=tilte_v,fg="black",font=("calibre ",15,"bold"))
     v_itle_lable.place(x=120,y=205)
     
     
     v_views1_lable=tk.Label(root,text=f"{views_v} view",fg="black",font=("calibre ",15,"bold"))
     v_views1_lable.place(x=420,y=100)
     
     
     v_author1_lable=tk.Label(root,text=author_v,fg="black",font=("calibre ",15,"bold"))
     v_author1_lable.place(x=320,y=50)
     
     
     
     v_date1_lable=tk.Label(root,text=date_v,fg="black",font=("calibre ",15,"bold"))
     v_date1_lable.place(x=400,y=150)
     
     
     
     yt = YouTube(str(my_video.thumbnail_url))
     raw_data = urllib.request.urlopen(yt.thumbnail_url).read()
     im = Image.open(io.BytesIO(raw_data)).resize((200, 200))
     image = ImageTk.PhotoImage(im)
     c = Canvas(root, width=200, height=150)
     c.create_image(0,0,anchor='nw', image=image)
     c.place(x=10,y=50)
     my_video = my_video.streams.filter(res=resolution.get()).first().download(file_location)
    except:
     messagebox.showerror(title='Error', message='An error occurred while searching for video resolutions!\n'\
                'Below might be the causes\n->Unstable internet connection\n->Invalid link\n->Invalid Location\n->closing program')
     status.config(text="Status: Erorr")
     resolution_button.configure(state="normal")
     download_button.configure(state="normal")





def active_download():
  try:
     if link_entry.get()=="" and locate_entry.get()=="":
        messagebox.showerror("Empty Fields", "Fields are empty!")
     elif link_entry.get()=="":
        messagebox.showerror("Invalid Download","Please Enter Download Link!!")
     elif locate_entry.get()=="":
        messagebox.showerror("Invalid Download","Please Enter File location!!")   
     elif locate_entry.get()!=file_location:
        messagebox.showerror("Invalid Download","Please Enter The Correct File location!!")  
     elif resolution.get()=="":
       messagebox.showerror("Invalid Download","Please Enter video resolution..")
#    elif home_directory not in locate_entry.get():
#        messagebox.showerror("Invalid Download","Please Enter The Correct File location!!") 
     else:
        stop_threads = False
        download_button.configure(state="disable")
        resolution_button.configure(state="disable")
        status.config(text="Status: Downloading.......")
        Target=Thread(target=download_youtube_ved)
        Target.start()
  except:
      messagebox.showerror(title='Error', message='An error occurred while searching for video resolutions!\n'\
                'Below might be the causes\n->Unstable internet connection\n->Invalid link\n->Invalid Location\n->closing program',parent=root)
      download_button.configure(state="normal")
      resolution_button.configure(state="normal")



def finish_down(stream=None,chunk=None,file_handle=None,remaining=None):
    messagebox.showinfo("Successful Download","Downloaded Successfully...!!")
    download_button.configure(state="normal")
    resolution_button.configure(state="normal")
    link_entry.delete(0,1000)
    locate_entry.delete(0,100)
    v_itle_lable.destroy()
    v_date1_lable.destroy()
    v_author1_lable.destroy()
    v_views1_lable.destroy()
    v_title_lable=tk.Label(root,text="Download Done!!!",fg="black",font=("calibre ",15,"bold"))
    v_title_lable.place(x=120,y=205)
    status.config(text="Status: Complete Successful Enjoy...")


def searchResolution():
    video_link = link_entry.get()
    if video_link == '':
        messagebox.showerror(title='Error', message='Provide the video link please!')
    else:
        try:
            video = YouTube(video_link)
            resolutions = []
            for i in video.streams.filter(file_extension='mp4'):
                resolutions.append(i.resolution)
            resolution['values'] = resolutions
            resolution.current(0)
            messagebox.showinfo(title='Search Complete', message='Check the Combobox for the available video resolutions')
            resolution_button.configure(state="normal")
        except:
            messagebox.showerror(title='Error', message='An error occurred while searching for video resolutions!\n'\
                'Below might be the causes\n->Unstable internet connection\n->Invalid link\n->Invalid Location\n->closing program')
            resolution_button.configure(state="normal")
            download_button.configure(state="normal")

def searchThread():
    video_link = link_entry.get()
    res_text=resolution.get()
    if video_link == '':
        messagebox.showerror(title='Error', message='Provide the video link please!')
    
        
    else:
     resolution_button.configure(state="disable")
     t1 = threading.Thread(target=searchResolution)
     t1.start()


#tkinter componots.....
link_entry=tk.Entry(root,width=49,highlightthickness=6,font=("arial,20,bold"))
link_entry.place(x=193,y=250)

locate_entry=tk.Entry(root,width=50,highlightthickness=6,font=("arial,20,bold"))
locate_entry.place(x=110,y=300)


button_img=PhotoImage(file="images/youtube.png")
file_locte_button=tk.Button(root,image=button_img,width=50,height=40,bd=0,command=locate)
file_locte_button.place(x=730,y=300)


link_lable=Label(root,text="Youtube Link Here",font=("TLabel ",16))
link_lable.place(x=0,y=255)

locate_lable=Label(root,text="Location",font=("TLabel",18))
locate_lable.place(x=0,y=300)


image100 = Image.open("images/youtube.png")
image100 = image100.resize((50,50), Image.ANTIALIAS)
img100= ImageTk.PhotoImage(image100)
img22= ImageTk.PhotoImage(image100)
download_button=tk.Button(root,text="download video..",image=img22,font=('Helvetica 15 bold'), compound= LEFT,bd=0,command=active_download)
download_button.place(x=10,y=354)



status=tk.Label(root,text="Status: Ready",font=("calibre 10 italic"),fg="black",bg="white",anchor="w")
status.place(rely=1,anchor="sw",relwidth=1)


v_name_label=tk.Label(root,text="Video Name:",fg="black",font=("calibre 15 italic"))
v_name_label.place(x=0,y=205)

v_author_label=tk.Label(root,text="Author:",fg="black",font=("calibre 15 italic"))
v_author_label.place(x=250,y=50)

v_views_label=tk.Label(root,text="Number of Views:",fg="black",font=("calibre 15 italic"))
v_views_label.place(x=250,y=100)

v_data_label=tk.Label(root,text="Published date:",fg="black",font=("calibre 15 italic"))
v_data_label.place(x=250,y=150)

resolution=Combobox(root,width=20,font=("arial 12"))
resolution.place(x=300,y=370)

v_resolution_label=tk.Label(root,text="resolution:",fg="black",font=("calibre 15 italic"))
v_resolution_label.place(x=300,y=340)
resolution_button=tk.Button(root,text="Serch resolution",font=('Helvetica 10'), compound= LEFT,bd=1,command=searchThread,activebackground="white")
resolution_button.place(x=520,y=368)







#tkinter componots.....

root.mainloop()
