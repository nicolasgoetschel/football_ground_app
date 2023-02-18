class FootballGround:
    def __init__(self, name, team, location, capacity, visited=False):
        self.name = name
        self.team = team
        self.location = location
        self.capacity = capacity
        self.namevisited = visited