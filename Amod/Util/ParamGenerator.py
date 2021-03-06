from numpy.random import SeedSequence, default_rng


class ParamGenerator:
    def __init__(self, seed, number_stream):
        seed_sequence = SeedSequence(seed)
        child_seeds = seed_sequence.spawn(number_stream)
        self.streams = [default_rng(s) for s in child_seeds]

    def get_setup_cost(self, max_cost, number_facility):
        return self.streams[0].integers(1, max_cost, number_facility)

    def get_allocation_cost(self, max_cost, number_allocation):
        return self.streams[1].integers(1, max_cost, number_allocation)

    def get_client_demand(self, max_value, number_client):
        return self.streams[2].integers(1, max_value, number_client)

    def get_facility_capacity(self, max_value, number_facility):
        return self.streams[3].integers(1, max_value, number_facility)

    """
        :param number: parametri da generare
        :type number: int
    """
    def get_param_lambda(self, number):
        vet = self.streams[4].integers(1,30,number)
        print(vet)
        return vet