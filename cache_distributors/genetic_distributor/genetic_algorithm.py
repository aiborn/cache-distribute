import random


class GeneticAlgorithm(object):
    def __init__(self, genetics):
        self.genetics = genetics

    def run(self):
        population = self.genetics.initial()
        is_solution = False
        while not is_solution:
            fits = [(self.genetics.fitness(ch),  ch) for ch in population]
            is_solution = self.genetics.check_stop(fits)
            population = self.next(fits)

        return self.genetics.get_generation_count()

    def next(self, fits):
        parents_generator = self.genetics.parents(fits)
        size = len(fits)
        nexts = []
        while len(nexts) < size:
            parents = next(parents_generator)
            cross = random.random() < self.genetics.probability_crossover()
            children = self.genetics.crossover(parents) if cross else parents
            for ch in children:
                mutate = random.random() < self.genetics.probability_mutation()
                nexts.append(self.genetics.mutation(ch) if mutate else ch)

        return nexts[0:size]

