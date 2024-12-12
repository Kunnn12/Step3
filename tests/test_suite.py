import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.test_character import TestCharacter
from tests.test_npc import TestNPC
from tests.test_player import TestPlayer
from tests.test_combat import TestCombat
from tests.test_events import TestEvents
from tests.test_interface import TestInterface

def my_suite():
    suite = unittest.TestSuite()
    
    # Add test classes to the suite
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCharacter))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestNPC))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestPlayer))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCombat))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestEvents))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestInterface))

    # Run the tests
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    my_suite()
