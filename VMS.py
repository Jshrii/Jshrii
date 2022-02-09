from tkinter import *
import time
from time import sleep
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox 
import pandas as pd
import winsound
import requests
import json
import smtplib
from gtts import gTTS
from playsound import playsound
import os

root = Tk()
root.title('ventilator Monitoring System')


def open():
    top = Toplevel()
    top.geometry("700x600")
    top.configure(background="black")
    s = ttk.Style()
    s.theme_use('clam')
    s.configure("grey.Horizontal.TProgressbar", foreground='grey', background='grey',width = '20',height = '20')
    my_progress = ttk.Progressbar(top,style = "grey.Horizontal.TProgressbar",orient = HORIZONTAL,length = 300)
    my_progress.pack(pady=60)
    my_progress.place(x = 200 , y = 250)
    #time.sleep(3)
    my_progress.start(20)
    df = pd.read_csv("expiratory.csv")
    #print(df)
    for i in df.index:
        if(df[' flow (L/min)'][i] > 3):
            messagebox.showwarning("Caution","Flow is above the threshold\n"+"flow (L/min) : "+str(df[' flow (L/min)'][i]))
            #winsound.Beep(440, 5000)
            mytext = "Flow is above the threshold\n"+"flow (L/min) : "+str(df[' flow (L/min)'][i])
            language = 'en'
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save("D:\\alert.mp3")
            os.system("D:\\alert.mp3")
            #playsound("D:\\alert.mp3")
            # mention url
            url = "https://www.fast2sms.com/dev/bulkV2"
  
            querystring = {
                "authorization": "q1Hafgzm5QJB7Fr04yu8CvL2NjlRicwVApDGU6nhoK3SdYZIxM7oTjFHAepX4vcWEMgbZ2qtRUNI8a09",
                "message": "Alert from Ventilator",
                "language": "english",
                "route": "q",
                "numbers": "9035895795"}

            headers = {
                'cache-control': "no-cache"
            }
            try:
                response = requests.request("GET", url,
                                            headers = headers,
                                            params = querystring)

                print("SMS Successfully Sent")
            except:
                print("Oops! Something wrong")
                
            str1 = "adsd"
            server = smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login("jayashreedayalan98@gmail.com","Cuboid@12345")
            server.sendmail("jayashreedayalan98@gmail.com","jshri918@gmail.com",message3)
            server.quit()
            break

my_img = ImageTk.PhotoImage(Image.open("Intro_Image.png"))
my_label = Label(image=my_img).pack()

next_btn = PhotoImage(file = 'Next_button.png')
#img_label = Label(image = next_btn)
label2 = Button( root, image = next_btn,highlightthickness = 0, bd = 0,command = open)
label2.place(x = 265 , y = 475)

root.mainloop()
