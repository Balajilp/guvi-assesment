import re
def register():
    
    def check_email(email):
        regex = r"\b\w+@\w+\.[a-z]{2,3}\b"
        if re.search(regex, email):
            return True
        else:
            print("please enter a valid email id")
            register()


    def password_check(passwd):
        SpecialSym = ['$', "@", '#', "%"]

        if len(passwd) <= 5:
            print("password must be greater than 5")
            register()
            return
        if len(passwd) >= 16:
            print("password must be less than 16")
            register()
            return

        if not any(ch.isdigit() for ch in passwd):
            print("password must have 1 digit")
            register()
            return

        if not any(ch.isupper() for ch in passwd):
            print("password must have 1 upper character")
            register()
            return

        if not any(ch.islower() for ch in passwd):
            print("pasword must have 1 lowyer characer")
            register()
            return

        if not any(ch in SpecialSym for ch in passwd):
            print("password must have 1 spcl chacractr")
            register()
            return
        return True



    x = input("Enter Email Id: ")
    y = input("Enter Your password: ")
    if check_email(x) and password_check(y):
        a = open("task.txt", 'a')
        a.write(x+", "+y+"\n")
        a.close()
        print("registration successful")
        home()


def access():
    db = open("task.txt", "r")
    kk = input("enter email id: ")
    gk = input("Enter Password: ")
    # forgot = input("forgotten possword")
    if kk and gk:
        d = []
        f = []
        for i in db:
            a, b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d,f))
        if data[kk] == gk:
            print("login successfull")
            home()
        else:
            print("Invalid Username or Password")
            option2 = input("Reregister or forget")
            if option2 == "Reregister":
                register()
            elif option2 == "forget":
                forget()


def forget():
    ab = input("Enter your registered email address: ")
    fb = open("task.txt", 'r')
    mail = []
    pas = []
    for x in fb:
        new_mail, new1_mail = x.split(", ")
        new1_mail = new1_mail.strip()
        if new_mail == ab:
            print("Your password is", new1_mail)
            access()
            return
    print("No match found, please register")
    home()



def home(option=None):
    option = input("Login | signup: ")
    if option == "Login":
        access()
    elif option == "signup":
        register()
    else:
        print("please enter an option without mistake")
home()



