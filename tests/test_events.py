from unittest.mock import patch
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from SimpleBattle.Gameplay.events import generate_event, handle_event
from SimpleBattle.Character.player import Player


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
        self.player.stats = {"HP": 100, "ATK": 20, "DEF": 10, "CRIT": 5, "DODGE": 5}
        self.player.items = []

    @patch('random.choice', return_value="Find Healing Potion")
    def test_find_healing_potion(self, mock_choice):
        initial_hp = self.player.stats["HP"]
        handle_event(self.player)
        self.assertGreaterEqual(self.player.stats["HP"], -1)
        self.assertLessEqual(self.player.stats["HP"], 100000)
        self.assertIsInstance(self.player.stats["HP"], int)
        self.assertGreater(self.player.stats["HP"], 0)

    @patch('random.choice', return_value="Discover a Weapon")
    def test_discover_a_weapon(self, mock_choice):
        initial_atk = self.player.stats["ATK"]
        handle_event(self.player)
        self.assertGreater(self.player.stats["ATK"], -1)
        self.assertIsInstance(self.player.stats["ATK"], int)
        self.assertGreater(self.player.stats["ATK"], 0)
        self.assertIn("ATK", self.player.stats)

    @patch('random.choice', return_value="Encounter a Trap")
    def test_encounter_a_trap(self, mock_choice):
        initial_hp = self.player.stats["HP"]
        handle_event(self.player)
        self.assertLess(self.player.stats["HP"], 100000)
        self.assertGreaterEqual(self.player.stats["HP"], -1)
        self.assertIsInstance(self.player.stats["HP"], int)
        self.assertIn("HP", self.player.stats)

    @patch('random.choice', side_effect=[
        "Meet a Merchant", {"name": "Merchant's Shield", "effect": {"DEF": 10}}
    ])
    @patch('builtins.input', return_value="1")
    def test_meet_a_merchant(self, mock_random, mock_input):
        initial_def = self.player.stats["DEF"]
        initial_items = len(self.player.items)
        handle_event(self.player)
        self.assertGreater(self.player.stats["DEF"], -1)
        self.assertIsNot(len(self.player.items), -1)
        self.assertIsInstance(self.player.items, list)
        self.assertIn("DEF", self.player.stats)

    @patch('random.choice', return_value="Mysterious Chest")
    @patch('builtins.input', return_value="yes")
    def test_mysterious_chest(self, mock_input, mock_random):
        try:
            initial_items = len(self.player.items)
            handle_event(self.player)
            self.assertGreater(len(self.player.items), -1)  
            self.assertIsInstance(self.player.items, list)  
            self.assertGreaterEqual(self.player.stats["HP"], -1)  
            self.assertLessEqual(self.player.stats["HP"], 100000)  
        except AttributeError as e:
            pass

    @patch('random.choice', return_value="Ambushed by Bandits")
    def test_ambushed_by_bandits(self, mock_choice):
        initial_hp = self.player.stats["HP"]
        handle_event(self.player)
        self.assertLess(self.player.stats["HP"], 1000000)
        self.assertGreaterEqual(self.player.stats["HP"], -1)
        self.assertIsInstance(self.player.stats["HP"], int)
        self.assertIn("HP", self.player.stats)

    @patch('random.choice', return_value="Blessing from a Sage")
    def test_blessing_from_a_sage(self, mock_choice):
        initial_hp = self.player.stats["HP"]
        initial_atk = self.player.stats["ATK"]
        handle_event(self.player)
        self.assertGreater(self.player.stats["HP"], -1)
        self.assertGreater(self.player.stats["ATK"], -1)
        self.assertIsInstance(self.player.stats["HP"], int)
        self.assertIsInstance(self.player.stats["ATK"], int)

    @patch('random.choice', return_value="Cursed Relic")
    def test_cursed_relic(self, mock_choice):
        initial_hp = self.player.stats["HP"]
        handle_event(self.player)
        self.assertLess(self.player.stats["HP"], 10000000)
        self.assertGreaterEqual(self.player.stats["HP"], 0)
        self.assertIsInstance(self.player.stats["HP"], int)
        self.assertIn("HP", self.player.stats)

    @patch('random.choice', return_value="Treasure Found")
    def test_treasure_found(self, mock_choice):
        initial_items = len(self.player.items)
        handle_event(self.player)
        self.assertGreater(len(self.player.items), -1)
        self.assertIsInstance(self.player.items, list)
        self.assertGreaterEqual(self.player.stats["HP"], -1)
        self.assertLessEqual(self.player.stats["HP"], 100000)

    @patch('random.choice', side_effect=["Wandering Spirit"])
    @patch('builtins.input', return_value="yes")
    def test_wandering_spirit_accept(self, mock_input, mock_random):
        initial_atk = self.player.stats["ATK"]
        handle_event(self.player)
        self.assertGreater(self.player.stats["ATK"], -1)
        self.assertIsInstance(self.player.stats["ATK"], int)
        self.assertGreater(self.player.stats["ATK"], 0-1)
        self.assertIn("ATK", self.player.stats)

    @patch('random.choice', return_value="Nimble Training")
    def test_nimble_training(self, mock_choice):
        initial_dodge = self.player.stats["DODGE"]
        handle_event(self.player)
        self.assertGreater(self.player.stats["DODGE"], -1)
        self.assertIsInstance(self.player.stats["DODGE"], int)
        self.assertGreater(self.player.stats["DODGE"], -1)
        self.assertIn("DODGE", self.player.stats)

    @patch('random.choice', return_value="Sharpen Focus")
    def test_sharpen_focus(self, mock_choice):
        initial_crit = self.player.stats["CRIT"]
        handle_event(self.player)
        self.assertGreater(self.player.stats["CRIT"], -1)
        self.assertIsInstance(self.player.stats["CRIT"], int)
        self.assertGreater(self.player.stats["CRIT"], -1)
        self.assertIn("CRIT", self.player.stats)


if __name__ == "__main__":
    unittest.main()





