import unittest
# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from SimpleBattle.Character.player import Player
from SimpleBattle.Character.npc import NPC
from SimpleBattle.Gameplay.combat import execute_player_turn, execute_npc_turn, start_combat

class TestCombat(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.npc = NPC()
        self.player.stats = {"HP": 50, "ATK": 20, "DEF": 10}
        self.npc.stats = {"HP": 40, "ATK": 15, "DEF": 8}

    @patch('builtins.input', side_effect=["1", "1"])
    def test_player_turn_execution(self, mock_input):
        initial_npc_hp = self.npc.stats["HP"]
        execute_player_turn(self.player, self.npc)
        self.assertLess(self.npc.stats["HP"], initial_npc_hp)
        self.assertGreaterEqual(self.npc.stats["HP"], 0)
        self.assertIsInstance(self.npc.stats["HP"], int)
        self.assertIsInstance(self.npc.stats["HP"], (int, float))

    def test_npc_turn_execution(self):
        initial_player_hp = self.player.stats["HP"]
        execute_npc_turn(self.npc, self.player)
        self.assertLessEqual(self.player.stats["HP"], initial_player_hp)
        self.assertGreaterEqual(self.player.stats["HP"], 0)
        self.assertIsInstance(self.player.stats["HP"], (int, float))

    def test_combat_loop(self):
        with patch('builtins.print') as mock_print:
            start_combat(self.player, self.npc)
            mock_print.assert_called()
            self.assertTrue(self.player.stats["HP"] == 0 or self.npc.stats["HP"] == 0)

    @patch('builtins.input', side_effect=["2", "2"])
    def test_player_skip_turn(self, mock_input):
        initial_player_hp = self.player.stats["HP"]
        execute_player_turn(self.player, self.npc)
        self.assertEqual(self.player.stats["HP"], initial_player_hp)

    def test_npc_zero_hp(self):
        self.npc.stats["HP"] = 0
        with patch('builtins.print') as mock_print:
            start_combat(self.player, self.npc)
            mock_print.assert_called()
        self.assertTrue(self.player.stats["HP"] > 0)
if __name__ == "__main__":
    unittest.main()


