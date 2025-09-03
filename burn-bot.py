import time

print("WELCOME TO BURN BOT! PREPARE TO BE BURNED!!!")

name = input("What's your name? ")
age = int(input("How old are you? "))
activity = input("What's something you like to do? ")
wake_up_time = input("What time did you wake up this morning? ")
breakfast = input("What did you have for breakfast? ")

name_insults = [
    "Arrogant",
    "Bitter",
    "Cruel",
    "Deceitful",
    "Envious",
    "Foolish",
    "Greedy",
    "Hostile",
    "Ignorant",
    "Jealous",
    "Killer-like",
    "Lazy",
    "Malicious",
    "Negligent",
    "Obnoxious",
    "Petty",
    "Quarrelsome",
    "Ruthless",
    "Selfish",
    "Toxic",
    "Untrustworthy",
    "Vulgar",
    "Worthless",
    "Xenophobic",
    "Yawning",
    "Zealous"
]

name_insult = name_insults[ord(name[0]) - ord("A")]

if age < 20:
    age_insult = "You still need Google to spell your own name"
elif age < 30:
    age_insult = 'You think "adulting" is paying rent once'
elif age < 40:
    age_insult = "You have a back that groans louder than you do"
elif age < 50:
    age_insult = "You get excited about a new brand of dishwasher tablets"
else:
    age_insult = "You own more pain relief creams than hobbies"

print("CALCULATING BURN...")
end_time = time.time() + 5
number = 0
while time.time() < end_time:
    number += 1

print(f"Hello, {name_insult} {name}\n" +
      f"{age} years old?? {age_insult}\n" +
      f"You like to {activity}, huh?" +
      " I tried that once, and I almost quit on the spot\n" +
      f"You woke up at {wake_up_time} this morning" +
      " and think that you're better than everyone\n" +
      f"You ate {breakfast} for breakfast? That's so basic." +
      " My breakfast is so much cooler\n" +
      "You're so slow, during the time you were waiting," +
      f" I couinted to {number}")
