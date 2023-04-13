from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
from pytube import YouTube
from tkinter import messagebox
from threading import Thread
from PIL import ImageTk,Image
import urllib.request, io
from tkinter.ttk import *
#all libraries here.....

def down_sound():
 root1=tk.Toplevel()
 root1.title("youtube sound downloader")
 root1.geometry("800x470+400+200")
 root1.iconbitmap("images/download.ico")
 img=PhotoImage(file="images/music.png")
 root1.resizable(0,0)
 root1.attributes('-topmost',True)
 Label1=Label(root1,image=img)
 Label1.place(x=10,y=0)
 
 
 hello_world=Label(root1,text="Hello World!!",foreground="black",font=("SF Arabic",20,"bold"))
 hello_world.place(x=550,y=60)

 program_d=Label(root1,text="Made By:AHMED RAMADAN®",foreground="black",font=("SF Arabic",15,"bold"))
 program_d.place(x=510,y=16)
 
 img200=PhotoImage(file="images/earth.png")
 world_img=Label(root1,image=img200)
 world_img.place(x=730,y=50)


 
 youtupe_lable=Label(root1,text="Youtube Sound Downloader",font=("calibre ",20,"bold"))
 youtupe_lable.place(x=70,y=10)

 Menubar=Menu(root1)
 root1.config(menu=Menubar)
 organise_menue=Menu(Menubar,tearoff=False)
 
 def stop():
    stop_threads = True
    root1.destroy()
    return stop_threads 
    
 Menubar.add_command(label="Exit",command=stop,font=('Technolog', 3, ' bold '))   




 def locate_sound():
    global file_location
    file_location=filedialog.askdirectory(initialdir=os.getcwd(),title="select location",parent=root1)
    locate_entry.insert(END,file_location)




 def download_sound_ved():
     global tilte_v
     global v_itle_lable
     global v_author1_lable
     global v_views1_lable
     global v_date1_lable
     if link_entry.get()=="":
         messagebox.showerror(title='Error', message='An error occurred while searching for video resolutions!\n'\
             'Below might be the causes\n->Unstable internet connection\n->Invalid link\n->Invalid Location\n->closing program',parent=root1)
     else:
         try:
          url =link_entry.get()
          my_video = YouTube(url,on_complete_callback=finish_down)
          tilte_v=my_video.title
          views_v=my_video.views
          date_v=my_video.publish_date.strftime("%Y/%m/%d")
          author_v=my_video.author
     
     
          v_itle_lable=tk.Label(root1,text=tilte_v,fg="black",font=("calibre ",15,"bold"))
          v_itle_lable.place(x=130,y=205)
     
     
          v_views1_lable=tk.Label(root1,text=views_v,fg="black",font=("calibre ",15,"bold"))
          v_views1_lable.place(x=420,y=100)
     
     
          v_author1_lable=tk.Label(root1,text=author_v,fg="black",font=("calibre ",15,"bold"))
          v_author1_lable.place(x=320,y=50)
     
     
     
          v_date1_lable=tk.Label(root1,text=date_v,fg="black",font=("calibre ",15,"bold"))
          v_date1_lable.place(x=400,y=150)
    
    
    
    
    
          yt = YouTube(str(my_video.thumbnail_url))
          raw_data = urllib.request.urlopen(yt.thumbnail_url).read()
          im = Image.open(io.BytesIO(raw_data)).resize((200, 200))
          image = ImageTk.PhotoImage(im)
          c = Canvas(root1, width=200, height=150)
          c.create_image(0,0,anchor='nw', image=image)
          c.place(x=10,y=50)
    
          my_video = my_video.streams.get_audio_only("mp4").download(file_location)
         except:
          messagebox.showerror(title='Error', message='An error occurred while searching for video resolutions!\n'\
                'Below might be the causes\n->Unstable internet connection\n->Invalid link\n->Invalid Location\n->closing program',parent=root1)
          status.config(text="Status: Erorr")
          download_button.configure(state="normal")
          



 def active_download():
    try:
       if link_entry.get()=="" and locate_entry.get()=="":
        messagebox.showerror("Empty Fields", "Fields are empty!",parent=root1)
       elif link_entry.get()=="":
        messagebox.showerror("Invalid Download","Please Enter Download Link!!",parent=root1)
       elif locate_entry.get()=="":
        messagebox.showerror("Invalid Download","Please Enter File location!!",parent=root1)   
       elif locate_entry.get()!=file_location:
        messagebox.showerror("Invalid Download","Please Enter The Correct File location!!",parent=root1)  
       else:
         global stop_threads
         stop_threads = False
         download_button.configure(state="disable")
         status.config(text="Status: Downloading.......")
         Target=Thread(target=download_sound_ved)
         Target.start()
    except:
       messagebox.showerror(title='Error', message='An error occurred while searching for video resolutions!\n'\
                'Below might be the causes\n->Unstable internet connection\n->Invalid link\n->Invalid Location\n->closing program',parent=root1)
       download_button.configure(state="normal")
       


 def finish_down(stream=None,chunk=None,file_handle=None,remaining=None):
    messagebox.showinfo("Successful Download","Downloaded Successfully...!!",parent=root1)
    download_button.configure(state="normal")
    link_entry.delete(0,1000)
    locate_entry.delete(0,100)
    v_itle_lable.destroy()
    v_date1_lable.destroy()
    v_author1_lable.destroy()
    v_views1_lable.destroy()
    v_title_lable=tk.Label(root1,text="Download Done!!!",fg="black",font=("calibre ",15,"bold"))
    v_title_lable.place(x=120,y=205)
    status.config(text="Status: Complete Successful Enjoy...")












 link_entry=tk.Entry(root1,width=49,highlightthickness=6,font=("arial,20,bold"))
 link_entry.place(x=193,y=250)

 locate_entry=tk.Entry(root1,width=50,highlightthickness=6,font=("arial,20,bold"))
 locate_entry.place(x=110,y=300)


 button_sound_img=PhotoImage(file="images/music.png")
 file_locte_sound=tk.Button(root1,image=button_sound_img,width=50,height=40,bd=0,command=locate_sound)
 file_locte_sound.place(x=730,y=305)


 link_lable=Label(root1,text="Video Link Here",font=("TLabel ",16))
 link_lable.place(x=0,y=255)

 locate_lable=Label(root1,text="Location",font=("TLabel",18))
 locate_lable.place(x=0,y=300)


 image100 = Image.open("images/music.png")
 image100 = image100.resize((50,50), Image.ANTIALIAS)
 img100= ImageTk.PhotoImage(image100)
 img22= ImageTk.PhotoImage(image100)
 download_button=tk.Button(root1,text="Download Sound",image=img22,font=('Helvetica 15 bold'), compound= LEFT,bd=0,command=active_download)
 download_button.place(x=300,y=340)



 status=tk.Label(root1,text="Status: Ready",font=("calibre 10 italic"),fg="black",bg="white",anchor="w")
 status.place(rely=1,anchor="sw",relwidth=1)


 v_name_label=tk.Label(root1,text="Sound Name:",fg="black",font=("calibre 15 italic"))
 v_name_label.place(x=0,y=205)

 v_author_label=tk.Label(root1,text="Author:",fg="black",font=("calibre 15 italic"))
 v_author_label.place(x=250,y=50)

 v_views_label=tk.Label(root1,text="Number of Views:",fg="black",font=("calibre 15 italic"))
 v_views_label.place(x=250,y=100)

 v_data_label=tk.Label(root1,text="Published date:",fg="black",font=("calibre 15 italic"))
 v_data_label.place(x=250,y=150)





 root1.mainloop()
 

