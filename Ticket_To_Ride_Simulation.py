import numpy as np
import pandas as pd
import random
import heapq


def Creating_The_Board():
    # Define the list of cities
    cities = ['Helena', 'Winnipeg', 'Calgary', 'Vancouver', 'Seattle', 'Portland', 'San Francesco',
              'Los Angeles', 'Salt Lake City', 'Sault St. Marie', 'Montreal', 'Toronto', 'Boston',
              'New York', 'Duluth', 'Pittsburgh', 'Chicago', 'Washington DC', 'Omaha', 'Denver',
              'Las Vegas', 'Phoenix', 'Sante Fe', 'El Palo', 'Oklahoma City', 'Kansas City', 'Saint Louis',
              'Nashville', 'Raleigh', 'Little Rock', 'Alanta', 'Charleston', 'Miami', 'Dallas',
              'Houston', 'New Orleans', 'Miami']

    fill_in_color = {
        city: {other_city: [('no_Connection', 0)] for other_city in cities} for city in cities
    }

    # Create the DataFrame
    board = pd.DataFrame(fill_in_color)

    # Optionally, fill in some example counts and colors
    board.loc['Helena', 'Winnipeg'] = [('blue', 4)]
    board.loc['Winnipeg', 'Helena'] = [('blue', 4)]
    board.loc['Helena', 'Calgary'] = [('any', 4)]
    board.loc['Calgary', 'Helena'] = [('any', 4)]
    board.loc['Seattle', 'Helena'] = [('yellow', 6)]
    board.loc['Helena', 'Seattle'] = [('yellow', 6)]
    board.loc['Helena', 'Duluth'] = [('orange', 6)]
    board.loc['Duluth', 'Helena'] = [('orange', 6)]
    board.loc['Helena', 'Omaha'] = [('red', 5)]
    board.loc['Omaha', 'Helena'] = [('red', 5)]
    board.loc['Helena', 'Salt Lake City'] = [('pink', 3)]
    board.loc['Salt Lake City', 'Helena'] = [('pink', 3)]
    board.loc['Vancouver', 'Calgary'] = [('any', 3)]
    board.loc['Calgary', 'Vancouver'] = [('any', 3)]
    board.loc['Vancouver', 'Seattle'] = [('any', 1)]
    board.loc['Seattle', 'Portland'] = [('any', 1)]
    board.loc['Portland', 'Seattle'] = [('any', 1)]
    board.loc['Seattle', 'Calgary'] = [('any', 4)]
    board.loc['Calgary', 'Seattle'] = [('any', 4)]
    board.loc['Calgary', 'Winnipeg'] = [('white', 6)]
    board.loc['Winnipeg', 'Calgary'] = [('white', 6)]
    board.loc['Winnipeg', 'Duluth'] = [('black', 5)]
    board.loc['Duluth', 'Winnipeg'] = [('black', 5)]
    board.loc['Winnipeg', 'Sault St. Marie'] = [('any', 6)]
    board.loc['Sault St. Marie', 'Winnipeg'] = [('any', 6)]
    board.loc['Sault St. Marie', 'Montreal'] = [('black', 5)]
    board.loc['Montreal', 'Sault St. Marie'] = [('black', 5)]
    board.loc['Sault St. Marie', 'Toronto'] = [('any', 2)]
    board.loc['Toronto', 'Sault St. Marie'] = [('any', 2)]
    board.loc['Sault St. Marie', 'Duluth'] = [('any', 3)]
    board.loc['Duluth', 'Sault St. Marie'] = [('any', 3)]
    board.loc['Duluth', 'Omaha'] = [('any', 2)]
    board.loc['Omaha', 'Duluth'] = [('any', 2)]
    board.loc['Duluth', 'Chicago'] = [('red', 3)]
    board.loc['Chicago', 'Duluth'] = [('red', 3)]
    board.loc['Duluth', 'Toronto'] = [('pink', 6)]
    board.loc['Toronto', 'Duluth'] = [('pink', 6)]
    board.loc['Toronto', 'Montreal'] = [('any', 3)]
    board.loc['Montreal', 'Toronto'] = [('any', 3)]
    board.loc['Toronto', 'Chicago'] = [('white', 4)]
    board.loc['Chicago', 'Toronto'] = [('white', 4)]
    board.loc['Toronto', 'Pittsburgh'] = [('any', 2)]
    board.loc['Pittsburgh', 'Toronto'] = [('any', 2)]
    board.loc['Montreal', 'Boston'] = [('any', 2), ('any', 2)]
    board.loc['Boston', 'Montreal'] = [('any', 2), ('any', 2)]
    board.loc['Montreal', 'New York'] = [('blue', 3)]
    board.loc['New York', 'Montreal'] = [('blue', 3)]
    board.loc['Boston', 'New York'] = [('yellow', 2), ('red', 2)]
    board.loc['New York', 'Boston'] = [('yellow', 2), ('red', 2)]
    board.loc['New York', 'Pittsburgh'] = [('white', 2), ('green', 2)]
    board.loc['Pittsburgh', 'New York'] = [('white', 2), ('green', 2)]
    board.loc['New York', 'Washington DC'] = [('orange', 2), ('black', 2)]
    board.loc['Washington DC', 'New York'] = [('orange', 2), ('black', 2)]
    board.loc['Pittsburgh', 'Washington DC'] = [('any', 2)]
    board.loc['Washington DC', 'Pittsburgh'] = [('any', 2)]
    board.loc['Pittsburgh', 'Raleigh'] = [('any', 2)]
    board.loc['Raleigh', 'Pittsburgh'] = [('any', 2)]
    board.loc['Pittsburgh', 'Nashville'] = [('yellow', 4)]
    board.loc['Nashville', 'Pittsburgh'] = [('yellow', 4)]
    board.loc['Pittsburgh', 'Saint Louis'] = [('green', 5)]
    board.loc['Saint Louis', 'Pittsburgh'] = [('green', 5)]
    board.loc['Pittsburgh', 'Chicago'] = [('orange', 3), ('black', 3)]
    board.loc['Chicago', 'Pittsburgh'] = [('orange', 3), ('black', 3)]
    board.loc['Chicago', 'Saint Louis'] = [('white', 2), ('green', 2)]
    board.loc['Saint Louis', 'Chicago'] = [('white', 2), ('green', 2)]
    board.loc['Chicago', 'Omaha'] = [('blue', 4)]
    board.loc['Omaha', 'Chicago'] = [('blue', 4)]
    board.loc['Omaha', 'Kansas City'] = [('any', 1), ('any', 1)]
    board.loc['Kansas City', 'Omaha'] = [('any', 1), ('any', 1)]
    board.loc['Omaha', 'Denver'] = [('pink', 4)]
    board.loc['Denver', 'Omaha'] = [('pink', 4)]
    board.loc['Denver', 'Kansas City'] = [('orange', 4), ('black', 4)]
    board.loc['Kansas City', 'Denver'] = [('orange', 4), ('black', 4)]
    board.loc['Denver', 'Oklahoma City'] = [('red', 4)]
    board.loc['Oklahoma City', 'Denver'] = [('red', 4)]
    board.loc['Denver', 'Sante Fe'] = [('any', 2)]
    board.loc['Sante Fe', 'Denver'] = [('any', 2)]
    board.loc['Denver', 'Phoenix'] = [('white', 2)]
    board.loc['Phoenix', 'Denver'] = [('white', 2)]
    board.loc['Denver', 'Salt Lake City'] = [('red', 3), ('yellow', 3)]
    board.loc['Salt Lake City', 'Denver'] = [('red', 3), ('yellow', 3)]
    board.loc['Salt Lake City', 'Portland'] = [('blue', 6)]
    board.loc['Portland', 'Salt Lake City'] = [('blue', 6)]
    board.loc['Salt Lake City', 'Las Vegas'] = [('orange', 3)]
    board.loc['Las Vegas', 'Salt Lake City'] = [('orange', 3)]
    board.loc['Salt Lake City', 'San Francesco'] = [('orange', 5), ('white', 5)]
    board.loc['San Francesco', 'Salt Lake City'] = [('orange', 5), ('white', 5)]
    board.loc['Portland', 'San Francesco'] = [('pink', 5), ('green', 5)]
    board.loc['San Francesco', 'Portland'] = [('pink', 5), ('green', 5)]
    board.loc['Washington DC', 'Raleigh'] = [('any', 2), ('any', 2)]
    board.loc['Raleigh', 'Washington DC'] = [('any', 2), ('any', 2)]
    board.loc['San Francesco', 'Los Angeles'] = [('pink', 3), ('yellow', 3)]
    board.loc['Los Angeles', 'San Francesco'] = [('pink', 3), ('yellow', 3)]
    board.loc['Los Angeles', 'Las Vegas'] = [('any', 2)]
    board.loc['Las Vegas', 'Los Angeles'] = [('any', 2)]
    board.loc['Los Angeles', 'Phoenix'] = [('any', 2)]
    board.loc['Phoenix', 'Los Angeles'] = [('any', 2)]
    board.loc['Los Angeles', 'El Palo'] = [('black', 6)]
    board.loc['El Palo', 'Los Angeles'] = [('black', 6)]
    board.loc['Phoenix', 'El Palo'] = [('any', 3)]
    board.loc['El Palo', 'Phoenix'] = [('any', 3)]
    board.loc['Phoenix', 'Sante Fe'] = [('any', 3)]
    board.loc['Sante Fe', 'Phoenix'] = [('any', 3)]
    board.loc['Sante Fe', 'Oklahoma City'] = [('blue', 3)]
    board.loc['Oklahoma City', 'Sante Fe'] = [('blue', 3)]
    board.loc['Sante Fe', 'El Palo'] = [('any', 2)]
    board.loc['El Palo', 'Sante Fe'] = [('any', 2)]
    board.loc['Oklahoma City', 'El Palo'] = [('yellow', 6)]
    board.loc['El Palo', 'Oklahoma City'] = [('yellow', 6)]
    board.loc['Oklahoma City', 'Dallas'] = [('any', 2), ('any', 2)]
    board.loc['Dallas', 'Oklahoma City'] = [('any', 2), ('any', 2)]
    board.loc['Oklahoma City', 'Little Rock'] = [('any', 2)]
    board.loc['Little Rock', 'Oklahoma City'] = [('any', 2)]
    board.loc['Oklahoma City', 'Kansas City'] = [('any', 2), ('any', 2)]
    board.loc['Kansas City', 'Oklahoma City'] = [('any', 2), ('any', 2)]
    board.loc['Kansas City', 'Saint Louis'] = [('blue', 2), ('pink', 2)]
    board.loc['Omaha', 'Kansas City'] = [('any', 1)]
    board.loc['Kansas City', 'Omaha'] = [('any', 1)]
    board.loc['Saint Louis', 'Kansas City'] = [('blue', 2), ('pink', 2)]
    board.loc['Saint Louis', 'Little Rock'] = [('any', 2)]
    board.loc['Little Rock', 'Saint Louis'] = [('any', 2)]
    board.loc['Saint Louis', 'Nashville'] = [('any', 2)]
    board.loc['Nashville', 'Saint Louis'] = [('any', 2)]
    board.loc['Nashville', 'Little Rock'] = [('white', 3)]
    board.loc['Little Rock', 'Nashville'] = [('white', 3)]
    board.loc['Nashville', 'Alanta'] = [('any', 1)]
    board.loc['Alanta', 'Nashville'] = [('any', 1)]
    board.loc['Nashville', 'Raleigh'] = [('black', 3)]
    board.loc['Raleigh', 'Nashville'] = [('black', 3)]
    board.loc['Raleigh', 'Charleston'] = [('any', 2)]
    board.loc['Charleston', 'Raleigh'] = [('any', 2)]
    board.loc['Raleigh', 'Alanta'] = [('any', 2), ('any', 2)]
    board.loc['Alanta', 'Raleigh'] = [('any', 2), ('any', 2)]
    board.loc['Charleston', 'Miami'] = [('pink', 4)]
    board.loc['Miami', 'Charleston'] = [('pink', 4)]
    board.loc['Alanta', 'Charleston'] = [('any', 2)]
    board.loc['Charleston', 'Alanta'] = [('any', 2)]
    board.loc['Alanta', 'Miami'] = [('blue', 5)]
    board.loc['Miami', 'Alanta'] = [('blue', 5)]
    board.loc['New Orleans', 'Alanta'] = [('yellow', 4), ('orange', 4)]
    board.loc['Alanta', 'New Orleans'] = [('yellow', 4), ('orange', 4)]
    board.loc['Little Rock', 'Dallas'] = [('any', 2)]
    board.loc['Dallas', 'Little Rock'] = [('any', 2)]
    board.loc['New Orleans', 'Miami'] = [('red', 6)]
    board.loc['Miami', 'New Orleans'] = [('red', 6)]
    board.loc['New Orleans', 'Houston'] = [('any', 2)]
    board.loc['Houston', 'New Orleans'] = [('any', 2)]
    board.loc['Houston', 'Dallas'] = [('any', 1)]
    board.loc['Dallas', 'Houston'] = [('any', 1)]
    board.loc['Dallas', 'El Palo'] = [('red', 4)]
    board.loc['El Palo', 'Dallas'] = [('red', 4)]
    board.loc['El Palo', 'Houston'] = [('green', 6)]
    board.loc['Houston', 'El Palo'] = [('green', 6)]

    # print(board)
    return board


