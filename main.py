# from tkinter import *
# from tkinter import messagebox
# import requests
# from PIL import Image, ImageTk
# from io import BytesIO
# import urllib

# class Request:
#     def __init__(self,methods ,args):
#         self.args = args

# def search(CustomRequest):
#     custom_request = CustomRequest('GET', {'search': Search.get()})

#     if custom_request.method == 'GET':
#         search = urllib.parse.quote(custom_request.args.get('search', ''))
#         url = f"https://www.googleapis.com/books/v1/volumes?q={search}&maxResults=5"
#         response = requests.get(url)
#         # print(response.json())
        
#         if response.status_code == 200:   #200 means the request was successful, 404 means the page was not found ,401 means unauthorized
#             data = response.json()
#             for item in data.get('items',[]):
#                 volume_info = item.get('volumeInfo',{})
#                 title=volume_info.get('title','N/A')
#                 publisher=volume_info.get('publisher','N/A')
#                 published_date=volume_info.get('publishedDate','N/A')
#                 authors=volume_info.get('authors',['N/A'])
#                 rating=volume_info.get('averageRating','N/A')
#                 image_link=volume_info.get('imageLinks',{})
#                 image=image_link.get('thumbnail') if 'thumbnail' in image_link else None

#                 print(title)   
#                 print(publisher)
#                 print(published_date)
#                 print(authors)
#                 print(rating)
#                 print(image)

# def show_menu(event):
#     menu.post(event.x_root, event.y_root)



# root=Tk()
# root.title("Book Recommender")
# root.geometry("1250x700")
# root.config(bg="#111119")

# #################################################################################################

# # icon

# icon_image = PhotoImage(file=r"D:\book_recomendation_tkinter\Images\icon.png")
# root.iconphoto(False, icon_image)

# # background image

# background_image = PhotoImage(file=r"D:\book_recomendation_tkinter\Images\background.png")
# Label(root, image=background_image, bg="#111119").place(x=-2, y=-2)

# # logo

# logo_image = PhotoImage(file=r"D:\book_recomendation_tkinter\Images\logo.png")
# Label(root, image=logo_image, bg="#0099ff").place(x=300, y=80)

# # heading

# heading = Label(root, text="Book Recommender", font=("Loto", 30, "bold"), bg="#0099ff", fg="white")
# heading.place(x=410, y=90)

# # search background

# search_image = PhotoImage(file=r"D:\book_recomendation_tkinter\Images\Rectangle 2.png")
# Label(root, image=search_image, bg="#0099ff").place(x=300, y=155)

# # entry box / search bar

# Search=StringVar()
# entry_box = Entry(root, textvariable=Search, width=30, font=("Loto", 25), bg="white" ,fg="black" ,bd=0)
# entry_box.place(x=415, y=172)

# # search button

# recommand_button = PhotoImage(file=r"D:\book_recomendation_tkinter\Images\Search.png")
# recommand_button=Button(root, image=recommand_button, bg="#0099ff", bd=0,activebackground="#252532", cursor="hand2")
# recommand_button.place(x=860, y=169)

# # setting button

# setting_button = PhotoImage(file=r"D:\book_recomendation_tkinter\Images\setting.png")
# setting=Button(root, image=setting_button, bg="#0099ff", bd=0,activebackground="#0099ff", cursor="hand2")
# setting.place(x=1050, y=175)
# setting.bind("<Button-1>", show_menu)


# menu=Menu(root, tearoff=0) #tearoff removes the line from the menu

# check_var =BooleanVar()
# menu.add_checkbutton(label="Publish Date", variable=check_var,command=lambda:print(f"Date option is {'chacked' if check_var.get() else 'not chacked'}"))

# check_var2 =BooleanVar()
# menu.add_checkbutton(label="Ratings", variable=check_var2,command=lambda:print(f"rating check option is {'chacked' if check_var2.get() else 'not chacked'}"))


# # logout button

# logout_button = PhotoImage(file=r"D:\book_recomendation_tkinter\Images\logout.png")
# Button(root, image=logout_button, bg="#0099ff", bd=0, cursor="hand1",command=lambda:root.destroy()).place(x=1150, y=20)

# ############################################################################################

