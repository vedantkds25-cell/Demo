# Personal Expense Tracker - Concise & Complete Implementation
# Student: Vedant Khedkar (CD25060) · Python Lab Assessment

from collections import deque


# =========================================================
# SOCIAL NETWORK FRIEND RECOMMENDATION SYSTEM
# Using Graph and Breadth First Search (BFS)
# =========================================================


# Dictionary to store users
users = {}


# Dictionary to store the graph
# Graph is represented using an adjacency list
graph = {}


# =========================================================
# FUNCTION 1: ADD USER
# =========================================================

def add_user():

    user_id = input("Enter User ID: ")
    user_name = input("Enter User Name: ")

    # Check duplicate user
    if user_id in users:
        print("User already exists!")
        return

    # Add user
    users[user_id] = user_name

    # Create empty friend list
    graph[user_id] = []

    print("User added successfully!")


# =========================================================
# FUNCTION 2: ADD FRIENDSHIP
# =========================================================

def add_friendship():

    user1 = input("Enter User ID 1: ")
    user2 = input("Enter User ID 2: ")

    # Check users
    if user1 not in users or user2 not in users:
        print("Invalid User ID!")
        return

    # Same user check
    if user1 == user2:
        print("A user cannot be friends with himself!")
        return

    # Duplicate friendship check
    if user2 in graph[user1]:
        print("Friendship already exists!")
        return

    # Add friendship
    graph[user1].append(user2)
    graph[user2].append(user1)

    print("Friendship added successfully!")


# =========================================================
# FUNCTION 3: BFS FRIEND RECOMMENDATION
# =========================================================

def get_recommendations():

    user_id = input("Enter User ID: ")

    # Check user
    if user_id not in users:
        print("User not found!")
        return

    # Direct friends
    direct_friends = set(graph[user_id])

    # Queue for BFS
    queue = deque()

    # Visited set
    visited = set()

    # Dictionary for mutual friends
    mutual = {}

    # Start BFS
    queue.append(user_id)
    visited.add(user_id)

    # BFS traversal
    while queue:

        current = queue.popleft()

        # Visit all friends
        for friend in graph[current]:

            # Add to queue if not visited
            if friend not in visited:

                visited.add(friend)
                queue.append(friend)

            # Ignore current user
            if friend == user_id:
                continue

            # Ignore direct friends
            if friend in direct_friends:
                continue

            # Count mutual friends
            if friend not in mutual:
                mutual[friend] = 1
            else:
                mutual[friend] += 1

    # Sort recommendations
    recommendations = sorted(
        mutual.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # Display recommendations
    print("\n================================")
    print(" FRIEND RECOMMENDATIONS")
    print("================================")

    print("Selected User:",
          users[user_id])

    if len(recommendations) == 0:

        print("No recommendations available.")

    else:

        rank = 1

        for friend_id, count in recommendations:

            print(
                rank,
                ".",
                users[friend_id],
                "(" + friend_id + ")",
                "- Mutual Friends:",
                count
            )

            rank += 1


# =========================================================
# FUNCTION 4: DISPLAY NETWORK
# =========================================================

def display_network():

    print("\n================================")
    print("       NETWORK OVERVIEW")
    print("================================")

    print("Total Users:", len(users))

    # Calculate total friendships
    total = 0

    for user in graph:
        total = total + len(graph[user])

    # Each friendship is counted twice
    total = total // 2

    print("Total Friendships:", total)

    print("\nUsers and their Friends:")

    for user_id in users:

        print("\nUser:",
              users[user_id],
              "(" + user_id + ")")

        if len(graph[user_id]) == 0:

            print("No friends")

        else:

            for friend in graph[user_id]:

                print(
                    " ->",
                    users[friend],
                    "(" + friend + ")"
                )


# =========================================================
# FUNCTION 5: DISPLAY USERS
# =========================================================

def display_users():

    print("\n================================")
    print("          ALL USERS")
    print("================================")

    if len(users) == 0:

        print("No users available.")

    else:

        for user_id in users:

            print(
                user_id,
                "-",
                users[user_id]
            )


# =========================================================
# FUNCTION 6: SHOW DIRECT FRIENDS
# =========================================================

def show_friends():

    user_id = input("Enter User ID: ")

    if user_id not in users:

        print("User not found!")
        return

    print("\nDirect Friends of",
          users[user_id])

    friends = graph[user_id]

    if len(friends) == 0:

        print("No direct friends.")

    else:

        for friend in friends:

            print(
                "->",
                users[friend],
                "(" + friend + ")"
            )


# =========================================================
# FUNCTION 7: ADD SAMPLE DATA
# =========================================================

def add_sample_data():

    users["U001"] = "Vedant"
    users["U002"] = "Alice"
    users["U003"] = "Charlie"
    users["U004"] = "Bob"
    users["U005"] = "Diana"

    graph["U001"] = ["U002", "U004"]
    graph["U002"] = ["U001", "U003", "U005"]
    graph["U003"] = ["U002", "U004", "U005"]
    graph["U004"] = ["U001", "U003"]
    graph["U005"] = ["U002", "U003"]

    print("Sample data added successfully!")


# =========================================================
# MAIN MENU
# =========================================================

while True:

    print("\n")
    print("==========================================")
    print("   SOCIAL NETWORK FRIEND RECOMMENDATION")
    print("==========================================")

    print("1. Add User")
    print("2. Add Friendship")
    print("3. Get Recommendations")
    print("4. Display Network")
    print("5. Display All Users")
    print("6. Show Direct Friends")
    print("7. Add Sample Data")
    print("8. Exit")

    print("==========================================")

    choice = input("Enter your choice: ")


    # OPTION 1
    if choice == "1":

        add_user()


    # OPTION 2
    elif choice == "2":

        add_friendship()


    # OPTION 3
    elif choice == "3":

        get_recommendations()


    # OPTION 4
    elif choice == "4":

        display_network()


    # OPTION 5
    elif choice == "5":

        display_users()


    # OPTION 6
    elif choice == "6":

        show_friends()


    # OPTION 7
    elif choice == "7":

        add_sample_data()


    # OPTION 8
    elif choice == "8":

        print("\nThank you!")
        print("Program ended.")

        break


    # INVALID CHOICE
    else:

        print("\nInvalid choice!")
        print("Please enter a number from 1 to 8.")