def Test_Board():
    # Define the list of cities
    cities = ['Helena', 'Winnipeg', 'Calgary', 'Seattle']

    fill_in_color = {
        city: {other_city: [('no_Connection', 0)] for other_city in cities} for city in cities
    }

    # Create the DataFrame
    board = pd.DataFrame(fill_in_color)

    # Optionally, fill in some example counts and colors
    board.loc['Helena', 'Winnipeg'] = [('blue', 4)]
    board.loc['Winnipeg', 'Helena'] = [('blue', 4)]
    board.loc['Helena', 'Calgary'] = [('any', 4)]
    board.loc['Calgary', 'Helena'] = [('any', 4)]
    board.loc['Seattle', 'Helena'] = [('yellow', 6)]
    board.loc['Helena', 'Seattle'] = [('yellow', 6)]
    board.loc['Calgary', 'Winnipeg'] = [('yellow', 20)]
    board.loc['Winnipeg', 'Calgary'] = [('yellow', 20)]

    print(board)
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
        {"city1": "Denver", "city2": "El Paso", "points": 4},
        {"city1": "Duluth", "city2": "El Paso", "points": 10},
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

    # Display the selected routes
    for route in city_pairs:
        print(f"{route['city1']} to {route['city2']} - Points For completing route: {route['points']}")

    return city_pairs


