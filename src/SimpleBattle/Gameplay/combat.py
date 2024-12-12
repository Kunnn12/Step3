from SimpleBattle.Character.player import Player
from SimpleBattle.Character.npc import NPC
from SimpleBattle.Gameplay.interface import (
    display_combat_round, display_last_message, get_player_action
)

class InvalidActionError(Exception):
    """Custom exception for invalid player actions."""
    pass

def execute_player_turn(player, npc):
    """
    Executes the player's turn in combat.

    The player selects an action: attack or skip the turn. 
    If the player chooses to attack, they select the type of attack, which is then processed. 
    Damage and dodge mechanics are applied accordingly.

    Args:
        player (Player): The player character instance.
        npc (NPC): The enemy character instance.
    """
    try:
        action = get_player_action()
        if action not in ["1", "2"]:
            raise InvalidActionError("Invalid action! Please choose 1 (Attack) or 2 (Skip).")


        if action == "1":  # Attack
            try:
                attack_choice = input("Choose your attack: 1. Basic Attack  2. Heavy Strike  3. Quick Attack\n")
                if attack_choice not in ["1", "2", "3"]:
                    raise ValueError("Invalid attack choice! Choose 1, 2, or 3.")
                player_attack = player.choose_attack(attack_choice)
            except ValueError as e:
                print(e)
                return
            print(f"{player.name} chooses {player_attack['attack_type']}!")
            if npc.dodge_attack(player_attack["dodge_chance_modifier"]):
                print(f"{npc.name} dodges the attack!")
            else:
                damage = player_attack["damage"]
                if player.critical_attack(player_attack["crit_chance_modifier"]):
                    damage *= 2
                    print("Critical Hit!")
                npc.take_damage(damage)
                print(f"{npc.name} takes {damage} damage. Remaining HP: {npc.stats['HP']}")

        elif action == "2":  # Skip Turn
            print(f"{player.name} skips the turn.")

    except InvalidActionError as e:
        print(f"Invalid action error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during the player's turn: {e}")
        
def execute_npc_turn(npc, player):
    """
    Executes the NPC's turn in combat.

    The NPC randomly selects an attack, which is then processed. 
    Damage and dodge mechanics are applied accordingly.

    Args:
        npc (NPC): The enemy character instance.
        player (Player): The player character instance.
    """
    try:
        npc_attack = npc.choose_attack()
        if not npc_attack:  # Check if choose_attack returned None or invalid attack
            raise ValueError("NPC attack selection failed. No attack chosen.")
    
        print(f"{npc.name} chooses {npc_attack['attack_type']}!")
        if player.dodge_attack(npc_attack["dodge_chance_modifier"]):
            print(f"{player.name} dodges the attack!")
        else:
            damage = npc_attack["damage"]
            if npc.critical_attack(npc_attack["crit_chance_modifier"]):
                damage *= 2
                print("Critical Hit!")
            player.take_damage(damage)
            print(f"{player.name} takes {damage} damage. Remaining HP: {player.stats['HP']}")
    except ValueError as e:
        print(f"Error during NPC's turn: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during NPC's turn: {e}")

def start_combat(player, npc):
    """
    Manages the combat loop between the player and the NPC.

    Alternates turns between the player and the NPC until one of them is defeated. 
    The combat process includes attack selection, damage calculations, and taunts from the NPC.

    Args:
        player (Player): The player character instance.
        npc (NPC): The enemy character instance.

    Prints:
        The sequence of combat events and the final winner of the battle.
    """
    try:
        if not player or not npc:
            raise ValueError("Player or NPC instance is invalid.")
        
        round_number = 1

        while player.stats["HP"] > 0 and npc.stats["HP"] > 0:
            print(f"\n--- Combat Round {round_number} ---")
            display_combat_round(round_number, player, npc)

            # Player's Turn
            execute_player_turn(player, npc)
            if npc.stats["HP"] <= 0:
                print(f"{npc.name} has been defeated!")
                break

            # NPC's Turn
            execute_npc_turn(npc, player)
            if player.stats["HP"] <= 0:
                print(f"{player.name} has been defeated!")
                break
            
            print(f"{npc.name} is taunting you: \"{npc.taunt_player()}\"")
            round_number += 1

        # Determine and Display Result
        winner = player.name if player.stats["HP"] > 0 else npc.name
        display_last_message(f"The winner is {winner}!")
        
    except ValueError as e:
        print(f"Error during combat: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during combat: {e}")

def take_damage(self, damage):
    """
    Reduces the character's HP by the specified damage amount.

    Ensures that the HP does not drop below 0 and that it remains an integer.

    Args:
        damage (int or float): The amount of damage to apply.

    Modifies:
        self.stats["HP"]: Decrements the character's HP by the damage value.
    """
    try:
        if not isinstance(damage, (int, float)) or damage < 0:
            raise ValueError("Damage must be a positive number.")
        self.stats["HP"] -= damage
        self.stats["HP"] = max(0, round(self.stats["HP"]))  # Round to the nearest integer and ensure non-negative
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while applying damage: {e}")


