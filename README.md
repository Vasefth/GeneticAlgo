# GeneticAlgo

# Genetic Algorithm for Simulated Environment Generation

## Overview

This project presents a novel approach using a Genetic Algorithm (GA) to generate and optimize simulated environments for training Neural Networks (NN) mounted on cars. The core idea is to evolve scenarios that are challenging for the NN to navigate, thereby potentially improving the robustness of autonomous driving systems. Scenarios are characterized by variables such as traffic density, weather conditions, and road conditions. Through the process of selection, crossover, and mutation, the algorithm aims to discover environments that present the NN with complex driving situations.

## Features

- Implementation of a Genetic Algorithm to evolve simulation scenarios.
- Custom scenario representation including traffic density, weather, and road conditions.
- Fitness evaluation based on a simplified function considering scenario variables.
- Selection, crossover, and mutation operations to evolve scenarios.
- Tracking of average fitness per generation to monitor the GA's progress.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Installation

Ensure you have Python installed on your system. If not, download and install the latest version from [python.org](https://www.python.org/). Then, install the required libraries using pip:

```bash
pip install numpy matplotlib
```

## Usage

The script can be executed directly from the command line. Navigate to the directory containing the script and run:

```bash
python simulated_environment_genetic_algorithm.py
```

This will start the Genetic Algorithm process and, upon completion, display a plot showing the average fitness of the population over generations. This plot helps in understanding how the scenario simulations evolve and become more challenging over time.

## Approach

The GA starts by generating an initial population of scenarios, each defined by:
- **Traffic Density:** A measure of how congested the traffic is.
- **Weather Condition:** A continuous variable representing the severity of weather (e.g., rain, fog).
- **Road Condition:** A measure of road quality or obstacles present.

Each scenario's fitness is evaluated based on a simplified function that combines these variables. The GA then selects the fittest scenarios to serve as parents for the next generation. Offspring are produced through crossover and mutation operations, introducing variability and allowing the population to explore a wider space of possible scenarios.

## Configuration

- **Iterations:** The number of generations the GA will evolve the population through.
- **Population Size:** The total number of scenarios in each generation.
- **Number of Parents:** The number of scenarios selected for reproduction in each generation.

These parameters can be adjusted in the script to explore their effects on the algorithm's performance and the quality of generated scenarios.

## Contributing

Contributions to this project are welcome! To contribute, please fork the repository, make your changes, and submit a pull request. We are interested in enhancements that improve the GA's effectiveness, introduce more complex scenario variables, or refine the fitness evaluation function.
