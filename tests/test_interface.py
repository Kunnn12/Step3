import unittest
# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from SimpleBattle.Gameplay.interface import display_stats
from SimpleBattle.Gameplay.interface import display_visual_health_bar
from SimpleBattle.Character.player import Player

class TestInterface(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.player = Player()
        self.player.name = "Hero"
        self.player.stats = {"HP": 50, "ATK": 20, "DEF": 10}

    def tearDown(self):
        del self.player

    def test_display_stats(self):
        try:
            display_stats(self.player)
        except Exception as e:
            self.fail(f"display_stats raised an exception: {e}")
        self.assertIn("HP", self.player.stats)
        self.assertGreaterEqual(self.player.stats["HP"], 0)
        self.assertGreaterEqual(self.player.stats["ATK"], 0)
        self.assertGreaterEqual(self.player.stats["DEF"], 0)

    def test_visual_health_bar(self):
        try:
            display_visual_health_bar(self.player.name, 50, 100)
        except Exception as e:
            self.fail(f"display_visual_health_bar raised an exception: {e}")
        self.assertEqual(self.player.stats["HP"], 50)
        self.assertIn("HP", self.player.stats)
        self.assertGreaterEqual(self.player.stats["HP"], 0)
        self.assertLessEqual(self.player.stats["HP"], 100)

if __name__ == "__main__":
    unittest.main()


