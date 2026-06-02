from tkinker import *
from PIL import Image,ImageTk
root = Tk()
root.title("image")
root.geometry("400x400")


upload = Image.open("cool.png")

image=ImageTK.PhotoImage(upload)

label = label(root,image=image, height=350, width=300)
label.place(x=50, y=0)
label12 = Label(root, text="this is how you add image in tkinter window")
label12.place(x=40, y=360)
root.mainloop()