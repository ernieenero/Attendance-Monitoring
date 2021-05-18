# Imports
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime

WINDOW_SIZE = '600x500'
FONT = ('Verdana', 15)


class Main:
    def __init__(self, main_page):
        # Student info initialization
        self.student_id = 0
        self.first_name = ''
        self.middle_name = ''
        self.last_name = ''
        self.course = ''
        self.section = ''

        self.exit_button = ''

        # Time Initialization
        self.time_label = 0

        # Application Logo
        self.app_logo = ImageTk.PhotoImage(Image.open('system daw eh.png').resize((150, 150), Image.ANTIALIAS))
        Label(main_page, image=self.app_logo, bg='#FAF1E6').place(x=225, y=50)

        # User name Entry
        Label(main_page, text='Username', bg='#FAF1E6').place(x=225, y=200)
        self.username = Entry(main_page, width=20)
        self.username.place(x=225, y=225)

        # Password Entry
        Label(main_page, text='Password', bg='#FAF1E6').place(x=225, y=275)
        self.password = Entry(main_page, width=20)
        self.password.place(x=225, y=300)

        # Log in Button
        login_button = Button(main_page, text='Login', width=10, bg='#E4EFE7', command=lambda: self.menu(main_page))
        login_button.place(x=245, y=330)

        # Exit Button
        exit_button = Button(main_page, text='Exit ', width=10,  bg='#E4EFE7', command=main_page.destroy)
        exit_button.place(x=245, y=365)

    def menu(self, main_page):
        if self.username.get() == 'admin' and self.password.get() == 'admin':
            # Hide Main Window
            main_page.withdraw()
            self.username.delete(0, END)
            self.password.delete(0, END)

            # Create Menu Window
            menu_page = Toplevel()
            menu_page.title('Student Attendance Monitoring System')
            menu_page.config(bg='#FAF1E6')
            menu_page.geometry(WINDOW_SIZE)
            menu_page.resizable(0, 0)

            # Current Time Label
            self.time_label = Label(menu_page, relief=SUNKEN, bg='#AAAAAA')
            self.time_label.place(x=450, y=10)
            self.current_time()

            # Logo
            Label(menu_page, image=self.app_logo, bg='#FAF1E6').place(x=420, y=150)

            # Add Button
            Button(menu_page, text='Add Record', bg='orange', font=FONT, width=10, height=2).place(x=50, y=150)

            # View Report Button
            Button(menu_page, text='View Report', bg='pink', font=FONT, width=10, height=2).place(x=50, y=250)

            # View Record Button
            Button(menu_page, text='View Record', bg='coral', font=FONT, width=10, height=2).place(x=250, y=250)

            # View Report Button
            Button(menu_page, text='Attendance', bg='purple', font=FONT, width=10, height=2).place(x=250, y=150)

            # Cancel Button
            Button(menu_page, text='Log Out', bg='#E4EFE7',command=lambda: [menu_page.destroy(), main_page.deiconify()]).place(x=50, y=400)

            # check if the Exit th Window Manually
            menu_page.protocol("WM_DELETE_WINDOW", lambda: [menu_page.destroy(), main_page.deiconify()])

            menu_page.mainloop()
        else:
            error = Label(main_page, text='Invalid Username or Password', fg='white', bg='#da7f8f', relief=RAISED)
            error.place(x=200, y=410)
            error.after(3000, error.destroy)



    def current_time(self):
        date_time_now = datetime.now()
        date_time_now = date_time_now.strftime('%I:%M:%S %p  %B %d, %Y')
        self.time_label.config(text=date_time_now)
        self.time_label.after(200, self.current_time)


root = Tk()
root.title('Student Attendance Monitoring System')
root.geometry(WINDOW_SIZE)
root.config(bg='#FAF1E6')
root.resizable(0, 0)
main = Main(root)
root.mainloop()

