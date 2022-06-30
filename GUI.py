import os.path
import tkinter as tk
from tkinter import filedialog
import copyfile
import predict
from PIL import Image, ImageTk

selected = []
file_addr = []
saved_addr = []
saved_addr_unet = []
page = 0
total_page = 0

def back():
    global page
    global saved_addr
    global imTK
    global imTK2
    global saved_addr_unet
    global total_page
    global text
    if saved_addr == []:
        pass
    else:
        try:
            page -= 1
            # print(saved_addr[page])
            im = Image.open(saved_addr[page])
            im2 = Image.open(saved_addr_unet[page])
            w, h = im.size
            # print("size:",w, h)
            if w > img_size:
                h_resize = round(img_size * int(h) / int(w))
                imTK = ImageTk.PhotoImage(im.resize((img_size, h_resize)))
                imTK2 = ImageTk.PhotoImage(im2.resize((img_size, h_resize)))
            else:
                imTK = ImageTk.PhotoImage(im)
                imTK2 = ImageTk.PhotoImage(im2)

            total_page = len(saved_addr)
            text = str(page % total_page + 1)+ " / " + str(total_page)
            page_text.set(text)
        except:
            page = -1
            total_page = len(saved_addr)
            text = str(page % total_page + 1) + " / " + str(total_page)
            page_text.set(text)
            # print(saved_addr[page])
            im = Image.open(saved_addr[page])
            im2 = Image.open(saved_addr_unet[page])
            w, h = im.size
            # print("size:",w, h)
            if w > img_size:
                h_resize = round(img_size * int(h) / int(w))
                imTK = ImageTk.PhotoImage(im.resize((img_size, h_resize)))
                imTK = ImageTk.PhotoImage(im.resize((img_size, h_resize)))

            else:
                imTK = ImageTk.PhotoImage(im)
                imTK2 = ImageTk.PhotoImage(im2)
        image_main.configure(image=imTK)
        image_unet.configure(image=imTK2)

def next():
    global page
    global saved_addr
    global imTK
    global imTK2
    global saved_addr_unet
    global total_page
    if saved_addr == []:
        pass
    else:
        try:
            page += 1
            #print(saved_addr[page])
            im = Image.open(saved_addr[page])
            im2 = Image.open(saved_addr_unet[page])
            w, h = im.size
            #print("size:",w, h)
            if w > img_size:
                h_resize = round(img_size * int(h) / int(w))
                imTK = ImageTk.PhotoImage(im.resize((img_size, h_resize)))
                imTK2 = ImageTk.PhotoImage(im2.resize((img_size, h_resize)))

            else:
                imTK = ImageTk.PhotoImage(im)
                imTK2 = ImageTk.PhotoImage(im2)

            total_page = len(saved_addr)
            text = str(page % total_page + 1) + " / " + str(total_page)
            page_text.set(text)


        except:
            page = 0
            total_page = len(saved_addr)
            text = str(page % total_page + 1) + " / " + str(total_page)
            page_text.set(text)
            #print(saved_addr[page])
            im = Image.open(saved_addr[page])
            im2 = Image.open(saved_addr_unet[page])
            w, h = im.size
            #print("size:",w, h)
            if w > img_size:
                h_resize = round(img_size * int(h) / int(w))
                imTK = ImageTk.PhotoImage(im.resize((img_size, h_resize)))
                imTK = ImageTk.PhotoImage(im.resize((img_size, h_resize)))

            else:
                imTK = ImageTk.PhotoImage(im)
                imTK2 = ImageTk.PhotoImage(im2)

        image_main.configure(image=imTK)
        image_unet.configure(image=imTK2)

def start():
    global saved_addr
    global saved_addr_unet
    global imTK
    global imTK2
    global page
    global total_page
    saved_addr = []
    saved_addr_unet = []
    page = 0
    total_page = 0
    try:
        if selected == []:
            copyfile.deletefile()
            for i in file_addrs:
                saved_addr.append(copyfile.cpfile(i))
                #print("OK")
        else:
            copyfile.deletefile()
            for i in selected:
                saved_addr.append(copyfile.cpfile(i))
        #print(saved_addr)
        predict.predict()
        (path, fname) = os.path.split(saved_addr[0])
        unet_path = os.path.join(path, "results")

        total_page = len(saved_addr)
        text = str(page % total_page + 1) + " / " + str(total_page)
        page_text.set(text)

        for u in os.listdir(unet_path):
            saved_addr_unet.append(os.path.join(unet_path, u))
        #print(saved_addr_unet)
        if saved_addr == []:
            pass
        else:
                #print(saved_addr[page])
                im = Image.open(saved_addr[page])
                im2 = Image.open(saved_addr_unet[page])
                w, h = im.size
                #print("size:",w, h)
                if w > img_size:
                    h_resize = round(img_size * int(h) / int(w))
                    imTK = ImageTk.PhotoImage(im.resize((img_size, h_resize)))
                    imTK2 = ImageTk.PhotoImage(im2.resize((img_size, h_resize)))

                else:
                    imTK = ImageTk.PhotoImage(im)
                    imTK2 = ImageTk.PhotoImage(im2)
        image_main.configure(image=imTK)
        image_unet.configure(image=imTK2)
    except:
        pass

