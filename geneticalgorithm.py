import numpy as np
from sklearn.linear_model import LinearRegression
from random import randint, random, choice
import matplotlib.pyplot as plt

# Define the structure of a scenario (simplified for this prototype)
#In our case scenarios will be defined by the VerifAI toolkit and Spinroot class Scenario:
class Scenario:
  def __init__(self, traffic_density, weather_condition, road_condition):
    self.traffic_density = traffic_density
    self.weather_condition = weather_condition
    self.road_condition = road_condition


  def get_features(self):
    return [self.traffic_density, self.weather_condition, self.road_condition]

# Generate an initial population of scenarios
def generate_initial_population(size):
  return [Scenario(randint(1, 10), random(), randint(1, 5)) for _ in range(size)]

#Evaluate the fitness of each scenario
def evaluate_fitness(scenario):
  # Simplified fitness function
  return scenario.traffic_density * scenario.weather_condition * scenario.road_condition

# Perform selection based on fitness
def select(population, fitnesses, num_parents):
  return list(np.random.choice(population, size=num_parents, replace=False, p=fitnesses/np.sum(fitnesses)))

# Perform crossover between scenarios
def crossover (parent1, parent2):
  child = Scenario(parent1.traffic_density, parent2.weather_condition, parent1.road_condition)
  return child

#Perform mutation on a scenario
def mutate(scenario):
  scenario.traffic_density = randint(1,10)
  scenario.weather_condition = random()
  scenario.road_condition = randint(1,5)

#Main Loop of the Genetic Algorithm
# Modified genetic_algorithm function to track average fitness per generation
def genetic_algorithm_with_plot(iterations, population_size, num_parents):
    population = generate_initial_population(population_size)
    average_fitness_per_generation = []

    for _ in range(iterations):
        fitnesses = np.array([evaluate_fitness(scenario) for scenario in population])
        average_fitness_per_generation.append(np.mean(fitnesses))
        parents = select(population, fitnesses, num_parents)
        next_generation = []

        # Generate next generation through crossover and mutation
        for i in range(len(parents) // 2):
            for _ in range(2):  # For each pair of parents, produce two children
                child = crossover(parents[i], parents[len(parents) - i - 1])
                mutate(child)
                next_generation.append(child)

        population = next_generation

    return population, average_fitness_per_generation

# Run the modified genetic algorithm and plot the results
final_population, avg_fitness = genetic_algorithm_with_plot(10, 50, 10)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(avg_fitness, marker='o')
plt.title("Average Fitness per Generation in Genetic Algorithm")
plt.xlabel("Generation")
plt.ylabel("Average Fitness")
plt.grid(True)
plt.show()