def Shortest_Path(board, routes):
    # points per track
    points_schema = {1: 1, 2: 3, 3: 4, 4: 7, 5: 10, 6: 15}
    # Define the list of cities test case
    # cities = ['Helena', 'Winnipeg', 'Calgary', 'Seattle']
    # Define the list of cities
    cities = ['Helena', 'Winnipeg', 'Calgary', 'Vancouver', 'Seattle', 'Portland', 'San Francesco',
              'Los Angeles', 'Salt Lake City', 'Sault St. Marie', 'Montreal', 'Toronto', 'Boston',
              'New York', 'Duluth', 'Pittsburgh', 'Chicago', 'Washington DC', 'Omaha', 'Denver',
              'Las Vegas', 'Phoenix', 'Sante Fe', 'El Palo', 'Oklahoma City', 'Kansas City', 'Saint Louis',
              'Nashville', 'Raleigh', 'Little Rock', 'Alanta', 'Charleston', 'Miami', 'Dallas',
              'Houston', 'New Orleans', 'Miami']

    start_node = routes["city1"]
    end_node = routes["city2"]

    # Initialize distance and points dictionaries with large values
    distances = {city: np.inf for city in cities}
    points = {city: 0 for city in cities}  # Initialize points for each city
    previous = {city: None for city in cities}  # To track the route
    distances[start_node] = 0

    # Initialize a priority queue (min-heap)
    priority_queue = [(0, start_node, 0)]  # (distance, city, accumulated_points)

    # Dijkstra's algorithm using the priority queue
    while priority_queue:
        current_distance, current_city, current_points = heapq.heappop(priority_queue)

        # If the current distance is greater than the stored distance, skip processing
        if current_distance > distances[current_city]:
            continue

        for neighbor in cities:
            # Retrieve connection color, distance, and points
            connection = board.loc[current_city, neighbor]
            if connection[0][1] > 0:  # Valid connection
                new_distance = current_distance + connection[0][1]
                earned_points = points_schema[connection[0][1]]  # Points earned for this track

                # Only update distance and points if we found a shorter path
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    points[neighbor] = current_points + earned_points  # Accumulate points
                    previous[neighbor] = current_city  # Track the route
                    heapq.heappush(priority_queue, (new_distance, neighbor, points[neighbor]))

    # Convert distances and points to a DataFrame for easy viewing
    distance_df = pd.DataFrame.from_dict(distances, orient='index', columns=['Distance_From_Start'])
    points_df = pd.DataFrame.from_dict(points, orient='index', columns=['Points_Earned'])

    # Merge distance and points data into one DataFrame
    result_df = pd.concat([distance_df, points_df], axis=1)
    print(result_df)

    # Reconstruct the shortest path
    path = []
    current = end_node
    while current is not None:
        path.append(current)
        current = previous[current]

    # Reverse the path to get it from start to end
    path.reverse()

    print("Optimal path from {} to {}:".format(start_node, end_node))
    print(" -> ".join(path))

    print("Total points earned for track: ", points_df.loc[end_node, 'Points_Earned'] + routes['points'])

    return result_df, path

def main():
    board = Creating_The_Board()
    routes = Get_City_Pairs(1)
    # test case simplified
    # board = Test_Board()
    # # Define a list to hold each route card with city pairs and points
    # routes = [
    #     {"city1": "Winnipeg", "city2": "Calgary", "points": 11}]
    for route in routes:
        Shortest_Path(board, route)
        


if __name__ == "__main__":
    main()
