'''
Name: Jacob Miranda & Daniel Puerto
Date: 5/6/26
Group: 11
Description:
'''

from puppy_state import PuppyState
from state_eat import StateEat
from state_play import StatePlay


class StateAsleep(PuppyState):
    def feed(self, puppy):
        puppy.change_state(StateEat())
        puppy.inc_feeds()
        return "The puppy wakes up slowly and begins to eat."

    def play(self, puppy):
        puppy.change_state(StatePlay())
        puppy.inc_plays()
        return "The puppy wakes up excitedly and starts playing!"
