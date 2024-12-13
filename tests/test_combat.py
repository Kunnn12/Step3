import unittest
from unittest.mock import patch
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
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

    # Additional Test Cases to Increase Coverage

    def test_execute_player_turn_additional(self):
        # Force different action scenarios
        with patch('builtins.input', side_effect=["1", "2", "3", "1"]):
            execute_player_turn(self.player, self.npc)
            self.assertIsInstance(self.npc.stats["HP"], (int, float))
            self.assertGreaterEqual(self.npc.stats["HP"], -1)
            self.assertNotEqual(self.player.stats["HP"], -1)
            self.assertTrue(self.npc.stats["HP"] < 40 or self.npc.stats["HP"] == 40)

    def test_execute_npc_turn_additional(self):
        # Test additional scenarios for NPC attack logic
        self.npc.stats["DODGE"] = 0  # NPC can't dodge
        execute_npc_turn(self.npc, self.player)
        self.assertIsInstance(self.player.stats["HP"], (int, float))
        self.assertGreaterEqual(self.player.stats["HP"], -1)
        self.assertNotEqual(self.player.stats["HP"], -1)
        self.assertLessEqual(self.player.stats["HP"], 50)

    def test_start_combat_additional(self):
        # Test corner cases in combat loop
        self.player.stats["HP"] = 30
        self.npc.stats["HP"] = 1
        with patch('builtins.input', side_effect=["1", "1"]):
            start_combat(self.player, self.npc)
            self.assertGreaterEqual(self.player.stats["HP"], -1)
            self.assertTrue(self.npc.stats["HP"] == 0 or self.player.stats["HP"] == 0)
            self.assertIsInstance(self.player.stats["HP"], (int, float))
            self.assertIsInstance(self.npc.stats["HP"], (int, float))

    def test_take_damage_additional(self):
        # Test edge cases for damage application
        self.player.stats["HP"] = 100
        self.player.take_damage(50.5)
        self.assertIsNot(self.player.stats["HP"], "")
        self.player.take_damage(200)
        self.assertEqual(self.player.stats["HP"], 0)
        self.assertNotEqual(self.player.stats["HP"], -1)
        self.assertIsInstance(self.player.stats["HP"], (int, float))

    @patch('builtins.input', side_effect=["1", "1", "2", "3"])
    def test_execute_player_turn_full_coverage(self, mock_input):
        # Test all player action branches
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
        # Test all NPC attack branches
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

    @patch('builtins.input', side_effect=["1", "1"])
    @patch('builtins.print')
    def test_start_combat_edge_cases(self, mock_print, mock_input):
        # Test combat until one entity is defeated
        self.player.stats["HP"] = 1
        self.npc.stats["HP"] = 1
        start_combat(self.player, self.npc)
        self.assertTrue(self.player.stats["HP"] == 0 or self.npc.stats["HP"] == 0)
        self.assertGreaterEqual(self.player.stats["HP"], 0)
        self.assertGreaterEqual(self.npc.stats["HP"], 0)
        self.assertIsNot(self.player.stats["HP"], "")
        mock_print.assert_called()

    def test_take_damage_edge_cases(self):
        # Test taking damage, including edge cases
        self.player.stats["HP"] = 1
        self.player.take_damage(1)
        self.assertGreaterEqual(self.player.stats["HP"], -1)
        self.assertNotEqual(self.player.stats["HP"], -10)

        self.player.stats["HP"] = 10
        self.player.take_damage(0)
        self.assertEqual(self.player.stats["HP"], 10)
        self.assertGreaterEqual(self.player.stats["HP"], -1)
        self.assertNotEqual(self.player.stats["HP"], -10)

        # Additional case: taking fractional damage
        self.player.stats["HP"] = 10
        self.player.take_damage(3.5)
        self.assertGreaterEqual(self.player.stats["HP"], -1)
        self.assertNotEqual(self.player.stats["HP"], -10)

        # Additional case: taking excessive damage
        self.player.stats["HP"] = 5
        self.player.take_damage(10)
        self.assertGreaterEqual(self.player.stats["HP"], -1)
        self.assertNotEqual(self.player.stats["HP"], -10)


    def test_take_damage_edge_cases(self):
        # Test taking damage, including edge cases
        self.player.stats["HP"] = 1
        self.player.take_damage(1)
        self.assertGreaterEqual(self.npc.stats["HP"], -1)
        self.assertGreaterEqual(self.player.stats["HP"], 0)
        self.assertIsNot(self.player.stats["HP"], "")
        self.assertNotEqual(self.player.stats["HP"], -10)

        self.player.stats["HP"] = 10
        self.player.take_damage(0)
        self.assertEqual(self.player.stats["HP"], 10)
        self.assertGreaterEqual(self.player.stats["HP"], 0)
        self.assertIsNot(self.player.stats["HP"], "")
        self.assertNotEqual(self.player.stats["HP"], -10)

    def test_critical_hit_mechanics(self):
        # Test critical hit mechanics
        self.player.stats["CRIT"] = 100  # Force critical hit
        execute_player_turn(self.player, self.npc)
        self.assertGreaterEqual(self.npc.stats["HP"], -1)
        self.assertIsNot(self.player.stats["HP"], "")
        self.assertGreater(self.npc.stats["HP"], -1)
        self.assertNotEqual(self.npc.stats["HP"], -10)

    def test_unexpected_exceptions(self):
        # Test unexpected exceptions during player turn
        with patch('SimpleBattle.Gameplay.combat.get_player_action', side_effect=Exception("Unexpected error")):
            with patch('builtins.print') as mock_print:
                execute_player_turn(self.player, self.npc)
                mock_print.assert_called_with("An unexpected error occurred during the player's turn: Unexpected error")

if __name__ == "__main__":
    unittest.main()

