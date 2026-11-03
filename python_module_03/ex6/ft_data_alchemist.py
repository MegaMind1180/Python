import random

players = [
    "shadowKnight", "PixelWarrior", "cyberninja", "DragonSlayer", 
    "neonViper", "PhantomRider", "frostByte", "IronClad"
]

all_capitalized = [name.capitalize() for name in players]
already_capitalized = [name for name in players if name[0].isupper()]
player_scores = {name: random.randint(50, 100) for name in all_capitalized}
average_score = sum(player_scores.values()) / len(player_scores)
above_average_scores = {name: score for name, score in player_scores.items() if score > average_score}

print("All Capitalized:", all_capitalized)
print("Already Capitalized:", already_capitalized)
print("Player Scores:", player_scores)
print("Average Score:", average_score)
print("Above Average Scores:", above_average_scores)
