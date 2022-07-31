# importing the module
import re
import geocoder
import folium
from tkinter import *


# opening and reading the file
with open("textip.txt") as fh:
    fstring = fh.readlines()

# declaring the regex pattern for IP addresses
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

# initializing the list object
lst = []

# extracting the IP addresses
for line in fstring:
    lst.append(pattern.search(line))

res = []
for val in lst:
    if val != None :
        res.append(val)
# print(res)


mynm=str(res)
# li = list(mynm.split("="))
# mylist=str(li[2])
# li1=list(mylist.split("'"))
# print(li1[1])

a= re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', mynm).group()
# print("**************** IP ADDRESS OF EMAIL**********************")
# print(f"                    {a}                              ")
# print("**********************************************************")


def location():
    ip = geocoder.ip(str(a))
    # print("*********************Location of Email********************\n")
    # print(f"   Country-------------------->{ip.country}")
    # print(f"   State---------------------->{ip.state}")
    # print(f"   City----------------------> {ip.city}")
    # print(f"   latitude and longitude ---->{ip.latlng}")
    # print("  ",ip.address)
    # print("\n********************************************************")
    # print(ip.street)
    # print(ip.housenumber)

    global l1,l2,l3,l4,l5,l6
    # win=Toplevel(root)
    # win.geometry("500x600")
    l1 = Label(win, text=(a), font=('Helvetica', 30, 'bold'), fg='black')
    l1.pack(padx=15,pady=15)
    l2=Label(win,text=("Country----->",ip.country),font=('Arial', 15 , 'bold'), fg = 'green')
    l2.pack()
    l3=Label(win,text=("City-------->",ip.city),font=('Arial', 15 , 'bold'), fg = 'green')
    l3.pack()
    l4=Label(win,text=("State------->",ip.state),font=('Arial', 15 , 'bold'), fg = 'green')
    l4.pack()
    l5=Label(win,text=("Longitude---->",ip.latlng),font=('Arial', 15 , 'bold'), fg = 'green')
    l5.pack()
    l6=Label(win,text=("Address------>",ip.address),font=('Arial', 15 , 'bold'), fg = 'green')
    l6.pack()
#     b['state']=DISABLED


# Define a function to clear the input text
def on_click():
   l1.destroy()
   l2.destroy()
   l3.destroy()
   l4.destroy()
   l5.destroy()
   l6.destroy()
   b['state']=NORMAL


# def remove_text():
#     l1.config(text="")
#     l2.config(text="")
#     l3.config(text="")
#     l4.config(text="")
#     l5.config(text="")
#     l6.config(text="")



# location()
# location = ip.latlng
# map = folium.Map(location=location, zoom_start=10)
# folium.CircleMarker(location=location, radius=50, color="red").add_to(map)
# folium.Marker(location).add_to(map)
# mapon_click()
# map.save("map.html")


win=Tk()
win.geometry("1200x600")
b = Button(win, text = 'Location', font=('Arial', 25 , 'bold'), fg = 'white', bg = 'red', command = location,borderwidth=5)
b.pack(padx=100,side=LEFT)
b1=Button(win, text="Clear", font=('Arial', 25 , 'bold'),fg = 'white', bg = 'black',command=on_click,borderwidth=5)
b1.pack(padx=100,side=RIGHT)
# Button(win, text="Delete", command=remove_text).pack()
win.mainloop()





















