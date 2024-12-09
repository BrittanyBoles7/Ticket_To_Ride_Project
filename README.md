# Ticket_To_Ride_Project
This code simulates a simple case of ticket to ride comparing two different strategies. For the full report see: [CSCI_532___Final_Project___Ticket_to_Ride__Alg__Implementation](CSCI_532___Final_Project___Ticket_to_Ride__Alg__Implementation.pdf)
# Ticket_To_Ride_Simulation
This is where we did the simple case. It's just using Dijktras to calculate the shortest path between two cities on the board. 

# Two_Player_Version
This is where we made it more complex. It's two players against eachother using the fewest number of trains. It's one game, and we keep track of what cities each player is connecting, and the routes they complete. 
Each player has their own copy of the board, that we update each time a player makes a move, then recalculate the shortest path for both players for their route. If they complete the route we given them those points, or if they are unable to complete it, they loose those points. The game ends when a player runs out of trains, which we assign and keep track of. We also keep track of how many points each player gets for placing down their trains. 

# Two_Player_Version_Fewest_turns
This is where we had two different stratgeies compete against eachother, and kept track of who wins each time. We added a fewest_turns strategy, with the goal of finding the route that visits the feweset cities. We found with our assumptions that visting the fewest cities was the optimal strategy. 
