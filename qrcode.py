import random
import qrcode

def password_generate(length):
    lower="abcdefghijklmnopqrstuvwxyz"
    upper=lower.upper()
    digit="0123456789"
    symbol="!@#$%^&*(_)-+=<>?/\{}[]|:"
    mixed=upper+lower+digit+symbol
    password="".join(random.sample(mixed,length))
    return password

def qrcode_generate(password):
    file=input("Enter File name: ")
    img=qrcode.make(password)
    img.save(file+"png")

def main():
    length=int(input("Enter Password Length"))
    password=password_generate(length)
    print(f"Your Password is : {password}")
    qrcode_generate(password)
    print("Your password has been save as OR code.")

if __name__=="__main__":
    main()          