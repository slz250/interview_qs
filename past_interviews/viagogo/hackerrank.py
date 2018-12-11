from queue import PriorityQueue

# Classes
class Event(object):
    def __init__(self, id_=None, coord=None, tix_prices=None):
        self.id = id_
        self.coord = coord
        self.tix_prices = tix_prices

    def print(self):
        print(f'Event - Id: {self.id}, Coord: {self.coord}, Ticket Prices: {self.tix_prices}')
class Buyer(object):
    def __init__(self, coord=None):
        self.coord = coord

    def print(self):
        print(f'Buyer - Coord: {self.coord}')

class MapCoordinate(object):
    def __init__(self):
        self.objects = list()

    def add(self, obj):
        self.objects.append(obj)

class Map(object):
    def __init__(self, dimension=None):
        self.dimension = dimension
        self.mat = [[MapCoordinate() for c in range(self.dimension)] for r in range(self.dimension)]
        self.events = list()
        self.buyers = list()

    def addEvent(self, event):
        self.events.append(event)
        map_coord = self.mat[event.coord[0]][event.coord[1]]
        map_coord.add(event)

    def addBuyer(self, buyer):
        self.buyers.append(buyer)
        map_coord = self.mat[buyer.coord[0]][buyer.coord[1]]
        map_coord.add(buyer)

# The following method get the manhatten distance betwen two points (x1,y1) and (x2,y2)
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# Enter your code here. Read input from STDIN. Print output to STDOUT
sizeOfWorld = int(input())

numberOfEvents = int(input())
events = list()
for i in range(numberOfEvents):
    eventLine = input()
    # TODO: you will need to parse and store the events
    event = eventLine.split(' ')
    coord = (event[1], event[2])
    prices = list()
    for j in range(3, len(event)):
        prices.append(event[j])
    events.append(Event(event[0], coord, prices))

numberOfBuyers = int(input())
buyers = list()
for i in range(numberOfBuyers):
    buyerLine = input()
    buyer = buyerLine.split(' ')
    coord = (buyer[0], buyer[1])
    # TODO: you will need to parse and store the buyers
    buyers.append(Buyer(coord))

def test():
    for e in events:
        e.print()
    for b in buyers:
        b.print()

def findCheapest(events):
    pq = PriorityQueue()
    for e in events:
        for p in e.tix_prices:
            pq.put((p, e))

    res = list()
    cheapest_tuple = pq.get()
    res.append(cheapest_tuple)
    cheapest = cheapest_tuple[0]
    finished = False
    while not finished:
        popped = pq.get()
        if popped[0] == cheapest:
            res.append(popped)
        else:
            finished = True

    return res

def findLowestId(cheapest):
    pq = PriorityQueue()
    for tuple_ in cheapest:
        e = tuple_[1]
        pq.put(e.id, tuple_[0])
    return pq.get()

def gettingTicketsToFansV3(sizeOfWorld, events, buyers):
    map = Map(sizeOfWorld)
    for e in events:
        map.addEvent(e)
    for b in buyers:
        map.addBuyer(b)
    #BF way, better way would probably be to do a diamond-like BFS from
    #each buyer coordinate
    #i.e:
    # [' ',' ','2',' ',' ']
    # [' ','2','1','2',' ']
    # ['2','1','S','1','2']
    # [' ','2','1','2',' ']
    # [' ',' ','2',' ',' ']
    # here S is buyer coordinate, the numbers represent the distance
    # from the coordinate (diamond-like BFS)
    # we continue searching until we hit an event

    valid_events = set(map.events.copy())
    res = list()
    for b in map.buyers:
        min_dist = map.dimension + map.dimension - 2
        min_dist_events = list()
        for e in valid_events:
            temp_dist = manhattan_distance(b.coord[0], b.coord[1], e.coord[0], e.coord[1])
            if temp_dist < min_dist:
                min_dist = temp_dist
                min_dist_events.clear()
                min_dist_events.append(e)
            elif temp_dist == min_dist:
                min_dist_events.append(e)

        cheapest = findCheapest(min_dist_events)
        if len(cheapest) > 1:
            lowest_id = findLowestId(cheapest)
            res.append((b, (lowest_id[0], lowest_id[1])))
        else:





# The solution to the first sample above would be to output the following to console:
# (Obviously, your solution will need to figure out the output and not just hard code it)
if __name__ == '__main__':
    pass