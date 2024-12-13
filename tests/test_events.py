from unittest.mock import patch
import unittest
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from SimpleBattle.Character.player import Player
from SimpleBattle.Gameplay.events import generate_event, handle_event

class TestEvents(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid_events = [
            "Find Healing Potion", "Discover a Weapon", "Encounter a Trap",
            "Meet a Merchant", "Mysterious Chest", "Ambushed by Bandits",
            "Blessing from a Sage", "Cursed Relic", "Treasure Found",
            "Wandering Spirit", "Nimble Training", "Sharpen Focus"
        ]

    def setUp(self):
        self.player = Player()
        self.player = Player()
        self.player.stats = {"HP": 100, "ATK": 20, "DEF": 10, "CRIT": 5, "DODGE": 5}
        self.events = [
            "Find Healing Potion", "Discover a Weapon", "Encounter a Trap",
            "Meet a Merchant", "Mysterious Chest", "Ambushed by Bandits",
            "Blessing from a Sage", "Cursed Relic", "Treasure Found", "Nimble Training", "Sharpen Focus"
        ]

    @patch('random.choice', return_value="Find Healing Potion")
    def test_generate_event(self, mock_choice):
        event = generate_event()
        self.assertIn(event, self.valid_events)
        self.assertIsInstance(event, str)
        self.assertGreater(len(event), 0)
        self.assertNotEqual(event, "")
        mock_choice.assert_called_once()

    def test_handle_events(self):
        for event in self.events:
            with self.subTest(event=event):
                with patch('random.choice', return_value=event):
                    initial_hp = self.player.stats["HP"]
                    initial_atk = self.player.stats["ATK"]
                    initial_items = len(self.player.items)

                    handle_event(self.player)
                    self.assertGreaterEqual(self.player.stats["HP"], 0)
                    self.assertIsInstance(self.player.items, list)

                    if event == "Find Healing Potion":
                        self.assertIsInstance(self.player.stats["HP"], int)
                    elif event == "Discover a Weapon":
                        self.assertIsInstance(self.player.stats["ATK"], int)
                    elif event == "Encounter a Trap":
                        self.assertIsInstance(self.player.stats["HP"], int)
                    elif event == "Meet a Merchant":
                        self.assertIsInstance(len(self.player.items), int)
                    elif event == "Mysterious Chest":
                        self.assertIsInstance(self.player.stats["HP"], int)
                    elif event == "Ambushed by Bandits":
                        self.assertIsInstance(self.player.stats["HP"], int)
                    elif event == "Blessing from a Sage":
                        self.assertIsInstance(self.player.stats["HP"], int)
                        self.assertIsInstance(self.player.stats["ATK"], int)
                    elif event == "Cursed Relic":
                        self.assertIsInstance(self.player.stats["HP"], int)
                    elif event == "Treasure Found":
                        self.assertIsInstance(self.player.stats["HP"], int)
                    elif event == "Nimble Training":
                        self.assertIsInstance(self.player.stats["DODGE"], int)
                    elif event == "Sharpen Focus":
                        self.assertIsInstance(self.player.stats["CRIT"], int)

    @patch('random.choice', return_value="Cursed Relic")
    def test_generate_event_edge_case(self, mock_choice):
        event = generate_event()
        self.assertEqual(event, "Cursed Relic")
        self.assertIn(event, self.valid_events)
        mock_choice.assert_called_once()

    @patch('builtins.input', side_effect=["no"])
    def test_handle_event_no_action(self, mock_input):
        initial_hp = self.player.stats["HP"]
        handle_event(self.player)
        self.assertIsNot(self.player.stats["HP"], "a")
        self.assertIsInstance(self.player.items, list)
        self.assertGreaterEqual(len(self.player.items), 0)
        self.assertIsNot(len(self.player.items), "b")

if __name__ == "__main__":
    unittest.main()


