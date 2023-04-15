class Grafo:

    # constructor
    def __init__(self):
        self.vertices = []
    
    # methods
    def add_vertice(self, key):
        if self.key_not_exists(key):
            vertice = Vertice(key, len(self.vertices))
            self.vertices.append(vertice)
            return vertice

        print(f'Key {key} already exists')
        return None

    def key_exists(self, key):
        for v in self.vertices:
            if v.key == key:
                return True
        
        return False

    def key_not_exists(self, key):
        return not self.key_exists(key)
    
    def get_vertice_by_key(self, key):

        for v in self.vertices:
            if v.key == key:
                return v

        print(f'Key {key} not found')
        return None

    def liga_vertices(self, key1, key2, weight=1):

        vertex1 = self.get_vertice_by_key(key1)
        vertex2 = self.get_vertice_by_key(key2)

        if vertex1 == None:
            print(f'Vertex {key1} not found')
        elif vertex2 == None:
            print(f'Vertex {key2} not found')
        else:
            self.vertices[vertex1.get_index()].add_point(key2, weight)
            self.vertices[vertex2.get_index()].add_point(key1, weight)
    

    def get_all_vertices(self):
        return self.vertices
    
    def str_all_vertices(self):
        vertices = []

        for v in self.vertices:
            vertices.append(v.__str__())

        return vertices

class Vertice:

    # constructor
    def __init__(self, key, index):
        self.key = key
        self.points_to = {}
        self._index = index

    # getters and setters
    def get_points(self):
        return list(self.points_to.keys())
    
    def get_key(self):
        return self.key

    def get_index(self):
        return self._index
    
    # methods
    def add_point(self, point, weight):
        self.points_to[point] = weight
    
    def __str__(self):
        return f'{self.key} - {self.points_to}'
    