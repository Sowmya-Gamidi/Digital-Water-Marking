import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from dct_watermark import DCT_Watermark
from dwt_watermark import DWT_Watermark
import numpy as np
import cv2


global imgfile, original_img, up, bt,cov_img,label1, h, org_img, wm_img

my_w = tk.Tk()
width= my_w.winfo_screenwidth() 
height= my_w.winfo_screenheight()
#setting tkinter window size
my_w.geometry("%dx%d" % (width, height))
#my_w.geometry("800x500")  # Size of the window 
my_w.title('Digital Image Watermarking Based on DCT Technique')
my_font1=('times', 25, 'bold')
my_font2=('times',20)
my_font3=('times',15)
label1 = tk.Label()
org_img=tk.Label()
wm_img=tk.Label()
cov_img = tk.Label()
up_img_em=tk.Label()
w_img_em=tk.Label()
org_img_em_f=tk.Label()
w_img_em_f=tk.Label()
up_img_em_f=tk.Label()
up_img = tk.Label(my_w,text='Uploaded Image',width=18,font=my_font3)
w_img = tk.Label(my_w,text='Extracted Image',width=18,font=my_font3)
up = tk.Label(my_w,text='Uploaded Successfully!!',width=15)
bt=tk.Button(my_w, text='Click here to Extract', width=20, command = lambda:extract_final(filename))
l1 = tk.Label(my_w,text='Digital Image Watermarking Based on DCT Technique',width=73,font=my_font1)
l1.place(x=50,y=70)
b1 = tk.Button(my_w, text='Extract the Watermark', 
   width=18,height=3,font=my_font2,command = lambda:extract())
b1.place(x=450, y=180)
b2 = tk.Button(my_w, text='Embed the Watermark', 
   width=18,height=3,font=my_font2,command = lambda:embed())
b2.place(x=800, y=180)
original_img = tk.Button(my_w, text='Select the Original Image', width=20,command = lambda:open_image())
def home():
    #my_w = tk.Tk()
    #my_w.geometry("600x300")  # Size of the window
    global b1,b2
    up.destroy()
    h.destroy()
    label1.destroy()
    bt.destroy()
    cov_img.destroy()
    original_img.destroy()
    up_img.destroy()
    w_img.destroy()
    org_img.destroy()
    wm_img.destroy()
    my_w.title('Digital Image Watermarking')
    my_font1=('times', 18, 'bold')
    up_img_em.destroy()
    w_img_em.destroy()
    org_img_em_f.destroy()
    up_img_em_f.destroy()
    w_img_em_f.destroy()
    b1 = tk.Button(my_w, text='Extract the Watermark', 
   width=18,height=3,font=my_font2,command = lambda:extract())
    b1.place(x=450, y=180)
    b2 = tk.Button(my_w, text='Embed the Watermark', 
   width=18,height=3,font=my_font2,command = lambda:embed())
    b2.place(x=800, y=180)
def extract():
    b1.destroy()
    b2.destroy()
    global h, original_img
    h = tk.Button(my_w, text='Back to Home', width=20,height=2,font=my_font3,command = lambda:home())
    h.place(x=600, y=160)
    original_img = tk.Button(my_w, text='Select the Image to Extract', width=20,height=2,font=my_font3,command = lambda:open_image_extract())
    original_img.place(x=600,y=240)
    
def open_image_extract():
    global imgfile, filename, bt, up, cov_img
    original_img.destroy()
    f_types = [('Jpg Files', '*.jpg'),
    ('PNG Files','*.png')]   # type of files to select 
    filename = tk.filedialog.askopenfilename(filetypes=f_types)
    org=Image.open(filename)
    im=cv2.imread(filename)
    img=org.resize((200,200)) # new width & height
    img=ImageTk.PhotoImage(img)
    cov_img = tk.Label(image=img)
    cov_img.image = img
    cov_img.place(x=500,y=280)
    original_img.destroy()
    up = tk.Label(my_w,text='Uploaded Successfully!!',width=18,font=my_font3)
    up.place(x=750,y=370)
    bt=tk.Button(my_w, text='Click here to Extract', width=20,height=3, font=my_font3,command = lambda:extract_final(filename))
    bt.place(x=600, y=500)

