import random 
subjects=[
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitaraman",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Ministed Modi",
    "Auto Rickshaw Driver from Delhi"
]

actions=[
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"

]

places_or_things=[
    "at Red Fort",
    "in Mumbai Local Train",
    "a plote of samosa",
    "inside parlament",
    "at Ganga Ghat",
    "during IPL Match",
    "at indea Gate"
]

while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place_or_thing=random.choice(places_or_things)
    headline=f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n"+headline)

    user_input=input("\nDo you want another headline ? (yes/no)").strip().lower()
    if user_input=="no":
        break
print("\nThanks for using the fake News Headline Generator. Have a fun day")    