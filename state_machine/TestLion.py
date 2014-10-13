__author__ = 'admin'

from unittest import TestCase
import unittest
import Lion_class as Li
from Lion_class import Lion


class LionTests(TestCase):
    def test_init(self):
        lion = Lion(Li.HUNGRY)
        self.assertEqual(Li.HUNGRY, lion.currentState, '"Hungry" is wrong')
        lion = Lion(Li.FULL)
        self.assertEqual(Li.FULL, lion.currentState, '"Full" is wrong')
        with self.assertRaises(ValueError):
            Lion("blablabla")

    def test_shiftHungryAntelope(self):
        lion = Lion(Li.HUNGRY)
        self.assertEqual(Li.EAT, lion.shiftToNextState(Li.ANTELOPE), 'HUNGRY <- ANTELOPE: wrong return')
        self.assertEqual(Li.FULL, lion.currentState, 'HUNGRY <- ANTELOPE: wrong currentState')

    def test_shiftHungryHunter(self):
        lion = Lion(Li.HUNGRY)
        self.assertEqual(Li.RUN_AWAY, lion.shiftToNextState(Li.HUNTER), 'HUNGRY <- HUNTER: wrong return')
        self.assertEqual(Li.HUNGRY, lion.currentState, 'HUNGRY <- HUNTER: wrong currentState')

    def test_shiftHungryTree(self):
        lion = Lion(Li.HUNGRY)
        self.assertEqual(Li.SLEEP, lion.shiftToNextState(Li.TREE), 'HUNGRY <- TREE: wrong return')
        self.assertEqual(Li.HUNGRY, lion.currentState, 'HUNGRY <- TREE: wrong currentState')

    def test_shiftFullAntelope(self):
        lion = Lion(Li.FULL)
        self.assertEqual(Li.SLEEP, lion.shiftToNextState(Li.ANTELOPE), 'FULL <- ANTELOPE: wrong return')
        self.assertEqual(Li.HUNGRY, lion.currentState, 'FULL <- ANTELOPE: wrong currentState')

    def test_shiftFullHunter(self):
        lion = Lion(Li.FULL)
        self.assertEqual(Li.RUN_AWAY, lion.shiftToNextState(Li.HUNTER), 'FULL <- HUNTER: wrong return')
        self.assertEqual(Li.HUNGRY, lion.currentState, 'FULL <- HUNTER: wrong currentState')

    def test_shiftWrongInput(self):
        lion = Lion(Li.FULL)
        with self.assertRaises(ValueError):
            lion.shiftToNextState("blabla")
        lion = Lion(Li.HUNGRY)
        with self.assertRaises(ValueError):
            lion.shiftToNextState("blabla")



if __name__ == '__main__':
    unittest.main()
