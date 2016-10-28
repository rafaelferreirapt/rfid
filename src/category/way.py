from tree_search import *
from halls.models import SubHall, SubHallConnection


class ParseModel:

    def __init__(self):
        self.connections = []
        self.coordinates = {}

    def parse(self):
        halls = SubHall.objects.all()

        for hall in halls:
            hall_connections = SubHallConnection.objects.filter(sub_hallA=hall)

            for con in hall_connections:
                if con.connected:
                    self.connections.append((hall.name, con.sub_hallB.name))

                if hall.name not in self.coordinates:
                    self.coordinates[hall.name] = {}

                self.coordinates[hall.name][con.sub_hallB.name] = {"distance": con.distance}


class Way:
    def __init__(self):
        parse = ParseModel()
        parse.parse()

        self.prob = GridConnections(parse)
        self.calculated = None

    def search_path(self, from_point, to):
        prob = SearchProblem(self.prob, from_point, to)

        tree = SearchTree(prob)

        self.calculated = tree.search()
        return self.calculated


class GridConnections(SearchDomain):
    def __init__(self, parse):
        SearchDomain.__init__(self)
        self.connections = parse.connections
        self.coordinates = parse.coordinates
        self.visited = []

    def actions(self, cell):
        self.visited += [cell]
        actlist = []
        for c1, c2 in self.connections:
            if c1 == cell and c2 not in self.visited:
                actlist += [(c1, c2)]
            elif c2 == cell and c1 not in self.visited:
                actlist += [(c2, c1)]
        return actlist

    def result(self, state, action):
        c1, c2 = action
        if c1 == state:
            return c2

    def cost(self, state, action):
        return 0

    def heuristic(self, state, goal_state):
        return self.coordinates[state][goal_state]["distance"]
