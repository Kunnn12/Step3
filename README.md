# DATA533_Project
# Simple Battle

**Simple Battle** is a turn-based battle simulator where players engage in combat with NPC opponents. The game features dynamic events, random stat generation, and critical hit/dodge mechanics for an engaging experience. The project is structured into two sub-packages: **Character** and **Gameplay**, each focusing on specific game elements.

---

## Package Structure

### 1. **Character Sub-Package**
Defines the characters participating in the game, including both players and NPCs. Inheritance is used to share common behavior.

#### Modules:
- **`character.py`**
  - The base `Character` class provides shared properties and methods for all characters in the game.
  - **Functions:**
    - `__init__(name="Unnamed")`: Initializes a character with a name, random stats, and an empty inventory.
    - `generate_stats()`: Randomly assigns stats for a character:
      - **HP (Health Points):** Range 50-100.
      - **ATK (Attack Power):** Range 5-15.
      - **CRIT (Critical Hit Chance):** Range 10-30%.
      - **DODGE (Dodge Chance):** Range 10-30%.
    - `take_damage(damage)`: Reduces the character's HP by a specified damage value. Ensures HP does not fall below 0.
    - `dodge_attack(dodge_modifier)`: Determines if the character successfully dodges an incoming attack using their dodge stats and a modifier.
    - `critical_attack(crit_modifier)`: Determines if a critical hit occurs, doubling the damage dealt.

- **`player.py`**
  - The `Player` class inherits from `Character` and represents the user-controlled player.
  - **Functions:**
    - `__init__()`: Initializes the player with default stats and an empty inventory.
    - `use_item(item)`: Applies the effect of an item to the player's stats. The item's effects are defined in a dictionary:
    - `choose_attack(player_input)`: Allows the player to select an attack type:
      - **Basic Attack:** Standard damage and dodge/crit chance.
      - **Heavy Strike:** High damage but easier to dodge.
      - **Quick Attack:** Lower damage but harder to dodge and higher crit chance.

- **`npc.py`**
  - The `NPC` class inherits from `Character` and represents the non-playable opponents.
  - **Functions:**
    - `__init__()`: Initializes the NPC with a default name ("Enemy") and a random characteristic ("gentle", "rude", or "neutral").
    - `choose_attack()`: Randomly selects an attack type (Basic, Heavy, or Quick) and returns its details.
    - `taunt_player()`: Generates a random taunt based on the NPC's characteristic.

---

### 2. **Gameplay Sub-Package**
Manages game mechanics, including random events, combat, and user interface interactions.

#### Modules:
- **`events.py`**
  - Handles random events that modify the player's stats or present challenges.
  - **Functions:**
    - `generate_event()`: Randomly selects an event from a predefined list of encounters.
    - `apply_item_effect(player, item)`: Applies the effects of an item (e.g., boost `CRIT`, `DODGE`, or `HP`) to the player's stats.
    - `handle_event(player)`: Triggers a random event and processes its outcome, such as discovering items, avoiding traps, or enhancing stats.

- **`combat.py`**
  - Manages the turn-based combat system.
  - **Functions:**
    - `execute_player_turn(player, npc)`: Prompts the player to choose an action (Attack or Skip Turn) and processes the action's result.
    - `execute_npc_turn(npc, player)`: Processes the NPC's turn by randomly selecting and executing an attack.
    - `start_combat(player, npc)`: Alternates turns between the player and the NPC until one is defeated, incorporating dodge and critical hit mechanics.

- **`interface.py`**
  - Handles the display and user interactions during the game.
  - **Functions:**
    - `print_with_delay(text, delay=0.05)`: Prints text with a typing effect to enhance engagement.
    - `display_ascii_art(title)`: Displays ASCII art for significant game moments like "Victory" or "Defeat."
    - `display_stats(character)`: Displays the current stats of a character with color-coded values.
    - `display_visual_health_bar(name, hp, max_hp)`: Renders a visual health bar for a character using emojis.
    - `get_player_action()`: Prompts the player to choose an action (e.g., Attack or Skip Turn) and validates the input.
    - `display_last_message(result)`: Displays the final result of the battle.
    - `display_event_description(event)`: Describes a random event with animated text.
    - `display_combat_round(round_number, player, npc)`: Shows the details of the current combat round, including health bars and round number.