# frame1=Frame(root,width=150,height=240, bg="white")
# frame2=Frame(root,width=150,height=240, bg="white")
# frame3=Frame(root,width=150,height=240, bg="white")
# frame4=Frame(root,width=150,height=240, bg="white")
# frame5=Frame(root,width=150,height=240, bg="white")
# frame1.place(x=160, y=350)
# frame2.place(x=360, y=350)
# frame3.place(x=560, y=350)
# frame4.place(x=760, y=350)
# frame5.place(x=960, y=350)


# # Book Title
# text={'a1':Label(frame1, text="The Alchemist", font=("arial", 10), bg="white", fg="black"),'a2':Label(frame2, text="The Alchemist", font=("arial", 10), bg="white", fg="black"),'a3':Label(frame3, text="The Alchemist", font=("arial", 10), bg="white", fg="black"),'a4':Label(frame4, text="The Alchemist", font=("arial", 10), bg="white", fg="black"),'a5':Label(frame2, text="The Alchemist", font=("arial", 10), bg="white", fg="black")}

# text['a1'].place(x=10,y=4)
# text['a2'].place(x=10,y=4)
# text['a3'].place(x=10,y=4)
# text['a4'].place(x=10,y=4)
# text['a5'].place(x=10,y=4)

# # poster image of book

# image={'b1':Label(frame1, bg="white"),'b2':Label(frame2, bg="white"),'b3':Label(frame3, bg="white"),'b4':Label(frame4, bg="white"),'b5':Label(frame5, bg="white")}

# image['b1'].place(x=10,y=40)
# image['b2'].place(x=10,y=40)
# image['b3'].place(x=10,y=40)
# image['b4'].place(x=10,y=40)
# image['b5'].place(x=10,y=40)

# # second frame

# frame11=Frame(root,width=150,height=50, bg="#e6e6e6")
# frame22=Frame(root,width=150,height=50, bg="#e6e6e6")
# frame33=Frame(root,width=150,height=50, bg="#e6e6e6")
# frame44=Frame(root,width=150,height=50, bg="#e6e6e6")
# frame55=Frame(root,width=150,height=50, bg="#e6e6e6")
# frame11.place(x=160, y=600)
# frame22.place(x=360, y=600)
# frame33.place(x=560, y=600)
# frame44.place(x=760, y=600)
# frame55.place(x=960, y=600)

# # published date
# text2={'a11':Label(frame11, text="date", font=("arial", 10), bg="#e6e6e6", fg="red"),'a22':Label(frame22,text='date',font=("arial",10),bg='#e6e6e6',fg="red"),'a33':Label(frame33,text='date',font=("arial",10),bg='#e6e6e6',fg="red"),'a44':Label(frame44,text='date',font=("arial",10),bg='#e6e6e6',fg="red"),'a55':Label(frame55,text='date',font=("arial",10),bg='#e6e6e6',fg="red")}

# text2['a11'].place(x=10,y=4)
# text2['a22'].place(x=10,y=4)
# text2['a33'].place(x=10,y=4)
# text2['a44'].place(x=10,y=4)
# text2['a55'].place(x=10,y=4)

# # rating

# text3={'a111':Label(frame11, text="rating", font=("arial", 10), bg="#e6e6e6", fg="red"),'a222':Label(frame22,text='rating',font=("arial",10),bg='#e6e6e6',fg="red"),'a333':Label(frame33,text='rating',font=("arial",10),bg='#e6e6e6',fg="red"),'a444':Label(frame44,text='rating',font=("arial",10),bg='#e6e6e6',fg="red"),'a555':Label(frame55,text='rating',font=("arial",10),bg='#e6e6e6',fg="red")}

# text3['a111'].place(x=20,y=30)
# text3['a222'].place(x=20,y=30)
# text3['a333'].place(x=20,y=30)
# text3['a444'].place(x=20,y=30)
# text3['a555'].place(x=20,y=30)

# root.mainloop()


from tkinter import *
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO
import urllib

class CustomRequest:  # * Renamed the class to CustomRequest
    def __init__(self, method, args):
        self.args = args
        self.method = method  # * Added the method attribute


