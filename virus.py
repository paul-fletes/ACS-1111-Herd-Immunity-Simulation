class Virus(object):
    # Properties and attributes of the virus used in Simulation.
    def __init__(self, name, repro_rate, mortality_rate):
        # Define the attributes of your your virus
        self.name = name
        # TODO Define the other attributes of Virus
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate
        pass


def test_virus():
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3
    print(virus.name, virus.repro_rate, virus.mortality_rate)


def test_virus():
    virus = Virus("Influenza", 0.8, 0.3)
    assert virus.name == "Influenza"
    assert virus.repro_rate == 0.9
    assert virus.mortality_rate == 0.05
    print(virus.name, virus.repro_rate, virus.mortality_rate)


def test_virus():
    virus = Virus("Smallpox", 0.8, 0.3)
    assert virus.name == "Smallpox"
    assert virus.repro_rate == 0.6
    assert virus.mortality_rate == 0.1
    print(virus.name, virus.repro_rate, virus.mortality_rate)
