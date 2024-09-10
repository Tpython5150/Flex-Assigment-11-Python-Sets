'''
Set Operation in Data Anaysis:  

Objective: 
The aim of this assignment is to enhance your skills in using Python sets for data analysis task. You will apply various set operations to handle real-world data scenarios, focusing on 
their practical application and efficiency.

Task 1 Duplicate Entries Clean up:
You are given a list of customer ID's, some of which are duplicated. Write a Python script to
remove duplicates and display the unique customer ID's.

Example Code:
'''
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

def display_all_ids(customer_ids):
  print("List of ID's:")
  for ids in customer_ids:
    print(f"- {ids}")

def remove_duplicates(customer_ids):
  unique_ids = list(set(customer_ids))
  return unique_ids

def display_unique_ids(customer_ids):
  unique_ids = remove_duplicates(customer_ids)
  print("Unique ID's: ")
  for ids in unique_ids:
    print(f"- {ids}")


while True:  
  print("Entries Clean Up:")
  print("\n1. Display all ID's ")
  print("2. Remove Duplicate ID's ")
  print("3. Display Unique ID's")
  print("4. Exit")
  choice = input("Enter your choice: ")

  if choice == '1':
    display_all_ids(customer_ids)
  elif choice == '2':
    remove_duplicates(customer_ids)
  elif choice == '3':
    display_unique_ids(customer_ids)
  elif choice == '4':
    break
  else:
    print("Invalid choice. Please try again.")  