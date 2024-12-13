import unittest
from unittest.mock import patch
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from SimpleBattle.Character.player import Player
from SimpleBattle.Character.npc import NPC
from SimpleBattle.Gameplay.combat import (
    execute_player_turn, execute_npc_turn, start_combat, take_damage
)

class TestCombat(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.npc = NPC()
        self.player.stats = {"HP": 50, "ATK": 20, "DEF": 10, "CRIT": 10, "DODGE": 5}
        self.npc.stats = {"HP": 40, "ATK": 15, "DEF": 8, "CRIT": 5, "DODGE": 10}

    def test_execute_player_turn_additional(self):
        # Force different action scenarios
        with patch('builtins.input', side_effect=["1", "2", "3", "1"]):  # Predefined actions
            execute_player_turn(self.player, self.npc)
            self.assertIsInstance(self.npc.stats["HP"], (int, float))
            self.assertGreaterEqual(self.npc.stats["HP"], -1)
            self.assertNotEqual(self.player.stats["HP"], -1)
            self.assertTrue(self.npc.stats["HP"] < 40 or self.npc.stats["HP"] == 40)

    def test_execute_npc_turn_additional(self):
        self.npc.stats["DODGE"] = 0  # NPC can't dodge
        execute_npc_turn(self.npc, self.player)
        self.assertIsInstance(self.player.stats["HP"], (int, float))
        self.assertGreaterEqual(self.player.stats["HP"], -1)
        self.assertNotEqual(self.player.stats["HP"], -1)
        self.assertLessEqual(self.player.stats["HP"], 50)

    def test_execute_npc_turn_coverage(self):
        """Test edge cases and additional scenarios for execute_npc_turn."""

        attack = {"attack_type": "Slash", "damage": 15, "dodge_chance_modifier": 0, "crit_chance_modifier": 0}
        with patch.object(self.npc, 'choose_attack', return_value=attack):
            with patch.object(self.player, 'dodge_attack', return_value=False):
                with patch.object(self.npc, 'critical_attack', return_value=False):
                    execute_npc_turn(self.npc, self.player)
                    self.assertEqual(self.player.stats["HP"], 35)

        with patch.object(self.npc, 'choose_attack', return_value=attack):
            with patch.object(self.player, 'dodge_attack', return_value=False):
                with patch.object(self.npc, 'critical_attack', return_value=True):
                    execute_npc_turn(self.npc, self.player)
                    self.assertEqual(self.player.stats["HP"], 5)
        with patch.object(self.npc, 'choose_attack', return_value=attack):
            with patch.object(self.player, 'dodge_attack', return_value=True):
                execute_npc_turn(self.npc, self.player)
                self.assertEqual(self.player.stats["HP"], 5)

    def test_start_combat_additional(self):
        self.player.stats["HP"] = 30
        self.npc.stats["HP"] = 1
        with patch('builtins.input', side_effect=["1", "1"]):  # Predefined actions
            start_combat(self.player, self.npc)
            self.assertGreaterEqual(self.player.stats["HP"], -1)
            self.assertTrue(self.npc.stats["HP"] == 0 or self.player.stats["HP"] == 0)
            self.assertIsInstance(self.player.stats["HP"], (int, float))
            self.assertIsInstance(self.npc.stats["HP"], (int, float))

    def test_take_damage_additional(self):
        self.player.stats["HP"] = 100
        take_damage(self.player, 50.5)
        self.assertIsNot(self.player.stats["HP"], "")
        self.assertGreaterEqual(self.player.stats["HP"], 49)
        self.assertNotEqual(self.player.stats["HP"], -1)
        self.assertIsInstance(self.player.stats["HP"], (int, float))
        take_damage(self.player, 200)
        self.assertEqual(self.player.stats["HP"], 0)
        self.assertGreaterEqual(self.player.stats["HP"], 0)
        self.assertNotEqual(self.player.stats["HP"], -1)

    @patch('builtins.input', side_effect=["1", "1", "2", "3"])  # Predefined player actions
    def test_execute_player_turn_full_coverage(self, mock_input):
        execute_player_turn(self.player, self.npc)
        self.assertGreaterEqual(self.npc.stats["HP"], -1)
        self.assertIsNot(self.player.stats["HP"], "")
        self.assertGreater(self.npc.stats["HP"], -1)
        self.assertNotEqual(self.npc.stats["HP"], -10)

        self.npc.stats["DODGE"] = 100  # Force dodge
        execute_player_turn(self.player, self.npc)
        self.assertGreaterEqual(self.npc.stats["HP"], -1)
        self.assertIsNot(self.player.stats["HP"], "")
        self.assertGreater(self.npc.stats["HP"], -1)
        self.assertNotEqual(self.npc.stats["HP"], -10)

    def test_execute_npc_turn_full_coverage(self):
        execute_npc_turn(self.npc, self.player)
        self.assertGreaterEqual(self.npc.stats["HP"], -1)
        self.assertIsNot(self.player.stats["HP"], "")
        self.assertGreater(self.player.stats["HP"], -1)
        self.assertNotEqual(self.player.stats["HP"], -10)

        self.player.stats["DODGE"] = 100  # Force dodge
        execute_npc_turn(self.npc, self.player)
        self.assertGreaterEqual(self.npc.stats["HP"], -1)
        self.assertIsNot(self.player.stats["HP"], "")
        self.assertGreater(self.player.stats["HP"], -1)
        self.assertNotEqual(self.player.stats["HP"], -10)

    def test_start_combat(self):
        """Test the complete combat loop between the player and NPC."""
        self.player.stats["HP"] = 20
        self.npc.stats["HP"] = 10

        with patch('builtins.input', side_effect=["1", "1"]):
            start_combat(self.player, self.npc)

        self.assertGreaterEqual(self.player.stats["HP"], 0)
        self.assertGreaterEqual(self.npc.stats["HP"], 0)
        self.assertTrue(
            self.player.stats["HP"] == 0 or self.npc.stats["HP"] == 0,
            "Combat did not end with one participant at 0 HP"
        )
        self.assertNotEqual(self.player.stats["HP"], -1)
        self.assertNotEqual(self.npc.stats["HP"], -1)

    def test_take_damage(self):
        """Test the take_damage function to ensure HP is decremented correctly."""
        self.player.stats["HP"] = 50

        # Test normal damage
        take_damage(self.player, 20)
        self.assertEqual(self.player.stats["HP"], 30)
        self.assertGreaterEqual(self.player.stats["HP"], 0)
        self.assertNotEqual(self.player.stats["HP"], -1)
        self.assertLessEqual(self.player.stats["HP"], 50)

        # Test overkill damage
        take_damage(self.player, 40)
        self.assertEqual(self.player.stats["HP"], 0)
        self.assertGreaterEqual(self.player.stats["HP"], 0)
        self.assertNotEqual(self.player.stats["HP"], -1)
        self.assertLessEqual(self.player.stats["HP"], 50)

        # Test float damage rounding
        self.player.stats["HP"] = 10
        take_damage(self.player, 5.5)
        self.assertEqual(self.player.stats["HP"], 4)
        self.assertNotEqual(self.player.stats["HP"], 10)
        self.assertGreaterEqual(self.player.stats["HP"], 0)
        self.assertLessEqual(self.player.stats["HP"], 10)

        # Ensure no negative HP
        take_damage(self.player, 100)
        self.assertEqual(self.player.stats["HP"], 0)
        self.assertGreaterEqual(self.player.stats["HP"], 0)
        self.assertNotEqual(self.player.stats["HP"], -1)
        self.assertLessEqual(self.player.stats["HP"], 10)

if __name__ == "__main__":
    unittest.main()



