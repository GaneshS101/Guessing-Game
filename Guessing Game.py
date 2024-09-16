import random
user_input = None
x = 0
y = 100
computer_num = random.randint(x,y)
while user_input != computer_num:
    try:
        user_input = int(input(f"Guess a number between {x} and {y}:"))
        if user_input > computer_num:
            print('Too Big')
        else:
            print('Too Small')
    except Exception:
        print('ERROR: Please provide a number not any charecters')
        user_input = None
print(f'YOU DID IT! {computer_num} was the correct answer')