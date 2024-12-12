import unittest
# import sys
# import os
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

    @patch('random.choice', return_value="Find Healing Potion")
    def test_generate_event(self, mock_choice):
        event = generate_event()
        self.assertIn(event, self.valid_events)
        self.assertIsInstance(event, str)
        self.assertGreater(len(event), 0)
        self.assertNotEqual(event, "")
        mock_choice.assert_called_once()

    @patch('builtins.input', side_effect=["1", "yes"])
    def test_handle_event(self, mock_input):
        initial_hp = self.player.stats["HP"]
        handle_event(self.player)
        self.assertNotEqual(self.player.stats["HP"], initial_hp)
        self.assertGreaterEqual(self.player.stats["HP"], 0)
        self.assertIsInstance(self.player.items, list)
        self.assertGreaterEqual(len(self.player.items), 0)
        mock_input.assert_called()

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
        self.assertEqual(self.player.stats["HP"], initial_hp)
        self.assertIsInstance(self.player.items, list)
        self.assertGreaterEqual(len(self.player.items), 0)
        mock_input.assert_called()

if __name__ == "__main__":
    unittest.main()
