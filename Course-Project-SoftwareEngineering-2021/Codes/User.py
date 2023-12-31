import tkinter as tk
from functools import partial
from PIL import ImageTk, Image
from tkinter import ttk
from tkmacosx import Button, Radiobutton
from Admin import *
import webbrowser

tk.TK_SILENCE_DEPRECATION=1

class UserUI:
    def __init__(self, username, result=None):
        self.username = username
        self.img = []
        
        self.browse_window = tk.Tk()
        self.current_window = self.browse_window
        self.browse_window.minsize(width=800, height=760)
        self.browse_window.maxsize(width=1024, height=1024)
        # self.browse_window.geometry("800x600")
        self.browse_window.configure(bg="#e85656")
        self.browse_window.title("Library")

        self.browse_window.grid_rowconfigure(0, minsize=300, weight=1)
        self.browse_window.grid_columnconfigure(0, minsize=250, weight=0)
        self.browse_window.grid_columnconfigure(1, weight=1)

        sidebar = tk.Frame(self.browse_window, bg='light yellow')
        sidebar.grid(row=0, column=0, sticky='nsew')


        # Browse
        btn1 = Button(sidebar, text="Browse", bg='white', fg='black', borderless=1,  command=self.browse)
        btn1.place(relx=0,rely=0.1, relwidth=1,relheight=0.1)

        # BookShelf
        btn2 = Button(sidebar, text="Book Shelf", bg='white', fg='black', borderless=1,  command=self.bookShelf)
        btn2.place(relx=0,rely=0.2, relwidth=1,relheight=0.1)

        # Check Subscription
        btn3 = Button(sidebar, text="Subscription", bg='white', fg='black', borderless=1,  command=self.subscription)
        btn3.place(relx=0,rely=0.3, relwidth=1,relheight=0.1)

        btn3 = Button(sidebar, text="Search", bg='white', fg='black', borderless=1,  command=self.search)
        btn3.place(relx=0,rely=0.4, relwidth=1,relheight=0.1)

        # Logout
        btn4 = Button(sidebar, text="Logout", bg='white', fg='black', borderless=1,  command=lambda : self.destroy_window(self.browse_window, False, True))
        btn4.place(relx=0,rely=0.5, relwidth=1,relheight=0.1)

        self.bookbar = tk.Frame(self.browse_window, bg="#e85656")
        self.bookbar.grid(row=0, column=1, sticky='nsew')

        self.next_button = Button(self.bookbar, text="Next", bg='black', fg='white', disabledbackground="black", borderless=1)
        self.prev_button = Button(self.bookbar, text="Next", bg='black', fg='white', disabledbackground="black", borderless=1)
        

        self.browse(result)
        
        self.browse_window.mainloop()


    def bookShelf(self):
        
        try:
            self.bookbar.grid_forget()
        except Exception:
            pass

        # Book List Browser
        self.bookbar = tk.Frame(self.browse_window, bg="#e85656")
        self.bookbar.grid(row=0, column=1, sticky='nsew')

        headingFrame1 = tk.Frame(self.bookbar, bg="#fcffbf", bd=5)
        headingFrame1.place(relx=0.05,rely=0.01,relwidth=0.9,relheight=0.12)
        headingLabel = tk.Label(headingFrame1, text="Bookshelf", bg='black', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

        result = self.getSearchDetails("", "", "All", "All", "None", "", 0, user_bookshelf=True)
        
        index = tk.IntVar()
        index.set(-1)
        result_length = len(result)
        

        # Previous Button
        self.prev_button = Button(self.bookbar, text="Previous", bg='black', fg='white', disabledbackground="black", borderless=1, command=lambda : index.set(self.createBookView(result, index.get()-4, result_length, False)))
        self.prev_button.place(relx=0.1, rely=0.92, relwidth=0.18, relheight=0.05)
        

        # Next Button
        self.next_button = Button(self.bookbar, text="Next", bg='black', fg='white', disabledbackground="black", borderless=1, command=lambda : index.set(self.createBookView(result, index.get()+4, result_length, False)))
        self.next_button.place(relx=0.74, rely=0.92, relwidth=0.18, relheight=0.05)
        

        index.set(self.createBookView(result, index.get(), result_length, False))


        self.bookbar.mainloop()

    
    def subscription(self):

        try:
            self.bookbar.grid_forget()
        except Exception:
            pass

        # Book List Browser
        self.bookbar = tk.Frame(self.browse_window, bg="#e85656")
        self.bookbar.grid(row=0, column=1, sticky='nsew')

        headingFrame1 = tk.Frame(self.bookbar, bg="#fcffbf", bd=5)
        headingFrame1.place(relx=0.05,rely=0.01,relwidth=0.9,relheight=0.12)
        headingLabel = tk.Label(headingFrame1, text="Subscription Plans", bg='black', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

        labelFrame = tk.Frame(self.bookbar, bg='black')
        labelFrame.place(relx=0.05,rely=0.2,relwidth=0.9,relheight=0.4)

        # Plan 1
        plan1_label = tk.Label(labelFrame, text="Plan 1: 2 Months", fg="white", bg="black", font=("Times", 15, "bold underline"))
        plan1_label.place(relx=0.05, rely=0.1)
        plan1_label_details = tk.Label(labelFrame, text="•\tDescription: Borrow unlimited number of books for 2 months at 400 rupees\n•\tMonth: 2\n•\tCost: 400/-", fg="white", bg="black", justify="left", font=("Times", 13))
        plan1_label_details.place(relx=0.05, rely=0.2)

        # Plan 2
        plan2_label = tk.Label(labelFrame, text="Plan 2: 4 Months", fg="white", bg="black", font=("Times", 15, "bold underline"))
        plan2_label.place(relx=0.05, rely=0.38)
        plan2_label_details = tk.Label(labelFrame, text="•\tDescription: Borrow unlimited number of books for 4 months at 600 rupees\n•\tMonth: 4\n•\tCost: 600/-", fg="white", bg="black", justify="left", font=("Times", 13))
        plan2_label_details.place(relx=0.05, rely=0.48)

        # Plan 3
        plan3_label = tk.Label(labelFrame, text="Plan 3: 6 Months", fg="white", bg="black", font=("Times", 15, "bold underline"))
        plan3_label.place(relx=0.05, rely=0.68)
        plan3_label_details = tk.Label(labelFrame, text="•\tDescription: Borrow unlimited number of books for 6 months at 900 rupees\n•\tMonth: 6\n•\tCost: 900/-", fg="white", bg="black", justify="left", font=("Times", 13))
        plan3_label_details.place(relx=0.05, rely=0.78)     

        # Radio Choices
        choice = tk.IntVar()

        # Plan 1 Radio
        plan1_choice = Radiobutton(self.bookbar, text="Choose Plan 1", bg="#e85656", fg="black", variable=choice, value=1)
        plan1_choice.place(relx=0.05, rely=0.62)

        # Plan 2 Radio
        plan2_choice = Radiobutton(self.bookbar, text="Choose Plan 2", bg="#e85656", fg="black", variable=choice, value=2)
        plan2_choice.place(relx=0.05, rely=0.67)

        # Plan 3 Radio
        plan3_choice = Radiobutton(self.bookbar, text="Choose Plan 3", bg="#e85656", fg="black", variable=choice, value=3)
        plan3_choice.place(relx=0.05, rely=0.72)

                    
        SubmitBtn = Button(self.bookbar,text="Save Changes", bg='black', fg='white', borderless=1, command=lambda : self.changePlan(choice))
        SubmitBtn.place(relx=0.4,rely=0.8, relwidth=0.25, relheight=0.08)

        self.bookbar.mainloop()


    def changePlan(self, p_id):
        p_id = p_id.get()
        if p_id == 0:
            messagebox.showerror(title="Plan", message="Please Choose a Valid Plan")
            return
        database = Database()

        result = database.transact("plan", self.username, p_id=p_id)
        # print(database.cursor.execute("Select * from customers where username=\"{}\"".format(self.username)).fetchall())
        database.__close__()
        messagebox.showinfo(title="Plan", message=result)
        
        return


    def search(self):
        self.browse_window.destroy()
        
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
        SubmitBtn = Button(search_window, text="Submit", bg='black', fg='white', borderless=1, command=lambda : self.getSearchDetails(bookTitle.get(), bookAuthor.get(), bookCategory.get(), bookLanguage.get(), bookRating.get(), bookPublisher.get(), bookStatus.get(), search=True, frame=search_window))
        SubmitBtn.place(relx=0.28,rely=0.85, relwidth=0.18, relheight=0.08)
        
        quitBtn = Button(search_window,text="Quit", bg='black', fg='white', borderless=1, command=lambda : self.destroy_window(search_window, True))
        quitBtn.place(relx=0.53,rely=0.85, relwidth=0.18, relheight=0.08)
        
        search_window.mainloop()


    def getSearchDetails(self, title, author, category, language, rating, publisher, status, isbn=None, user_bookshelf=False, search=False, frame=None):
        
        database = Database()
        result = []

        if user_bookshelf:
            list_books = database.getCustomerBooks(self.username)
            # print(list_books)
            for i in list_books:
                result.extend(database.bookSearch(title, author, category, language, rating, publisher, status, isbn=i))
        else:
            result = database.bookSearch(title, author, category, language, rating, publisher, status, isbn)
            if result == "Books Not Found":
                messagebox.showerror(title="Search", message=result)
                return

        
        # print(*result, sep="\n")

        textLabel = []
        for i in result:
            output = list(i)
            if output[6] == None:
                output[6] = "0"
            if len(output[-1]) > 0:
                output[-1] = "Available"
            else:
                output[-1] = "Not Available"
            output = [str(i) for i in output]
            textLabel.append(output)
        if search:
            self.destroy_window(frame, search=True, result=textLabel)
            return
        return textLabel
        # self.destroy_window(search_window)


    def browse(self, result=None):
        # Book List Browser
        try:
            self.bookbar.grid_forget()
        except Exception as e:
            print(f"Exception: {e}")
        
        # print(result)
        self.bookbar = tk.Frame(self.browse_window, bg="#e85656")
        self.bookbar.grid(row=0, column=1, sticky='nsew')

        headingFrame1 = tk.Frame(self.bookbar, bg="#fcffbf", bd=5)
        headingFrame1.place(relx=0.05,rely=0.01,relwidth=0.9,relheight=0.12)
        headingLabel = tk.Label(headingFrame1, text=f"Welcome {self.username}", bg='black', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
        
        if result == None:
            result = self.getSearchDetails("", "", "All", "All", "None", "", 0)

        index = tk.IntVar()
        index.set(-1)
        result_length = len(result)

        # Previous Button
        self.prev_button = Button(self.bookbar, text="Previous", bg='black', fg='white', disabledbackground="black", borderless=1, command=lambda : index.set(self.createBookView(result, index.get()-4, result_length, True)))
        self.prev_button.place(relx=0.1, rely=0.92, relwidth=0.18, relheight=0.05)
        

        # Next Button
        self.next_button = Button(self.bookbar, text="Next", bg='black', fg='white', disabledbackground="black", borderless=1, command=lambda : index.set(self.createBookView(result, index.get()+4, result_length, True)))
        self.next_button.place(relx=0.74, rely=0.92, relwidth=0.18, relheight=0.05)
        
        index.set(self.createBookView(result, index.get(), result_length, True))

        self.bookbar.mainloop()
        

    def createBookView(self, result, index, result_length, browse_shelf):
        
        label_dimensions = {0 : [0.05, 0.15], 1 : [0.55, 0.15], 2 : [0.05, 0.55], 3 : [0.55, 0.55]}
        # print(index+1, index+5, result_length)
        result = result[index+1 : index+5]
        # print(result)
        
        self.img.clear()
        for i, values in label_dimensions.items():
            if index <= 0:
                self.prev_button.config(state="disabled")
            else:
                self.prev_button.config(state="normal")

            if index + 4 >= result_length:
                self.next_button.config(state="disabled")
            else:
                self.next_button.config(state="normal")

            if i >= len(result):
                book1 = tk.Canvas(self.bookbar, bg="#e85656")
                book1.place(relx=values[0], rely=values[1], relwidth=0.4, relheight=0.35)
                continue
            book1 = tk.Canvas(self.bookbar)
            book1.place(relx=values[0], rely=values[1], relwidth=0.4, relheight=0.35)

            self.img.append(ImageTk.PhotoImage(Image.open(f"{i}.jpg")))

            tk.Label(book1, image=self.img[i], bg="black").place(relx=0, rely=0, relwidth=1, relheight=0.5)
            tk.Label(book1, text=f"Title: {result[i][1]}", font=("Times", 14, "bold")).place(relx=0.05, rely=0.54)
            tk.Label(book1, text=f"Author: {result[i][2]}", font=("Times", 14, "bold")).place(relx=0.05, rely=0.62)
            tk.Label(book1, text=f"Category: {result[i][4]}", font=("Times", 14, "bold")).place(relx=0.05, rely=0.7)

            if result[i][6] == None:
                result[i][6] = 0
            else:
                result[i][6] = int(result[i][6])
            tk.Label(book1, text=f"Rating: {'★'*result[i][6]}{'☆'*(5 - result[i][6])}", font=("Times", 14, "bold")).place(relx=0.05, rely=0.78)

            Button(book1, text="See More", bg='black', fg='white', borderless=1, command=partial(self.seeMore, result[i][1], result[i][2], result[i][3], result[i][6], result[i][0], self.img[i], browse_shelf)).place(relx=0.275, rely=0.88)

        return index
        

    def seeMore(self, title, author, category, rating, isbn, img, browse_shelf):
        try:
            self.bookbar.grid_forget()
        except Exception:
            pass

        # Book List Browser
        self.bookbar = tk.Frame(self.browse_window, bg="#e85656")
        self.bookbar.grid(row=0, column=1, sticky='nsew')

        headingFrame1 = tk.Frame(self.bookbar, bg="#fcffbf", bd=5)
        headingFrame1.place(relx=0.05,rely=0.01,relwidth=0.9,relheight=0.12)
        headingLabel = tk.Label(headingFrame1, text="Book Details", bg='black', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

        book1 = tk.Canvas(self.bookbar)
        book1.place(relx=0.3, rely=0.15, relwidth=0.4, relheight=0.35)

        tk.Label(book1, image=img, bg="black").place(relx=0, rely=0, relwidth=1, relheight=0.5)
        tk.Label(book1, text=f"Title: {title}", font=("Times", 14, "bold")).place(relx=0.05, rely=0.54)
        tk.Label(book1, text=f"Author: {author}", font=("Times", 14, "bold")).place(relx=0.05, rely=0.62)
        tk.Label(book1, text=f"Category: {category}", font=("Times", 14, "bold")).place(relx=0.05, rely=0.7)

        tk.Label(book1, text=f"Rating: {'★'*rating}{'☆'*(5 - rating)}", font=("Times", 14, "bold")).place(relx=0.05, rely=0.78)
        if browse_shelf:
            Button(book1, text="Add Book", bg='black', fg='white', borderless=1, command=lambda : self.BorrowBook(isbn, self.username)).place(relx=0.275, rely=0.88)
        else:
            Button(book1, text="Read Book", bg='black', fg='white', borderless=1, command=lambda : self.ReadBook(isbn, self.username)).place(relx=0.05, rely=0.88, relwidth=0.44)
            Button(book1, text="Remove Book", bg='black', fg='white', borderless=1, command=lambda : self.RemoveBook(isbn, self.username)).place(relx=0.52, rely=0.88, relwidth=0.44)
        #e85656

        lowerSection = tk.Canvas(self.bookbar)
        lowerSection.place(relx=0.05, rely=0.55, relwidth=0.9, relheight=0.30)
        tk.Label(lowerSection, text="Reviews", font=("Courier", 18, "underline"), bg="white").place(relx=0.01, rely=0.01)
        commentFrame = tk.Frame(lowerSection)
        commentFrame.place(relx=0.01, rely=0.15, relheight=0.8, relwidth=0.98)
        
        v = tk.Scrollbar(lowerSection)
        v.pack(side = tk.RIGHT, fill = tk.Y)
        textAreas = tk.Text(commentFrame, width = 15, height = 18, wrap = tk.NONE, yscrollcommand = v.set)
        # print(title, author, category)
        
        reviews = self.getSearchDetails(title, author, category, "All", rating, "", 1, isbn)[0][7]
        # print(reviews)
        delim = "|/n/n|"
        for i in reviews.split(delim):
            textAreas.insert(tk.END, i + "\n\n")
        textAreas.pack(side=tk.TOP, fill=tk.X)
        textAreas.config(state="disabled")
        v.config(command=textAreas.yview)

        search_variables = [title, author, category]
        # Add Review Button
        self.prev_button = Button(self.bookbar, text="Add Review", bg='black', fg='white', borderless=1, command=lambda : self.addReview(commentFrame, lowerSection, search_variables ))
        self.prev_button.place(relx=0.1, rely=0.92, relwidth=0.18, relheight=0.05)
        

        # Back Button
        if browse_shelf:
            self.next_button = Button(self.bookbar, text="Back", bg='black', fg='white', borderless=1, command=self.browse)
        else:
            self.next_button = Button(self.bookbar, text="Back", bg='black', fg='white', borderless=1, command=self.bookShelf)
        self.next_button.place(relx=0.74, rely=0.92, relwidth=0.18, relheight=0.05)
        # self.next_button.config(command=lambda)
        # = Button(self.bookbar, text="Back", bg='black', fg='white', borderless=1, command=lambda : self.browse())


    def BorrowBook(self, isbn, c_id):
        database = Database()
        result = database.transact("borrow", c_usn=c_id, isbn=int(isbn))
        messagebox.showinfo(title="Borrow Book", message=result)
        return


    def RemoveBook(self, isbn, c_id):
        database = Database()
        result = database.transact("return", c_usn=c_id, isbn=int(isbn))
        messagebox.showinfo(title="Borrow Book", message=result)
        return


    def ReadBook(self, bookID, customer_id):
        try:
            self.bookbar.grid_forget()
        except Exception:
            pass

        # Book List Browser
        self.bookbar = tk.Frame(self.browse_window, bg="#e85656")
        self.bookbar.grid(row=0, column=1, sticky='nsew')

        headingFrame1 = tk.Frame(self.bookbar, bg="#fcffbf", bd=5)
        headingFrame1.place(relx=0.05,rely=0.01,relwidth=0.9,relheight=0.12)
        headingLabel = tk.Label(headingFrame1, text="Read Book", bg='black', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

        lowerSection = tk.Canvas(self.bookbar, bd=1, bg="#e85656")
        lowerSection.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.35)

        database = Database()
        book_path, page = database.getReadBook(customer_id, bookID)
        if page == None:
            page = 0
        if book_path == None:
            messagebox.showerror(title="Read Book", message="Unable to open Book")
            self.bookShelf()
        
        bookmark_page = tk.Label(lowerSection, text=f"Bookmarked Page Number: {page}", bg="#e85656", font=("Courier", 18, "underline"))
        bookmark_page.place(relx=0.05, rely=0.05)

        bookmark_label = tk.Label(lowerSection, text="Change Bookmark: ", bg="#e85656")
        bookmark_label.place(relx=0.05, rely=0.25)

        bookmark = tk.IntVar()
        bookmark.set(page)

        modify_bookmark = tk.Entry(lowerSection, bd=0, textvariable=bookmark)
        modify_bookmark.place(relx=0.45, rely=0.25)

        modify_button = Button(lowerSection, text="Save Changes", bg='black', fg='white', borderless=1, command=lambda : self.changeBookmark(bookID, modify_bookmark.get(), bookmark_page, bookmark))
        modify_button.place(relx=0.05, rely=0.45, relwidth=0.3)

        self.prev_button = Button(self.bookbar, text="Back", bg='black', fg='white', borderless=1, command=self.bookShelf)
        self.prev_button.place(relx=0.05, rely=0.92, relwidth=0.9, relheight=0.05)   

        x = webbrowser.open_new(r'file://'+book_path)
        

    def changeBookmark(self, isbn, page, bookmark_page, bookmark):
        
        bookmark.set(page)
        
        database = Database()
        result = database.updateBookmark(self.username, isbn, page)
        database.__close__()
        
        bookmark_page.config(text=f"Bookmarked Page Number: {page}")
        messagebox.showinfo(title="Bookmark", message=result)


    def addReview(self, commentFrame, lowerSection, search_variables):
        try:
            commentFrame.place_forget()
        except Exception as e:
            print(e)

        commentFrame = tk.Frame(lowerSection)
        commentFrame.place(relx=0.01, rely=0.15, relheight=0.6, relwidth=0.98)

        textAreas = tk.Text(commentFrame, width = 12, height = 18, wrap = tk.WORD)
        textAreas.pack(side=tk.TOP, fill=tk.X)

        tk.Label(lowerSection, text="Rating: ",font=("Courier", 14, "bold")).place(relx=0.01, rely=0.85, relheight=0.1, relwidth=0.2)
        options1 = ['1', '2', '3', '4', '5']
        rating = tk.StringVar()
        ratingInfo = ttk.OptionMenu(lowerSection, rating, options1[0], *options1)
        ratingInfo.place(relx=0.25, rely=0.85, relheight=0.1, relwidth=0.2)
        # print(textAreas.get("1.0", "end"))
        
        
        # partial(database.updateBook, search_variables[0], search_variables[1], search_variables[2], textAreas.get("1.0", tk.END), True)
        self.prev_button.config(text="Insert Review", command=partial(self.sendReviewDetails, search_variables[0], search_variables[1], search_variables[2], self.username, textAreas, rating))


    def sendReviewDetails(self, title, author, category, username, review_string, rating):
        database = Database()
        check = database.updateBook(title, author, category, username, review_string, rating)
        database.__close__()
        messagebox.showinfo(title="Review", message=check)
        return


    def destroy_window(self, frame, return_frame=False, logout=False, search=False, result=None):
        if search:
            frame.destroy()
            self.__init__(self.username, result)
        from LoginRegister import LoginRegisterUI
        if logout:
            frame.destroy()
            login = LoginRegisterUI()
        elif return_frame:
            frame.destroy()
            self.__init__(self.username)


if __name__ == "__main__":
    user = UserUI("Test USER")