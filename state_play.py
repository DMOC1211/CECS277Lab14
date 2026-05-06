'''
Name: Jacob Miranda & Daniel Puerto
Date: 5/6/26
Group: 11
Description:
'''

from puppy_state import PuppyState
from state_asleep import StateAsleep
from state_eat import StateEat


class StatePlay(PuppyState):
    def feed(self, puppy):
        puppy.change_state(StateEat())
        puppy.inc_feeds()
        return "The puppy stops playing and runs over for food."

    def play(self, puppy):
        puppy.inc_plays()

        if puppy.plays >= 3:
            puppy.change_state(StateAsleep())
            return "The puppy gets tired from playing and falls asleep."

        return "The puppy keeps playing happily!"