inc = 0
def fetch_information(title, poster, date, rating):  # * Updated the parameter order
    global inc
    inc += 1
    text[f'a{inc}'].config(text=title)

    if check_var.get():
        text2[f'a{inc}{inc}'].config(text=date)
    
    else:
        text2[f'a{inc}{inc}'].config(text="")

    if check_var2.get():
        text3[f'a{inc}{inc}{inc}'].config(text=rating)
    
    else:
        text3[f'a{inc}{inc}{inc}'].config(text="")


    response = requests.get(poster)  # * Fixed the variable passed to requests.get
    img_data = response.content
    img = (Image.open(BytesIO(img_data)))
    resized_image = img.resize((130, 190))

    photo2 = ImageTk.PhotoImage(resized_image)
    image[f'b{inc}'].config(image=photo2)
    image[f'b{inc}'].image = photo2


def search():
    global inc
    inc = 0 
    custom_request = CustomRequest('GET', {'search': Search.get()})

    if custom_request.method == 'GET':
        search_term = urllib.parse.quote(custom_request.args.get('search', ''))
        url = f"https://www.googleapis.com/books/v1/volumes?q={search_term}&maxResults=5"
        response = requests.get(url)
        # print(response.json())
        
        if response.status_code == 200:   #200 means the request was successful, 404 means the page was not found ,401 means unauthorized
            data = response.json()
            for item in data.get('items', []):
                volume_info = item.get('volumeInfo', {})
                title = volume_info.get('title', 'N/A')
                publisher = volume_info.get('publisher', 'N/A')
                published_date = volume_info.get('publishedDate', 'N/A')
                authors = volume_info.get('authors', ['N/A'])
                rating = volume_info.get('averageRating', 'N/A')
                image_link = volume_info.get('imageLinks', {})
                image_url = image_link.get('thumbnail') if 'thumbnail' in image_link else None  # * Changed variable name to image_url

                print(title)   
                print(publisher)
                print(published_date)
                print(authors)
                print(rating)
                print(image_url)  # * Updated the print statement to use image_url

                fetch_information(title, image_url, published_date, rating)  # * Updated the parameter order
                
                if check_var.get() or check_var2.get():
                    frame11.place(x=160, y=600)
                    frame22.place(x=360, y=600)
                    frame33.place(x=560, y=600)
                    frame44.place(x=760, y=600)
                    frame55.place(x=960, y=600)
                else:
                    frame11.place_forget()
                    frame22.place_forget()
                    frame33.place_forget()
                    frame44.place_forget()
                    frame55.place_forget()
                   

        else:
            messagebox.showerror("Error", "Failed to fetch data from Google Books API.")

def show_menu(event):
    menu.post(event.x_root, event.y_root)

root = Tk()
root.title("Book Recommender")
root.geometry("1250x700")
root.config(bg="#111119")
root.resizable(False, False)

# icon
icon_image = PhotoImage(file=r"D:\book_recomendation_tkinter\Images\icon.png")
root.iconphoto(False, icon_image)

# background image
background_image = PhotoImage(file=r"D:\book_recomendation_tkinter\Images\background.png")
Label(root, image=background_image, bg="#111119").place(x=-2, y=-2)

# logo
logo_image = PhotoImage(file=r"D:\book_recomendation_tkinter\Images\logo.png")
Label(root, image=logo_image, bg="#0099ff").place(x=300, y=80)

# heading
heading = Label(root, text="Book Recommender", font=("Loto", 30, "bold"), bg="#0099ff", fg="white")
heading.place(x=410, y=90)

# search background
search_image = PhotoImage(file=r"D:\book_recomendation_tkinter\Images\Rectangle 2.png")
Label(root, image=search_image, bg="#0099ff").place(x=300, y=155)

# entry box / search bar
Search = StringVar()
entry_box = Entry(root, textvariable=Search, width=30, font=("Loto", 25), bg="white", fg="black", bd=0)
entry_box.place(x=415, y=172)

# search button
recommand_button_image = PhotoImage(file=r"D:\book_recomendation_tkinter\Images\Search.png")
recommand_button = Button(root, image=recommand_button_image, bg="#0099ff", bd=0, activebackground="#252532", cursor="hand2", command=search)  # * Added command=search
recommand_button.place(x=860, y=169)

# setting button
setting_button = PhotoImage(file=r"D:\book_recomendation_tkinter\Images\setting.png")
setting = Button(root, image=setting_button, bg="#0099ff", bd=0, activebackground="#0099ff", cursor="hand2")
setting.place(x=1050, y=175)
setting.bind("<Button-1>", show_menu)

menu = Menu(root, tearoff=0) #tearoff removes the line from the menu

