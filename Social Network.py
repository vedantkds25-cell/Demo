# =========================================================
# SOCIAL NETWORK FRIEND RECOMMENDATION SYSTEM
# Student: Vedant Khedkar (CD25060)
# Algorithm: Graph + BFS
# =========================================================

from collections import deque

# Store user names and friendship connections
users = {}
graph = {}


# =========================================================
# FUNCTION 1: ADD USER
# =========================================================

def add_user():

    user_id = input("Enter User ID: ").strip()
    user_name = input("Enter User Name: ").strip()

    # Check empty input
    if user_id == "" or user_name == "":
        print("User ID and name cannot be empty!")
        return

    # Check duplicate user
    if user_id in users:
        print("User already exists!")
        return

    # Add user
    users[user_id] = user_name
    graph[user_id] = []

    print("User added successfully!")


# =========================================================
# FUNCTION 2: ADD FRIENDSHIP
# =========================================================

def add_friendship():

    user1 = input("Enter User ID 1: ").strip()
    user2 = input("Enter User ID 2: ").strip()

    # Check whether users exist
    if user1 not in users or user2 not in users:
        print("Invalid User ID!")
        return

    # Same user condition
    if user1 == user2:
        print("A user cannot be friends with himself!")
        return

    # Check duplicate friendship
    if user2 in graph[user1]:
        print("Friendship already exists!")
        return

    # Add friendship in both directions
    graph[user1].append(user2)
    graph[user2].append(user1)

    print("Friendship added successfully!")


# =========================================================
# FUNCTION 3: BFS FRIEND RECOMMENDATION
# =========================================================

def get_recommendations():

    user_id = input("Enter User ID: ").strip()

    # Check user
    if user_id not in users:
        print("User not found!")
        return

    # Store direct friends
    direct_friends = set(graph[user_id])

    # Create BFS queue
    queue = deque([user_id])

    # Mark starting user as visited
    visited = {user_id}

    # Store recommendation candidates
    candidates = set()

    # BFS traversal
    while queue:

        current = queue.popleft()

        # Visit connected friends
        for friend in graph[current]:

            if friend not in visited:
                visited.add(friend)
                queue.append(friend)

            # Ignore the selected user
            if friend == user_id:
                continue

            # Ignore direct friends
            if friend in direct_friends:
                continue

            # Store potential recommendation
            candidates.add(friend)

    # Calculate mutual friends and scores
    recommendations = []

    for candidate in candidates:

        # Find common friends
        mutual_friends = (
            set(graph[user_id]) &
            set(graph[candidate])
        )

        score = len(mutual_friends)

        # Recommend only users with mutual friends
        if score > 0:
            recommendations.append(
                (candidate, score, mutual_friends)
            )

    # Sort by highest mutual-friend count
    recommendations.sort(
        key=lambda item: (-item[1], item[0])
    )

    # Display recommendations
    print("\n================================")
    print("     FRIEND RECOMMENDATIONS")
    print("================================")

    print("Selected User:", users[user_id])

    if not recommendations:
        print("No recommendations available.")
        return

    rank = 1

    for friend_id, count, mutual in recommendations:

        print("\nRank:", rank)
        print("Name:", users[friend_id])
        print("User ID:", friend_id)
        print("Mutual Friends:", count)

        print("Common Friends:")

        for mutual_id in sorted(mutual):
            print("-", users[mutual_id])

        rank += 1


# =========================================================
# FUNCTION 4: DISPLAY NETWORK
# =========================================================

def display_network():

    print("\n================================")
    print("       NETWORK OVERVIEW")
    print("================================")

    print("Total Users:", len(users))

    # Count all friendship connections
    total = 0

    for user_id in graph:
        total += len(graph[user_id])

    # Each friendship appears twice
    total = total // 2

    print("Total Friendships:", total)

    print("\nUsers and Their Friends:")

    if not users:
        print("No users available.")
        return

    for user_id in users:

        print("\nUser:", users[user_id], "(" + user_id + ")")

        if not graph[user_id]:
            print("No friends.")
        else:
            for friend in graph[user_id]:
                print("->", users[friend], "(" + friend + ")")


# =========================================================
# FUNCTION 5: DISPLAY ALL USERS
# =========================================================

def display_users():

    print("\n================================")
    print("            ALL USERS")
    print("================================")

    if not users:
        print("No users available.")
        return

    for user_id, user_name in users.items():
        print(user_id, "-", user_name)


# =========================================================
# FUNCTION 6: SHOW DIRECT FRIENDS
# =========================================================

def show_friends():

    user_id = input("Enter User ID: ").strip()

    # Check user
    if user_id not in users:
        print("User not found!")
        return

    print("\nDirect Friends of", users[user_id])

    friends = graph[user_id]

    if not friends:
        print("No direct friends.")
        return

    for friend in friends:
        print("->", users[friend], "(" + friend + ")")


# =========================================================
# FUNCTION 7: ADD SAMPLE DATA
# =========================================================

def add_sample_data():

    sample_users = {
        "U001": "Vedant",
        "U002": "Alice",
        "U003": "Charlie",
        "U004": "Bob",
        "U005": "Diana"
    }

    sample_graph = {
        "U001": ["U002", "U004"],
        "U002": ["U001", "U003", "U005"],
        "U003": ["U002", "U004", "U005"],
        "U004": ["U001", "U003"],
        "U005": ["U002", "U003"]
    }

    # Avoid overwriting existing users
    if any(uid in users for uid in sample_users):
        print("Some sample users already exist!")
        print("Add sample data only once.")
        return

    # Add sample users and connections
    users.update(sample_users)
    graph.update(sample_graph)

    print("Sample data added successfully!")


# =========================================================
# FUNCTION 8: BFS TRAVERSAL DISPLAY
# =========================================================

def show_bfs():

    user_id = input("Enter User ID: ").strip()

    # Check user
    if user_id not in users:
        print("User not found!")
        return

    queue = deque([user_id])
    visited = {user_id}
    order = []

    # Perform BFS
    while queue:

        current = queue.popleft()
        order.append(current)

        for friend in graph[current]:

            if friend not in visited:
                visited.add(friend)
                queue.append(friend)

    print("\nBFS Traversal:")

    for user in order:
        print(users[user], "(" + user + ")")


# =========================================================
# MAIN MENU
# =========================================================

def main():

    while True:

        print("\n==========================================")
        print(" SOCIAL NETWORK FRIEND RECOMMENDATION")
        print("==========================================")

        print("1. Add User")
        print("2. Add Friendship")
        print("3. Get Recommendations")
        print("4. Display Network")
        print("5. Display All Users")
        print("6. Show Direct Friends")
        print("7. Add Sample Data")
        print("8. Show BFS Traversal")
        print("9. Exit")

        print("==========================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_user()

        elif choice == "2":
            add_friendship()

        elif choice == "3":
            get_recommendations()

        elif choice == "4":
            display_network()

        elif choice == "5":
            display_users()

        elif choice == "6":
            show_friends()

        elif choice == "7":
            add_sample_data()

        elif choice == "8":
            show_bfs()

        elif choice == "9":
            print("\nThank you!")
            print("Program ended.")
            break

        else:
            print("\nInvalid choice!")
            print("Please enter a number from 1 to 9.")


# =========================================================
# PROGRAM START
# =========================================================

if __name__ == "__main__":
    main()
