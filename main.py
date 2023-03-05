from art import logo, vs
from game_data import data
import random

questions = data
print(logo)
winning = True
A = random.choice(questions)
questions.remove(A)
score = 0

while winning:
    B = random.choice(questions)
    questions.remove(B)
    x = A['follower_count']
    y = B['follower_count']
    if x > y:
        answer_letter = 'A'
        answer = A
    else:
        answer_letter = 'B'
        answer = B
    print(f"Compare A : {A['name']}, a {A['description']}, from {A['country']} ")
    print(vs)
    print(f"Compare B : {B['name']}, a {B['description']}, from {B['country']} ")
    choice = input("Who has more followers ? Type 'A' or 'B' : ")
    if choice.upper() == answer_letter:
        score += 1
        print(f"You are correct !! Your Score = {score}")
        A = answer
    else:
        print(f"You lose. Your score is : {score}")
        print(
            f"{A['name']} has {A['follower_count']} million followers and {B['name']} has {B['follower_count']} million followers")
        winning = False
