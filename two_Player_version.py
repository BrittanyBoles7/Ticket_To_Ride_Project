import numpy as np
import pandas as pd
import random
import heapq
import unittest


def Creating_The_Board():
    # Define the list of cities
    cities = ['Helena', 'Winnipeg', 'Calgary', 'Vancouver', 'Seattle', 'Portland', 'San Francesco',
              'Los Angeles', 'Salt Lake City', 'Sault St. Marie', 'Montreal', 'Toronto', 'Boston',
              'New York', 'Duluth', 'Pittsburgh', 'Chicago', 'Washington DC', 'Omaha', 'Denver',
              'Las Vegas', 'Phoenix', 'Sante Fe', 'El Palo', 'Oklahoma City', 'Kansas City', 'Saint Louis',
              'Nashville', 'Raleigh', 'Little Rock', 'Atlanta', 'Charleston', 'Miami', 'Dallas',
              'Houston', 'New Orleans']

    fill_in_color = {
        city: {other_city: [np.inf] for other_city in cities} for city in cities
    }

    # Create the DataFrame
    board = pd.DataFrame(fill_in_color)

    # Optionally, fill in some example counts and colors
    board.loc['Helena', 'Winnipeg'] = [4]
    board.loc['Winnipeg', 'Helena'] = [4]
    board.loc['Helena', 'Calgary'] = [4]
    board.loc['Calgary', 'Helena'] = [4]
    board.loc['Seattle', 'Helena'] = [6]
    board.loc['Helena', 'Seattle'] = [6]
    board.loc['Helena', 'Duluth'] = [6]
    board.loc['Duluth', 'Helena'] = [6]
    board.loc['Helena', 'Omaha'] = [5]
    board.loc['Omaha', 'Helena'] = [5]
    board.loc['Helena', 'Salt Lake City'] = [3]
    board.loc['Salt Lake City', 'Helena'] = [3]
    board.loc['Vancouver', 'Calgary'] = [3]
    board.loc['Calgary', 'Vancouver'] = [3]
    board.loc['Vancouver', 'Seattle'] = [1,1]
    board.loc['Seattle', 'Vancouver'] = [1,1]
    board.loc['Seattle', 'Portland'] = [1,1]
    board.loc['Portland', 'Seattle'] = [1,1]
    board.loc['Seattle', 'Calgary'] = [4]
    board.loc['Calgary', 'Seattle'] = [4]
    board.loc['Calgary', 'Winnipeg'] = [6]
    board.loc['Winnipeg', 'Calgary'] = [6]
    board.loc['Winnipeg', 'Duluth'] = [5]
    board.loc['Duluth', 'Winnipeg'] = [5]
    board.loc['Winnipeg', 'Sault St. Marie'] = [6]
    board.loc['Sault St. Marie', 'Winnipeg'] = [6]
    board.loc['Sault St. Marie', 'Montreal'] = [5]
    board.loc['Montreal', 'Sault St. Marie'] = [5]
    board.loc['Sault St. Marie', 'Toronto'] = [2]
    board.loc['Toronto', 'Sault St. Marie'] = [2]
    board.loc['Sault St. Marie', 'Duluth'] = [3]
    board.loc['Duluth', 'Sault St. Marie'] = [3]
    board.loc['Duluth', 'Omaha'] = [2]
    board.loc['Omaha', 'Duluth'] = [2]
    board.loc['Duluth', 'Chicago'] = [3]
    board.loc['Chicago', 'Duluth'] = [3]
    board.loc['Duluth', 'Toronto'] = [6]
    board.loc['Toronto', 'Duluth'] = [6]
    board.loc['Toronto', 'Montreal'] = [3]
    board.loc['Montreal', 'Toronto'] = [3]
    board.loc['Toronto', 'Chicago'] = [4]
    board.loc['Chicago', 'Toronto'] = [4]
    board.loc['Toronto', 'Pittsburgh'] = [2]
    board.loc['Pittsburgh', 'Toronto'] = [ 2]
    board.loc['Montreal', 'Boston'] = [2,2]
    board.loc['Boston', 'Montreal'] = [2, 2]
    board.loc['Montreal', 'New York'] = [3]
    board.loc['New York', 'Montreal'] = [3]
    board.loc['Boston', 'New York'] = [2,2]
    board.loc['New York', 'Boston'] = [2, 2]
    board.loc['New York', 'Pittsburgh'] = [2, 2]
    board.loc['Pittsburgh', 'New York'] = [2, 2]
    board.loc['New York', 'Washington DC'] = [2, 2]
    board.loc['Washington DC', 'New York'] = [2, 2]
    board.loc['Pittsburgh', 'Washington DC'] = [2]
    board.loc['Washington DC', 'Pittsburgh'] = [2]
    board.loc['Pittsburgh', 'Raleigh'] = [2]
    board.loc['Raleigh', 'Pittsburgh'] = [2]
    board.loc['Pittsburgh', 'Nashville'] = [4]
    board.loc['Nashville', 'Pittsburgh'] = [4]
    board.loc['Pittsburgh', 'Saint Louis'] = [5]
    board.loc['Saint Louis', 'Pittsburgh'] = [5]
    board.loc['Pittsburgh', 'Chicago'] = [3,3]
    board.loc['Chicago', 'Pittsburgh'] = [3,3]
    board.loc['Chicago', 'Saint Louis'] = [2,2]
    board.loc['Saint Louis', 'Chicago'] = [2, 2]
    board.loc['Chicago', 'Omaha'] = [4]
    board.loc['Omaha', 'Chicago'] = [4]
    board.loc['Omaha', 'Kansas City'] = [1, 1]
    board.loc['Kansas City', 'Omaha'] = [1, 1]
    board.loc['Omaha', 'Denver'] = [4]
    board.loc['Denver', 'Omaha'] = [4]
    board.loc['Denver', 'Kansas City'] = [4, 4]
    board.loc['Kansas City', 'Denver'] = [4,4]
    board.loc['Denver', 'Oklahoma City'] = [4]
    board.loc['Oklahoma City', 'Denver'] = [4]
    board.loc['Denver', 'Sante Fe'] = [2]
    board.loc['Sante Fe', 'Denver'] = [2]
    board.loc['Denver', 'Phoenix'] = [2]
    board.loc['Phoenix', 'Denver'] = [2]
    board.loc['Denver', 'Salt Lake City'] = [3, 3]
    board.loc['Salt Lake City', 'Denver'] = [3,3]
    board.loc['Salt Lake City', 'Portland'] = [6]
    board.loc['Portland', 'Salt Lake City'] = [6]
    board.loc['Salt Lake City', 'Las Vegas'] = [3]
    board.loc['Las Vegas', 'Salt Lake City'] = [3]
    board.loc['Salt Lake City', 'San Francesco'] = [5,5]
    board.loc['San Francesco', 'Salt Lake City'] = [5, 5]
    board.loc['Portland', 'San Francesco'] = [5, 5]
    board.loc['San Francesco', 'Portland'] = [5,5]
    board.loc['Washington DC', 'Raleigh'] = [2,2]
    board.loc['Raleigh', 'Washington DC'] = [2,2]
    board.loc['San Francesco', 'Los Angeles'] = [3,3]
    board.loc['Los Angeles', 'San Francesco'] = [3,3]
    board.loc['Los Angeles', 'Las Vegas'] = [2]
    board.loc['Las Vegas', 'Los Angeles'] = [2]
    board.loc['Los Angeles', 'Phoenix'] = [2]
    board.loc['Phoenix', 'Los Angeles'] = [2]
    board.loc['Los Angeles', 'El Palo'] = [6]
    board.loc['El Palo', 'Los Angeles'] = [6]
    board.loc['Phoenix', 'El Palo'] = [3]
    board.loc['El Palo', 'Phoenix'] = [3]
    board.loc['Phoenix', 'Sante Fe'] = [3]
    board.loc['Sante Fe', 'Phoenix'] = [3]
    board.loc['Sante Fe', 'Oklahoma City'] = [3]
    board.loc['Oklahoma City', 'Sante Fe'] = [3]
    board.loc['Sante Fe', 'El Palo'] = [2]
    board.loc['El Palo', 'Sante Fe'] = [2]
    board.loc['Oklahoma City', 'El Palo'] = [6]
    board.loc['El Palo', 'Oklahoma City'] = [6]
    board.loc['Oklahoma City', 'Dallas'] = [2,2]
    board.loc['Dallas', 'Oklahoma City'] = [2,2]
    board.loc['Oklahoma City', 'Little Rock'] = [2]
    board.loc['Little Rock', 'Oklahoma City'] = [2]
    board.loc['Oklahoma City', 'Kansas City'] = [2,2]
    board.loc['Kansas City', 'Oklahoma City'] = [2,2]
    board.loc['Kansas City', 'Saint Louis'] = [2,2]
    board.loc['Omaha', 'Kansas City'] = [1]
    board.loc['Kansas City', 'Omaha'] = [1]
    board.loc['Saint Louis', 'Kansas City'] = [2, 2]
    board.loc['Saint Louis', 'Little Rock'] = [2]
    board.loc['Little Rock', 'Saint Louis'] = [2]
    board.loc['Saint Louis', 'Nashville'] = [2]
    board.loc['Nashville', 'Saint Louis'] = [2]
    board.loc['Nashville', 'Little Rock'] = [3]
    board.loc['Little Rock', 'Nashville'] = [3]
    board.loc['Nashville', 'Atlanta'] = [1]
    board.loc['Atlanta', 'Nashville'] = [1]
    board.loc['Nashville', 'Raleigh'] = [3]
    board.loc['Raleigh', 'Nashville'] = [3]
    board.loc['Raleigh', 'Charleston'] = [2]
    board.loc['Charleston', 'Raleigh'] = [2]
    board.loc['Raleigh', 'Atlanta'] = [2, 2]
    board.loc['Atlanta', 'Raleigh'] = [2, 2]
    board.loc['Charleston', 'Miami'] = [4]
    board.loc['Miami', 'Charleston'] = [4]
    board.loc['Atlanta', 'Charleston'] = [2]
    board.loc['Charleston', 'Atlanta'] = [2]
    board.loc['Atlanta', 'Miami'] = [5]
    board.loc['Miami', 'Atlanta'] = [5]
    board.loc['New Orleans', 'Atlanta'] = [4, 4]
    board.loc['Atlanta', 'New Orleans'] = [4,4]
    board.loc['Little Rock', 'Dallas'] = [2]
    board.loc['Dallas', 'Little Rock'] = [2]
    board.loc['New Orleans', 'Miami'] = [6]
    board.loc['Miami', 'New Orleans'] = [6]
    board.loc['New Orleans', 'Houston'] = [2]
    board.loc['Houston', 'New Orleans'] = [2]
    board.loc['Houston', 'Dallas'] = [1]
    board.loc['Dallas', 'Houston'] = [1]
    board.loc['Dallas', 'El Palo'] = [4]
    board.loc['El Palo', 'Dallas'] = [4]
    board.loc['El Palo', 'Houston'] = [6]
    board.loc['Houston', 'El Palo'] = [6]

    # print(board)
    return board

