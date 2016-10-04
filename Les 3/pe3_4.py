def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:
        return True
    else:
        return False
oldpassword = input("Oude wachtwoord")
newpassword = input("Nieuwe wachtwoord")
print(new_password(oldpassword,newpassword))
