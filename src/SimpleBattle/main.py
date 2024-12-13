from Character.player import Player
from Character.npc import NPC
from Gameplay.combat import start_combat
from Gameplay.events import handle_event
from Gameplay.interface import (
    display_ascii_art, display_stats, display_last_message, get_player_action
)

def main():
    """
    The main function to start and execute the game.

    It initializes the game, allows the player to create a character, 
    triggers a random event to modify player stats, and starts a combat session 
    between the player and an NPC. After the battle concludes, it displays the 
    result and ends the game.

    Flow:
    1. Display the game title with ASCII art.
    2. Create a player character and an NPC opponent.
    3. Trigger a random event that can positively or negatively impact the player's stats.
    4. Display updated stats for the player and NPC.
    5. Start and manage a turn-based combat sequence.
    6. Display the winner and a closing message.

    Note:
    - The player's and NPC's stats are updated dynamically during the event and combat.
    - ASCII art and visual elements enhance the gaming experience.
    """
    display_ascii_art("start")
    print("Welcome to Simple Battle!")  

    player_name = input("Enter your character's name: ").strip()
    player = Player()
    player.name = player_name

    npc = NPC()
    npc.name = "Goblin"

    print("\nYour journey begins with a mysterious event...")
    handle_event(player)

    print("\nHere are your stats after the event:")
    display_stats(player)
    print("\nA wild Goblin appears to challenge you!")
    display_stats(npc)

    print("\nThe battle begins!")
    start_combat(player, npc)

    winner = player.name if player.stats["HP"] > 0 else npc.name
    result_message = f"The winner is {winner}!"
    display_ascii_art("win" if winner == player.name else "lose")
    display_last_message(result_message)

    print("\nThanks for playing Simple Battle! Goodbye!")  

if __name__ == "__main__":
    main()

    


