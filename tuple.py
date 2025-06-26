users = ('sana','sarvamm','sarthak','asif')
keys = ('sana123','sarvamm123','sarthak123','asif123')
def login():
    user = input("Enter your username: ")
    if user in users:
        index = users.index(user)  
        password = input("Enter your password: ")
        if password == keys[index]:  
            print("Login successful!✔ ")
        else:
            print("Incorrect password.")
    else:
        print("Username not found.😒(*/ω＼*)")

login()