def extract_final(x):
    bt.destroy()
    up.destroy()
    original_img.destroy()
    global label1,up_img,w_img
    
    op="./images/watermarked.jpg"
    img=cv2.imread(x)
    model = DCT_Watermark()
    ext_img = model.extract(img)
    cv2.imwrite(op, ext_img)
    img_extracted=Image.open(op)
    img_extracted=img_extracted.resize((200,200)) 
    img_extracted=ImageTk.PhotoImage(img_extracted)
    label1 = tk.Label(image=img_extracted)
    label1.image = img_extracted
    label1.place(x=800,y=280)
    up_img = tk.Label(my_w,text='Uploaded Image',width=18,font=my_font3)
    up_img.place(x=500,y=500)
    w_img = tk.Label(my_w,text='Extracted Image',width=18,font=my_font3)
    w_img.place(x=800,y=500)
    
def embed():
    b1.destroy()
    b2.destroy()
    global h, original_img
    h = tk.Button(my_w, text='Back to Home', width=20,height=2,font=my_font3,command = lambda:home())
    h.place(x=640, y=160)
    original_img = tk.Button(my_w, text='Select the Original Image \n& Watermark Image', width=30,height=2,font=my_font3,command = lambda:open_image_embed())
    original_img.place(x=580,y=240)

def open_image_embed():
    global imgfile, filename, bt, up, cov_img, org_img, wm_img,up_img_em,w_img_em
    original_img.destroy()
    f_types = [('Jpg Files', '*.jpg'),
    ('PNG Files','*.png')]   # type of files to select 
    filename = tk.filedialog.askopenfilename(multiple=True,filetypes=f_types)
    print(filename)
    org=Image.open(filename[0])
    wm=Image.open(filename[1])
    org_cv=cv2.imread(filename[0])
    wm_cv=cv2.imread(filename[1])
    org=org.resize((200,200))
    wm=wm.resize((200,200))
    # new width & height
    org=ImageTk.PhotoImage(org)
    org_img = tk.Label(image=org)
    org_img.image = org
    org_img.place(x=500,y=300)
    wm=ImageTk.PhotoImage(wm)
   
    wm_img = tk.Label(image=wm)
    wm_img.image = wm
    wm_img.place(x=800,y=300)
    original_img.destroy()
    bt=tk.Button(my_w, text='Click here to Embed the watermark', width=30, height=2, font=my_font3,command = lambda:embed_final(filename))
    bt.place(x=570, y=550)
    up_img_em = tk.Label(my_w,text='Original Image',width=18,font=my_font3)
    up_img_em.place(x=500,y=500)
    w_img_em = tk.Label(my_w,text='Watermark',width=18,font=my_font3)
    w_img_em.place(x=800,y=500)

def embed_final(x):
    global  up_img_em_f, org_img_em_f, w_img_em_f, org_img, wm_img, h, label1, org, wm
    original_img.destroy()
    up_img_em.destroy()
    w_img_em.destroy()
    wm_img.destroy()
    org_img.destroy()
    bt.destroy()
    global label1
    op="./images/watermarked.jpg"
    img=cv2.imread(x[0])
    wm=cv2.imread(x[1])
    model = DCT_Watermark()
    emb_img = model.embed(img, wm)
    cv2.imwrite(op, emb_img)
    org=Image.open(filename[0])
    wm=Image.open(filename[1])
    org=org.resize((200,200))
    wm=wm.resize((200,200))
    # new width & height
    org=ImageTk.PhotoImage(org)
    org_img = tk.Label(image=org)
    org_img.image = org
    org_img.place(x=250,y=300)
    wm=ImageTk.PhotoImage(wm)
   
    wm_img = tk.Label(image=wm)
    wm_img.image = wm
    wm_img.place(x=500,y=300)
    img_embed=Image.open(op)
    img_embed=img_embed.resize((200,200))
    img_embed=ImageTk.PhotoImage(img_embed)
    label1 = tk.Label(image=img_embed)
    label1.image = img_embed
    label1.place(x=800,y=300)
    org_img_em_f = tk.Label(my_w,text='Original Image',width=18,font=my_font3)
    org_img_em_f.place(x=300,y=500)
    up_img_em_f = tk.Label(my_w,text='Watermark',width=18,font=my_font3)
    up_img_em_f.place(x=500,y=500)
    w_img_em_f = tk.Label(my_w,text='Watermarked Image ',width=18,font=my_font3)
    w_img_em_f.place(x=800,y=500)


my_w.mainloop()  # Keep the window open