def openfile():
    global file_addrs
    file_addrs = []
    file_path = filedialog.askopenfilenames(filetypes=[('png','*.png'),('jpg','*.jpg')])
    for path in file_path:
        file_addrs.append(path)
    #print(file_addrs)
    for p in file_addrs:
        pic_listbox.insert('end', p)
    #return file_addrs

def picSelected(event):
    global selected
    selected = []
    indexs = pic_listbox.curselection()
    for index in indexs:
        print(pic_listbox.get(index))
        selected.append(pic_listbox.get(index))
    print("------------------")
    return indexs

def define_layout(obj, cols=1, rows=1):
    
    def method(trg, col, row):
        
        for c in range(cols):    
            trg.columnconfigure(c, weight=1)
        for r in range(rows):
            trg.rowconfigure(r, weight=1)

    if type(obj)==list:        
       [ method(trg, cols, rows) for trg in obj ]
    else:
        trg = obj
        method(trg, cols, rows)

window = tk.Tk()
window.title('Window')
align_mode = 'nswe'
pad = 10

img_size = 400
div_size = 400
div1 = tk.Frame(window,  width=div_size*2, height=div_size, bg='blue')
div2 = tk.Frame(window,  width=img_size, height=img_size, bg='orange')
div3 = tk.Frame(window,  width=img_size, height=img_size, bg='green')
div4 = tk.Frame(window,  width=div_size*2 , height=div_size*2, bg='yellow')
div5 = tk.Frame(window,  width=div_size , height=div_size*2)
#div1.pack_propagate(0)

window.update()
#win_size = min( window.winfo_width(), window.winfo_height())
#print(win_size)

div1.grid(column=0, row=0, padx=pad, pady=pad, sticky=align_mode)
div2.grid(column=1, row=0, padx=pad, pady=pad, sticky=align_mode)
div3.grid(column=2, row=0, padx=pad, pady=pad, sticky=align_mode)
div4.grid(column=0, row=1, padx=pad, pady=pad, sticky=align_mode)
div5.grid(column=1, row=1, padx=pad, pady=pad, columnspan=2, sticky=align_mode)

define_layout(window, cols=3, rows=2)
#define_layout([div1, div2, div3, div4, div5])

'''pic list'''
listbox_xbar = tk.Scrollbar(div1,orient="horizontal")
listbox_ybar = tk.Scrollbar(div1)
pic_listbox = tk.Listbox(div1,selectbackground="darkgoldenrod",bd=3,selectmode='multiple',yscrollcommand=listbox_ybar.set,xscrollcommand=listbox_xbar.set)
pic_listbox.bind("<<ListboxSelect>>",picSelected)

listbox_ybar.pack(side="right",fill="y")
pic_listbox.pack(fill="both",expand="true")
listbox_xbar.pack(fill="x")

listbox_xbar.config(command=pic_listbox.xview)
listbox_ybar.config(command=pic_listbox.yview)

define_layout(div1)


'''for oringnal'''
im_main = Image.open('2021-04-09_1618_0.png')
w_main,h_main = im_main.size
if w_main > img_size:
    h_resize = round(img_size * int(h_main) / int(w_main))
    imTK = ImageTk.PhotoImage(im_main.resize((img_size, h_resize)))
else:
    imTK = ImageTk.PhotoImage(im_main)

image_main = tk.Label(div2,image=imTK)
image_main['height'] = img_size
image_main['width'] = img_size

image_main.grid(sticky=align_mode)

'''for unet'''

im_unet = Image.open('2021-04-09_1618_0_predict.png')
w_unet,h_unet = im_unet.size
if w_unet > img_size:
    h_unet_resize = round(img_size * int(h_main) / int(w_main))
    imTK_unet = ImageTk.PhotoImage(im_main.resize((img_size, h_unet_resize)))
else:
    imTK_unet = ImageTk.PhotoImage(im_unet)


image_unet = tk.Label(div3, image=imTK_unet)
image_unet['height'] = img_size
image_unet['width'] = img_size

image_unet.grid(sticky=align_mode)

'''upload and start'''
upload_bt = tk.Button(div4, height=3,text='Upload', fg='Black',relief="raised",activeforeground="green", command=openfile)
upload_bt.grid(column=0, row=0, sticky=align_mode)

start_bt = tk.Button(div4, text='Start', fg='Black',relief="raised",activeforeground="green",command=start)
start_bt.grid(column=1, row=0, sticky=align_mode)

'''page'''
back_bt = tk.Button(div5, text='<', fg='Black',activeforeground="green",command=back)
back_bt.grid(column=3, row=0, sticky=align_mode)

next_bt = tk.Button(div5, text='>', fg='Black',activeforeground="green",command=next)
next_bt.grid(column=5, row=0, sticky=align_mode)

page_text = tk.StringVar()
page_text.set(" / ")
page_lb = tk.Label(div5,textvariable=page_text,fg='black')
page_lb.grid(column=4, row=0, sticky=align_mode)


window.bind("<Escape>",lambda x:window.destroy())


define_layout(div2)
define_layout(div3)
define_layout(div5, cols=9)
window.mainloop()