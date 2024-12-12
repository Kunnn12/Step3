import random

class Character:
    """
    Represents a character in the RPG game, with attributes like name, stats, and items.

    Attributes:
        name (str): The name of the character.
        stats (dict): A dictionary containing the character's statistics, including:
                      - HP: Health Points (50-100).
                      - ATK: Attack Power (5-15).
                      - CRIT: Critical Hit Chance (10%-30%).
                      - DODGE: Dodge Chance (10%-30%).
        items (list): A list of items the character possesses.
    """

    def __init__(self, name="Unnamed"):
        """
        Initializes a character with a name, generated stats, and an empty inventory.

        Args:
            name (str): The name of the character. Defaults to "Unnamed".
        """
        self.name = name
        self.stats = self.generate_stats()
        self.items = []

    def generate_stats(self):
        """
        Generates random statistics for the character.

        Returns:
            dict: A dictionary with the following stats:
                  - HP: Random integer between 50 and 100.
                  - ATK: Random integer between 5 and 15.
                  - CRIT: Random integer between 10 and 30.
                  - DODGE: Random integer between 10 and 30.
        """
        return {
            "HP": int(50 + 50 * random.random()),
            "ATK": int(5 + 10 * random.random()),
            "CRIT": int(10 + 20 * random.random()),  # Critical hit chance
            "DODGE": int(10 + 20 * random.random())  # Dodge chance
        }

    def take_damage(self, damage):
        """
        Reduces the character's HP by a specified amount, ensuring HP does not drop below 0.

        Args:
            damage (int): The amount of damage to subtract from the character's HP.
        """
        self.stats["HP"] = max(0, self.stats["HP"] - damage)

    def dodge_attack(self, dodge_chance_modifier):
        """
        Determines if the character successfully dodges an incoming attack.

        Args:
            dodge_chance_modifier (int): A modifier to the dodge chance.

        Returns:
            bool: True if the character dodges the attack, False otherwise.
        """
        dodge_chance = int(100 * random.random())
        dodge_value = self.stats.get("DODGE", 0)  
        return dodge_chance <= dodge_value + dodge_chance_modifier

    def critical_attack(self, crit_chance_modifier):
        """
        Determines if the character lands a critical hit.

        Args:
            crit_chance_modifier (int): A modifier to the critical hit chance.

        Returns:
            bool: True if the character lands a critical hit, False otherwise.
        """
        critical_chance = int(100 * random.random())
        crit_value = self.stats.get("CRIT", 0) 
        return critical_chance <= crit_value + crit_chance_modifier

