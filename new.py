from random import randint

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

correct = 0
ran_var = randint(0, 7) # random variable
planet = planets[ran_var] # random planet 

answer = int(input(f'Part 1 \nWhat is the position of {planet} relative to the Sun?\n'))

if ran_var+1 == answer: # counts from 0 so add 1
    print ("Yes that's correct\n")
    correct += 1
else:
    print ("Oh my goodness\n")

ran_var = randint(0, 7)
planet = planets[ran_var]

answer = input(f'Part 2 \nWhat is the name of planet number {ran_var+1} from the Sun?\n')

if answer.lower() == planet.lower():
    print ("Yes that's correct\n")
    correct += 1
else:
    print ("Oh my goodness\n")

ran_var = randint(0, 6)
planet = planets[ran_var]

answer = input(f"The name of the planet that comes after {planet} is...\n")

if answer.lower() == planets[ran_var+1].lower():
    print ("Yes that's correct\n")
    correct += 1
else:
    print ("Oh my goodness\n")

if correct == 3:
    print ("Here's a trophy: \n🏆🏆🏆")
else:
    print(f'You got {correct} of them correct')
# python new.py