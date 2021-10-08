import tkinter as tk
from tkinter import font
from tkinter.constants import END, W
from tkinter.font import BOLD
from typing import ForwardRef
from PIL import ImageTk
from selenium.webdriver.support.expected_conditions import frame_to_be_available_and_switch_to_it
import commonapp
import udemy
import linkedin
import jamboree
import perfectelearning
import khanacademy
import netflix
import edX
import amazonlogin
import cognitive

root = tk.Tk()

HEIGHT = 700
WIDTH = 800

#functions
def onclicklistener(i):
    
    if i == '1':
        commonapp.commonapp()

    elif i == '2':
        label['text'] = 'What do you want to search'
        entry.delete(0, END)
        button = tk.Button(frame, text="RUN", font=40,command=lambda: amazonlogin.login(str(entry.get())))
        button.place(relx=0.7, relheight=1, relwidth=0.3)

    elif i == '3':
        perfectelearning.login()


    elif i == '4':
        udemy.login()
    
    elif i == '5':
        linkedin.login()

    elif i == '6':
        khanacademy.login()
    
    elif i == '7':
        netflix.login()
    
    elif i == '8':
        edX.login()
    
    elif i == '9':
        jamboree.login()
    
    elif i == '10':
        cognitive.login()

    
    else:
        entry.delete(0, END)
        label['text'] = '\nIncorrect Values Given\n\nPress any key to see the list again'
        option = entry.get()
        final = str(option)
        if final == "0":
            entry.delete(0, END)
            
        else:
            entry.delete(0, END)
            label["text"] = "Incorrect Option\n\nType respective number to run the bots\n\n1 -  Comman App\n2 -  Amazon\n3 -  Perfect E Learning \n4 -  Udemy\n5 -  Linked In\n6 -  Khan Academy\n7 -  Netflix\n8 -  edX\n9 -  Jamboree Portal\n10 - Cognitive Classes AI"
            

     
    


canvas = tk.Canvas(root, height=HEIGHT , width=WIDTH,bg='#FBFFDF')
canvas.pack(expand='YES', fill='both')


background = 'background.png'
img = ImageTk.PhotoImage(file=background)
canvas.create_image(10,10, image=img)

menu_bar = tk.Menu(root)
exit_bar = tk.Menu(menu_bar , tearoff = 0)
exit_bar.add_command(label='Exit' , command = exit)
menu_bar.add_cascade(label='Exit' , menu=exit_bar)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="RUN", font=40,command=lambda: onclicklistener(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

# button10 = tk.Button(frame, text="QUIT", font=40,command=exit)
# button10.place(relx=0.8, rely=0.1,relheight=0.5, relwidth=0.5)

root.config(menu=menu_bar)


lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame , text="""
Type respective number to run the respective bot\n
1 -  Comman App\n
2 -  Amazon\n
3 -  Perfect E Learning \n
4 -  Udemy\n
5 -  Linked In\n
6 -  Khan Academy\n
7 -  Netflix\n
8 -  edX\n
9 -  Jamboree Portal\n
10 - Cognitive Classes AI
""", anchor=W, justify='left',bg='#FFE5DF',font="Verdana 14 bold")

label.place(relwidth=1, relheight=1)

root.title('BOTS')
root.mainloop()



