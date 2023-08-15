from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
from tkinter.ttk import Combobox

root = Tk()
root.title("Main Window")
root.minsize(width=800, height=300)
root.maxsize(width=800, height=300)
Total = 0
Items = {}


def Customer():
    root.withdraw()
    customer_login_window = Toplevel(root)
    customer_login_window.title("Customer login")
    customer_login_window.minsize(height=160, width=510)
    customer_login_window.maxsize(height=160, width=510)

    def login():
        username = username_entry.get()
        password = password_entry.get()

        if username == "" or password == "":
            Messagebox.showinfo(".", "Please Fill all fields")
        else:
            customer_login_window.withdraw()
            con = mysql.connect(host="localhost", user="root", database="online_order")
            cursor = con.cursor()
            cursor.execute(" select * from customer_login")
            check = cursor.fetchall()
            for i in check:
                if i[0] == username and i[1] == password:
                    con.close()
                    customer_window = Toplevel(root)
                    customer_window.title("New Window")
                    customer_window.geometry("450x100")
                    dropdown = Combobox(customer_window, values=["kfc", "bovichic", "burger hut", "broadway"],
                                        font=("Product Sans Bold", 15))
                    dropdown.pack()
                    dropdown.set("Select a restaurant")

                    def kfc():
                        order_window = Toplevel(customer_window)
                        order_window.title("Cart")
                        order_window.minsize(width=500, height=300)
                        Label(order_window, text="Item  :  Price", font=("Neutral Face", 15)).pack()
                        Label(order_window, text="Your Total is: ", font=("Product Sans Bold", 15)).place(x=10, y=5)

                        kfc_window = Toplevel(customer_window, bg="white")
                        kfc_window.minsize(width=500, height=300)
                        kfc_window.maxsize(width=500, height=300)
                        Label(kfc_window, fg="black", bg="white", text="Welcome to",
                              font=("CeraCondensedPro-Bold", 25)).pack()
                        Label(kfc_window, fg="firebrick1", bg="white", text="KFC",
                              font=("FrizQuadrataBold", 40, "normal", "italic")).pack()
                        con = mysql.connect(host="localhost", user="root", database="online_order")
                        cursor = con.cursor()

                        def populate_dropdown():
                            conn = mysql.connect(host="localhost", user="root", database="online_order")
                            cursor = conn.cursor()
                            cursor.execute('SELECT Name FROM kfc')
                            data = cursor.fetchall()
                            conn.close()
                            dropdown['values'] = ()
                            dropdown['values'] = [row[0] for row in data]

                        label = Label(kfc_window, bg="white", text="Select Item:", font=("CeraCondensedPro-Bold", 25))
                        label.pack(pady=10)
                        dropdown = Combobox(kfc_window, font=("Product Sans Bold", 15))
                        populate_dropdown()
                        dropdown.pack()

                        def Add():
                            global Total
                            global Items
                            con = mysql.connect(host="localhost", user="root", database="online_order")
                            cursor = con.cursor()
                            cursor.execute("select * from kfc where Name='" + dropdown.get() + "'")
                            price = cursor.fetchall()
                            for i in price:
                                abc = str(i[0]) + " : " + str(i[1])
                                Label(order_window, text=abc, font=("Product Sans Bold", 15)).pack()
                                Total += int(i[1])
                                Items.update({i[0]: i[1]})
                            Label(order_window, text=Total, width=5, font=("Neutral Face", 30, "bold")).place(x=1, y=30)
                            return Total and Items

                        def Checkout():
                            global Total
                            global Items
                            Total = str(Total)
                            Restaurant = "Kfc"
                            con = mysql.connect(host="localhost", user="root", database="online_order")
                            cursor = con.cursor()
                            cursor.execute(
                                "insert into orders values('" + username + "','" + Restaurant + "', '" + Total + "')")
                            cursor.execute("commit")
                            con.close()
                            kfc_window.withdraw()
                            print("Receipt:")
                            for a, b in Items.items():
                                print(a, " : ", b)
                            print("Total: ", Total)

                        Button(kfc_window, bg="white", font=("CeraCondensedPro-Bold", 15), text="Add",
                               command=Add).pack()
                        Button(kfc_window, bg="white", font=("CeraCondensedPro-Bold", 15),
                               text="Checkout", command=Checkout).pack()

                        con.close()

                    def bovichic():
                        order_window = Toplevel(customer_window)
                        order_window.title("Cart")
                        order_window.minsize(width=500, height=300)
                        Label(order_window, text="Item  :  Price", font=("Neutral Face", 15)).pack()
                        Label(order_window, text="Your Total is: ", font=("Product Sans Bold", 15)).place(x=10, y=5)

                        bovichic_window = Toplevel(customer_window, bg="white")
                        bovichic_window.minsize(width=500, height=300)
                        bovichic_window.maxsize(width=500, height=300)
                        Label(bovichic_window, fg="darkgoldenrod1", bg="white", text="WELCOME TO",
                              font=("Product Sans Bold", 25)).pack()
                        Label(bovichic_window, fg="firebrick1", bg="white", text="Bovi Chic",
                              font=("Candy Beans", 40)).pack()
                        con = mysql.connect(host="localhost", user="root", database="online_order")
                        cursor = con.cursor()

                        def populate_dropdown():
                            conn = mysql.connect(host="localhost", user="root", database="online_order")
                            cursor = conn.cursor()
                            cursor.execute('SELECT Name FROM bovichic')
                            data = cursor.fetchall()
                            conn.close()
                            dropdown['values'] = ()
                            dropdown['values'] = [row[0] for row in data]

                        label = Label(bovichic_window, bg="white", text="SELECT ITEM", font=("Product Sans Bold", 15))
                        label.pack(pady=10)
                        dropdown = Combobox(bovichic_window, font=("Product Sans Bold", 15))
                        populate_dropdown()
                        dropdown.pack()

                        def Add():
                            global Total
                            global Items
                            con = mysql.connect(host="localhost", user="root", database="online_order")
                            cursor = con.cursor()
                            cursor.execute("select * from bovichic where Name='" + dropdown.get() + "'")
                            price = cursor.fetchall()
                            for i in price:
                                abc = str(i[0]) + " : " + str(i[1])
                                Label(order_window, text=abc, font=("Product Sans Bold", 15)).pack()
                                Total += int(i[1])
                                Items.update({i[0]: i[1]})
                            Label(order_window, text=Total, width=5, font=("Neutral Face", 30, "bold")).place(x=1, y=30)
                            return Total and Items

                        def Checkout():
                            global Total
                            global Items
                            Total = str(Total)
                            Restaurant = "Bovichic"
                            con = mysql.connect(host="localhost", user="root", database="online_order")
                            cursor = con.cursor()
                            cursor.execute(
                                "insert into orders values('" + username + "','" + Restaurant + "', '" + Total + "')")
                            cursor.execute("commit")
                            con.close()
                            bovichic_window.withdraw()
                            print("Receipt:")
                            for a, b in Items.items():
                                print(a, " : ", b)
                            print("Total: ", Total)

                        Button(bovichic_window, bg="white", font=("Product Sans Bold", 15), text="ADD",
                               command=Add).pack()
                        Button(bovichic_window, bg="white", font=("Product Sans Bold", 15),
                               text="CHECKOUT", command=Checkout).pack()

                        con.close()

                    def burger_hut():
                        order_window = Toplevel(customer_window)
                        order_window.title("Cart")
                        order_window.minsize(width=500, height=300)
                        Label(order_window, text="Item  :  Price", font=("Neutral Face", 15)).pack()
                        Label(order_window, text="Your Total is: ", font=("Product Sans Bold", 15)).place(x=10, y=5)

                        burger_hut_window = Toplevel(customer_window, bg="white")
                        burger_hut_window.minsize(width=500, height=300)
                        burger_hut_window.maxsize(width=500, height=300)
                        Label(burger_hut_window, fg="black", bg="white", text="Welcome to",
                              font=("Product Sans Bold", 25)).pack()
                        Label(burger_hut_window, fg="firebrick1", bg="white", text="Burger Hut",
                              font=("Neutral Face", 40, "bold")).pack()
                        con = mysql.connect(host="localhost", user="root", database="online_order")
                        cursor = con.cursor()

                        def populate_dropdown():
                            conn = mysql.connect(host="localhost", user="root", database="online_order")
                            cursor = conn.cursor()
                            cursor.execute('SELECT Name FROM burger_hut')
                            data = cursor.fetchall()
                            conn.close()
                            dropdown['values'] = ()
                            dropdown['values'] = [row[0] for row in data]

                        label = Label(burger_hut_window, bg="white", text="Select Item:",
                                      font=("CeraCondensedPro-Bold", 25))
                        label.pack(pady=10)
                        dropdown = Combobox(burger_hut_window, font=("Product Sans Bold", 15))
                        populate_dropdown()
                        dropdown.pack()

                        def Add():
                            global Total
                            global Items
                            con = mysql.connect(host="localhost", user="root", database="online_order")
                            cursor = con.cursor()
                            cursor.execute("select * from burger_hut where Name='" + dropdown.get() + "'")
                            price = cursor.fetchall()
                            for i in price:
                                abc = str(i[0]) + " : " + str(i[1])
                                Label(order_window, text=abc, font=("Product Sans Bold", 15)).pack()
                                Total += int(i[1])
                                Items.update({i[0]: i[1]})
                            Label(order_window, text=Total, width=5, font=("Neutral Face", 30, "bold")).place(x=1, y=30)
                            return Total and Items

                        def Checkout():
                            global Total
                            global Items
                            Total = str(Total)
                            Restaurant = "Burger Hut"
                            con = mysql.connect(host="localhost", user="root", database="online_order")
                            cursor = con.cursor()
                            cursor.execute(
                                "insert into orders values('" + username + "','" + Restaurant + "', '" + Total + "')")
                            cursor.execute("commit")
                            con.close()
                            burger_hut_window.withdraw()
                            print("Receipt:")
                            for a, b in Items.items():
                                print(a, " : ", b)
                            print("Total: ", Total)

                        Button(burger_hut_window, bg="white", font=("CeraCondensedPro-Bold", 15),
                               text="Add", command=Add).pack()
                        Button(burger_hut_window, bg="white", font=("CeraCondensedPro-Bold", 15),
                               text="Checkout", command=Checkout).pack()

                        con.close()

                    def broadway():
                        order_window = Toplevel(customer_window)
                        order_window.title("Cart")
                        order_window.minsize(width=500, height=300)
                        Label(order_window, text="Item  :  Price", font=("Neutral Face", 15)).pack()
                        Label(order_window, text="Your Total is: ", font=("Product Sans Bold", 15)).place(x=10, y=5)

                        broadway_window = Toplevel(customer_window, bg="white")
                        broadway_window.minsize(width=500, height=300)
                        broadway_window.maxsize(width=500, height=300)
                        Label(broadway_window, fg="darkgoldenrod1", bg="white", text="Welcome to",
                              font=("Product Sans Bold", 25)).pack()
                        Label(broadway_window, fg="black", bg="white", text="Broadway",
                              font=("Neutral Face", 40, "bold")).pack()
                        con = mysql.connect(host="localhost", user="root", database="online_order")
                        cursor = con.cursor()

                        def populate_dropdown():
                            conn = mysql.connect(host="localhost", user="root", database="online_order")
                            cursor = conn.cursor()
                            cursor.execute('SELECT Name FROM broadway')
                            data = cursor.fetchall()
                            conn.close()
                            dropdown['values'] = ()
                            dropdown['values'] = [row[0] for row in data]

                        label = Label(broadway_window, fg="darkgoldenrod1", bg="white", text="Select Item:",
                                      font=("CeraCondensedPro-Bold", 25))
                        label.pack(pady=10)
                        dropdown = Combobox(broadway_window, font=("Product Sans Bold", 15))
                        populate_dropdown()
                        dropdown.pack()

                        def Add():
                            global Total
                            global Items
                            con = mysql.connect(host="localhost", user="root", database="online_order")
                            cursor = con.cursor()
                            cursor.execute("select * from broadway where Name='" + dropdown.get() + "'")
                            price = cursor.fetchall()
                            for i in price:
                                abc = str(i[0]) + " : " + str(i[1])
                                Label(order_window, text=abc, font=("Product Sans Bold", 15)).pack()
                                Total += int(i[1])
                                Items.update({i[0]: i[1]})
                            Label(order_window, text=Total, width=5, font=("Neutral Face", 30, "bold")).place(x=1, y=30)
                            return Total and Items

                        def Checkout():
                            global Total
                            global Items
                            Total = str(Total)
                            Restaurant = "Broadway"
                            con = mysql.connect(host="localhost", user="root", database="online_order")
                            cursor = con.cursor()
                            cursor.execute(
                                "insert into orders values('" + username + "','" + Restaurant + "', '" + Total + "')")
                            cursor.execute("commit")
                            con.close()
                            broadway_window.withdraw()
                            print("Receipt:")
                            for a, b in Items.items():
                                print(a, " : ", b)
                            print("Total: ", Total)

                        Button(broadway_window, bg="white", font=("CeraCondensedPro-Bold", 15), text="Add",
                               command=Add).pack()
                        Button(broadway_window, bg="white", font=("CeraCondensedPro-Bold", 15),
                               text="Checkout", command=Checkout).pack()

                        con.close()

                    def select():

                        if dropdown.get() == "kfc":
                            kfc()
                            customer_window.withdraw()
                        elif dropdown.get() == "bovichic":
                            bovichic()
                            customer_window.withdraw()
                        elif dropdown.get() == "burger hut":
                            burger_hut()
                            customer_window.withdraw()
                        elif dropdown.get() == "broadway":
                            broadway()
                            customer_window.withdraw()
                        else:
                            Messagebox.showinfo("", "Please Select a Resturant")

                    Button(customer_window, text="Select", command=select).pack()

    def Register():

        register_window = Toplevel(root)
        register_window.title("Registration")
        register_window.minsize(height=100,width=800)
        register_window.maxsize(height=100,width=800)
        lbl12 = Label(register_window, text="Username:", font=("Product Sans Bold", 15))
        lbl12.grid(row=0, column=0)
        username_entry2 = Entry(register_window, width=50, font=("Product Sans Bold", 15))
        username_entry2.grid(row=0, column=1)
        lbl22 = Label(register_window, text="Password:", font=("Product Sans Bold", 15))
        lbl22.grid(row=1, column=0)
        password_entry2 = Entry(register_window, width=50, font=("Product Sans Bold", 15))
        password_entry2.grid(row=1, column=1)


        def Click():
            username2 = username_entry2.get()
            password2 = password_entry2.get()
            if username_entry2 == "" or password_entry2 == "":
                Messagebox.showinfo(".", "Please Fill all fields")
            else:
                con = mysql.connect(host="localhost", user="root", database="online_order")
                cursor = con.cursor()

                cursor.execute("insert into customer_login values('" + username2 + "', '" + password2 + "')")
                cursor.execute("commit")
                Messagebox.showinfo(".", "User registered")
                con.close()
                register_window.withdraw()

        Button(register_window, text="submit", command=Click).grid(row=2, column=1)

    lbl1 = Label(customer_login_window, text="Username:", font=("Product Sans Bold", 15))
    lbl1.grid(row=0, column=0)
    username_entry = Entry(customer_login_window, width=30, font=("Product Sans Bold", 15))
    username_entry.grid(row=0, column=1)
    lbl2 = Label(customer_login_window, text="Password:", font=("Product Sans Bold", 15))
    lbl2.grid(row=1, column=0)
    password_entry = Entry(customer_login_window, width=30, font=("Product Sans Bold", 15))
    password_entry.grid(row=1, column=1)
    Button(customer_login_window, text="Login", command=login, font=("Product Sans Bold", 15)).place(x=100, y=70)
    Label(customer_login_window, text="Don't have an account:", font=("Product Sans Bold", 15)).place(x=178, y=76)
    Button(customer_login_window, text="Register", command=Register, font=("Product Sans Bold", 15)).place(x=400, y=70)


