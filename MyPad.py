# MyPad-TextEdior
Texteditor In Tkinter

from tkinter import Tk, scrolledtext, Menu, filedialog,END, messagebox, simpledialog
import tkinter.scrolledtext as ScrolledText
import os


# Root For Main Window
root=Tk(className=" MyPad")
textArea = scrolledtext.ScrolledText(root, width=100, height=80)
textArea.pack()
#
#functions
#
def newFile():
    # There is content?
    if len(textArea.get('1.0',END+'-1c')) >0 :
        if messagebox.askyesno("Save?","Do you wish to Save?"):
            savefile()
    textArea.delete('1.0',END)
        
def openFile():
    file=filedialog.askopenfile(parent=root,title="select a text file",filetype=(("Text file", "*.txt"),("All files","*.*")))
    
    if file!=None:
        contents=file.read()
        textArea.insert('1.0',contents)
        file.close()
        
def saveFile():
    file = filedialog.asksaveasfile(mode='w')
    
    if file!=None:
        # Slice off the last character from get , as an extra return (enter)  is added
        data=textArea.get('1.0',END+'-1c')
        file.write(data)
        file.close()
def findInFile():
    findstring=simpledialog.askstring("find..........","Enter Text")
    textData=textArea.get('1.0',END)
    occurs = textData.upper().count(findstring.upper())
    if textData.upper().count(findstring.upper()):
         label1 = messagebox.showinfo("Result",findstring + " has " +str(occurs) +" occurences")
    else:
         l2 = messagebox.showinfo("Result","No match found") 
         
def undo_():
    textArea.edit_undo()

def redo_():
    textArea.edit_redo()
def FontHelvetica():
   global text
   textArea.config(font="Helvetica")

def FontCourier():
   global text
   textArea.config(font="Courier")
   
def FontTimes():
   global text
   textArea.config(font="Times")   

def FontArial():
   global text
   textArea.config(font="Arial")
           
def FontChiller():
   global text
   textArea.config(font="Chiller") 

   
def FontCorbel():
   global text
   textArea.config(font="Corbel")
   
def FontEdwardianScriptITC():
   global text
   textArea.config(font="Edwardian Script ITC")
def FontFreestyleScript():
   global text
   textArea.config(font="Freestyle Script")
   
def about():
        label=messagebox.showinfo("A python Alternative to NotePad Created by Arun Bhabhoria !!!!!!","All  Rights  Reserved")
        
def exitRoot():
    if messagebox.askyesno("Quit","Are you sure you want to quit?"):
        root.destroy()

# Menu Options
menu=Menu(root)
root.config(menu=menu)
fileMenu=Menu(menu)
menu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_cascade(label="New",command=newFile)
fileMenu.add_cascade(label="Open" ,command=openFile)
fileMenu.add_cascade(label="Save",command=saveFile)
fileMenu.add_cascade(label="Find",command=findInFile)
fileMenu.add_cascade(label="Print")
fileMenu.add_separator()
fileMenu.add_cascade(label="Exit",command=exitRoot)

editMenu = Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label = "Undo",command=undo_)
editMenu.add_command(label = "Redo",command=redo_)

fontMenu = Menu(menu) 
menu.add_cascade(label="Fonts",menu=fontMenu)
fontMenu.add_checkbutton(label="FreestyleScript",command=FontFreestyleScript)
fontMenu.add_checkbutton(label="Courier",command=FontCourier)
fontMenu.add_checkbutton(label="Times New Roman",command=FontTimes)  
fontMenu.add_checkbutton(label="Arial",command=FontArial)  
fontMenu.add_checkbutton(label="Chiller",command=FontChiller)
fontMenu.add_checkbutton(label="EdwardianScriptITC",command=FontEdwardianScriptITC)
fontMenu.add_checkbutton(label="Corbel",command= FontCorbel)



helpMenu=Menu(menu)
menu.add_cascade(label="Help")
menu.add_cascade(label="About",command=about)



#keep Window Open
root.mainloop()

