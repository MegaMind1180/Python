import random
from typing import Dict, List, Set

ALL_ACHIEVEMENTS: List[str] = [
    "First Kill",
    "Master Builder",
    "Biggest Coward",
    "Tank",
    "Highest Damage Dealer",
    "Assassin",
    "Speedrunner",
    "Pacifist",
    "Treasure Hunter",
    "Survivor",
]


def gen_player_achievements(achievements: List[str]) -> Set[str]:
    rando: int = random.randint(1, len(achievements))
    randoachiev: List[str] = random.sample(achievements, rando)
    return set(randoachiev)


players: Dict[str, Set[str]] = {
    "Harald": gen_player_achievements(ALL_ACHIEVEMENTS),
    "Kevin": gen_player_achievements(ALL_ACHIEVEMENTS),
    "Chantal": gen_player_achievements(ALL_ACHIEVEMENTS),
    "Erika": gen_player_achievements(ALL_ACHIEVEMENTS),
}

for name, achievements in players.items():
    print(f"Player {name}: {achievements}")

ach_united: Set[str] = set.union(*players.values())
print(f"\nALL distinct achievements: {ach_united}")

everyone: Set[str] = set.intersection(*players.values())
print(f"Common achievements: {everyone}")

print("\nExklusive Achievements:")
for name, achs in players.items():
    other_sets: List[Set[str]] = [
        p_achs for p_name, p_achs in players.items() if p_name != name
    ]
    other_union: Set[str] = set.union(*other_sets) if other_sets else set()

    onlyone: Set[str] = achs.difference(other_union)
    print(f"- Only {name} has: {onlyone}")

master_set: Set[str] = set(ALL_ACHIEVEMENTS)

print("\nMissing achievements for 100%:")
for name, achs in players.items():
    missing: Set[str] = master_set.difference(achs)
    print(f"- {name} fehlen noch: {missing}")
