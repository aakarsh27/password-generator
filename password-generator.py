import random
import string

def generate_password(length=12):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    specialchar = string.punctuation

    allchar= lowercase+uppercase+digits+specialchar

    password= ''.join(random.choice(allchar) for _ in range(length))

    return password

if  __name__ == "__main__":
    password_length = 12

    try:
        password_length = int(input("enter the length off the password (default is 12): "))
    except ValueError:
        print("invalid input. using default password length")

    password = generate_password(password_length)
    print("generatede password: ", password)

    