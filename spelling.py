from tkinter import *
from textblob import TextBlob

def check_spelling():
    a = TextBlob(spell_check.get())
    spell = Label(window , text= "THE CORRECT SPELLING IS :" , font=("Arial", 30 ,"bold"), bg = "grey")
    spell.pack()
    correct_text = Label(window , text = str(a.correct()),font=("Arial",45 ,"bold") , bg ="pink")
    correct_text.pack()

window = Tk()
window.title("MY SPELLING CHECKER")
window.geometry("800x600")
window.config(background = "Beige")


text_heading = Label(window,text= "SPELLING CHECKER" , font = ("Arial",40 ,"bold"), bg="black" , fg = "white")
text_heading.pack()

text_check = Label(window , text = "ENTER THE TEXT" ,font = ("Arial" , 30 , "bold"), bg= "lavender" , fg = "black")
text_check.pack()

spell_check = Entry(window , font = ("Arial" , 45 , "bold") , width=500,bg = "blue")
spell_check.pack()

Check_button = Button(window , text ="Check" , font = ("Arial" ,30 , "bold") , fg = "white" , bg = "black" , command = check_spelling)
Check_button.pack()





window.mainloop()
