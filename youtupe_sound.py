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
import time
import customtkinter
from PIL import Image
import json


#all libraries here.....

def down_sound():
 global is_cancelled_sound
 y_sound=customtkinter.CTkToplevel()
 y_sound.title("Youtube Sound Downloader... (version 1.0)")
 y_sound.geometry("800x470+500+200")
 y_sound.iconbitmap("images/music.ico")
 y_sound.resizable(0,0)
 root.withdraw()
 is_cancelled_sound=False
 
 img=customtkinter.CTkImage(light_image=Image.open("images/music.png"),size=(30, 30))

 Label1=customtkinter.CTkLabel(y_sound,text="",image=img)
 Label1.place(x=220,y=9)

 youtupe_lable=customtkinter.CTkLabel(y_sound,text="Youtube Video Downloader",font=("calibre ",20,"bold"))
 youtupe_lable.place(x=275,y=10)

 
 
 def locate():
    locate_entry.delete(0,1000)
    global file_location
    file_location=filedialog.askdirectory(initialdir=os.getcwd(),title="select location")
    locate_entry.insert(END,file_location)




 def download_youtube_ved():
    try:
     global tilte_v_sound
     global v_itle_lable_sound
     global v_author1_lable_sound
     global v_views1_lable_sound
     global v_date1_lable_sound
     global c_image_sound
     global v_rating_sound_lable
     global v_lenthe_sound_lable
     url =link_entry.get()
     my_video = YouTube(url,on_complete_callback=finish_down)
     tilte_v_sound=my_video.title
     views_v_sound=my_video.views
     date_v_sound=my_video.publish_date.strftime("%Y/%m/%d")
     author_v_sound=my_video.author
     lenthe=my_video.length
     #############################################
     v_itle_lable_sound=customtkinter.CTkLabel(y_sound,text=tilte_v_sound,font=("calibre ",15,"bold"))
     v_itle_lable_sound.place(x=100,y=180)
     
     
     v_views1_lable_sound=customtkinter.CTkLabel(y_sound,text=f"{views_v_sound} view",font=("calibre ",15,"bold"))
     v_views1_lable_sound.place(x=380,y=100)
     
     
     v_author1_lable_sound=customtkinter.CTkLabel(y_sound,text=author_v_sound,font=("calibre ",15,"bold"))
     v_author1_lable_sound.place(x=310,y=50)
     
     
     
     v_date1_lable_sound=customtkinter.CTkLabel(y_sound,text=date_v_sound,font=("calibre ",15,"bold"))
     v_date1_lable_sound.place(x=380,y=150)
     
     
     v_rating_sound_lable=customtkinter.CTkLabel(y_sound,text="No Rating",font=("calibre ",15,"bold"))
     v_rating_sound_lable.place(x=650,y=50)
     
     v_lenthe_sound_lable=customtkinter.CTkLabel(y_sound,text=lenthe,font=("calibre ",15,"bold"))
     v_lenthe_sound_lable.place(x=650,y=100)
     
     
     
     yt_sound = YouTube(str(my_video.thumbnail_url))
     raw_data = urllib.request.urlopen(yt_sound.thumbnail_url).read()
     im = Image.open(io.BytesIO(raw_data)).resize((290, 200))
     image = ImageTk.PhotoImage(im)
     c_image_sound = customtkinter.CTkCanvas(y_sound, width=290, height=150)
     c_image_sound.create_image(0,0,anchor='nw', image=image)
     c_image_sound.place(x=10,y=50)
     # youtube photo
     #############################################
     # progress par function
     total_size =100
     GB =int(total_size)
     download = 0
     speed = 1
     while(download<GB) and not is_cancelled_sound:
      time.sleep(0.02)
      progress_bar['value']+=(speed/GB)*100
      download=download+speed
      progress_label.configure(text=str(download)+"%/"+str(GB)+" Complete")
      y_sound.update_idletasks()
      if progress_bar['value']==99:
        status.config(text="Status: Processing Sound.......")
        my_video = my_video.streams.get_audio_only("mp4").download(file_location)
      
     progress_label.configure(text='')
     progress_bar['value'] = 0
     y_sound.update()
    
    
    
    except:
     messagebox.showerror(title='Error', message='An error occurred while searching for video resolutions!\n'\
                'Below might be the causes\n->Unstable internet connection\n->Invalid link\n->Invalid Location\n->closing program')
     status.config(text="Status: Erorr")
     download_button.configure(state=NORMAL)
     back_button.configure(state=NORMAL)
     progress_label.configure(text='')
     progress_bar['value'] = 0
     v_itle_lable_sound.destroy()
     v_date1_lable_sound.destroy()
     v_author1_lable_sound.destroy()
     v_lenthe_sound_lable.destroy()
     v_views1_lable_sound.destroy()
     v_rating_sound_lable.destroy()





 def active_download():
  global is_cancelled_sound
  try:
     if link_entry.get()=="" and locate_entry.get()=="":
        messagebox.showerror("Empty Fields", "Fields are empty!")
     elif link_entry.get()=="":
        messagebox.showerror("Invalid Download","Please Enter Download Link!!")
     elif locate_entry.get()=="":
        messagebox.showerror("Invalid Download","Please Enter File location!!")   
     elif locate_entry.get()!=file_location:
        messagebox.showerror("Invalid Download","Please Enter The Correct File location!!")  
     else:
        is_cancelled_sound=False
        cancel_sound_button.configure(state=NORMAL)
        download_button.configure(state=DISABLED)
        back_button.configure(state=DISABLED)
        status.config(text="Status: Downloading.......")
        Target=Thread(target=download_youtube_ved)
        Target.start()
  except:
      messagebox.showerror(title='Error', message='An error occurred while searching for video resolutions!\n'\
                'Below might be the causes\n->Unstable internet connection\n->Invalid link\n->Invalid Location\n->closing program',parent=y_sound)
      download_button.configure(state=NORMAL)
      back_button.configure(state=NORMAL)





 def finish_down(stream=None,chunk=None,file_handle=None,remaining=None):
    messagebox.showinfo("Successful Download","Downloaded Successfully...!!")
    download_button.configure(state=NORMAL)
    back_button.configure(state=NORMAL)
    link_entry.delete(0,1000)
    locate_entry.delete(0,100)
    v_author1_lable_sound.destroy()
    v_itle_lable_sound.destroy()
    v_date1_lable_sound.destroy()
    v_views1_lable_sound.destroy()
    v_rating_sound_lable.destroy()
    v_lenthe_sound_lable.destroy()
    c_image_sound.destroy()
    v_title_lable=customtkinter.CTkLabel(y_sound,text="Download Done!!!",font=("calibre ",15,"bold"))
    v_title_lable.place(x=100,y=180)
    status.config(text="Status: Complete Successful Enjoy...")



 #tkinter componots youtupe video dowload.....
 link_entry=customtkinter.CTkEntry(y_sound,width=600,font=("arial",20,"bold"))
 link_entry.place(x=180,y=220)

 locate_entry=customtkinter.CTkEntry(y_sound,width=550,font=("arial",20,"bold"))
 locate_entry.place(x=110,y=260)


 button_img=PhotoImage(file="images/music.png")
 file_locte_button=customtkinter.CTkButton(y_sound,text="location",image=button_img,width=50,height=40,command=locate)
 file_locte_button.place(x=670,y=255)


 link_lable=customtkinter.CTkLabel(y_sound,text="Youtube Link Here",font=("TLabel ",20,"bold"))
 link_lable.place(x=0,y=220)

 locate_lable=customtkinter.CTkLabel(y_sound,text="Location",font=("TLabel",25,"bold"))
 locate_lable.place(x=0,y=257)


 image100 = Image.open("images/music.png")
 image100 = image100.resize((50,50), Image.ANTIALIAS)
 img100= ImageTk.PhotoImage(image100)
 img22= ImageTk.PhotoImage(image100)
 download_button=customtkinter.CTkButton(y_sound,text="download sound..",image=img22,font=('Helvetica' ,15,'bold'), compound= LEFT,command=active_download)
 download_button.place(x=10,y=300)



 status=tk.Label(y_sound,text="Status: Ready",font=("calibre 10 italic"),fg="black",bg="white",anchor="w")
 status.place(rely=1,anchor="sw",relwidth=1)


 v_name_label_sound_text=customtkinter.CTkLabel(y_sound,text="sound Name:",font=("calibre" ,15, "italic"))
 v_name_label_sound_text.place(x=0,y=180)

 v_author_label_sound_text=customtkinter.CTkLabel(y_sound,text="Author:",font=("calibre" ,15, "italic"))
 v_author_label_sound_text.place(x=250,y=50)

 v_views_label_sound_text=customtkinter.CTkLabel(y_sound,text="Number of Views:",font=("calibre" ,15,"italic"))
 v_views_label_sound_text.place(x=250,y=100)

 v_data_label_sound_text=customtkinter.CTkLabel(y_sound,text="Published date:",font=("calibre" ,15, "italic"))
 v_data_label_sound_text.place(x=250,y=150)



 v_rating_label_sound_text=customtkinter.CTkLabel(y_sound,text="sound Rating:",font=("calibre" ,15, "italic"))
 v_rating_label_sound_text.place(x=550,y=50)

 v_lenthe_label_sound_text=customtkinter.CTkLabel(y_sound,text="sound Lenthe:",font=("calibre" ,15, "italic"))
 v_lenthe_label_sound_text.place(x=550,y=100)


 resolution_combo_sound=Combobox(y_sound,width=25,font=("arial" ,12),state="disable")
 resolution_combo_sound.place(x=375,y=465)
 resolution_combo_sound.set("mp4")


 v_Bitart_label=customtkinter.CTkLabel(y_sound,text="Sound Bitrat:",font=("calibre",15, "italic"))
 v_Bitart_label.place(x=300,y=340)



 progress_label =customtkinter.CTkLabel(y_sound,text='')
 progress_label.place(x=690,y=410)
 progress_bar =ttk.Progressbar(y_sound,length=500,mode="determinate")
 progress_bar.place(x=355,y=520)
 progress_label_text = customtkinter.CTkLabel(y_sound, text='progress:',font=("calibre",15, "italic"))
 progress_label_text.place(x=210,y=410)


 #themes on program
 def get_bg_theme():
    with open("theme.json", "r") as f:
        theme = json.load(f)
    return theme["bg_theme"]
 def get_default_color():
    with open("theme.json", "r") as f:
        theme = json.load(f)
    return theme["default_color"]
 def changeTheme(color):
    color = color.lower()
    themes_list = ["system", "dark", "light"]
    if color in themes_list:
        customtkinter.set_appearance_mode(color) 
        to_change = "bg_theme"
    else:
        customtkinter.set_default_color_theme(color)
        customtkinter.CTkLabel(y_sound, text = "(Restart to take full effect)", font = ("arial", 12)).place(x = 242 , y =445)
        to_change = "default_color"
    with open("theme.json", "r", encoding="utf8") as f:
        theme = json.load(f)
    with open("theme.json", "w", encoding="utf8") as f:
        theme[to_change] = color
        json.dump(theme, f, sort_keys = True, indent = 4, ensure_ascii = False)

 themes_menu = customtkinter.CTkOptionMenu(y_sound, values = ["System", "Dark", "Light"], width = 110, command = changeTheme, corner_radius = 15)
 themes_menu.place(x = 10 , y = 420)
 defaultcolor_menu = customtkinter.CTkOptionMenu(y_sound, values = ["Blue", "Dark-blue", "Green"], width = 110, command = changeTheme, corner_radius = 15)
 defaultcolor_menu.place(x = 10 , y = 380)
 defaultcolor_menu.set(get_default_color().title())
 #themes on program

 def cancel_sound_download():
    global is_cancelled_sound
    is_cancelled_sound= True
    messagebox.showinfo("Canceld","Downloaded Canceld....")
    status.configure(text="Status: Download Canceld....")
    download_button.configure(state=NORMAL)
    back_button.configure(state=NORMAL)
    cancel_sound_button.configure(state=DISABLED)
    v_author1_lable_sound.destroy()
    v_itle_lable_sound.destroy()
    v_date1_lable_sound.destroy()
    v_views1_lable_sound.destroy()
    v_rating_sound_lable.destroy()
    v_lenthe_sound_lable.destroy()
    c_image_sound.destroy()
    y_sound.update()
 
 def back():
    y_sound.withdraw()
    root.deiconify()
    
    

 cancel_sound_button = customtkinter.CTkButton(y_sound, text = "Cancel downlaod", font = ("arial bold", 12), fg_color = "red2", hover_color = "red4", width = 80, height = 26, command = cancel_sound_download, corner_radius = 20)
 cancel_sound_button.place(x =540 , y = 368)
 cancel_sound_button.configure(state=DISABLED) 
 
 
 back_button = customtkinter.CTkButton(y_sound, text = "Back To Youtube", font = ("arial bold", 12), fg_color = "red2", hover_color = "red4", width = 150, height = 26, command = back, corner_radius = 20)
 back_button.place(x = 550 , y = 10)

down_sound_button = customtkinter.CTkButton(root, text = "download sound", font = ("arial bold", 12), fg_color = "red2", hover_color = "green", width = 150, height = 26, command =down_sound, corner_radius = 20)
down_sound_button.place(x = 550 , y =10)
#tkinter componots youtupe sound dowload.....

down_sound()
 

