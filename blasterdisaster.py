import numpy as np
import random as rnd
from tkinter import Tk
import time as tmr

class Direction:
    """
    This can serve as our action space reference
    """
    Up = -1
    Down = 1
    Nothing = 0


class Marker:
    AGENT = 1
    BEAM = 2
    EMPTY = 0
    LASER_HIT = 3


class Laser:
    """
    Represents a laser beam on the star field
    """
    def __init__(self, init_coord):
        """
        :param init_row: this represents the start row of where a laser will be generated
        #
        """
        self.coord = init_coord # This keeps track of the row, col of the laser beam


class Environment:
    """
    This creates the main game environment
    """
    def __init__(self, p_size, int_max_lasers=3):
        """
        :param p_size: A tuple indicating size of the star field, typically (10, 10)
        :param int_max_lasers: how many lasers can appear on the field.
        """
        self.StarField = np.zeros(p_size, dtype=int)
        self.laser_array = []  # Keeps track of all the lasers in the field. These must be laser objects
        self.agent_position = ()  # Keeps track of agent (x, y)
        self.max_lasers = int_max_lasers
        self.started = False

    def spawn_laser(self):
        """
        Spawn a laser at row
        :param init_row: row where the laser will be
        :return: void
        """

        # Add a laser to the array providing it doesn't exceed the max
        if len(self.laser_array) < self.max_lasers:
            # Spawn a laser and add to the array
            mypos = self.get_random_laser_position()

            # Append only if the spot is empty
            if self.StarField[(mypos, self.StarField.shape[1] - 1)] == Marker.EMPTY:
                new_laser = Laser(mypos)
                new_laser.coord = (mypos, self.StarField.shape[1] - 1) # set the coordinate
                self.laser_array.append(new_laser)

    def get_random_laser_position(self):
        """
        Returns an integer indicating the row of the laser
        :return: int
        """
        return rnd.randint(0, self.StarField.shape[0] - 1)

    def spawn_agent(self):
        """
        randomly places agent along (row, 1) at the beginning of a game
        :return: void
        """

    def animate(self):
        """
        This goes through the laser array and animates each laser step by step, and will also
        eliminate any laser
        :return:
        """

        # spawn a laser
        self.spawn_laser()

        # First we'll place the laser in the star field
        if len(self.laser_array) > 0:
            # the laser array has at least one or more lasers in it.
            for idx, lsr in enumerate(self.laser_array):
                # Place a laser
                row, col = lsr.coord
                if col > 0:
                    self.StarField[row, col] = Marker.BEAM  # Place the beam in the matrix
                elif col == 0:
                    # delete the laser
                    self.laser_array.remove(lsr)
                    self.StarField[row, col] = Marker.EMPTY  # Clear out the beam

            # next we'll animate the lasers to the left one spot
            for index_in, lsr in enumerate(self.laser_array):
                row, col = lsr.coord
                if col > 0:
                    lsr.coord = (row, col - 1)
                    r, c = lsr.coord
                    self.StarField[r, c] = Marker.BEAM
                    self.StarField[row, col] = Marker.EMPTY # update the previous

    def check_contact(self):
        """
        This checks if a laser makes contact with the agent, garnering a negative reward,
        If it does, the contacting laser should be despawned
        :return:
        """

    def start(self):
        """
        This starts the environment and the loop
        """


def testing():
    r = Environment((10, 10), 10)
    print(r.StarField)

    while True:
        print(r.StarField)
        r.animate()
        tmr.sleep(1)

testing()
