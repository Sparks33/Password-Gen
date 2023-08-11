import string
import random

def generate_password(length, use_symbols):
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation if use_symbols else ""
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    return "".join(s[0:length])

def main():
    while True:
        passlen = int(input("Enter your password length: "))
        
        use_symbols = input("Do you want an extremely hard-to-crack password? (yes/no): ").lower()
        if use_symbols == "yes":
            use_symbols = True
        else:
            use_symbols = False
        
        password = generate_password(passlen, use_symbols)
        print("Generated Password:", password)
        
        while True:
            another = input("Do you want to generate another password? (yes/no): ").lower()
            if another == "yes":
                break
            elif another == "no":
                return
            else:
                print("Please write either 'yes' or 'no'. Otherwise, I will close the code.")

if __name__ == "__main__":
    main()
