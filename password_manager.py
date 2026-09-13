import random
import string

passwords={}
#load existing password file
try:
    with open ("passwords.txt","r") as file:
        for line in file:
            website,pwd=line.strip().split(":")
            passwords[website]=pwd

except:
    pass

def generate_password():
    chars= string.ascii_letters +string.digits + "!@#$%^&*()-+"
    password= "".join(random.choice(chars)for _ in range(8))
    return password

while True:
      print("-----PASSWORD MANAGER APP----- ")
      print("1.SAVE PASSWORD")
      print("2.view PASSWORDS")
      print("3.GENERATE PASSWORD")
      print("5.exit")
      choice=input("ENTER YOUR CHOICE: ")

      if choice=="1":
          site = input("enter the website name:")
          pwd = input("enter the password:")

          passwords[site]=pwd

          with open("passwords.txt","a") as file:
              file.write(f"{site}:{pwd}\n")

          print("password saved")  

      elif choice=="2":
            if not passwords:
                print("no data")

            else:
                for site,pwd in passwords.items():
                    print(site,":",pwd)


      elif choice=="3":
              print("generated password:",generate_password())

      elif choice=="4":
               print("ok bii")
               break

      else:
            print("invalid choice")
    
                                
                             

              
