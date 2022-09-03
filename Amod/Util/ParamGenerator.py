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

    def get_setup_cost_normal(self, mean, var, number_facility):
        return abs(self.streams[0].normal(mean, var, number_facility))

    def get_allocation_cost_normal(self, mean, var, number_allocation):
        return abs(self.streams[1].normal(mean, var, number_allocation))

    def get_client_demand_normal(self, mean, var, number_client):
        return abs(self.streams[2].normal(mean, var, number_client))

    def get_facility_capacity_normal(self, mean, var, number_facility):
        return abs(self.streams[3].normal(mean, var, number_facility))

    def get_param_lambda(self, number):
        return self.streams[4].normal(0,1,number)