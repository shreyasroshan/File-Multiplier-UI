import tkinter
from tkinter import filedialog
from tkinter import messagebox
import os
import sys
import shutil
window = tkinter.Tk()
window.title("File_Multiplier")

# file count field

global file_count
file_count = tkinter.IntVar()
label1 = tkinter.Label(window, text = "File_Count").grid(row = 0)
entry1 = tkinter.Entry(window,width=40,textvariable=file_count)
entry1.grid(row = 0, column = 3)

# input_path function

def inputpath():
    global source
    source = filedialog.askdirectory()
    entry2.delete(0,tkinter.END)
    entry2.insert(tkinter.END,source)
    return source

# output_path function

def outputpath():
    global destination
    destination = filedialog.askdirectory()
    entry3.delete(0,tkinter.END)
    entry3.insert(tkinter.END,destination)
    messagebox.showinfo("Check","Make sure the folder selected doesn't contain the source before Generating")
    return destination 

# input_path widgets

label2 = tkinter.Label(window, text = "Input_Path").grid(row = 2)
browse1 = tkinter.Button(window,text="Browse",command=inputpath)
browse1.grid(row = 2, column = 5)
entry2 = tkinter.Entry(window,width=40)
entry2.grid(row = 2, column = 3)

# output_path widgets

label3 = tkinter.Label(window, text = "Output_Path").grid(row = 4)
browse2 = tkinter.Button(window,text="Browse",command=outputpath)
browse2.grid(row = 4, column = 5)
entry3=tkinter.Entry(window,width=40)
entry3.grid(row = 4, column = 3)

def finalprocess():
    
    # path check
    
    if os.path.exists(destination):
        shutil.rmtree(destination)
        os.makedirs(destination)
    else:
        os.makedirs(destination)
    
    # file extension extraction
    
    extension = os.listdir(source)
    extension = (extension[0].split("."))[1]
    
    # Temp declaration
    
    Temp = destination+'\\'+'Temp'
    
    # file copy paste section
    
    count = 0
    for i in range(file_count.get()):
        new_file_name = str(i)+'.'+extension
        os.makedirs(Temp)
        if count < len(os.listdir(source)):
            shutil.copy(source+'\\'+os.listdir(source)[count],Temp,follow_symlinks=True)
            os.rename(Temp+'\\'+os.listdir(Temp)[0],Temp+'\\'+new_file_name)
            shutil.copy(Temp+'\\'+os.listdir(Temp)[0],destination,follow_symlinks=True)
            shutil.rmtree(Temp)
            count+=1
        else:
            count=0
            shutil.copy(source+'\\'+os.listdir(source)[count],Temp,follow_symlinks=True)
            os.rename(Temp+'\\'+os.listdir(Temp)[0],Temp+'\\'+new_file_name)
            shutil.copy(Temp+'\\'+os.listdir(Temp)[0],destination,follow_symlinks=True)
            shutil.rmtree(Temp)
            count+=1
            
    messagebox.showinfo("Success","Process Done :)")
    
# generate widget
    
generate = tkinter.Button(window,text="Generate",command=finalprocess)
generate.grid(row = 6, column = 3)

# app starter

tkinter.mainloop() 
