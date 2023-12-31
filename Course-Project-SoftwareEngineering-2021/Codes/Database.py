import sqlite3
from os import path
# import pandas as pd
from shutil import copy2
from os import remove, path
from datetime import datetime

class Database:

    def __init__(self, name=None):
        if name == None:
            name = 'ebook_system.db'
        if not path.exists(name):
            self.create_database(name)
        self.db, self.cursor = self.__connect__(name)


    def create_database(self, name):
        db, cursor = self.__connect__(name)

        cursor.execute("PRAGMA foreign_keys = ON")
        
        cursor.execute("CREATE TABLE IF NOT EXISTS admins(username text PRIMARY KEY, password text)")
        db.commit()

        cursor.execute("CREATE TABLE IF NOT EXISTS plans(p_id integer PRIMARY KEY autoincrement, name text, desc text, validity integer(2), cost integer)")
        db.commit()
        cursor.execute("INSERT INTO plans(p_id) VALUES(0)")
        cursor.execute("DELETE FROM plans where p_id=0")
        db.commit()
        cursor.execute(""" insert into plans(name, desc, validity, cost) VALUES('2months','borrow unlimited number of books for 2 months at 400 rupees', 2, 400) """)
        db.commit()
        cursor.execute(""" insert into plans(name, desc, validity, cost) VALUES('4months','borrow unlimited number of books for 4 months at 600 rupees', 4, 600) """)
        db.commit()
        cursor.execute(""" insert into plans(name, desc, validity, cost) VALUES('6months','borrow unlimited number of books for 6 months at 900 rupees', 6, 900) """)
        db.commit()

        cursor.execute("CREATE TABLE IF NOT EXISTS customers( username text PRIMARY KEY NOT NULL, name text, email text, mobile_no integer(10), age integer(3), password text NOT NULL,p_id integer,FOREIGN KEY(p_id) REFERENCES plans(p_id))")
        db.commit()

        cursor.execute("CREATE TABLE if not EXISTS bookshelf(isbn integer PRIMARY KEY, title text, author text, category text, language text, publication text, ratings integer(1), reviews text, edition integer(2), path text)")
        db.commit()

        cursor.execute("CREATE TABLE If not EXISTS books(issueDate text, returnDate text, username text, page int, FOREIGN KEY(username) REFERENCES customers(username))")
        db.commit()
        cursor.execute("ALTER TABLE books ADD COLUMN isbn INTEGER REFERENCES bookshelf(isbn)")
        db.commit()

        cursor.execute("CREATE TABLE if not EXISTS transactions(t_id integer PRIMARY KEY autoincrement, type text, t_date text,id integer, username text, FOREIGN KEY(username) REFERENCES customers(username))")
        db.commit()

        cursor.execute("INSERT INTO transactions(t_id) VALUES(999)")
        cursor.execute("DELETE FROM transactions where t_id=999")
        db.commit()

        db.close()


    def __connect__(self, name):
        db = sqlite3.connect(name)
        cursor = db.cursor()
        return db, cursor


    def addAdmin(self, username, password):
        try:
            self.cursor.execute("""insert into admins(username, password) 
            VALUES('{}', '{}')""".format(username, password))
            self.db.commit()
            return "Successful"
        except Exception as e:
            print(e)
            return "Admin Already Exists"


    def removeAdmin(self, username):
        self.cursor.execute("""delete from admins 
        where username='{}'""".format(username))
        self.db.commit()
        return "Successful"


    def addUser(self, username, name, email, phone, age, password, plan):
        try:
            self.cursor.execute("""insert into customers(
                username, name, email, mobile_no, age, password, p_id
                ) VALUES('{}', '{}', '{}', {}, {}, '{}', {})
                """.format(username, name, email, phone, age, password, plan))
            self.db.commit()
            return "Registeration Successful"
        except Exception as e:
            print(e)
            return "User with Username Already Exists"


    def removeUser(self, username):
        self.cursor.execute("""delete from customers 
        where username='{}'""".format(username))
        self.db.commit()
        return "Successful"


    def verifyLogin(self, username, password):

        check_admin = self.cursor.execute(f"SELECT password from admins where username='{username}' AND password={password}").fetchone()
        # print(check_admin)
        check_user = self.cursor.execute(f"SELECT password from customers where username='{username}' AND password='{password}'").fetchone()
        # print(check_user)

        if check_admin:
            return "Admin Successful"
        elif check_user:
            return "User Successful"
        else:
            return "Failed"


    def insertBook(self, isbn, title, author, category, language, publication, edition, path):
        
        
        try:
            file_name = path.split("/")[-1]
            new_path = "/Users/afzalmukhtar/Desktop/Front End Python/PDFs/" + file_name
            copy2(path, new_path)
            
            self.cursor.execute("""Insert into bookshelf(isbn, title, author, category, language, publication, edition, path, ratings)
                Values({}, \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", {}, \"{}", {})
                """.format(isbn, title, author, category, language, publication, edition, new_path, 0))
            self.db.commit()
            
            return "Successful"
        except Exception as e:
            print ("Exception Caught: \n{}".format(e))
            return "Failed"
        

    def removeBook(self, isbn, title):
        
        read = self.cursor.execute("""Select * from bookshelf where isbn={} and title=\"{}\"""".format(isbn, title)).fetchone()
        try:
            self.cursor.execute("""update bookshelf set path='' where isbn={} and title=\"{}\"""".format(isbn, title))
            self.db.commit()
            if path.exists(read[-1]):
                remove(read[-1])
                return "Book Successfully Removed"
            # print("File deleted: {}".format(read[-1]))
            # self.cursor.execute("""update bookshelf set path='' where isbn={} and title=\"{}\"""".format(isbn, title))
            # self.db.commit()
            # return "Book Successfully Removed"
            return "Book Not in Path"
        except Exception as e:
            print(f"Error Raised: \n{e}")
            return "Book Does not Exist"


    def updateBook(self, title, author, category, username, review_string, rating):
        
        review_string = review_string.get("1.0", "end")
        old_reviews_query = f"Select reviews from bookshelf where title=\"{title}\" AND author=\"{author}\" AND category=\"{category}\""
        old_reviews = self.cursor.execute(old_reviews_query).fetchone()[0]
        old_rating = f"Select ratings from bookshelf where title=\"{title}\" AND author=\"{author}\" AND category=\"{category}\""
        old_rating = self.cursor.execute(old_rating).fetchone()[0]
        
        # print(repr(review_string))
        if review_string == "" or review_string == "\n":
            return "Field Cannot Be Empty"

        if old_reviews == None:
            new_review = f"{username}\n{review_string}"
        else:
            new_review = old_reviews + f"|/n/n|@{username}\n{review_string}"
        
        total_review = len(new_review.split("|/n/n|"))
        if total_review == 0:
            total_review = 1
        if old_rating == None:
            old_rating = 0
        total_review = int((int(rating.get()) + int(old_rating)) / total_review)
        
        query = f"Update bookshelf set reviews=\"{new_review}\", ratings={total_review} where title=\"{title}\" AND author=\"{author}\" AND category=\"{category}\""
        self.cursor.execute(query)
        self.db.commit()
        return "Review Added Successfully"
        # print(self.cursor.execute(f"SELECT reviews from bookshelf where title=\"{title}\" AND author=\"{author}\" AND category=\"{category}\"").fetchall())


    def bookSearch(self, title, author, category, language, rating, publisher, status, isbn=None):

        query = """Select * from bookshelf """
        query_list = []
        # print(title, author, category, language, rating, genre, status)
        
        if isbn != None:
            query_list.append(f"""isbn={int(isbn)}""")
        else:
            if title != "":
                query_list.append(f"""LOWER(title)=LOWER(\"{title}\")""")
            if author != "":
                query_list.append(f"""LOWER(author)=LOWER(\"{author}\")""")
            if category != "All":
                query_list.append(f"""LOWER(category)=LOWER(\"{category}\")""")
            if language != "All":
                query_list.append(f"""LOWER(language)=LOWER(\"{language}\")""")
            if rating != "None":
                query_list.append(f"""ratings={int(rating)}""")
            if publisher != "" and publisher != "All":
                query_list.append(f"publication=\"{publisher}\"")
            if status == 1:
                query_list.append("""LOWER(path)!=\'\' """)
        
        if len(query_list) >= 1:
            query += """Where """ + """ AND """.join(query_list)
        # print(query)
        search_result = self.cursor.execute(query).fetchall()
        # print(*search_result, sep="\n")
        if len(search_result):
            return search_result
        else:
            return "Books Not Found"


    def getCustomerBooks(self, c_id):
        result = self.cursor.execute("Select isbn from books where username=\"{}\" AND (returnDate IS NULL OR returnDate=\'\')".format(c_id)).fetchall()
        if len(result):
            result = [i[0] for i in result]
        # print(result)
        return result


    def check_plan(self, c_usn):
        st=self.cursor.execute(""" select(p_id) from customers where username='{}'""".format(c_usn)).fetchall()
        # print(st)
        try:
            if st[0][0]:
                return True
            else:
                return False
        except Exception as e:
            print(f"Exception: {e}")
            return False


    def transact(self, t_type, c_usn, isbn=0, p_id=1):
        
        date = datetime.now().date().strftime("%d/%m/%Y")
        if t_type == "plan":
            self.cursor.execute(""" insert into transactions(type, t_date, id, username) VALUES('plan', \"{}\", {}, \"{}\")""".format(date, p_id, c_usn))
            self.cursor.execute(""" update customers set p_id={} where username=\"{}\" """.format(p_id, c_usn))
            self.db.commit()
            return "Plan Updated"
        
        res = self.check_plan(c_usn)
        if not res:
            return "You Donot Have a Subscription"
        
        book_list = self.getCustomerBooks(c_usn)
        # print(book_list)
        # print(isbn in book_list, isbn, type(isbn))
        if t_type == "borrow" and isbn not in book_list:
            self.cursor.execute(""" insert into transactions(type, t_date, id, username) VALUES ('borrow',\"{}\",{},\"{}\")""".format(date, isbn, c_usn))
            self.cursor.execute(""" insert into books(issueDate, username, isbn, page) VALUES (\"{}\", \"{}\", {}, {})""".format(date, c_usn, isbn, 0))
            self.db.commit()
            return "Book Added To Bookshelf"
            
        elif t_type == 'return':
            self.cursor.execute(""" insert into transactions(type, t_date, id, username) VALUES ('return', \"{}\", {}, \"{}\")""".format(date, isbn, c_usn))
            self.cursor.execute(""" update books set returnDate=\"{}\" where isbn={} AND username=\"{}\" """.format(date, isbn, c_usn))
            self.db.commit()
            return "Book Returned"
        else:
            return "Book Already in Bookshelf"


    def getReadBook(self, c_id, isbn):
        try:
            path = self.cursor.execute("Select path from bookshelf where isbn=\"{}\"".format(isbn)).fetchone()[0]
            page = self.cursor.execute("Select page from books where username=\"{}\" AND isbn=\"{}\"".format(c_id, isbn)).fetchone()[0]
            return (path, page)
        except Exception as e:
            print(f"Exception: {e}")


    def updateBookmark(self, c_id, isbn, page):
        self.cursor.execute("UPDATE books set page={} where username=\"{}\" AND isbn={}".format(page, c_id, isbn))
        self.db.commit()
        return "Bookmark Updated Successfully"


    def getTransactions(self):
        try:
            return self.cursor.execute("Select * from transactions").fetchall()
        except Exception as e:
            print(f"Exception: {e}")
            return []


    def __close__(self):
        if self.cursor:
            self.cursor.close()
        if self.db: 
            self.db.close()


if __name__ == "__main__":
    database = Database()