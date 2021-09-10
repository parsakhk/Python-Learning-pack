import sqlite3
from tkinter import *

def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :zipcode)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': a_name.get(),
            'city': c_name.get(),
            'zipcode': z_name.get()
        }
    )
    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("DELETE from addresses WHERE oid = " + deleteBox.get() )
    deleteBox.delete(0, END)    
    conn.commit()
    conn.close()

def update():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode,

        WHERE oid = :oid""",
        {
            'first': f_name_editor.get(),
            'last':  l_name_editor.get(),
            'address': a_name_editor.get(),
        }
        
        )
    conn.commit()
    conn.close()


def update():
    editor = Tk()
    editor.title("Update Record")
    editor.geometry("400x600")
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("SELECT * FROM addresses WHERE oid = " + deleteBox.get() )
    records = c.fetchall()


    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=10)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=10)
    a_name_editor = Entry(editor, width=30)
    a_name_editor.grid(row=2, column=1, padx=10)
    c_name_editor = Entry(editor, width=30)
    c_name_editor.grid(row=3, column=1, padx=10)
    z_name_editor = Entry(editor, width=30)
    z_name_editor.grid(row=4, column=1, padx=10)
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        a_name_editor.insert(0, record[2])
        c_name_editor.insert(0, record[3])
        z_name_editor.insert(0, record[4])

    f_label_editor = Label(editor, text="First name:")
    f_label_editor.grid(row=0, column=0)
    l_label_editor = Label(editor, text="Last name:")
    l_label_editor.grid(row=1, column=0)
    a_label_editor = Label(editor, text="Address:")
    a_label_editor.grid(row=2, column=0)
    c_label_editor = Label(editor, text="City:")
    c_label_editor.grid(row=3, column=0)
    z_label_editor = Label(editor, text="Zip Code:")
    z_label_editor.grid(row=4, column=0)

    Save = Button(editor, text="Save", command=edit)
    Save.grid(row=5, column=0, columnspan=2, pady=10, padx=20, ipadx=135)
    conn.commit()
    conn.close()

def show():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()

    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" +str(record[5]) + "\n"

    queryLabel = Label(root, text=print_records)
    queryLabel.grid(row=10, column=0, columnspan=2)

    conn.commit()
    conn.close()

root = Tk()
root.geometry("400x600")
#Create Entries
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=10)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=10)
a_name = Entry(root, width=30)
a_name.grid(row=2, column=1, padx=10)
c_name = Entry(root, width=30)
c_name.grid(row=3, column=1, padx=10)
z_name = Entry(root, width=30)
z_name.grid(row=4, column=1, padx=10)

deleteBox = Entry(root, width=30)
deleteBox.grid(row=8, column=1  )

#Create Label entries
f_label = Label(root, text="First name:")
f_label.grid(row=0, column=0)
l_label = Label(root, text="Last name:")
l_label.grid(row=1, column=0)
a_label = Label(root, text="Address:")
a_label.grid(row=2, column=0)
c_label = Label(root, text="City:")
c_label.grid(row=3, column=0)
z_label = Label(root, text="Zip Code:")
z_label.grid(row=4, column=0)
deleteBox_label = Label(root, text="Delete ID")
deleteBox_label.grid(row=8, column=0)

#Make submit Button
submitButton = Button(root, text="Submit a record to Database", command=submit)
submitButton.grid(row=5, column=0, columnspan=2, padx=20, pady=20, ipadx=100)

query_button = Button(root, text="Show records", command=show)
query_button.grid(row=6, column=0, columnspan=2, pady=10, padx=20, ipadx=135)

Delete_button = Button(root, text="Delete record", command=delete)
Delete_button.grid(row=9, column=0, columnspan=2, padx=10, pady=20, ipadx=135)

Update_bUTTON = Button(root, text="Update record", command=update)
Update_bUTTON.grid(row=10, column=0, columnspan=2, pady=10, padx=20, ipadx=135)

root.mainloop()
