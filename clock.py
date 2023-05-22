from tkinter import *
from PIL import Image,ImageTk
from datetime import datetime
import pytz
import time

root = Tk()

root.title("Clock")
root.geometry("800x900")

clock_img = ImageTk.PhotoImage(Image.open("clock.jpg"))

label_ind = Label(root,text="India: ")
label_ind.place(relx=0.2,rely=0.3,anchor=CENTER)

clock_india = Label(root)
clock_india["image"]=clock_img
clock_india.place(relx=0.2,rely=0.5,anchor=CENTER)

time_ind = Label(root)
time_ind.place(relx=0.2,rely=0.7,anchor=CENTER)

#USA
label_usa = Label(root,text="U.S.A: ")
label_usa.place(relx=0.8,rely=0.3,anchor=CENTER)

clock_usa = Label(root)
clock_usa["image"]=clock_img
clock_usa.place(relx=0.8,rely=0.5,anchor=CENTER)

time_usa = Label(root)
time_usa.place(relx=0.8,rely=0.7,anchor=CENTER)

class india_time():
    def time(self):
        home = pytz.timezone("Asia/Kolkata")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        time_ind["text"]=current_time
        
        time_ind.after(200,self.time)
        
class usa_time():
    def time(self):
        home = pytz.timezone("US/Central")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        time_usa["text"]=current_time
        
        time_usa.after(200,self.time)
        
us_time_obj = usa_time()
btn_usa=Button(root,text="USA TIME",command=us_time_obj.time)

ind_time_obj = india_time()
btn_ind=Button(root,text="INDIA TIME",command=ind_time_obj.time)

btn_ind.place(relx=0.2,rely=0.9,anchor=CENTER)
btn_usa.place(relx=0.8,rely=0.9,anchor=CENTER)

root.mainloop()