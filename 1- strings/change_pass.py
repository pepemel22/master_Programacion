
password = "PollastreAlast@2022"
letter_init ="aeios"
letter_mod = "43105"

change_pass = str.maketrans(letter_init,letter_mod)
print(password.translate(change_pass))