check_var = BooleanVar()
menu.add_checkbutton(label="Publish Date", variable=check_var, command=lambda: print(f"Date option is {'checked' if check_var.get() else 'not checked'}"))

check_var2 = BooleanVar()
menu.add_checkbutton(label="Ratings", variable=check_var2, command=lambda: print(f"Rating check option is {'checked' if check_var2.get() else 'not checked'}"))

# logout button
logout_button = PhotoImage(file=r"D:\book_recomendation_tkinter\Images\logout.png")
Button(root, image=logout_button, bg="#0099ff", bd=0, cursor="hand1", command=lambda: root.destroy()).place(x=1150, y=20)

frame1 = Frame(root, width=150, height=240, bg="white")
frame2 = Frame(root, width=150, height=240, bg="white")
frame3 = Frame(root, width=150, height=240, bg="white")
frame4 = Frame(root, width=150, height=240, bg="white")
frame5 = Frame(root, width=150, height=240, bg="white")
frame1.place(x=160, y=350)
frame2.place(x=360, y=350)
frame3.place(x=560, y=350)
frame4.place(x=760, y=350)
frame5.place(x=960, y=350)

# Book Title
text = {'a1': Label(frame1, text="The Alchemist", font=("arial", 10), bg="white", fg="black"),
        'a2': Label(frame2, text="The Alchemist", font=("arial", 10), bg="white", fg="black"),
        'a3': Label(frame3, text="The Alchemist", font=("arial", 10), bg="white", fg="black"),
        'a4': Label(frame4, text="The Alchemist", font=("arial", 10), bg="white", fg="black"),
        'a5': Label(frame5, text="The Alchemist", font=("arial", 10), bg="white", fg="black")}

text['a1'].place(x=10, y=4)
text['a2'].place(x=10, y=4)
text['a3'].place(x=10, y=4)
text['a4'].place(x=10, y=4)
text['a5'].place(x=10, y=4)

# poster image of book
image = {'b1': Label(frame1, bg="white"),
         'b2': Label(frame2, bg="white"),
         'b3': Label(frame3, bg="white"),
         'b4': Label(frame4, bg="white"),
         'b5': Label(frame5, bg="white")}

image['b1'].place(x=10, y=40)
image['b2'].place(x=10, y=40)
image['b3'].place(x=10, y=40)
image['b4'].place(x=10, y=40)
image['b5'].place(x=10, y=40)

# second frame
frame11 = Frame(root, width=150, height=50, bg="#e6e6e6")
frame22 = Frame(root, width=150, height=50, bg="#e6e6e6")
frame33 = Frame(root, width=150, height=50, bg="#e6e6e6")
frame44 = Frame(root, width=150, height=50, bg="#e6e6e6")
frame55 = Frame(root, width=150, height=50, bg="#e6e6e6")


# published date
text2 = {'a11': Label(frame11, text="date", font=("arial", 10), bg="#e6e6e6", fg="red"),
         'a22': Label(frame22, text='date', font=("arial", 10), bg='#e6e6e6', fg="red"),
         'a33': Label(frame33, text='date', font=("arial", 10), bg='#e6e6e6', fg="red"),
         'a44': Label(frame44, text='date', font=("arial", 10), bg='#e6e6e6', fg="red"),
         'a55': Label(frame55, text='date', font=("arial", 10), bg='#e6e6e6', fg="red")}

text2['a11'].place(x=10, y=4)
text2['a22'].place(x=10, y=4)
text2['a33'].place(x=10, y=4)
text2['a44'].place(x=10, y=4)
text2['a55'].place(x=10, y=4)

# rating
text3 = {'a111': Label(frame11, text="rating", font=("arial", 10), bg="#e6e6e6", fg="red"),
         'a222': Label(frame22, text='rating', font=("arial", 10), bg='#e6e6e6', fg="red"),
         'a333': Label(frame33, text='rating', font=("arial", 10), bg='#e6e6e6', fg="red"),
         'a444': Label(frame44, text='rating', font=("arial", 10), bg='#e6e6e6', fg="red"),
         'a555': Label(frame55, text='rating', font=("arial", 10), bg='#e6e6e6', fg="red")}

text3['a111'].place(x=20, y=30)
text3['a222'].place(x=20, y=30)
text3['a333'].place(x=20, y=30)
text3['a444'].place(x=20, y=30)
text3['a555'].place(x=20, y=30)

root.mainloop()
