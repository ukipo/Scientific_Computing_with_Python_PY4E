import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.contents.extend([key] * int(value))

    def draw(self, no_drawn):
        self.draws = list()
        if no_drawn > len(self.contents):
            no_drawn = len(self.contents)

        for i in range(no_drawn):
            ball = random.choice(self.contents)
            self.draws.append(ball)
            self.contents.remove(ball)
        
        return self.draws


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # convert expected_balls
    expected = list()
    for key, value in expected_balls.items():
            expected.extend([key] * int(value))
    print("Expected:", expected)

    # count how many experiments return expected_balls
    successes = 0

    # run defined number of experiments
    for i in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        new_expected = copy.deepcopy(expected)
        new_hat.draw(num_balls_drawn)
        for ball in new_hat.draws:
            if ball in new_expected:
                new_expected.remove(ball)
        if len(new_expected) == 0:
            successes += 1

    # compute probability
    prob = successes/num_experiments

    return prob