def Get_City_Pairs(num_of_cards):
    # Define a list to hold each route card with city pairs and points
    routes = [
        {"city1": "Winnipeg", "city2": "Little Rock", "points": 11},
        {"city1": "Duluth", "city2": "Houston", "points": 8},
        {"city1": "Vancouver", "city2": "Sante Fe", "points": 13},
        {"city1": "Denver", "city2": "Pittsburgh", "points": 11},
        {"city1": "Sault St. Marie", "city2": "Nashville", "points": 8},
        {"city1": "Dallas", "city2": "New York", "points": 11},

        {"city1": "Los Angeles", "city2": "New York", "points": 21},
        {"city1": "Denver", "city2": "El Palo", "points": 4},
        {"city1": "Duluth", "city2": "El Palo", "points": 10},
        {"city1": "Portland", "city2": "Phoenix", "points": 11},
        {"city1": "Sault St. Marie", "city2": "Oklahoma City", "points": 9},
        {"city1": "Helena", "city2": "Los Angeles", "points": 8},

        {"city1": "Chicago", "city2": "New Orleans", "points": 7},
        {"city1": "Toronto", "city2": "Miami", "points": 10},
        {"city1": "Houston", "city2": "Winnipeg", "points": 12},
        {"city1": "Boston", "city2": "Miami", "points": 12},
        {"city1": "Los Angeles", "city2": "Chicago", "points": 16},
        {"city1": "Chicago", "city2": "Sante Fe", "points": 9},

        {"city1": "New York", "city2": "Atlanta", "points": 6},
        {"city1": "Montreal", "city2": "New Orleans", "points": 13},
        {"city1": "Montreal", "city2": "Atlanta", "points": 9},
        {"city1": "Seattle", "city2": "Los Angeles", "points": 9},
        {"city1": "Kansas City", "city2": "Houston", "points": 5},
        {"city1": "Calgary", "city2": "Salt Lake City", "points": 7},

        {"city1": "Los Angeles", "city2": "Miami", "points": 20},
        {"city1": "Seattle", "city2": "New York", "points": 22},
        {"city1": "Portland", "city2": "Nashville", "points": 17},
        {"city1": "San Francisco", "city2": "Atlanta", "points": 17},
        {"city1": "Vancouver", "city2": "Montreal", "points": 20},
        {"city1": "Calgary", "city2": "Phoenix", "points": 13},

    ]

    # Randomly select the specified number of unique routes
    city_pairs = random.sample(routes, num_of_cards)

    return city_pairs



