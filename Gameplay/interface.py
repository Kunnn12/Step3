import pyfiglet
from colorama import Fore, Style
import sys
import time

# Typing Effect for Text
def print_with_delay(text, delay=0.05):
    """
    Prints text with a typing effect.
    
    Each character is printed with a short delay to simulate typing, 
    creating a dynamic and engaging effect.

    Args:
        text (str): The text to be printed.
        delay (float): Time in seconds between printing each character.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ASCII Art Display
def display_ascii_art(title):
    """
    Displays ASCII art for important game events using pyfiglet.

    Args:
        title (str): A key indicating the type of event (e.g., "start", "win", "lose").
    """
    art_map = {
        "start": pyfiglet.figlet_format("Simple Battle"),
        "win": pyfiglet.figlet_format("Victory!"),
        "lose": pyfiglet.figlet_format("Defeat...")
    }
    print(Fore.CYAN + art_map.get(title, "") + Style.RESET_ALL)

# Enhanced Stats Display
def display_stats(character):
    """
    Displays the current stats of a character with formatting and colors.

    Stat values are color-coded for easy readability: 
    green for high, yellow for moderate, and red for low.

    Args:
        character (Character): The character whose stats are to be displayed.
    """
    print(Fore.YELLOW + "=" * 40)
    print(f"{character.name}'s Stats:")
    for key, value in character.stats.items():
        color = Fore.GREEN if value > 50 else Fore.RED if value < 20 else Fore.YELLOW
        print(f"{color}{key}: {value}{Style.RESET_ALL}")
    print("=" * 40 + Style.RESET_ALL)

# Health Bar with Emojis
def display_visual_health_bar(name, hp, max_hp):
    """
    Displays a visual health bar for a character using emojis.

    The health bar is dynamically updated based on the character's 
    current and maximum HP. Colors represent different health levels.

    Args:
        name (str): The name of the character.
        hp (int): The current health points of the character.
        max_hp (int): The maximum health points of the character.
    """
    bar_length = 20
    filled_length = int(bar_length * hp / max_hp)
    bar = "🟩" * filled_length + "⬛" * (bar_length - filled_length)
    color = Fore.RED if hp / max_hp <= 0.3 else Fore.YELLOW if hp / max_hp <= 0.6 else Fore.GREEN
    print(f"{name}: {color}{bar} {hp:.1f}/{max_hp} HP{Style.RESET_ALL}")

# Interactive Menus
def get_player_action():
    """
    Displays an interactive menu for the player's action and captures the input.

    The player can choose from a predefined set of actions, and the function 
    ensures valid input before proceeding.

    Returns:
        str: The number corresponding to the player's chosen action.
    """
    actions = {
        "1": "Attack",
        "2": "Skip Turn",
    }
    print("\nChoose your action:")
    for key, action in actions.items():
        print(f"{key}. {action}")
    print(Style.RESET_ALL)

    while True:
        action = input(Fore.LIGHTBLUE_EX + "Enter the number of your action: " + Style.RESET_ALL)
        if action in actions:
            return action
        print(Fore.RED + "Invalid choice, try again." + Style.RESET_ALL)


# Result Display
def display_last_message(result):
    """
    Displays the final result of the combat with animation.

    Args:
        result (str): The message to display as the final result.
    """
    print(Fore.RED + "=" * 40)
    print_with_delay(f"Final Result: {result}")
    print("=" * 40 + Style.RESET_ALL)

# Event Description
def display_event_description(event):
    """
    Describes a random event with animated text.

    Args:
        event (str): The name or description of the event to display.
    """
    print(Fore.MAGENTA + "=" * 40)
    print_with_delay(f"Event: {event}")
    print("=" * 40 + Style.RESET_ALL)

# Combat Round Display
def display_combat_round(round_number, player, npc):
    """
    Displays the details of the current combat round with dynamic visuals.

    The health of both the player and the NPC is displayed as a visual bar,
    alongside the current round number.

    Args:
        round_number (int): The current combat round number.
        player (Character): The player character involved in combat.
        npc (Character): The NPC character involved in combat.
    """
    print(Fore.GREEN + "-" * 40)
    print_with_delay(f"Round {round_number}", delay=0.02)
    display_visual_health_bar(player.name, player.stats["HP"], 100)
    display_visual_health_bar(npc.name, npc.stats["HP"], 100)
    print("-" * 40 + Style.RESET_ALL)