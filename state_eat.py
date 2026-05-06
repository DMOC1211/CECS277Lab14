'''
Name: Jacob Miranda & Daniel Puerto
Date: 5/6/26
Group: 11
Description:
'''

from puppy_state import PuppyState
from state_asleep import StateAsleep
from state_play import StatePlay


class StateEat(PuppyState):
    def feed(self, puppy):
        puppy.inc_feeds()

        if puppy.feeds >= 2:
            puppy.change_state(StateAsleep())
            return "The puppy is full and curls up to sleep."

        return "The puppy keeps eating happily."

    def play(self, puppy):
        puppy.change_state(StatePlay())
        puppy.inc_plays()
        return "The puppy stops eating and starts playing!"
