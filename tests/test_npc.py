import unittest
from unittest.mock import patch

# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from SimpleBattle.Character.npc import NPC

class TestNPC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Initializing TestNPC Class")

    @classmethod
    def tearDownClass(cls):
        print("Cleaning TestNPC Class")

    def setUp(self):
        self.npc = NPC()

    def tearDown(self):
        del self.npc

    def test_initialization(self):
        self.assertEqual(self.npc.name, "Enemy")
        self.assertIn(self.npc.characteristic, ["gentle", "rude", "neutral"])
        self.assertIn("HP", self.npc.stats)
        self.assertIn("ATK", self.npc.stats)
        self.assertIn("CRIT", self.npc.stats)
        self.assertIn("DODGE", self.npc.stats)

    def test_choose_attack(self):
        attack_choice_list = []
        while len(attack_choice_list) < 3:
            attack = self.npc.choose_attack()
            self.assertIn(attack["attack_type"], ["Basic Attack", "Heavy Strike", "Quick Attack"])
            if attack["attack_type"] == "Basic Attack":
                self.assertTrue(attack["damage"] == self.npc.stats["ATK"])
                self.assertEqual(attack["dodge_chance_modifier"], 0)
                self.assertEqual(attack["crit_chance_modifier"], 0)
            elif attack["attack_type"] == "Heavy Strike":
                self.assertTrue(attack["damage"] == self.npc.stats["ATK"] * 1.5)
                self.assertEqual(attack["dodge_chance_modifier"], 20)
                self.assertEqual(attack["crit_chance_modifier"], 0)
            elif attack["attack_type"] == "Quick Attack":
                self.assertTrue(attack["damage"] == self.npc.stats["ATK"] * 0.5)
                self.assertEqual(attack["dodge_chance_modifier"], -20)
                self.assertEqual(attack["crit_chance_modifier"], 15)
            if attack["attack_type"] not in attack_choice_list:
                attack_choice_list.append(attack["attack_type"])
            else:
                pass

    def test_taunt_player(self):
        # Define the expected taunts based on the NPC's characteristic
        expected_taunts = {
            "gentle": [
                "You fight bravely, but this is not your day.",
                "A valiant effort, but you should surrender.",
                "You have skill, but I must prevail.",
                "Your heart is strong, but so is my blade.",
                "This battle will end peacefully—for me.",
            ],
            "rude": [
                "You think you can defeat me?",
                "Prepare to lose!",
                "Is that all you've got?",
                "I'll crush you like an insect!",
                "You're pathetic, even for a challenge!",
            ],
            "neutral": [
                "Let us see who is stronger.",
                "A good fight is what I live for!",
                "This will be a battle to remember.",
                "Strength meets strength today.",
                "May the best fighter win!",
            ],
        }

        # Call the taunt_player method
        
        taunt = self.npc.taunt_player()
        # Verify the taunt is a string and not empty
        self.assertIsInstance(taunt, str)
        self.assertGreater(len(taunt), 0)
        self.assertLess(len(taunt), 50)

        # Verify the taunt belongs to the correct characteristic group
        characteristic_taunts = expected_taunts[self.npc.characteristic]
        self.assertIn(taunt, characteristic_taunts)
