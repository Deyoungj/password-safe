import sqlite3
from hashlib import sha256


ADMIN_PASSWORD = '1234567'


print('Password:')
password =input(':')

while password != ADMIN_PASSWORD:
    print('wrong password')
    print('Password:')
    password = input(':')

if  password == ADMIN_PASSWORD:
    print('what would you like to do today:')
    conn = sqlite3.connect('password_safe.db')
    cursor = conn.cursor()
    try:
        cursor.execute("""CREATE TABLE PASSWORD_SAFE(
            service text,
            password text
            )""")
        print('your safe as been created')
    except:
        print('you already have a save.')

def save_password(name,passcode):
    # service and password to be saved.
    with conn:
        cursor.execute("INSERT INTO PASSWORD_SAFE VALUES(:service,:password)",{'service':name, 'password':passcode})

def password_gen(secret_key):
    # generating hashed password.
    return sha256(secret_key.encode('utf-8')).hexdigest()[:20]

def delete_password(delete):
    # deleting service and password
    with conn:
        cursor.execute("DELETE from PASSWORD_SAFE WHERE service=:service",{'service':delete})

def view_password(views):
        # viewing service and password.
        cursor.execute("SELECT *FROM PASSWORD_SAFE WHERE service=:service",{'service':view})
        for row in cursor.fetchone():
            print(row)
            
while True:
    print('*'*4,'COMMAND','*'*5)
    print(' q = quit')
    print(' s = save')
    print(' d = delete')
    print(' v = view')
    print('*'*4,'COMMAND','*'*5)

    command = input(':')
    if command == 'q':
        break

    if command == 's':
        print('Name of service you want to save?')
        save = input(':')
        hashed = password_gen(save)
        print('Here is your password:', hashed)
        save_password(save,hashed)
        print('your password as been saved.')

    if command == 'd':
        print('name of service you want to delete:')
        service = input(':')
        delete_password(service)
        print(service, 'has been deleted')

    if command == 'v':
        print('name of service you want to view:')
        view = input(':')
        view_password(view)
conn.close()
