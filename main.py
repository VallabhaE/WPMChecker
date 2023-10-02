import random
from tkinter import *
import time

window = Tk()
window.title("WPMChecker")
window.config(bg="white")
words=["In the vast tapestry of existence, every thread of experience, every emotion woven into the fabric of our lives, contributes to the masterpiece that is the story of who we are.",
       "Amidst the kaleidoscope of changing seasons, nature unveils its breathtaking symphony, where the rustling leaves whisper secrets of ancient trees, and the dance of sunlight and shadows paints an ever-evolving portrait of the world.",
       "As the moonlight cascades through the silken veil of the night, casting ethereal glow upon the slumbering earth, one can't help but marvel at the celestial poetry written across the canvas of the cosmos."

,"In the labyrinth of human connection, where each encounter leaves an indelible mark on the soul, we navigate the intricate web of relationships, finding solace in the shared laughter, and strength in the bonds that withstand the tests of time."
       "Beneath the city's bustling facade, a symphony of life unfolds, where the rhythmic footsteps of hurried commuters merge with the melodic hum of traffic, creating a pulsating heartbeat that resonates through the urban landscape."]



def word():
    global words
    button.config(state=DISABLED)
    button2.config(state=ACTIVE)
    a=random.choice(words)
    if not a:
        label1 = Label(text=a, bg="white")
        label1.pack()
        label1.config(text="No More Words Present Inside list you can wait till time end,because you are good to go",
                      bg="red")

    if a:
        words.remove(a)
        label1 = Label(text=a, bg="white")
        label1.pack()

def check():
    button.config(state=ACTIVE)
    button2.config(state=DISABLED)
    data = name.get()
    score = len(data)/5
    Label(text="Score: "+str(score),bg="white",fg="red",font=(40)).pack(padx=30,pady=20)

label = Label(text="Start Assignment",font=("Ariel",15))
label.pack(side="top")
button = Button(text="Start",command=lambda :word())
button.pack()
button2=Button(text="Stop",command=lambda :check())
button2.pack()
name=Entry(width=50, font=('Arial 24'))
name.pack(padx=40, pady=50)















window.mainloop()