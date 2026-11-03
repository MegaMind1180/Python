import random
import typing

ALL_ACTIONS = (
    "move_forward", "move_backward", "strafe_left", "strafe_right", "jump",
    "double_jump", "crouch", "prone", "sprint", "walk",
    "climb", "vault", "slide", "swim", "dive",
    "dodge", "roll", "grapple", "wall_run", "ledge_grab",

    "attack_light", "attack_heavy", "shoot", "reload", "aim_down_sights",
    "throw_grenade", "melee", "block", "parry", "counter",
    "cast_spell", "use_ability_1", "use_ability_2", "use_ultimate", "switch_weapon",
    "drop_weapon", "inspect_weapon", "reload_special", "charge_attack", "stealth_kill",

    "interact", "open_door", "lock_pick", "hack_terminal", "loot_chest",
    "gather_resource", "mine", "chop_wood", "fish", "craft",
    "salvage", "repair", "plant_bomb", "defuse_bomb", "mount_vehicle",
    "dismount_vehicle", "drive", "honk", "switch_seat", "use_item",

    "open_inventory", "close_inventory", "equip_item", "unequip_item", "consume_potion",
    "use_heal", "craft_item", "discard_item", "sort_inventory", "inspect_item",

    "emote_wave", "emote_dance", "taunt", "chat_global", "chat_team",
    "whisper", "ping_location", "mark_enemy", "surrender", "vote_kick",

    "pause_game", "resume_game", "open_map", "close_map", "open_quest_log",
    "save_game", "load_game", "change_settings", "quit_to_menu", "take_screenshot",

    "rest", "sleep", "wait", "sit", "stand",
    "read_book", "listen_audio_log", "feed_pet", "pet_animal", "trade"
)

PLAYER_NAMES = (
    "ShadowKnight", "PixelWarrior", "CyberNinja", "DragonSlayer", "NeonViper",
    "PhantomRider", "FrostByte", "IronClad", "StormBreaker", "MysticRogue",
    "StarLord", "BlazeRanger", "VortexHunter", "GhostRecon", "AlphaWolf",
    "TitanShield", "ThunderStrike", "SolarFlare", "QuantumAce", "OmegaPilot"
)

def gen_event() -> typing.Generator[tuple, None, None]:
    while True:
        pair = (random.choice(PLAYER_NAMES), random.choice(ALL_ACTIONS))
        yield pair

def consume_event(my_list: list) -> typing.Generator[tuple, None, None]:
    while my_list:
        element = random.choice(my_list)
        my_list.remove(element)
        yield element
        
def printer() -> None:
    generator = gen_event()
    
    for n in range(1000):
        name, action = next(generator)
        print(f"Event {n}: Player {name} did action {action}")
        
    my_list = []
    for _ in range(10):
        my_list.append(next(generator))
        
    for element in consume_event(my_list):
        print(f"Got event from list: {element}")
        print(f"Remains in list: {my_list}")

if __name__ == "__main__":
    printer()
