from random import choice

options = ['Go for a walk', 'Play a video game', 'Do something productive', 'Netflix & Chill', 'Go shopping']

#How are you feeling?
print("What mood are you in?")

mood = input()

outcome = choice(options)

print("Since you are: " + mood + ", lets go for " + outcome)

