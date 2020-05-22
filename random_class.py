from random import choice


class RandomWalk:
    """A class to generate a random walk."""

    def __init__(self, num_points=5000):
        """Initialize attributes of walk."""

        self.num_points = num_points

        # All walks start at (0, 0).
        self.x = [0]
        self.y = [0]

    def get_step(self):
        """Refactoring steps."""

        # Decide which direction to go and how far to go in that direction.
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance

        return step

    # Choosing Directions.

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x[-1] + x_step
            y = self.y[-1] + y_step

            self.x.append(x)
            self.y.append(y)
