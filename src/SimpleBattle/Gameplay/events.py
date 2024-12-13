import random

def generate_event():
    """
    Randomly selects an event that can happen during the game.
    """
    events = [
        "Find Healing Potion",
        "Discover a Weapon",
        "Encounter a Trap",
        "Meet a Merchant",
        "Mysterious Chest",
        "Ambushed by Bandits",
        "Blessing from a Sage",
        "Cursed Relic",
        "Treasure Found",
        "Wandering Spirit",
        "Nimble Training",
        "Sharpen Focus"
    ]
    return random.choice(events)

def apply_item_effect(player, item):
    """
    Applies the effects of an item to the player's stats.
    """
    effect = item.get("effect", {})
    print(f"\nYou received {item['name']}!")
    for key, value in effect.items():
        player.stats[key] = max(0, player.stats.get(key, 0) + value)
        print(f"{key} {'increased' if value > 0 else 'decreased'} by {abs(value)}.")
    print(f"Updated stats: {player.stats}")

def handle_event(player):
    """
    Triggers a random event and ensures all events affect the player's stats.
    """
    event = generate_event()
    print(f"\nEvent: {event}")

    # Base random effects applied to every event
    base_effects = {
        "HP": random.randint(-10, 20),
        "ATK": random.randint(-5, 15),
        "CRIT": random.randint(-5, 10),
        "DODGE": random.randint(-5, 10)
    }

    if event == "Find Healing Potion":
        item = {"name": "Healing Potion", "effect": {"HP": 20, **base_effects}}
        apply_item_effect(player, item)

    elif event == "Discover a Weapon":
        item = {"name": "Legendary Sword", "effect": {"ATK": 15, **base_effects}}
        apply_item_effect(player, item)

    elif event == "Encounter a Trap":
        item = {"name": "Trap Damage", "effect": {"HP": -15, **base_effects}}
        apply_item_effect(player, item)

    elif event == "Meet a Merchant":
        print("You met a merchant! He offers to sell you an item:")
        merchant_items = [
            {"name": "Merchant's Weapon", "effect": {"ATK": 10, **base_effects}},
            {"name": "Focus Elixir", "effect": {"CRIT": 10, **base_effects}},
            {"name": "Evasion Boots", "effect": {"DODGE": 10, **base_effects}}
        ]
        for i, item in enumerate(merchant_items, 1):
            print(f"{i}. {item['name']} ({item['effect']})")
        choice = input("Choose an item to buy (1/2/3) or type 'no' to skip: ").strip().lower()
        if choice in ["1", "2", "3"]:
            item = merchant_items[int(choice) - 1]
            apply_item_effect(player, item)
        else:
            print("You walk away from the merchant.")

    elif event == "Mysterious Chest":
        print("You found a mysterious chest!")
        choice = input("Do you open it? (yes/no): ").strip().lower()
        if choice == "yes":
            chest_rewards = [
                {"name": "Treasure", "effect": {"HP": 30, "ATK": 10, **base_effects}},
                {"name": "Focus Elixir", "effect": {"CRIT": 10, **base_effects}},
                {"name": "Evasion Boots", "effect": {"DODGE": 10, **base_effects}},
                {"name": "Poison Gas", "effect": {"HP": -20, **base_effects}}
            ]
            item = random.choice(chest_rewards)
            apply_item_effect(player, item)
        else:
            print("You leave the chest untouched.")

    elif event == "Ambushed by Bandits":
        item = {"name": "Bandit Attack", "effect": {"HP": -25, **base_effects}}
        apply_item_effect(player, item)

    elif event == "Blessing from a Sage":
        item = {"name": "Sage's Blessing", "effect": {"HP": 20, "ATK": 10, **base_effects}}
        apply_item_effect(player, item)

    elif event == "Cursed Relic":
        item = {"name": "Cursed Relic", "effect": {"HP": -15, "ATK": -5, **base_effects}}
        apply_item_effect(player, item)

    elif event == "Treasure Found":
        item = {"name": "Gold Coins", "effect": {"HP": 10, **base_effects}}
        apply_item_effect(player, item)

    elif event == "Wandering Spirit":
        choice = input("A wandering spirit offers you power at a cost. Do you accept its gift? (yes/no): ").strip().lower()
        if choice == "yes":
            item = {"name": "Spirit's Power", "effect": {"ATK": 20, "HP": -10, **base_effects}}
            apply_item_effect(player, item)
        else:
            print("The spirit vanishes into the void.")

    elif event == "Nimble Training":
        item = {"name": "Agility Boost", "effect": {"DODGE": 15, **base_effects}}
        apply_item_effect(player, item)

    elif event == "Sharpen Focus":
        item = {"name": "Focus Training", "effect": {"CRIT": 15, **base_effects}}
        apply_item_effect(player, item)
