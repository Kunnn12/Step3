import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Character.player import Player
from Character.npc import NPC
from Gameplay.combat import execute_player_turn, execute_npc_turn, start_combat

class TestCombat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.player = Player()
        self.npc = NPC()
        self.player.stats = {"HP": 50, "ATK": 20, "DEF": 10}
        self.npc.stats = {"HP": 40, "ATK": 15, "DEF": 8}

    def tearDown(self):
        del self.player
        del self.npc

    def test_player_turn_execution(self):
        initial_npc_hp = self.npc.stats["HP"]
        execute_player_turn(self.player, self.npc)
        current_npc_hp = self.npc.stats["HP"]

        # Ensure NPC HP decreases or remains the same
        self.assertTrue(
            current_npc_hp <= initial_npc_hp,
            f"NPC HP should decrease or remain the same, but got: {current_npc_hp} (Initial: {initial_npc_hp})"
        )

        # Ensure NPC HP is non-negative
        self.assertGreaterEqual(current_npc_hp, 0, "NPC HP should not be negative")

        # Ensure HP is properly rounded
        rounded_hp = round(current_npc_hp)
        self.assertEqual(current_npc_hp, rounded_hp, "NPC HP should be properly rounded to an integer")
        self.assertIsInstance(rounded_hp, int, "NPC HP should be an integer after rounding")


    def test_combat_loop(self):
        start_combat(self.player, self.npc)
        self.assertTrue(
            self.player.stats["HP"] == 0 or self.npc.stats["HP"] == 0,
            "Combat should end when one character's HP reaches zero"
        )
        self.assertNotEqual(
            self.player.stats["HP"] == 0 and self.npc.stats["HP"] == 0,
            True,
            "Both player and NPC should not die simultaneously"
        )
        self.assertGreaterEqual(self.player.stats["HP"], 0)
        self.assertGreaterEqual(self.npc.stats["HP"], 0)

if __name__ == "__main__":
    unittest.main()


