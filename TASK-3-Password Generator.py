import string
import random
def random_password_generator(length=15):
    char=string.ascii_letters + string.digits 
    password = "".join(random.choice(char)for i in range(length))
    return password

def main():
    length=int(input("enter the length of password:"))

    if length > 0:
        password = random_password_generator(length)
        print(f"your password:{password}")

    else:
        print("Invalid input.Please give a valid input.")
    
if __name__ =="__main__":
    main()
    