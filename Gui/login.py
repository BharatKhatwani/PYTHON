from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Logic Form')
root.geometry('350x500')
root.config(background='#0096DC')

# Load and display the image
img = Image.open('logo.png')
resized_img = img.resize((70, 70))
photo_img = ImageTk.PhotoImage(resized_img)
img_label = Label(root, image=photo_img, bg='#0096DC')
img_label.image = photo_img  # Prevent garbage collection
img_label.pack(pady=(20, 20))

# Login function
def handle_login():
    email = email_entry.get()
    password = password_entry.get()

    if email == 'bharatkhatwani796@gmail.com' and password == '123456789':
        messagebox.showinfo("Success", "Login Successful")  # Fixed
    else:
        messagebox.showerror("Error", "Login Failed")      # Fixed

# Text label
text_label = Label(root, text='Flipkart', fg='white', bg='#0096DC', font=('Verdana', 24, 'bold'))
text_label.pack(pady=(0, 30))

# Email label and entry
email_label = Label(root, text='Enter Email', fg='white', bg='#0096DC', font=('Verdana', 12))
email_label.pack(pady=(0,5))
email_entry = Entry(root, width=30, font=('Verdana', 12))
email_entry.pack(pady=(0,20))

# Password label and entry
password_label = Label(root, text='Enter Password', fg='white', bg='#0096DC', font=('Verdana', 12))
password_label.pack(pady=(0,5))
password_entry = Entry(root, width=30, show='*', font=('Verdana', 12))
password_entry.pack(pady=(0,20))

# Login button
login_button = Button(root, text='Login', width=20, bg='white', fg='#0096DC', command=handle_login, font=('Verdana', 12, 'bold'))
login_button.pack(pady=20)

root.mainloop()
