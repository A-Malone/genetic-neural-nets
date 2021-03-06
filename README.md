# Genetic Neural Nets
This repository serves as a repository of my testing of using genetic algorithms to train neural networks.

OpenAi test
====
[openai_test.py](openai_test.py) demonstrates the successful implementation of ESP-style decompostion to convert neural nets into genes which can be spliced together by neural nets. The ESP decomposition itself and the neural nets are implemented in the pybrain library, with the genetic training algorithm presented in the file. In this demonstration, the [Cart Pole](https://gym.openai.com/envs/CartPole-v0) environment from OpenAI gym  is used as a test. The algorithm solves the problem (As defined by OpenAI gym) in as few as 8 100-individual generations.

Requirements
----
* OpenAI gym
* numpy
* PyBrain >= 0.3.3

Colearning (UNDER CONSTRUCTION)
====
An attempt to train neural networks adversarily to play a simple combat game. Progress is on-going.