def admin():
    admin_login_window = Toplevel(root)
    admin_login_window.title("Admin Login")
    admin_login_window.minsize(width=500, height=300)
    admin_login_window.maxsize(width=500, height=300)
    root.withdraw()
    lbl3 = Label(admin_login_window, text="Username:", font=("Product Sans Bold", 15))
    lbl3.grid(row=0, column=0)
    username3_entry = Entry(admin_login_window, width=50, font=("Product Sans Bold", 15))
    username3_entry.grid(row=0, column=1)
    lbl3 = Label(admin_login_window, text="Password:", font=("Product Sans Bold", 15))
    lbl3.grid(row=1, column=0)
    password_entry3 = Entry(admin_login_window, width=50, font=("Product Sans Bold", 15))
    password_entry3.grid(row=1, column=1)

    def admin_login():
        username3 = username3_entry.get()
        password3 = password_entry3.get()

        if username3 == "admin" and password3 == "123456":
            admin_window = Toplevel(admin_login_window)
            admin_window.title("Admin Dashboard")
            admin_window.minsize(width=500, height=300)
            admin_window.maxsize(width=500, height=300)
            admin_login_window.withdraw()

            def orders():
                view_order_window = Toplevel(admin_window)
                con = mysql.connect(host="localhost", user="root", database="online_order")
                cursor = con.cursor()
                cursor.execute("select * from orders")
                orderr = cursor.fetchall()
                for i in orderr:
                    abcd = "Customer: " + str(i[0]) + "|Restaurant: " + str(i[1]) + "|Total Bill: " + str(i[2])
                    Label(view_order_window, text=abcd).pack()

            Button(admin_window, text=" View Orders", command=orders).pack()
            Button(admin_window, text="Manage Resturants").pack()

        else:
            Messagebox.showinfo("", "Invalid Username or Password")

    Button(admin_login_window, text="Login", command=admin_login, font=("Product Sans Bold", 15)).place(x=103, y=80)


Start = Label(root, text="Who are you?", font=("Neutral Face", 50, "bold"))
Start.place(x=135, y=15)
Customer = Button(root, text="Customer", font=("Product Sans Bold", 15), command=Customer, width=15, height=3)
Customer.place(x=25, y=140)
Owner = Button(root, text="Restaurant Owner", font=("Product Sans Bold", 15), width=15, height=3)
Owner.place(x=300, y=140)
Admin = Button(root, text="Admin", font=("Product Sans Bold", 15), command=admin, width=15, height=3)
Admin.place(x=570, y=140)
root.mainloop()
