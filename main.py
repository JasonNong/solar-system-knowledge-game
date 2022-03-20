'''from random import randint

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
index = randint(0, 7)
planet = planets[index]
right = 0

print ("Part 1 lee kum sun")
print ("What is the position of", planet," relative to the Sun?")
answer = int(input()) - 1
if index == answer:
  print ("Yes that's correct")
  right = right +1
else:
  print ("WRONG ANSWER")

index = index +1
print (planet, "is planet number", index, "from the sun")

position = randint(0, 7)
planet = planets[position]
position = position +1
print ("Part 2 pee poo")
print ("What is the name of planet number", position, "from the Sun?")
user = input()
if planet == user:
  print ("KOLREKT YES")
  right = right +1
else:
  print("NOT KOLREKT NO")
print (planet, "Is the right answer")

print ("Part 3 knees deep")
index = randint(0, 6)
planet = planets[index]

print ("The name of the planet that comes after", planet,  "is...")
index = index +1
planet = planets[index]
answer = input()
indexminus = index -1
planetminus = planets[indexminus]
if answer == planet:
  print ("very samrt my good fellow yes")
  right = right +1
else:
  print ("Not good enough my subpar fellow")
print (planetminus, "comes after", planet)

print ("you got", right, "out of 3 answers right")
if right == 3:
  print ("🏆🏆🏆") '''

# wow... that is inefficient



import new