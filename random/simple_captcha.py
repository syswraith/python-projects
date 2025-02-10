import string
import random

def captcha():
    no_chars = 6
    no_attempts = 3

    while no_attempts != 0 or enter_captcha_pass == captcha_pass:
        captcha_pass = str(''.join(random.choices(string.ascii_letters + string.digits, k=no_chars)))
        print(captcha_pass)
        enter_captcha_pass = input("Enter captcha string: ")

        if enter_captcha_pass == captcha_pass:
            print("You got in")
            break

        else:
            print(f"{no_attempts - 1} attempts left.")
            no_attempts -= 1
            no_chars += 1

            if no_attempts == 0:
                print("Not today, thank you")

            else: pass

captcha()
