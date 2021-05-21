# Imports
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime

WINDOW_SIZE = '800x600'
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
        Label(main_page, image=self.app_logo, bg='#FAF1E6').place(x=325, y=50)

        # User name Entry
        Label(main_page, text='Username', bg='#FAF1E6').place(x=335, y=200)
        self.username = Entry(main_page, width=20)
        self.username.place(x=335, y=225)

        # Password Entry
        Label(main_page, text='Password', bg='#FAF1E6').place(x=335, y=275)
        self.password = Entry(main_page, width=20)
        self.password.place(x=335, y=300)

        # Log in Button
        login_button = Button(main_page, text='Login', width=10, bg='#E4EFE7', command=lambda: self.menu(main_page))
        login_button.place(x=355, y=340)

        # Exit Button
        exit_button = Button(main_page, text='Exit ', width=10,  bg='#E4EFE7', command=main_page.destroy)
        exit_button.place(x=355, y=385)

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
            self.time_label.place(x=620, y=10)
            self.current_time()

            # Logo
            Label(menu_page, image=self.app_logo, bg='#FAF1E6').place(x=620, y=150)

            # Add Button
            Button(menu_page, text='Add Record', bg='orange', font=FONT, width=10, height=2, command=lambda: [menu_page.withdraw(), self.add_record(menu_page)]).place(x=100, y=100)

            # View Report Button
            Button(menu_page, text='View Report', bg='pink', font=FONT, width=10, height=2).place(x=100, y=300)

            # View Record Button
            Button(menu_page, text='View Record', bg='coral', font=FONT, width=10, height=2).place(x=350, y=300)

            # View Report Button
            Button(menu_page, text='Attendance', bg='purple', font=FONT, width=10, height=2).place(x=350, y=100)

            # Cancel Button
            Button(menu_page, text='Log Out', bg='#E4EFE7',command=lambda: [menu_page.destroy(), main_page.deiconify()]).place(x=50, y=500)

            # check if the Exit th Window Manually
            menu_page.protocol("WM_DELETE_WINDOW", lambda: [menu_page.destroy(), main_page.deiconify()])

            menu_page.mainloop()
        else:
            error = Label(main_page, text='Invalid Username or Password', fg='white', bg='#da7f8f', relief=RAISED)
            error.place(x=315, y=410)
            error.after(3000, error.destroy)

    def add_record(self, menu_page):
        add_record_page = Toplevel()
        add_record_page.title('Add Record')
        add_record_page.geometry(WINDOW_SIZE)
        add_record_page.config(bg='#FAF1E6')


        # Getting the Student Id
        Label(add_record_page, text='STUDENT ID:', bg='#FAF1E6').place(x=150, y=50)
        self.student_id = Entry(add_record_page, width=40)
        self.student_id.place(x=250, y=50)

        # Getting the First Name
        Label(add_record_page, text='FIRST NAME: ', bg='#FAF1E6').place(x=150, y=150)
        self.first_name = Entry(add_record_page, width=40)
        self.first_name.place(x=250, y=150)

        # Getting the Middle Name
        Label(add_record_page, text='MIDDLE NAME: ', bg='#FAF1E6').place(x=150, y=200)
        self.middle_name = Entry(add_record_page, width=40)
        self.middle_name.place(x=250, y=200)

        # Getting the Last Name
        Label(add_record_page, text='LAST NAME: ', bg='#FAF1E6').place(x=150, y=250)
        self.last_name = Entry(add_record_page, width=40)
        self.last_name.place(x=250, y=250)

        # Getting the Course
        Label(add_record_page, text='COURSE: ', bg='#FAF1E6').place(x=150, y=300)
        self.course = Entry(add_record_page, width=40)
        self.course.place(x=250, y=300)

        # Getting the Section
        Label(add_record_page, text='SECTION: ', bg='#FAF1E6').place(x=150, y=350)
        self.section = Entry(add_record_page, width=40)
        self.section.place(x=250, y=350)

        # Cancel Button
        Button(add_record_page, text='Cancel', width=10, bg='#E4EFE7', command=lambda: [add_record_page.destroy(), menu_page.deiconify()]).place(x=300, y=400)

        # Save Button
        Button(add_record_page, text='Save', bg='#E4EFE7', width=10, command=self.subok).place(x=400, y=400)

        # check if the Exit th Window Manually
        add_record_page.protocol("WM_DELETE_WINDOW", lambda: [add_record_page.destroy(), menu_page.deiconify()])

        add_record_page.mainloop()

    def subok(self):
        print(self.student_id.get())
        print(self.first_name.get())
        print(self.middle_name.get())
        print(self.last_name.get())
        print(self.course.get())
        print(self.section.get())

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
