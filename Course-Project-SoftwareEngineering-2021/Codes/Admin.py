import tkinter as tk
from functools import partial
from tkinter import ttk
from tkmacosx import Button
from tkinter import filedialog
from Database import Database
from tkinter import messagebox
tk.TK_SILENCE_DEPRECATION=1

# ADD MAINLOOP EVERY WINDOW AT THE END
class AdminGUI:
    def __init__(self, username):
        self.username = username
        self.admin_window = tk.Tk()
        self.admin_window.configure(bg="#e85656")
        self.admin_window.title("Library")
        self.admin_window.minsize(width=400,height=400)
        self.admin_window.geometry("600x500")

        headingFrame1 = tk.Frame(self.admin_window, bg="#fcffbf", bd=5)
        headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
        headingLabel = tk.Label(headingFrame1, text=f"Welcome {self.username}", bg='black', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

        btn1 = Button(self.admin_window,text="Add Book", bg='black', fg='white', borderless=1,  command=self.addBooks)
        btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
            
        btn2 = Button(self.admin_window,text="Remove Book",bg='black', fg='white', borderless=1,  command=self.removeBooks)
        btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
            
        btn3 = Button(self.admin_window,text="Search Book",bg='black', fg='white', borderless=1,  command=self.searchBook)
        btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
            
        btn4 = Button(self.admin_window,text="Check Transactions",bg='black', borderless=1, fg='white', command=self.getTransactionLogs)
        btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
            
        quitBtn = Button(self.admin_window,text="Logout", bg='black', fg='white', borderless=1, command=lambda : self.destroy_window(self.admin_window, False, True))
        quitBtn.place(relx=0.4,rely=0.85, relwidth=0.18, relheight=0.08)

        self.admin_window.mainloop()


    def addBooks(self):
        try:
            self.admin_window.destroy()
        except Exception as e:
            print(e)
        

        self.addBook_window = tk.Tk()
        self.addBook_window.title("Library")
        self.addBook_window.configure(bg="#e85656")
        self.addBook_window.minsize(width=600,height=650)
        self.addBook_window.geometry("700x650")
            
        headingFrame1 = tk.Frame(self.addBook_window,bg="#fcffbf",bd=5)
        headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        headingLabel = tk.Label(headingFrame1, text="Add Books ", bg='black', fg='white', font=('Courier',15), padx=5, pady=5)
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
        labelFrame = tk.Frame(self.addBook_window,bg='black')
        labelFrame.place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.58)
            
        # ISBN 
        lb1 = tk.Label(labelFrame, text="ISBN: ", bg='black', fg='white', padx=5, pady=5)
        lb1.place(relx=0.05,rely=0.1, relheight=0.08)
        bookID = tk.StringVar()
        bookInfo1 = tk.Entry(labelFrame, textvariable=bookID, bd=0)
        bookInfo1.place(relx=0.3,rely=0.1, relwidth=0.62, relheight=0.08)
        
        # Title
        lb2 = tk.Label(labelFrame,text="Title: ", bg='black', fg='white', padx=5, pady=5)
        lb2.place(relx=0.05,rely=0.2, relheight=0.08)
        bookTitle = tk.StringVar()
        bookInfo2 = tk.Entry(labelFrame, textvariable=bookTitle, bd=0)
        bookInfo2.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
        # Book Author
        lb3 = tk.Label(labelFrame,text="Author: ", bg='black', fg='white', padx=5, pady=5)
        lb3.place(relx=0.05,rely=0.3, relheight=0.08)
        bookAuthor = tk.StringVar()
        bookInfo3 = tk.Entry(labelFrame, textvariable=bookAuthor, bd=0)
        bookInfo3.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)

        
        # Publication
        lb4 = tk.Label(labelFrame,text="Publication: ", bg='black', fg='white', padx=5, pady=5)
        lb4.place(relx=0.05,rely=0.4, relheight=0.08)
        bookPublication = tk.StringVar()
        bookInfo4 = tk.Entry(labelFrame, textvariable=bookPublication, bd=0)
        bookInfo4.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)

        
        # Book Category
        lb5 = tk.Label(labelFrame,text="Category: ", bg='black', fg='white', padx=5, pady=5)
        lb5.place(relx=0.05,rely=0.5, relheight=0.08)
        
        options1 = ["All", "Book", "Journal", "Paper"]
        bookCategory = tk.StringVar()
        bookCategory.set("All")
        bookInfo5 = ttk.OptionMenu(labelFrame, bookCategory, options1[0], *options1)
        bookInfo5.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.08)


        # Search by Language
        lb6 = tk.Label(labelFrame,text="Language: ", bg='black', fg='white', padx=5, pady=5)
        lb6.place(relx=0.05,rely=0.6, relheight=0.08)

        options2 = ["All", "English", "French"]
        bookLanguage = tk.StringVar()
        bookLanguage.set("All")
        bookInfo6 = ttk.OptionMenu(labelFrame, bookLanguage, options2[0], *options2)
        bookInfo6.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)


        # Book Edition
        lb7 = tk.Label(labelFrame,text="Book Edition: ", bg='black', fg='white', padx=5, pady=5)
        lb7.place(relx=0.05,rely=0.7, relheight=0.08)
        bookEdition = tk.IntVar()
        bookInfo7 = tk.Entry(labelFrame, textvariable=bookEdition, bd=0)
        bookInfo7.place(relx=0.3,rely=0.7, relwidth=0.62, relheight=0.08)
        

        # Browse for book - path
        lb8 = tk.Label(labelFrame,text="File Chosen: ", bg='black', fg='white', padx=5, pady=5)
        lb8.place(relx=0.05,rely=0.85, relheight=0.08)

        self.file_label = tk.Label(labelFrame,text="None", bg='black', fg='white', padx=5, pady=5)
        self.file_label.place(relx=0.3,rely=0.85, relheight=0.08)
        
        filename = tk.StringVar()
        BrowseBtn = Button(self.addBook_window, text="Browse", bg='black', fg='white', borderless=1, command=lambda : filename.set(self.browse_file()))
        BrowseBtn.place(relx=0.68,rely=0.84, relwidth=0.18,relheight=0.04)

        #Submit Button
        SubmitBtn = Button(self.addBook_window, text="Submit", bg='black', fg='white', borderless=1, command=partial(self.sendBookDetails, bookID, bookTitle, bookAuthor, bookPublication, bookCategory, bookLanguage, bookEdition, filename))
        SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
        
        quitBtn = Button(self.addBook_window,text="Quit", bg='black', fg='white', borderless=1, command=lambda : self.destroy_window(self.addBook_window, True))
        quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

        self.addBook_window.mainloop()


    def browse_file(self):
        filename = filedialog.askopenfilename(initialdir = ".", title = "Select a File",
                                filetypes = (("PDF files", "*.pdf"), ))
        self.file_label.config(text=filename.split("/")[-1])
        return filename


    def sendBookDetails(self, bookID, bookTitle, bookAuthor, bookPublication, bookCategory, bookLanguage, bookEdition, filename):
        database = Database()
        missing = []

        bookID, bookTitle, bookAuthor, bookCategory = bookID.get(), bookTitle.get(), bookAuthor.get(), bookCategory.get() 
        bookLanguage, bookPublication, bookEdition, filename = bookLanguage.get(), bookPublication.get(), bookEdition.get(), filename.get()        
        
        if bookID == 0:
            missing.append("Book ID")
        if bookTitle == "":
            missing.append("Book Title")
        if bookAuthor == "":
            missing.append("Author")
        if filename == "":
            missing.append("File Name")
        if bookCategory == "All":
            missing.append("Book Category")
        if bookLanguage == "All":
            missing.append("Book Language")
                
        
        # print(missing)
        if len(missing):
            messagebox.showerror(title="Add Books", message="Missing Details:\n" + "\n".join(missing))
            self.destroy_window(self.addBook_window)
            self.addBooks()
            return

        
        check = database.insertBook(bookID, bookTitle, bookAuthor, bookCategory, bookLanguage, bookPublication, bookEdition, filename)
        
        if check == "Failed":
            messagebox.showerror(title="Add Books", message=f"Book With ISBN: {bookID} Already Exists")
            self.destroy_window(self.addBook_window)
            self.addBooks()
        else:
            messagebox.showinfo(title="Add Books", message=f"Book With ISBN: {bookID} Added Successfully")
            self.destroy_window(self.addBook_window, True)
        

    def removeBooks(self):

        try:
            self.admin_window.destroy()
        except Exception as e:
            print("Exception: ", e)
        

        self.removeBook_window = tk.Tk()
        self.removeBook_window.title("Library")
        self.removeBook_window.configure(bg="#e85656")
        self.removeBook_window.minsize(width=400, height=400)
        self.removeBook_window.geometry("600x500")

        headingFrame1 = tk.Frame(self.removeBook_window,bg="#fcffbf",bd=5)
        headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        headingLabel = tk.Label(headingFrame1, text="Remove Books ", bg='black', fg='white', font=('Courier',15), padx=5, pady=5)
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
        labelFrame = tk.Frame(self.removeBook_window, bg='black')
        labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

        # Book ID to Delete
        lb1 = tk.Label(labelFrame,text="Book ID: ", bg='black', fg='white')
        lb1.place(relx=0.05,rely=0.3)
        bookID = tk.IntVar()
        bookInfo1 = tk.Entry(labelFrame, bd=0, textvariable=bookID)
        bookInfo1.place(relx=0.3,rely=0.28, relwidth=0.62)

        # Book Title to Delete
        lb2 = tk.Label(labelFrame,text="Book Title: ", bg='black', fg='white')
        lb2.place(relx=0.05,rely=0.5)
        bookTitle = tk.StringVar()
        bookInfo2 = tk.Entry(labelFrame, bd=0, textvariable=bookTitle)
        bookInfo2.place(relx=0.3, rely=0.48, relwidth=0.62)

        #Submit Button
        SubmitBtn = Button(self.removeBook_window, text="Remove", bg='black', fg='white', borderless=1, command=partial(self.removeBookDetails, bookID, bookTitle))
        SubmitBtn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)
        
        quitBtn = Button(self.removeBook_window,text="Quit",bg='black', fg='white', borderless=1, command=lambda : self.destroy_window(self.removeBook_window, True))
        quitBtn.place(relx=0.53,rely=0.85, relwidth=0.18,relheight=0.08)

        self.removeBook_window.mainloop()


    def removeBookDetails(self, bookID, bookTitle):
        bookID, bookTitle = bookID.get(), bookTitle.get()
        database = Database()
        missing = []
        if bookID == 0:
            missing.append("Book ID")
        if bookTitle == "":
            missing.append("Book Title")
        
        if len(missing):
            messagebox.showerror(title="Remove Books", message="Missing Details:\n" + "\n".join(missing))
            self.destroy_window(self.removeBook_window)
            self.removeBooks()
            return
        
        check = database.removeBook(bookID, bookTitle)
        database.__close__()

        if check == "Book Successfully Removed":
            messagebox.showinfo(title="Remove Books", message=check)
            self.destroy_window(self.removeBook_window, True)
        elif check == "Book Not in Path":
            messagebox.showinfo(title="Remove Books", message=check)
            self.destroy_window(self.removeBook_window, True)
        else:
            messagebox.showerror(title="Remove Books", message=check)
            self.destroy_window(self.removeBook_window)
            self.removeBooks()
        return 
        

    def searchBook(self):
        self.admin_window.destroy()
        
        search_window = tk.Tk()

        search_window.title("Library")
        search_window.configure(bg="#e85656")
        search_window.minsize(width=600, height=500)
        search_window.geometry("600x500")

        headingFrame1 = tk.Frame(search_window,bg="#fcffbf",bd=5)
        headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        headingLabel = tk.Label(headingFrame1, text="Search Books ", bg='black', fg='white', font=('Courier',15), padx=5, pady=5)
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
        labelFrame = tk.Frame(search_window, bg='black')
        labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

        # Search by Book Title
        lb1 = tk.Label(labelFrame,text="Book Title: ", bg='black', fg='white', padx=5, pady=5)
        lb1.place(relx=0.05,rely=0.05, relheight=0.1)
        bookTitle = tk.StringVar()
        bookInfo1 = tk.Entry(labelFrame, bd=0, textvariable=bookTitle)
        bookInfo1.place(relx=0.3,rely=0.05, relwidth=0.62, relheight=0.1)

        # Search by Author
        lb2 = tk.Label(labelFrame,text="Author: ", bg='black', fg='white', padx=5, pady=5)
        lb2.place(relx=0.05,rely=0.18, relheight=0.1)
        bookAuthor = tk.StringVar()
        bookInfo2 = tk.Entry(labelFrame, bd=0, textvariable=bookAuthor)
        bookInfo2.place(relx=0.3,rely=0.18, relwidth=0.62, relheight=0.1)

        # Search by Category
        lb3 = tk.Label(labelFrame,text="Category: ", bg='black', fg='white', padx=5, pady=5)
        lb3.place(relx=0.05,rely=0.3, relheight=0.1)
        
        options1 = ["All", "Book", "Journal", "Paper"]
        bookCategory = tk.StringVar()
        bookCategory.set("All")
        bookInfo3 = ttk.OptionMenu(labelFrame, bookCategory, options1[0], *options1)
        bookInfo3.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.1)


        # Search by Language
        lb4 = tk.Label(labelFrame,text="Language: ", bg='black', fg='white', padx=5, pady=5)
        lb4.place(relx=0.05,rely=0.42, relheight=0.1)

        options2 = ["All", "English", "French"]
        bookLanguage = tk.StringVar()
        bookLanguage.set("All")
        bookInfo4 = ttk.OptionMenu(labelFrame, bookLanguage, options2[0], *options2)
        bookInfo4.place(relx=0.3,rely=0.42, relwidth=0.62, relheight=0.1)

        # Search by Rating
        lb5 = tk.Label(labelFrame,text="Rating: ", bg='black', fg='white', padx=5, pady=5)
        lb5.place(relx=0.05,rely=0.54, relheight=0.1)

        options3 = ["None"] + list(range(1, 6)) 
        bookRating = tk.StringVar()
        bookRating.set("None")
        bookInfo5 = ttk.OptionMenu(labelFrame, bookRating, options3[0], *options3)
        bookInfo5.place(relx=0.3,rely=0.54, relwidth=0.62, relheight=0.1)

        # # Search by Type
        # lb6 = tk.Label(labelFrame,text="Book Type: ", bg='black', fg='white', padx=5, pady=5)
        # lb6.place(relx=0.05,rely=0.66, relheight=0.1)

        # options5 = ["All", "Fiction", "Non-Fiction", "Knowledge", "Article", "Review"]
        # bookGenre = tk.StringVar()
        # bookGenre.set("All")
        # bookInfo7 = ttk.OptionMenu(labelFrame, bookGenre, options5[0], *options5)
        # bookInfo7.place(relx=0.3,rely=0.66, relwidth=0.62, relheight=0.1)

        # Search By Publisher
        lb6 = tk.Label(labelFrame,text="Publisher: ", bg='black', fg='white', padx=5, pady=5)
        lb6.place(relx=0.05,rely=0.66, relheight=0.1)
        bookPublisher = tk.StringVar()
        bookPublisher.set("")
        bookInfo7 = tk.Entry(labelFrame, bd=0, textvariable=bookPublisher)
        bookInfo7.place(relx=0.3,rely=0.66, relwidth=0.62, relheight=0.1)


        # Search by Availability
        bookStatus = tk.IntVar()
        bookInfo8 = tk.Checkbutton(labelFrame, text="Filter Availability", variable=bookStatus, onvalue=1, offvalue=0, bg='black')
        bookInfo8.place(relx=0.3,rely=0.78, relheight=0.1)

        #Submit Button
        SubmitBtn = Button(search_window, text="Submit", bg='black', fg='white', borderless=1, command=partial(self.getSearchDetails, bookTitle, bookAuthor, bookCategory, bookLanguage, bookRating, bookPublisher, bookStatus))
        SubmitBtn.place(relx=0.28,rely=0.85, relwidth=0.18, relheight=0.08)
        
        quitBtn = Button(search_window,text="Quit", bg='black', fg='white', borderless=1, command=lambda : self.destroy_window(search_window, True))
        quitBtn.place(relx=0.53,rely=0.85, relwidth=0.18, relheight=0.08)

        search_window.mainloop()


    def getSearchDetails(self, title, author, category, language, rating, publisher, status):
        title, author, category = title.get(), author.get(), category.get() 
        language, rating, publisher, status = language.get(), rating.get(), publisher.get(), status.get()

        database = Database()
        result = database.bookSearch(title, author, category, language, rating, publisher, status)
        database.__close__()
        # print(result)
        if result == "Books Not Found":
            messagebox.showerror(title="Search", message="Book Not Found")
            return

        textLabel = []
        # text_format = "{:^13}{:^5}{:^25}{:^5}{:^25}{:^5}{:^25}{:^5}{:^10}{:^5}{:^10}{:^5}{:^10}{:^5}{:^10}{:^5}{:^16}"
        
        # text_format = "%-13s%-5s%-25s%-5s%-25s%-5s%-25s%-5s%-10s%-5s%-10s%-5s%-10s%-5s%-10s%-5s%-16s"
        
        for i in result:
            output = list(i)
            del output[7]
            if output[6] == None:
                output[6] = "0"
            if len(output[-1]) > 0:
                output[-1] = "Available"
            else:
                output[-1] = "Not Available"
            output = [str(i) for i in output]
            textLabel.append(output)
        table_title = [['ISBN', 'TITLE', 'AUTHOR', 'CATEGORY', 'LANGUAGE', 'PUBLISHER', 'RATING', 'EDITION', 'STATUS']]
        label_length = len(textLabel)

        searchResult_window = tk.Tk()
        searchResult_window.title("Library")
        searchResult_window.configure(bg="#e85656")
        searchResult_window.minsize(width=1182, height=500)
        searchResult_window.geometry("1182x500")

        headingFrame1 = tk.Frame(searchResult_window, bg="#fcffbf",bd=5)
        headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        headingLabel = tk.Label(headingFrame1, text="Search Results ", bg='black', fg='white', font=('Courier',15), padx=5, pady=5)
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

        labelFrame = tk.Frame(searchResult_window, bg='black')
        labelFrame.place(relx=0.02,rely=0.25,relwidth=0.96,relheight=0.58)
        
        index = tk.IntVar()
        index.set(-1)
        
        PrevBtn = Button(searchResult_window, text="Previous", bg='black', fg='white', borderless=1, command=lambda : index.set(self.createEntryCells(textLabel, searchResult_window, index.get()-10, table_title, PrevBtn, NextBtn, label_length)))
        PrevBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
        
        NextBtn = Button(searchResult_window,text="Next", bg='black', fg='white', borderless=1, command=lambda : index.set(self.createEntryCells(textLabel, searchResult_window, index.get()+10, table_title, PrevBtn, NextBtn, label_length)))
        NextBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

        index.set(self.createEntryCells(textLabel, searchResult_window, index.get(), table_title, PrevBtn, NextBtn, label_length))
        searchResult_window.mainloop()


    def createEntryCells(self, textLabel, labelWindow, index, table_title, PrevBtn, NextBtn, label_length):
        
        textLabel = textLabel[index+1: index+11]
        # print(*textLabel, sep="\n")
        # labelFrame.place_forget()
        labelFrame = tk.Frame(labelWindow, bg='black')
        labelFrame.place(relx=0.02,rely=0.25,relwidth=0.96,relheight=0.58)
        
        row_count = 0
        for text in table_title + textLabel:
            if index <= 0:
                PrevBtn.config(state="disabled")
            else:
                PrevBtn.config(state="normal")

            if index + 11 >= label_length:
                NextBtn.config(state="disabled")
            else:
                NextBtn.config(state="normal")

            for j in range(len(textLabel[0])):
                b = tk.Entry(labelFrame, bg="black", fg="white", relief=tk.SUNKEN, justify="center", width=15)
                b.insert(0, text[j])
                b.config(state="disabled", disabledbackground="black", disabledforeground="white", highlightbackground="black",highlightthickness=0.1)
                b.grid(row=row_count, column=j)
            row_count += 1
        return index


    def getTransactionLogs(self):
        
        database = Database()
        query = database.getTransactions()
        database.__close__()

        if len(query) == 0:
            messagebox.showinfo(title="Transactions", message="No Transactions Logs Exist")
            return

        self.admin_window.destroy()

        transaction_window = tk.Tk()

        transaction_window.title("Library")
        transaction_window.configure(bg="#e85656")
        transaction_window.minsize(width=600, height=500)
        transaction_window.geometry("840x500")

        headingFrame1 = tk.Frame(transaction_window,bg="#fcffbf",bd=5)
        headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        headingLabel = tk.Label(headingFrame1, text="Transaction Log", bg='black', fg='white', font=('Courier',15), padx=5, pady=5)
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

        headingFrame1 = tk.Frame(transaction_window,bg="#fcffbf",bd=5)
        headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        headingLabel = tk.Label(headingFrame1, text="Transaction Log", bg='black', fg='white', font=('Courier',15), padx=5, pady=5)
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
        

        labelFrame = tk.Frame(transaction_window, bg='black', bd=0)
        labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)


        # extract data from databse
        # test data taken here
        # query = [["Afzal", "Book1", "Fiction", "Book"],
        #          ["Hritika", "Book2", "Non-Fiction", "Book"]]*3
        for i in range(len(query)):
            for j in range(len(query[0])):
                b = tk.Entry(labelFrame, bg="black", fg="white", relief=tk.SUNKEN, justify="center")
                b.insert(0, query[i][j])
                b.config(state="disabled", disabledbackground="black", disabledforeground="white", highlightbackground="black",highlightthickness=0.2)
                b.grid(row=i, column=j)
        
        quitBtn = Button(transaction_window,text="Quit", bg='black', fg='white', borderless=1, command=lambda : self.destroy_window(transaction_window, True))
        quitBtn.place(relx=0.4,rely=0.85, relwidth=0.18, relheight=0.08)

        transaction_window.mainloop()

    
    def destroy_window(self, frame, return_frame=False, logout=False):
        from LoginRegister import LoginRegisterUI
        frame.destroy()
        if logout:
            login = LoginRegisterUI()
        elif return_frame:
            self.__init__(self.username)


if __name__ == "__main__":
    admin = AdminGUI("Test Admin")