def Shortest_Path(board, routes, cities):
    start_node = routes["city1"]
    end_node = routes["city2"]

    # Initialize distance and previous city dictionaries
    distances = {city: np.inf for city in cities} # track distances to each city from current
    previous = {city: None for city in cities}  # To track the route
    distances[start_node] = 0

    priority_queue = [(0, start_node)]  # (distance, city)

    # Dijkstra's algorithm
    while priority_queue:
        current_distance, current_city = heapq.heappop(priority_queue)

        # Skip cities that have already been processed with a shorter distance
        if current_distance > distances[current_city]:
            continue

        # Explore neighboring cities
        for neighbor in cities:
            connections = board.loc[current_city, neighbor]
            for connection in connections:
                if connection < np.inf:  # Only valid connections not taken by opponents
                    new_distance = current_distance + connection

                    # If a shorter path is found, update distances and previous city
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        previous[neighbor] = current_city
                        heapq.heappush(priority_queue, (new_distance, neighbor))

    # Reconstruct the shortest path from end to start using 'previous'
    path = []
    current = end_node
    while current is not None:
        path.append(current)
        current = previous[current]

    # Reverse the path to get it from start to end
    path.reverse()

    # If the path length is 1 or the end node is not reached, there's no valid path
    if len(path) < 2 or distances[end_node] == np.inf:
        print(f"No valid path from {start_node} to {end_node}.")
        return None, []

    #print(f"Optimal path from {start_node} to {end_node}:")
    #print(" -> ".join(path))

    return distances, path


