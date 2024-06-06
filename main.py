from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk 



class QuizStarter:
    def __init__(self, parent):
        self.root = root
        self.root.title("Quiz")
        self.start_button = tk.Button(self.root, text="Continue", bg="Yellow", command=self.start_pressed)
        self.start_button.place(x=300, y=300)
       
        #background_color = "OldLace"
        background_color = "red"
        self.quiz_frame = Frame(self.root, bg=background_color)
        self.quiz_frame.pack(fill='both', expand=True)
        self.bg_image = Image.open("GAME GUI-3.png")
        width, height = 960, 540
        self.resize_image = self.bg_image.resize((width, height))
        self.bg_image = ImageTk.PhotoImage(self.resize_image)

        # Label for image
        self.image_label = Label(self.quiz_frame, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create the "Continue" button
        self.start_button = tk.Button(self.root, text="Continue", bg="Yellow", command=self.start_pressed)
        self.start_button.place(x=300, y=300, width=100, height=50)

        
    def start_pressed(self):
        print("Start button pressed")
    
       






#***********Starting point of the program***********#
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("960x540")
    root.title("Protect")
    quizstarter_object = QuizStarter(root)  
    root.mainloop() #So window won't disooiappear