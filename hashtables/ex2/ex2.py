#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    route = []
    flights = {}

    #source is none it is the head
    #destination none it is the tail
    
    #iterate first to makes dictionary
    for i in tickets:
        flights[i.source] = i.destination

    #initializer
    curr_flight = flights["NONE"]

    #append flight
    while curr_flight != "NONE":
        route.append(curr_flight)
        curr_flight = flights[curr_flight]
    route.append(curr_flight)

    return route
