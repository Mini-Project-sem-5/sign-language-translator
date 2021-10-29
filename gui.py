# import module from tkinter for UI
from tkinter import *
from tkinter import messagebox
import os
import json
import webbrowser
import threading

with open('gestures.json', 'r') as fp:
    data = json.load(fp)


def hellocallback():
    word = e1.get()
    try:
        os.mkdir('gesture/test/' + str(len(data) + 1).zfill(10))
    except OSError as error:
        print(error)
    try:
        os.mkdir('gesture/train/' + str(len(data) + 1).zfill(10))
    except OSError as error:
        print(error)
    f.destroy()
    os.system("py create_gesture_data.py " + str(len(data) + 1))
    data[len(data)] = word
    with open('gestures.json', 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
    with open('gesturesb.json', 'w', encoding='utf-8') as jsonb:
        jsonb.write("score=["+json.dumps(data, indent=4)+"];")
    os.system("py DataFlair_trainCNN.py " + str(len(data)))


# creating instance of TK
root = Tk()
root.configure(background="white")


def function1():
    global f, e1, e2, e3, e4
    f = Tk()

    l1 = Label(f, text='Gesture Name : ', width=23, height=2)
    e1 = Entry(f, width=40)

    b = Button(f, text='Submit', width=15, height=2, command=hellocallback, bg='blue', fg='white',
               activebackground='green', activeforeground='red')

    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)
    b.grid(row=4, column=0)

    f.mainloop()


def function3():
    os.system("py model_for_gesture.py")


def function6():
    root.destroy()


# stting title for the window
root.title("SIGN LANGUAGE TRANSLATOR")

# creating a text label
Label(root, text="SIGN LANGUAGE TRANSLATOR", font=("times new roman", 20), fg="white", bg="maroon",
      height=2).grid(row=0, rowspan=2, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

# creating first button
Button(root, text="Create Gesture", font=("times new roman", 20), bg="#0D47A1", fg='white', command=function1).grid(
    row=3, columnspan=2, sticky=W + E + N + S, padx=5, pady=5)

# creating third button
Button(root, text="Gesture Translator", font=('times new roman', 20), bg="#0D47A1", fg="white",
       command=function3).grid(row=5, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

# creating attendance button
Button(root, text="Gesture Details", font=('times new roman', 20), bg="#0D47A1", fg="white", command=None).grid(
    row=6, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

Button(root, text="Exit", font=('times new roman', 20), bg="maroon", fg="white", command=function6).grid(row=9,
                                                                                                         columnspan=2,
                                                                                                         sticky=N + E + W + S,
                                                                                                         padx=5, pady=5)

root.mainloop()
