import random

def random_generator():
    letter_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    number_list = ["1","2","3","4","5","6","7","8","9","0"]
    random_string = ''.join([random.choice(letter_list + number_list) for _ in range(10)])
    return random_string
    
random_generator()

filename = f'mind\DREAM{random_generator()}.wav'