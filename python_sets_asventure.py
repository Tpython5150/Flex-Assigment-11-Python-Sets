'''
Python Sets Adventure:  Task 1 Flight Route Comparison

Imagine you work for an irline and need to compare the flight routes of your airline with a 
competitor.  You have two sets of flight destinations, one for each airline. Write a Python 
program to find out:


1. Destinations that both fly to.

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

same_routes = our_routes.intersection(competitor_routes)
print(same_routes)



2. Destinations unique to your airline.


unique_routes = our_routes.difference(competitor_routes)
print(unique_routes)




3. Whether there are any destinations that neither airline shares.


no_routes_in_common = our_routes.symmetric_difference(competitor_routes)
print(neither_airline_shares)
'''
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}


def same_routes(our_routes, competitor_routes):
  same_routes = our_routes.intersection(competitor_routes)
  print(same_routes)

def unique_routes(our_routes, competitor_routes):
  unique_routes = our_routes.difference(competitor_routes)
  print(unique_routes)

def no_routes_in_common(our_routes, competitor_routes):
  no_routes_in_common = our_routes.symmetric_difference(competitor_routes)
  print(no_routes_in_common)
  


while True:  
  print(f"Ours vs. Competitors Routes")
  print("\n1. Destination both airlines fly to: ")
  print("2. Destination unique to our airline: ")
  print("3. No common Routes: ")
  print("4. Exit")
  choice = input("Enter your choice: ")
  
  if choice == '1':
    same_routes(our_routes, competitor_routes)
  elif choice == '2':
    unique_routes(our_routes, competitor_routes)
  elif choice == '3':
    no_routes_in_common(our_routes, competitor_routes)
  elif choice == '4':
    break
  else:
    print("Invalid choice. Please try again.")
  