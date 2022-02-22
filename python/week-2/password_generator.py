import random
import string

def create_random():
        """generate random password strings"""
        letters_count = 6
        digits_count = 3
        special_character_count = 1
        __letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
        __letters2 = __letters
        __digits = str(''.join((random.choice(string.digits) for i in range(digits_count))))
        __characters = ''.join((random.choice(string.punctuation) for i in range(special_character_count)))

        x = [__letters[2:],__digits[1],__characters, __digits[0], __letters2[:2]]
        split_list = []

        for element in range(0, len(x)):
            split_list = x[element].split()
            for item in split_list:
                for element in range(0, len(item)):
                        print(item[element], end="")