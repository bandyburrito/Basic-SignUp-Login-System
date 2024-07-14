
while True:
    accountlogin = input("Pershendetje,\nA deshironi te krijoni nje llogari: ")
    
    if accountlogin == "Po":
        username = input("Si deshironi ta keni Userin: ")
        print(f"Useri juaj eshte zgjedhur: {username}")

        while True:
            password = input("Si deshironi ta keni Passwordin (te jete vetem numra): ")
            if password.isdigit():
                print(f"Passwordi juaj eshte zgjedhur: {password}")
                print("Llogaria juaj eshte krijuar me sukses")
                break
            else:
                print("Passwordi duhet te jete vetem numra! Ju lutem, provoni perseri.")
        break
    elif accountlogin == "Jo":
        print("Faleminderit shume :D")
        continue
    else:
        print("Duhet te thuani: Po ose Jo")
    
    
while True:
    emri = input("Sheno username: ")
    if emri != username:
        continue
    passwordi = input("Shkruaje passwordin: ")
    if passwordi == password:
        break
        
print("Emri ose Passwordi esht sakte")




    
    









    




