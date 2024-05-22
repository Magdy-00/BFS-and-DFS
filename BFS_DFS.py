class Graph:
    # constractor
    def __init__(self):
        # using dictionary to add key(node) and value (edges)
        self.graph = {}

    def addEdge(self, n, v):
        # make it the first element in the graph
        if n not in self.graph:
            self.graph[n] = [v]
        else:
            # add to the last of the list
            self.graph[n].append(v)

    def BFS(self, s):
        # BFS implements queue data structre FIFO order

        # adds the first elemnt to the queue
        que = [s]
        # mark the nodes to be not visited at first
        visited = [False] * len(self.graph)
        # mark the first node as visited
        visited[s] = True

        while len(que) > 0:
            # pop the first element and print it
            s = que.pop(0)
            print(s)

            # this for loop to add the childern of the poped node
            for node in self.graph[s]:
                # if the node is not visited
                if visited[node] == False:
                    que.append(node)
                    # mark the node as visited
                    visited[node] = True

    def DFS(self, s):
        # DFS implements stack data structre LIFO order

        # adds the first elemnt to the queue
        stk = [s]
        # mark the nodes to be not visited at first
        visited = [False] * len(self.graph)
        # mark the first node as visited
        visited[s] = True

        while len(stk) > 0:
            # pop the last element and print it
            s = stk.pop()
            print(s)

            # this for loop to add the childern of the poped node
            for node in self.graph[s]:
                # if the node is not visited
                if visited[node] == False:
                    stk.append(node)
                    # mark the node as visited
                    visited[node] = True

    def BFS_Search(self, s, target):
        # BFS implements queue data structure FIFO order

        # Initialize the queue with the first element
        queue = [s]
        # Initialize the visited list for all nodes
        visited = [False] * len(self.graph)
        # Mark the first node as visited
        visited[s] = True

        while queue:
            # Pop the first element
            s = queue.pop(0)
            if s == target:
                print('True')

            # This for loop adds the children of the popped node to the queue
            for node in self.graph[s]:
                # If the node is not visited
                if not visited[node]:
                    queue.append(node)
                    # Mark the node as visited
                    visited[node] = True

        return False

    def DFS_Search(self, s, target):
        # DFS implements stack data structure LIFO order

        # Initialize the stack with the first element
        stack = [s]
        # Initialize the visited list for all nodes
        visited = [False] * len(self.graph)
        # Mark the first node as visited
        visited[s] = True

        while stack:
            # Pop the last element
            s = stack.pop()
            if s == target:
                print('True')

            # This for loop adds the children of the popped node to the stack
            for node in self.graph[s]:
                # If the node is not visited
                if not visited[node]:
                    stack.append(node)
                    # Mark the node as visited
                    visited[node] = True

        return False


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(1, 4)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(4, 0)
g.addEdge(5, 2)

g.BFS_Search(0, 5)
g.DFS_Search(0, 5)
