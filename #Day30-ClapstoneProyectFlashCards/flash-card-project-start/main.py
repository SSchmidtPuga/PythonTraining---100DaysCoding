from tkinter import *
from PIL import ImageTk, Image
BACKGROUND_COLOR = "#B1DDC6"
import random

# ---------------------------------------------- Random word------------------------------------------------------------

import pandas as pd

words = pd.read_csv("/Users/sebastianschmidtpuga/PycharmProjects/#Day30-ClapstoneProyectFlashCards/flash-card-project"
                    "-start/data/french_words.csv")

French_words = words["French"].tolist()
English_words = words["English"].tolist()


number  = []
French_word = []
English_word = []

def random_word():
    global number
    number = random.randint(0,100)
    French_word = French_words[number]
    card1.itemconfig(cardword,  text=French_word )
    card1.itemconfig(cardlenaguage, text= "French")


# ----------------------------------------------eliminate card------------------------------------------------------------


def delete_words():
    global French_word
    global French_words
    global English_words
    global English_word
    French_words.remove(French_word)
    English_words.remove(English_word)







# ---------------------------------------------- UI/UX ----------------------------------------------------------------

window = Tk()
window.title("Flash cards Claprtone proyect")
window.minsize(width=700, height=600)
window.config(bg = BACKGROUND_COLOR)



#Cards

my_card1 = ImageTk.PhotoImage(Image.open("images/card_front.png"))
card1 = Canvas( width=600, height=400)
card1.config(bg = BACKGROUND_COLOR, highlightthickness = 0)
card1.create_image(100,100, image= my_card1)
cardword = card1.create_text(300,225,text= "", font= ("Ariel", 60,"bold"))
cardlenaguage = card1.create_text(300, 150, text= "French", font= ("Ariel", 40,"italic"))
card1.place(x=50, y =25)

#Buttons

my_image2 = ImageTk.PhotoImage(Image.open("/Users/sebastianschmidtpuga/PycharmProjects/#Day30"
                                         "-ClapstoneProyectFlashCards/flash-card-project-start/images/wrong.png"))
incorrect = Button(image=my_image2, highlightthickness=0, command = random_word)
incorrect.place(x=100, y=475)


my_image = ImageTk.PhotoImage(Image.open("/Users/sebastianschmidtpuga/PycharmProjects/#Day30"
                                         "-ClapstoneProyectFlashCards/flash-card-project-start/images/right.png"))
Correct = Button(image=my_image, highlightthickness=0,  command = random_word)
Correct.place(x=425, y=475)



random_number = random_word()

def flipcards():
    global number
    window.after(10000, flipcards)
    English_word = English_words[number]
    card1.itemconfig(cardword, text=English_word)
    card1.itemconfig(cardlenaguage, text="English")

window.after(10000, flipcards)











window.mainloop()