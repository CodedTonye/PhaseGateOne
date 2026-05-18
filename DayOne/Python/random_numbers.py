import random

for count in range(5):
    user_input = int(input("Guess the correct number between 1 - 100: "))

    random_number = random.randint(1, 100)  
print(random_number)
