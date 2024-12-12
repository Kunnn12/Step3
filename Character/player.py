from Character.character import Character

class Player(Character):
    """
    Represents a player character in the RPG game, inheriting from the base Character class.

    Attributes:
        name (str): The default name for a player is "Player".
        stats (dict): Inherits stats from the Character class, including:
                      - HP: Health Points.
                      - ATK: Attack Power.
                      - CRIT: Critical Hit Chance.
                      - DODGE: Dodge Chance.
        items (list): A list of items the player has collected.
    """

    def __init__(self):
        """
        Initializes the player with a default name and inherited stats and items.
        """
        super().__init__(name="Player")

    def use_item(self, item):
        """
        Uses an item to modify the player's stats.

        Args:
            item (dict): A dictionary representing the item. Should include an "effect" key, 
                         where the value is another dictionary mapping stat names to their effect values.

        Example:
            item = {
                "name": "Health Potion",
                "effect": {"HP": 20}
            }
            The above item increases HP by 20, up to a maximum of 100.
        """
        effect = item.get("effect", {})
        for key, value in effect.items():
            self.stats[key] = min(self.stats.get(key, 0) + value, 100)

    def choose_attack(self, player_input):
        """
        Chooses an attack based on player input and returns attack details.

        Args:
            player_input (str): The player's input. Can be a number ("1", "2", "3") 
                                or the attack name ("Basic Attack", "Heavy Strike", "Quick Attack").

        Returns:
            dict: A dictionary containing attack details:
                  - attack_type (str): The name of the chosen attack.
                  - damage (float): The damage dealt by the attack.
                  - dodge_chance_modifier (int): A modifier to the opponent's dodge chance.
                  - crit_chance_modifier (int): A modifier to the player's critical hit chance.

        Example:
            Input: "1" or "basic attack"
            Output: {
                "attack_type": "Basic Attack",
                "damage": 10,
                "dodge_chance_modifier": 0,
                "crit_chance_modifier": 0
            }
        """
        attack_choice = ""
        damage = 0
        dodge_chance_modifier = 0
        crit_chance_modifier = 0  # Modifier for the crit chance

        player_input = player_input.strip().lower()

        if player_input in ["1", "basic attack"]:
            attack_choice = "Basic Attack"
            damage = self.stats["ATK"]
            dodge_chance_modifier = 0
            crit_chance_modifier = 0
        elif player_input in ["2", "heavy strike"]:
            attack_choice = "Heavy Strike"
            damage = self.stats["ATK"] * 1.5
            dodge_chance_modifier = 20  # Easier to dodge
            crit_chance_modifier = 0
        elif player_input in ["3", "quick attack"]:
            attack_choice = "Quick Attack"
            damage = self.stats["ATK"] * 0.7
            dodge_chance_modifier = -20  # Harder to dodge
            crit_chance_modifier = 15
        else:
            print("Invalid input, defaulting to Basic Attack.")
            attack_choice = "Basic Attack"
            damage = self.stats["ATK"]
            dodge_chance_modifier = 0
            crit_chance_modifier = 0

        return {
            "attack_type": attack_choice,
            "damage": damage,
            "dodge_chance_modifier": dodge_chance_modifier,
            "crit_chance_modifier": crit_chance_modifier
        }
