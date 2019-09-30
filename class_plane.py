class Plane():
    def __init__(self, model, cabin_crew, engine_type, capacity):
        self.model = model
        self.cabin_crew = cabin_crew
        self.engine_type = engine_type
        self.capacity = capacity

    def plane(self):
        return self.model + ',' + self.cabin_crew
    def fuelling_plane(self):
        return 'Fuel tanker has been connected to the plane'
    def adding_luggage(self):
        return 'luggage trailer has been connected to the plane'
    def boarding_call(self):
        return 'Could all the passengers please make way to the assigned gates'
    def boarding_passen(self):
        return 'Passengers are currently being boarded'
