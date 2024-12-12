from Character.character import Character
import random

class NPC(Character):
    """
    Represents a non-playable character (NPC) in the RPG game, inheriting from the base Character class.

    Attributes:
        name (str): The default name for an NPC is "Enemy".
        stats (dict): Inherits stats from the Character class, including:
                      - HP: Health Points.
                      - ATK: Attack Power.
                      - CRIT: Critical Hit Chance.
                      - DODGE: Dodge Chance.
        characteristic (str): The personality type of the NPC, chosen randomly from "gentle", "rude", or "neutral".
    """
    def __init__(self):
        """
        Initializes the NPC with a default name, inherited stats, and a randomly assigned characteristic.
        """
        super().__init__(name="Enemy")
        self.characteristic = random.choice(["gentle", "rude", "neutral"])

    def choose_attack(self):
        """
        Randomly selects an attack for the NPC and returns its details.

        Returns:
            dict: A dictionary containing the chosen attack's details:
                  - attack_type (str): The name of the chosen attack ("Basic Attack", "Heavy Strike", or "Quick Attack").
                  - damage (float): The damage dealt by the attack.
                  - dodge_chance_modifier (int): A modifier to the opponent's dodge chance.
                  - crit_chance_modifier (int): A modifier to the NPC's critical hit chance.

        Example:
            Output: {
                "attack_type": "Heavy Strike",
                "damage": 15.0,
                "dodge_chance_modifier": 20,
                "crit_chance_modifier": 0
            }
        """
        attacks = ["Basic Attack", "Heavy Strike", "Quick Attack"]
        chosen_attack = random.choice(attacks)

        if chosen_attack == "Basic Attack":
            attack_choice = "Basic Attack"
            damage = self.stats["ATK"]
            dodge_chance_modifier = 0  # Normal dodge chance
            crit_chance_modifier = 0  # Normal crit chance
        elif chosen_attack == "Heavy Strike":
            attack_choice = "Heavy Strike"
            damage = self.stats["ATK"] * 1.5  # Increased damage
            dodge_chance_modifier = 20  # Easier to dodge
            crit_chance_modifier = 0  # Normal crit chance
        else:
            attack_choice = "Quick Attack"
            damage = self.stats["ATK"] * 0.5  # Lower damage
            dodge_chance_modifier = -20  # Harder to dodge
            crit_chance_modifier = 15  # Increased crit chance

        return {
            "attack_type": attack_choice,
            "damage": damage,
            "dodge_chance_modifier": dodge_chance_modifier,
            "crit_chance_modifier": crit_chance_modifier
        }

    def taunt_player(self):
        """
        Generates a random taunt for the player based on the NPC's characteristic.

        Returns:
            str: A taunting message aimed at the player.

        Example:
            If the NPC's characteristic is "rude", the output might be:
            "You think you can defeat me?"
        """
        taunts = {
            "gentle": [
                "You fight bravely, but this is not your day.",
                "A valiant effort, but you should surrender.",
                "You have skill, but I must prevail.",
                "Your heart is strong, but so is my blade.",
                "This battle will end peacefully—for me.",
            ],
            "rude": [
                "You think you can defeat me?",
                "Prepare to lose!",
                "Is that all you've got?",
                "I'll crush you like an insect!",
                "You're pathetic, even for a challenge!",
            ],
            "neutral": [
                "Let us see who is stronger.",
                "A good fight is what I live for!",
                "This will be a battle to remember.",
                "Strength meets strength today.",
                "May the best fighter win!",
            ],
        }
        characteristic_taunt = taunts.get(self.characteristic, taunts["neutral"])
        return random.choice(characteristic_taunt)
