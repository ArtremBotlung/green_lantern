class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class RobotFallsError(Exception):
    pass


class Robot:
    def __init__(self, x, y, asteroid, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.asteroid = asteroid
        if self.x > self.asteroid.x:
            raise MissAsteroidError()
        if self.y > self.asteroid.y:
            raise MissAsteroidError()

    def turn_left(self):
        left_turns = {
            'N': 'W',
            'W': 'S',
            'S': 'E',
            'E': 'W',

        }
        self.direction = left_turns[self.direction]

    def turn_right(self):
        right_turns = {
            'N': 'E',
            'E': 'S',
            'S': 'W',
            'W': 'N'
        }
        self.direction = right_turns[self.direction]

    def move_forward(self):
        if self.direction == 'N':
            self.x += 1
        if self.direction == 'E':
            self.y += 1
        if self.direction == 'S':
            self.x -= 1
        if self.direction == 'W':
            self.y -= 1

        if self.x > self.asteroid.x or self.y > self.asteroid.y:
            raise RobotFallsError()

    def move_backward(self):
        if self.direction == 'N':
            self.x -= 1
        if self.direction == 'E':
            self.y -= 1
        if self.direction == 'S':
            self.x += 1
        if self.direction == 'W':
            self.y += 1
        if self.x > self.asteroid or self.y > self.asteroid.y:
            raise RobotFallsError()


class MissAsteroidError(Exception):
    pass
