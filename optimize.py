import pickle

from colearning.genetic_optimizer import Optimizer
from colearning.learning_optimizer import LearningOptimizer
from colearning.players import ActionQLearningPlayer, TurretPlayer
from pybrain.tools.shortcuts import buildNetwork

opt = LearningOptimizer()
teams = (2, 1)
problem = (5,7)

players = [ActionQLearningPlayer(problem), TurretPlayer()]

opt.run(
    players,
    teams,
    4
)

print("Saving players to players.cln...")
with open("players.cln", "w") as f:
    pickle.dump(players, f)