def update_boards(city1,city2, boardP, boardO):

    pl_path = boardP.loc[city1,city2]
    op_path = boardO.loc[city1,city2]

    # some cities have multiple tracks so we need to check for that.
    if len(pl_path) == 1 :
        # Update the current players board
        boardP.loc[city1, city2] = [0]
        boardP.loc[city2, city1] = [0]

        # Update the opponents board
        boardO.loc[city1, city2] = [np.inf]
        boardO.loc[city2, city1] = [np.inf]

    #if the opponent already has a track here but there is multiple tracks or vise versa
    elif len(pl_path)>2 and (0 in op_path or np.inf in pl_path):
        # doesn't matter the order, either way both players have access to this path.
        # in the real game one player could potentially occupy both tracks to mess with a player
        # we don't take this into consideration though.
        # Update the current players board
        boardP.loc[city1, city2]= [0,np.inf]
        boardP.loc[city2, city1] = [0,np.inf]

        # Update the opponents board
        boardO.loc[city1, city2] = [np.inf,0]
        boardO.loc[city2, city1] = [np.inf,0]

    #else if this is the first time a tracks laid on a multiple track path
    elif len(pl_path)>2:

        boardP.loc[city1,city2][1] =0
        boardP.loc[city1,city2][1] = 0

        boardO.loc[city1,city2][1] = np.inf
        boardO.loc[city1,city2][1] = np.inf



    return boardP,boardO

def next_path_placement(board,path):
    p1 = path[0]
    p2 = path[1]
    for i in range(1,len(path)):
        city1 = path[i-1]
        city2 = path[i]
        dist = board.loc[city1,city2]
        # get the first path we haven't already placed
        if 0 not in dist:
            p1 = path[i-1]
            p2 = path[i]
            break

    return p1,p2


