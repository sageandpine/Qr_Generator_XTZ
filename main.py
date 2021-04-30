# Tezos CleanQr Gen: A very basic Qr code generator made with connecting NFT art made on the Tezos blcokchain
# to physical objects in mind. Simply generate a Qr code
# that links to the origin hash of your object being minted, or the tx hash between you and the buyer and print the
# png, attaching it to your object however you feel is appropriate. You can Use this to generate anything else, like
# web address links or poetry. -pc84

from tkinter import messagebox
import pyqrcode
from tkinter import *


# Window
window = Tk()
window.title("Tezos NiFTy QR Gen")
window.config(padx=50, pady=50)


# Canvas
canvas = Canvas(width=500, height=500, highlightthickness=0, bg='#2cc2c6')
bg_image = PhotoImage(file="tezos-3466455-2899243.png")
canvas.create_image(250, 250, image=bg_image)
canvas.pack()


#Qr Code Generate Function
def generate():
    embed_this = data_input.get()
    title_of_piece = title_input.get()
    my_qr = pyqrcode.create(f'{title_of_piece}: Operation hash: {embed_this}', error='L', version=27, mode='binary')
    my_qr.png(f'{title_of_piece}_qr.png', scale=2, module_color=[0, 0, 0, 0], background=[0xff, 0xff, 0xff])
    messagebox.showinfo(title="All Done", message="That's it! A file has been saved for you and the Qr code will show in your browser when you close this message!")
    data_input.delete(0, END)
    title_input.delete(0, END)
    my_qr.show()

# Title of Work
title_label = Label(text="Title of Work")
title_label.pack()
title_input= Entry(width=48)
title_input.pack()

# Data to Encode
data_label = Label(text="Data to Encode:")
data_label.pack()
data_input = Entry(width=48)
data_input.pack()
data_input.focus()


# Buttons
gen_nifty_button = Button(width=25, text="Generate NiFTy QR code >", command=generate)
gen_nifty_button.pack()


window.mainloop()

