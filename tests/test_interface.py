from unittest.mock import patch
import unittest
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from SimpleBattle.Gameplay.interface import display_stats
from SimpleBattle.Gameplay.interface import display_visual_health_bar
from SimpleBattle.Character.player import Player

class TestInterface(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.player.name = "Hero"
        self.player.stats = {"HP": 50, "ATK": 20, "DEF": 10}

    def test_display_stats(self):
        with patch('builtins.print') as mock_print:
            display_stats(self.player)
            mock_print.assert_called()
            self.assertIn("HP", self.player.stats)
            self.assertGreaterEqual(self.player.stats["HP"], 0)
            self.assertGreaterEqual(self.player.stats["ATK"], 0)
            self.assertGreaterEqual(self.player.stats["DEF"], 0)

    def test_visual_health_bar(self):
        with patch('builtins.print') as mock_print:
            display_visual_health_bar(self.player.name, self.player.stats["HP"], 100)
            mock_print.assert_called()
            self.assertGreaterEqual(self.player.stats["HP"], 0)
            self.assertLessEqual(self.player.stats["HP"], 100)
            self.assertIsInstance(self.player.stats["HP"], int)

    def test_visual_health_bar_boundary(self):
        with patch('builtins.print') as mock_print:
            display_visual_health_bar(self.player.name, 0, 100)
            display_visual_health_bar(self.player.name, 100, 100)
            mock_print.assert_called()
            self.assertGreaterEqual(0, 0)
            self.assertLessEqual(100, 100)

if __name__ == "__main__":
    unittest.main()


