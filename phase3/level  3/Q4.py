import sqlite3

def create_connection():
    """建立 اتصال بقاعدة البيانات"""
    return sqlite3.connect('database.db')

def create_table():
    """إنشاء جدول في قاعدة البيانات"""
    conn = create_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users
        (id INTEGER PRIMARY KEY, name TEXT, email TEXT)
    ''')
    conn.commit()
    conn.close()

def add_user(name, email):
    """اضافة سجل جديد في قاعدة البيانات"""
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

def delete_user(id):
    """حذف سجل من قاعدة البيانات"""
    conn = create_connection()
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update_user(id, name, email):
    """تحديث سجل في قاعدة البيانات"""
    conn = create_connection()
    c = conn.cursor()
    c.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, id))
    conn.commit()
    conn.close()

def get_all_users():
    """استرجاع جميع السجلات من قاعدة البيانات"""
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close()
    return rows

def main():
    create_table()
    
    while True:
        print("اختر العملية:")
        print("1. اضافة سجل جديد")
        print("2. حذف سجل")
        print("3. تحديث سجل")
        print("4. استرجاع جميع السجلات")
        print("5. انهاء البرنامج")
        
        choice = input("الاختيار: ")
        
        if choice == '1':
            name = input("اسم المستخدم: ")
            email = input("البريد الالكتروني: ")
            add_user(name, email)
        elif choice == '2':
            id = int(input("رقم السجل: "))
            delete_user(id)
        elif choice == '3':
            id = int(input("رقم السجل: "))
            name = input("اسم المستخدم الجديد: ")
            email = input("البريد الالكتروني الجديد: ")
            update_user(id, name, email)
        elif choice == '4':
            rows = get_all_users()
            for row in rows:
                print(row)
        elif choice == '5':
            break
        else:
            print("اختيار غير صالح")

if __name__ == "__main__":
    main()