import time
from tkinter import *
import keyboard
import pyautogui


def StartWriting(times, speed):
    while (keyboard.is_pressed('s') == False):
        a = 3

    while(times != 0):
        pyautogui.press('backspace')
        pyautogui.write(MESSAGE.get('1.0', END))
        pyautogui.press('enter')
        speed = SPEED.get()
        while(speed != 0 and keyboard.is_pressed('q') == False):
            time.sleep(1)
            speed = speed-1
        if (keyboard.is_pressed('q') == True):
            pyautogui.press('backspace')
            break
        times = times-1


# WINDOW ARANGEMENTS
root = Tk()
root.configure(bg='#222222')
root.iconbitmap(r'C:\Projects\Message Looper\icon.ico')
root.title("Message Looper")
root.minsize(150, 100)
root.resizable(False, False)

# SHOW TITLE OF OUR APP
Label(root, text="Message Looper", font='Helvetica 18 bold',
      bg="#222", fg="white").grid(padx=20, pady=10)

# SHOW INSTRUCTIONS


def open_instructions():
    instructions = Toplevel()
    instructions.configure(bg='#222222')
    Label(instructions, text="STEP 1 : Write a Message in the field given below\nSTEP 2 : Click on start button \nSTEP 3 : Select the text field in your prefered messaging app.\nSTEP 4: Set the number of times the message must be sent and time delay in between two messages \nSTEP 5 : press \"s\" to start the looper \n\nIF YOU WANT TO ABORT THE PROGRAM PRESS \"q\".",
          anchor="e", justify=LEFT, bg='#222222', fg='#eeeeee', padx=20, pady=20).pack()
    instructions.mainloop()


Button(root, text="Instructions",
       command=open_instructions, bd=2, width=47, fg='#fff', bg='#444', activebackground='#444', activeforeground='#fff').grid(padx=20, pady=10)

# SHOW MESSAGE BOX
Label(root, text="Write a Message :",
      font='Helvetica 8 bold', bg='#222222', fg='#eeeeee').grid(padx=20, pady=10)
MESSAGE = Text(root, width=30, height=5, bg='#272727',
               bd=9, highlightbackground="yellow", fg='#eeeeee', insertbackground="#eee")
MESSAGE.grid(padx=20, pady=5)

# NUMBER OF TIMES MESSAGE TO BE SENT
Label(root, text="How many times do you want to send that message ?",
      font='Helvetica 8 bold', bg='#222222', fg='#eeeeee').grid(padx=20, pady=10)
TIMES = Entry(root, width=10, bg='#444444', bd=3,
              fg='#eeeeee', insertbackground="#eee")
TIMES.grid(padx=20, pady=5)

# SHOW SPEED CONTROL
Label(root, text="Select the duration of time between 2 messages(in seconds):",
      font='Helvetica 8 bold', bg='#222222', fg='#eeeeee').grid(padx=20, pady=10)
SPEED = Scale(root, orient=HORIZONTAL, from_=0.0, to=10.0,
              tickinterval=0.25, bg='#222222', fg='#eeeeee', activebackground="#333333", bd=0, highlightthickness=0, relief='ridge', troughcolor="#444444")
SPEED.grid(padx=20, pady=0)

# SHOW BUTTON TO START LOOPING
Button(root, text="START", command=lambda: StartWriting(
    int(TIMES.get()), SPEED.get()), bd=2, fg='#fff', bg='#444', width=47, activebackground='#444', activeforeground='#fff').grid(padx=20, pady=30)

# CREDITS
Label(root, text="Made by Srujan",
      font='Helvetica 8 bold', width=60, bg='#2ea44f', fg='#eeeeee').grid()
# START THE APP
root.mainloop()