def ticket_to_ride_two_players():

    cities = ['Helena', 'Winnipeg', 'Calgary', 'Vancouver', 'Seattle', 'Portland', 'San Francesco',
              'Los Angeles', 'Salt Lake City', 'Sault St. Marie', 'Montreal', 'Toronto', 'Boston',
              'New York', 'Duluth', 'Pittsburgh', 'Chicago', 'Washington DC', 'Omaha', 'Denver',
              'Las Vegas', 'Phoenix', 'Sante Fe', 'El Palo', 'Oklahoma City', 'Kansas City', 'Saint Louis',
              'Nashville', 'Raleigh', 'Little Rock', 'Atlanta', 'Charleston', 'Miami', 'Dallas',
              'Houston', 'New Orleans', 'Miami']

    board1 = Creating_The_Board()  # for player ones version
    board2 = Creating_The_Board()  # for player twos version as routes get set from opponent remove them from this players options.
    routes1 = Get_City_Pairs(1)  # player 1 routes
    routes2 = Get_City_Pairs(1)  # player 2 routes

    # points per track
    points_schema = {1: 1, 2: 3, 3: 4, 4: 7, 5: 10, 6: 15}
    # Define the list of cities test case

    # total number of trains per player
    t1 = 40
    t2 = 40
    points1 = 0
    points2 = 0
    while t1 > 0 and t2 > 0:

        #player one goes
        route1 = routes1[0]
        # figure out how to take a path , add to t1 and t2 and
        # update other players board to not have played route just played.
        results,path = Shortest_Path(board1, route1, cities)

        if len(path) ==1:
            print("debugging, this shouldn't happen but was")
        # we no longer can connect the city we lose points
        elif not path:
            points1 -= route1["points"]
            routes1 = Get_City_Pairs(1)
        else:
            c1,c2 = next_path_placement(board1,path)
            print("next placement player 1: ", (c1,c2))

            # update # of tracks laid and points for player
            t1 = t1 - board1.loc[c1, c2][0]  # cost to place
            points1 += points_schema[board1.loc[c1, c2][0]]


            board1,board2 = update_boards(c1,c2,board1,board2)
            if c2 == route1["city2"]: # the end destination
                points1 += route1["points"]
                routes1 = Get_City_Pairs(1) # pick a new city
                print("city reached through path: ", path)
                print("Points so far: ", points1)
            if t1 <= 0:
                print("player two laid all their tracks")
                break


        # player twos turn
        route2 = routes2[0]
        results, path = Shortest_Path(board2, route2, cities)
        if len(path) ==1:
            print("dah fuck")
            # we no longer can connect the city we lose points
        elif not path:
            points2 -= route2["points"]
        else:
            c1, c2 = next_path_placement(board2, path)
            print("next placement player 2: ", (c1, c2))

            # update trains and points player 2
            t1 = t1 - board2.loc[c1,c2][0] # cost to place
            points2 += points_schema[board2.loc[c1, c2][0]]

            # update board with new play
            board2,board1 = update_boards(c1,c2,board2,board1)

            if c2 == route2["city2"]: # the end destination
                routes2 = Get_City_Pairs(1) # pick a new city
                points2 += route2["points"]
                print("city reached through path: ",path)
                print("Points so far: ",points2)
            if t2 <= 0:
                print("player two laid all their tracks")
                break
    print("player 1 total: ", points1)
    print("player 2 total: ", points2)
    return






if __name__ == "__main__":
    ticket_to_ride_two_players()
# class TestBasic(unittest.TestCase):
#     def test_basic(self):
#         board = Test_Board()
#         # Define a list to hold each route card with city pairs and points
#         routes =[
#         {"city1": "Winnipeg", "city2": "Calgary", "points": 11}]
#
#         route = routes[0]
#         cities = ['Helena', 'Winnipeg', 'Calgary', 'Seattle']
#         results, path = Shortest_Path(board, route, cities)
#         self.assertEqual(path, ['Winnipeg', 'Helena', 'Calgary'],"path is correct")
#         end_node = route["city2"]
#         points = results.loc[end_node, 'Points_Earned'] + route['points']
#         self.assertEqual(points,15,"correct total points")
#
# if __name__ == "__main__":
#     unittest.main()

