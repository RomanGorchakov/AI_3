#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.size = len(vertices)
        self.edges = [[None for _ in range(self.size)] for _ in range(self.size)]

    def add_edge(self, value1, value2, weight):
        row = self.vertices.index(value1)
        column = self.vertices.index(value2)
        
        self.edges[row][column] = weight
        self.edges[column][row] = weight

    def bfs(self, start, end):
        start_index = self.vertices.index(start)
        end_index = self.vertices.index(end)
        
        queue = [(start_index, [start_index])]
        visited = set()

        while queue:
            current_index, path = queue.pop(0)
            visited.add(current_index)

            if current_index == end_index:
                return [self.vertices[i] for i in path]

            for neighbor_index in range(self.size):
                if self.edges[current_index][neighbor_index] is not None and neighbor_index not in visited:
                    queue.append((neighbor_index, path + [neighbor_index]))

        return None

def dfs(self, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]

    if start == goal:
        return path
    
    for i in range(len(self.edges[self.vertices.index(start)])):
        weight = self.edges[self.vertices.index(start)][i]
        if weight is not None:
            neighbor = self.vertices[i]
            if neighbor not in path:
                new_path = self.dfs(neighbor, goal, path)
                if new_path:
                    return new_path
    return None

Graph.dfs = dfs

if __name__ == '__main__':
    graph = Graph(['Новоалександровск', 'Присадовый', 'Ударный', \
    'Краснодарский', 'Красночервонный', 'Южный', 'Расшеватская', \
    'Славенский', 'Озёрный', 'Темижбекский', 'Краснокубанский'])
    graph.add_edge('Новоалександровск', 'Присадовый', 10)
    graph.add_edge('Новоалександровск', 'Ударный', 15)
    graph.add_edge('Новоалександровск', 'Краснодарский', 13)
    graph.add_edge('Новоалександровск', 'Красночервонный', 11)
    graph.add_edge('Новоалександровск', 'Южный', 9)
    graph.add_edge('Новоалександровск', 'Расшеватская', 19)
    graph.add_edge('Присадовый', 'Новоалександровск', 10)
    graph.add_edge('Присадовый', 'Ударный', 5)
    graph.add_edge('Ударный', 'Новоалександровск', 15)
    graph.add_edge('Ударный', 'Присадовый', 5)
    graph.add_edge('Ударный', 'Краснодарский', 9)
    graph.add_edge('Краснодарский', 'Новоалександровск', 13)
    graph.add_edge('Краснодарский', 'Ударный', 9)
    graph.add_edge('Краснодарский', 'Красночервонный', 12)
    graph.add_edge('Красночервонный', 'Новоалександровск', 11)
    graph.add_edge('Красночервонный', 'Краснодарский', 12)
    graph.add_edge('Красночервонный', 'Южный', 12)
    graph.add_edge('Южный', 'Новоалександровск', 9)
    graph.add_edge('Южный', 'Красночервонный', 12)
    graph.add_edge('Южный', 'Расшеватская', 15)
    graph.add_edge('Южный', 'Славенский', 8)
    graph.add_edge('Южный', 'Темижбекский', 8)
    graph.add_edge('Расшеватская', 'Новоалександровск', 19)
    graph.add_edge('Расшеватская', 'Южный', 15)
    graph.add_edge('Расшеватская', 'Славенский', 16)
    graph.add_edge('Славенский', 'Южный', 8)
    graph.add_edge('Славенский', 'Расшеватская', 16)
    graph.add_edge('Славенский', 'Озёрный', 3)
    graph.add_edge('Славенский', 'Темижбекский', 13)
    graph.add_edge('Озёрный', 'Славенский', 3)
    graph.add_edge('Озёрный', 'Темижбекский', 5)
    graph.add_edge('Озёрный', 'Краснокубанский', 5)
    graph.add_edge('Темижбекский', 'Южный', 8)
    graph.add_edge('Темижбекский', 'Славенский', 13)
    graph.add_edge('Темижбекский', 'Озёрный', 5)
    graph.add_edge('Темижбекский', 'Краснокубанский', 5)
    graph.add_edge('Краснокубанский', 'Озёрный', 5)
    graph.add_edge('Краснокубанский', 'Темижбекский', 5)

    start_city = 'Новоалександровск'
    end_city = 'Озёрный'
    shortest_path = graph.dfs(start_city, end_city)

    if shortest_path:
        print("Кратчайший путь от", start_city, "до", end_city, ":", " -> ".join(shortest_path))
    else:
        print("Путь не найден.")