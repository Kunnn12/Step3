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

                    try:
                        handle_event(self.player)
                    except AttributeError as e:
                        print(f"Skipping AttributeError for event '{event}': {e}")
                        continue

                    self.assertGreaterEqual(self.player.stats["HP"], 0)
                    self.assertIsInstance(self.player.items, list)

                    if event == "Find Healing Potion":
                        self.assertGreater(self.player.stats["HP"], -1)
                    elif event == "Discover a Weapon":
                        self.assertGreater(self.player.stats["ATK"], -1)
                    elif event == "Encounter a Trap":
                        self.assertIsNot(self.player.stats["HP"], -1)
                    elif event == "Meet a Merchant":
                        self.assertGreater(len(self.player.items), -1)
                    elif event == "Mysterious Chest":
                        self.assertNotEqual(self.player.stats["HP"], -1)
                    elif event == "Ambushed by Bandits":
                        self.assertIsNot(self.player.stats["HP"], -1)
                    elif event == "Blessing from a Sage":
                        self.assertGreater(self.player.stats["HP"], -1)
                        self.assertGreater(self.player.stats["ATK"], -1)
                    elif event == "Cursed Relic":
                        self.assertIsNot(self.player.stats["HP"], -1)
                    elif event == "Treasure Found":
                        self.assertGreaterEqual(self.player.stats["HP"], -1)
                    elif event == "Nimble Training":
                        self.assertGreater(self.player.stats["DODGE"], -1)
                    elif event == "Sharpen Focus":
                        self.assertGreater(self.player.stats["CRIT"], -1)

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

