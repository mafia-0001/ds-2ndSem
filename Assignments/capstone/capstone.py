class SocialNetwork:
    def __init__(self):
        self.users = {}          # user -> profile
        self.graph = {}          # adjacency list

    # ---------- PROFILE ----------
    def add_user(self, name, age, city):
        if name in self.users:
            print("User already exists")
            return
        self.users[name] = {"age": age, "city": city}
        self.graph[name] = []
        print("User added")

    def update_user(self, name, age=None, city=None):
        if name not in self.users:
            print("User not found")
            return
        if age:
            self.users[name]["age"] = age
        if city:
            self.users[name]["city"] = city
        print("Profile updated")

    def show_user(self, name):
        if name in self.users:
            print(name, ":", self.users[name])
        else:
            print("User not found")

    # ---------- GRAPH ----------
    def add_friend(self, u, v):
        if u not in self.graph or v not in self.graph:
            print("User missing")
            return
        if v not in self.graph[u]:
            self.graph[u].append(v)
            self.graph[v].append(u)
            print("Friend added")

    def remove_friend(self, u, v):
        if v in self.graph[u]:
            self.graph[u].remove(v)
            self.graph[v].remove(u)
            print("Friend removed")

    def show_friends(self, name):
        print("Friends of", name, ":", self.graph[name])

    # ---------- BFS (Shortest Path) ----------
    def shortest_path(self, start, end):
        if start not in self.graph or end not in self.graph:
            return "User not found"

        queue = [[start]]
        visited = set()

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node == end:
                return path

            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

        return "No connection"

    # ---------- DFS ----------
    def dfs_util(self, node, visited, depth, max_depth):
        if depth > max_depth:
            return
        print(node, end=" ")
        visited.add(node)

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited, depth+1, max_depth)

    def explore(self, start, depth):
        visited = set()
        print("DFS exploration:", end=" ")
        self.dfs_util(start, visited, 0, depth)
        print()

    # ---------- RECOMMENDATION ----------
    def recommend(self, user):
        suggestions = {}

        for friend in self.graph[user]:
            for foaf in self.graph[friend]:   # friend of friend
                if foaf != user and foaf not in self.graph[user]:
                    suggestions[foaf] = suggestions.get(foaf, 0) + 1

        sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)

        print("Recommendations:")
        for u, score in sorted_suggestions:
            print(u, " (common friends:", score, ")")

# ---------------- CLI ----------------
sn = SocialNetwork()

while True:
    print("\n1.Add User 2.Add Friend 3.Show Profile 4.Shortest Path")
    print("5.DFS Explore 6.Recommend 7.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        name = input("Name: ")
        age = int(input("Age: "))
        city = input("City: ")
        sn.add_user(name, age, city)

    elif ch == 2:
        u = input("User1: ")
        v = input("User2: ")
        sn.add_friend(u, v)

    elif ch == 3:
        name = input("Enter name: ")
        sn.show_user(name)

    elif ch == 4:
        u = input("Start: ")
        v = input("End: ")
        print("Path:", sn.shortest_path(u, v))

    elif ch == 5:
        u = input("Start: ")
        d = int(input("Depth: "))
        sn.explore(u, d)

    elif ch == 6:
        u = input("User: ")
        sn.recommend(u)

    elif ch == 7:
        break