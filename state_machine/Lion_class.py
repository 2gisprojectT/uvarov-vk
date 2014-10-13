__author__ = 'Vadim Uvarov'

# states
FULL = "full"
HUNGRY = "hungry"
# inputs
ANTELOPE = "antelope"
HUNTER = "hunter"
TREE = "tree"
# outputs
SLEEP = "sleep"
RUN_AWAY = "run away"
LOOK = "look"
EAT = "eat"


class Lion:
    currentState = FULL

    def __init__(self, startingState):
        if startingState != FULL and startingState != HUNGRY:
            raise ValueError("startingState must be + " + FULL + " or " + HUNGRY)
        self.currentState = startingState

    def shiftToNextState(self, inputSymbol):
        if inputSymbol != ANTELOPE and inputSymbol != HUNTER and inputSymbol != TREE:
            raise ValueError("input must be" + ANTELOPE + " or " + HUNTER + " or " + TREE)
        if self.currentState == FULL:
            self.currentState = HUNGRY
            if inputSymbol == ANTELOPE:
                return SLEEP
            if inputSymbol == HUNTER:
                return RUN_AWAY
            if inputSymbol == TREE:
                return LOOK
        else:
            if inputSymbol == ANTELOPE:
                self.currentState = FULL
                return EAT
            if inputSymbol == HUNTER:
                return RUN_AWAY
            if inputSymbol == TREE:
                return SLEEP
'''
lion = Lion(FULL)
print "Prev state: {} | Input: {} | Output: {} | New State: {}"\
    .format(lion.currentState, HUNTER, lion.shiftToNextState(HUNTER), lion.currentState)
print "Prev state: {} | Input: {} | Output: {} | New State: {}"\
    .format(lion.currentState, ANTELOPE, lion.shiftToNextState(ANTELOPE), lion.currentState)
print "Prev state: {} | Input: {} | Output: {} | New State: {}"\
    .format(lion.currentState, TREE, lion.shiftToNextState(TREE), lion.currentState)
'''