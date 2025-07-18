import random


class Direction:
    NORTH = (0, 1)
    NORTHEAST = (0.5, 0.5)
    EAST = (1, 0)
    SOUTHEAST = (0.5, -0.5)
    SOUTH = (0, -1)
    SOUTHWEST = (-0.5, -0.5)
    WEST = (-1, 0)
    NORTHWEST = (-0.5, 0.5)

    ###########
    # METHODS #
    ###########
    @staticmethod
    def getRandomDirection():
        """
        Return a random Direction
        """
        return random.choice(
            [
                Direction.NORTH,
                Direction.NORTHEAST,
                Direction.EAST,
                Direction.SOUTHEAST,
                Direction.SOUTH,
                Direction.SOUTHWEST,
                Direction.WEST,
                Direction.NORTHWEST,
            ]
        )

    @staticmethod
    def getRandomReplicationDirection():
        """
        Return a random Direction for replication -> chose only between North, South, East adn West
        """
        return random.choice(
            [Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST]
        )


if __name__ == "__main__":
    for i in range(5):
        print(Direction.getRandomDirection())
