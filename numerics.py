import random

def text_to_numeric(text):
    numeric_text = ''
    for char in text:
        numeric_text += str(ord(char))
    return int(numeric_text)

def rand_pat():
    return ''.join([str(random.randint(0, 9)) for _ in range(10)])
