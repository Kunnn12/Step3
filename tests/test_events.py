import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Character.player import Player
from Gameplay.events import generate_event, handle_event

class TestEvents(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid_events = [
            "Find Healing Potion", "Discover a Weapon", "Encounter a Trap",
            "Meet a Merchant", "Mysterious Chest", "Ambushed by Bandits",
            "Blessing from a Sage", "Cursed Relic", "Treasure Found",
            "Wandering Spirit", "Nimble Training", "Sharpen Focus"
        ]

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.player = Player()
        self.initial_hp = self.player.stats["HP"]
        self.initial_items = len(self.player.items)

    def tearDown(self):
        del self.player

    def test_generate_event(self):
        event = generate_event()
        self.assertIn(event, self.valid_events)
        self.assertIsInstance(event, str)
        self.assertGreater(len(event), 0)
        self.assertNotEqual(event, "")

    def test_handle_event(self):
        handle_event(self.player)
        final_hp = self.player.stats["HP"]
        final_items = len(self.player.items)
        self.assertTrue(final_hp != self.initial_hp or final_items != self.initial_items)
        self.assertGreaterEqual(final_hp, 0)
        self.assertIsInstance(self.player.items, list)
        self.assertGreaterEqual(len(self.player.items), 0)

if __name__ == "__main__":
    unittest.main()



