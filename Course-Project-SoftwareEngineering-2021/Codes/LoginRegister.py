import tkinter as tk
from functools import partial
from tkmacosx import Button
tk.TK_SILENCE_DEPRECATION=1
from Database import Database
from Admin import AdminGUI
from User import UserUI
from datetime import datetime
from tkinter import messagebox



class LoginRegisterUI:
    def __init__(self):

        self.login_page = tk.Tk()
        self.login_page.minsize(width=350, height=350)
        self.login_page.maxsize(width=400, height=400)
        
        self.login_page.geometry("350x350")
        self.login_page.title("Login to Library")
        tk.Label(self.login_page, text="Login", font=("Times New Roman", 24, "bold italic underline")).grid(row=0, column=1, sticky="NSEW", pady=10, padx=5)
        
        # Enter Username
        tk.Label(self.login_page, text="User Name ", font=("Times", 16)).grid(row=5, column=0, sticky="NSEW", pady=10, padx=5)
        username = tk.StringVar()
        tk.Entry(self.login_page, textvariable=username).grid(row=5, column=1, sticky="NSEW", pady=10, padx=5)

        # Enter Password
        tk.Label(self.login_page,text="Password", font=("Times", 16)).grid(row=6, column=0, sticky="NSEW", pady=10, padx=5)
        password = tk.StringVar()
        tk.Entry(self.login_page, textvariable=password, show='*').grid(row=6, column=1, sticky="NSEW", pady=10, padx=5)
        
        # button to login
        Button(self.login_page, text="Login", bg="black", fg="white", borderless=1, command=partial(self.validateLogin, username, password)).grid(row=8, column=1, sticky="NSEW", pady=10, padx=5)
        tk.Label(self.login_page,text="Or", font=("Times", 12)).grid(row=9, column=1, sticky="NSEW", padx=2)
        Button(self.login_page, text="Register", bg="black", fg="white", borderless=1, command=self.registerationDetails).grid(row=10, column=1, sticky="NSEW", pady=10, padx=5)

        self.login_page.mainloop()


    def validateLogin(self, username, password):
        database = Database()
        if isinstance(username, type(tk.StringVar())) and isinstance(username, type(tk.StringVar())):
            username, password = username.get(), password.get()

        if username == "" and password == "":
            messagebox.showerror(title="Missing Details", message="Username and Password Missing")
        elif username == "":
            messagebox.showerror(title="Missing Details", message="Username Missing")
        elif password == "":
            messagebox.showerror(title="Missing Details", message="Password Missing")
        
        else:
            check = database.verifyLogin(username, password)
            database.__close__()
            # print(check)
            if "Admin Successful" == check:
                try:
                    self.login_page.destroy()
                except Exception as e:
                    self.register_page.destroy()
                admin = AdminGUI(username)
            elif "User Successful" == check:
                try:
                    self.login_page.destroy()
                except Exception as e:
                    self.register_page.destroy()
                user = UserUI(username)
            else:
                messagebox.showerror(title="Invalid Details", message="User Does not Exist")
                
        return


    def registerationDetails(self, window=None):
        if window == None:
            self.destroy_window(self.login_page)
        else:
            self.destroy_window(window)
        
        self.register_page = tk.Tk()
        self.register_page.geometry("350x450")
        self.register_page.title("Register to Library")
        tk.Label(self.register_page, text="Register", font=("Times New Roman", 24, "bold italic underline")).grid(row=0, column=1, sticky="NSEW", pady=10, padx=5)
        
        # Enter Name
        tk.Label(self.register_page, text="Full Name ", font=("Times", 16)).grid(row=5, column=0, sticky="NSEW", pady=10, padx=5)
        name = tk.StringVar()
        tk.Entry(self.register_page, textvariable=name).grid(row=5, column=1, sticky="NSEW", pady=10, padx=5)

        # Enter Email
        tk.Label(self.register_page, text="Email ", font=("Times", 16)).grid(row=6, column=0, sticky="NSEW", pady=10, padx=5)
        email = tk.StringVar()
        tk.Entry(self.register_page, textvariable=email).grid(row=6, column=1, sticky="NSEW", pady=10, padx=5)

        # Enter Phone Number
        tk.Label(self.register_page, text="Phone ", font=("Times", 16)).grid(row=7, column=0, sticky="NSEW", pady=10, padx=5)
        ph_number = tk.IntVar()
        tk.Entry(self.register_page, textvariable=ph_number).grid(row=7, column=1, sticky="NSEW", pady=10, padx=5)

        # Enter Age
        tk.Label(self.register_page, text="Age ", font=("Times", 16)).grid(row=8, column=0, sticky="NSEW", pady=10, padx=5)
        age = tk.IntVar()
        tk.Entry(self.register_page, textvariable=age).grid(row=8, column=1, sticky="NSEW", pady=10, padx=5)
        

        # Enter Name
        tk.Label(self.register_page, text="User Name ", font=("Times", 16)).grid(row=9, column=0, sticky="NSEW", pady=10, padx=5)
        username = tk.StringVar()
        tk.Entry(self.register_page, textvariable=username).grid(row=9, column=1, sticky="NSEW", pady=10, padx=5)

        # Enter Password
        tk.Label(self.register_page,text="Password ", font=("Times", 16)).grid(row=10, column=0, sticky="NSEW", pady=10, padx=5)
        password = tk.StringVar()
        tk.Entry(self.register_page, textvariable=password, show='*').grid(row=10, column=1, sticky="NSEW", pady=10, padx=5)

        # button to submit
        Button(self.register_page, text="Submit", bg="black", fg="white", borderless=1, command=partial(self.sendRegistrationDetails, name, email, ph_number, age, username, password)).grid(row=11, column=1, sticky="NSEW", pady=10, padx=5)

        # button to go back
        Button(self.register_page, text="Back", bg="black", fg="white", borderless=1, command=lambda : self.destroy_window(self.register_page, True)).grid(row=12, column=1, sticky="NSEW", pady=10, padx=5)
        
        self.register_page.mainloop()


    def sendRegistrationDetails(self, name, email, ph_number, age, username, password):
        
        database = Database() 
        missing = []
        name, email, ph_number = name.get(), email.get(), ph_number.get()
        age, username, password = age.get(), username.get(), password.get()
        
        if name == "":
            missing.append("Name")
        if username == "":
            missing.append("Username")
        if password == "":
            missing.append("Password")
        if email == "":
            missing.append("Email")
        if len(missing):
            messagebox.showerror(title="Registeration", message="Required Fields:\n" + "\n".join(missing))
            return "Invalid Details"
        
        if len(password) < 8:
            messagebox.showerror(title="Registeration", message="Password Should be atleast 8 characters long")
            return "Password Too Short"
            
        plan = 1
        check = database.addUser(username, name, email, ph_number, age, password, plan)
        database.__close__()
        if check == "Registeration Successful":
            messagebox.showinfo(title="Registeration", message=check)
            self.validateLogin(username, password)
        else:
            messagebox.showinfo(title="Registeration", message=check)
            self.registerationDetails(self.register_page)
        

    def destroy_window(self, frame, return_frame=False):
        frame.destroy()
        if return_frame:
            self.__init__()


if __name__ == "__main__":
    library = LoginRegisterUI()
