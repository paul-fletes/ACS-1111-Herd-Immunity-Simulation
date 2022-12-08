import random
import sys
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected

        self.newly_infected = []
        self.newly_dead = 0

        self.current_vaccinated = 0
        self.current_infected = 0

        self.total_alive = 0
        self.total_dead = 0
        self.total_infected = 0

        self.time_step_counter = 0
        self.file_name = f"{virus_name}.{pop_size}.{vacc_percentage}.{initial_infected}.md"
        self.logger = Logger(self.file_name)
        self.population = self._create_population()

    def _create_population(self):
        start_population = []

        # Vaccinated
        vaccinated_group = self.pop_size * self.vacc_percentage
        vaccinated_group = int(vaccinated_group)
        self.current_vaccinated = vaccinated_group

        # Unvaccinated
        unvaccinated_group = self.pop_size - self.initial_infected - vaccinated_group

        # Infected
        infected_group = self.initial_infected

        # Testing
        print(f"Vaccinated: {vaccinated_group}")
        print(f"Unvaccinated: {unvaccinated_group}")
        print(f"Infected: {infected_group}")

        id_num = 0
        for num in range(vaccinated_group):
            id_num += 1
            person = Person(id_num, True, None)
            start_population.append(person)

        for num in range(unvaccinated_group):
            id_num += 1
            person = Person(id_num, False, self.virus)
            start_population.append(person)

        for num in range(infected_group):
            id_num += 1
            person = Person(id_num, False, self.virus)
            start_population.append(person)

        print(f"Total population: {int(self.pop_size)}")
        self.logger.write_metadata(
            self.pop_size, self.vacc_percentage, virus.name, virus.mortality_rate, virus.repro_rate)
        return start_population

    def _simulation_should_continue(self):
        # This method will return a booleanb indicating if the simulation
        # should continue.
        # The simulation should not continue if all of the people are dead,
        # or if all of the living people have been vaccinated.
        # TODO: Loop over the list of people in the population. Return True
        # if the simulation should continue or False if not.
        pass

    def run(self):
        # This method starts the simulation. It should track the number of
        # steps the simulation has run and check if the simulation should
        # continue at the end of each step.

        print('run check')
        time_step_counter = 0
        should_continue = True

        while should_continue:
            #     self.time_step()
            #     should_continue = self._simulation_should_continue()
            #     self.time_step_counter += 1
            # print("testing end of runtime")
            # TODO: Increment the time_step_counter
            # TODO: for every iteration of this loop, call self.time_step()
            # Call the _simulation_should_continue method to determine if
            # the simulation should continue
            should_continue = self._simulation_should_continue()
            pass

        # TODO: Write meta data to the logger. This should be starting
        # statistics for the simulation. It should include the initial
        # population size and the virus.

        # TODO: When the simulation completes you should conclude this with
        # the logger. Send the final data to the logger.

    def time_step(self):
        # time_step_deaths = 0
        # for person in self.population:
        #     if person.infection != None and person.is_alive == True:
        #         counter = 0
        #         while counter < 100:
        #             random_person = random.choice(self.population)
        #             self.interaction(person, random_person)
        #             counter += 1
        #         if person.did_survive_infection() == True:
        #             person.infection = None
        #             person.is_vaccinated = True
        #             self.current_infected -= 1
        #             self. current_vaccinated += 1
        #         else:
        #             self.total_dead += 1
        #             self.total_infected -= 1
        #             time_step_deaths += 1
        #             person.is_alive = False

        # total_alive = self.pop_size - self.total_dead
        # print(f"Total alive: {total_alive}")
        # print(f"Current Infected: {self.current_infected}")
        # print(f"Current Vaccinated: {self.current_vaccinated}")

        # This method will simulate interactions between people, calulate
        # new infections, and determine if vaccinations and fatalities from infections
        # The goal here is have each infected person interact with a number of other
        # people in the population
        # TODO: Loop over your population
        # For each person if that person is infected
        # have that person interact with 100 other living people
        # Run interactions by calling the interaction method below. That method
        # takes the infected person and a random person
        pass

    def interaction(self, infected_person, random_person):
        # TODO: Finish this method.
        # assert infected_person.is_alive == True
        # assert random_person.is_alive == True

        # if random_person.is_vaccinated == True or random_person.infection != None:
        #     pass
        # elif random_person.is_vaccinated == False and random_person.infection == None:
        #     if random.random() < infected_person.infection.repro_rate:
        #         if random_person._id not in self.newly_infected:
        #             self.newly_infected.append(random_person._id)
        #             self.total_infected += 1

        # The possible cases you'll need to cover are listed below:
        # random_person is vaccinated:
        #     nothing happens to random person.
        # random_person is already infected:
        #     nothing happens to random person.
        # random_person is healthy, but unvaccinated:
        #     generate a random number between 0.0 and 1.0.  If that number is smaller
        #     than repro_rate, add that person to the newly infected array
        #     Simulation object's newly_infected array, so that their infected
        #     attribute can be changed to True at the end of the time step.
        # TODO: Call logger method during this method.
        pass

    def _infect_newly_infected(self):
        # for id in self.newly_infected:
        #     for person in self.population:
        #         if person._id == id:
        #             person.infection = self.virus

        # self.newly_infected = []
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        pass


if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.2
    initial_infected = 50

    # Make a new instance of the simulation
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)
    # virus = Virus(virus, pop_size, vacc_percentage, initial_infected)

    sim.run()
    sim.logger.write_metadata(
        pop_size, vacc_percentage, virus.name, virus.mortality_rate, virus.repro_rate)
