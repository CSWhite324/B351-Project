class House:
    def __init__(self, node):
        self.address = node
        self.adj = {}

    def __str__(self):
        return str(self.address) + ' adjacent: ' + str([x.address for x in self.adj])

    def add_neighbor(self, neighbor, weight=0):
        self.adj[neighbor] = weight

    def get_connections(self):
        return self.adj.keys()  

    def get_address(self):
        return self.address

    def get_speed(self, neighbor):
        return self.adj[neighbor]

class Map:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_house(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = House(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_street(self, frm, to, highway, speed = 0):
        if frm not in self.vert_dict:
            self.add_house(frm)
        if to not in self.vert_dict:
            self.add_house(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], speed)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], speed)

    def get_vertices(self):
        return self.vert_dict.keys()

if __name__ == '__main__':

    g = Map()

    g.add_house('a')
    g.add_house('b')
    g.add_house('c')
    g.add_house('d')
    g.add_house('e')
    g.add_house('f')

    g.add_street('a', 'b', False, 7)  
    g.add_street('a', 'c', True, 9)
    g.add_street('a', 'f', False, 14)
    g.add_street('b', 'c', False, 10)
    g.add_street('b', 'd', False, 15)
    g.add_street('c', 'd', True, 11)
    g.add_street('c', 'f', False, 2)
    g.add_street('d', 'e', True, 6)
    g.add_street('e', 'f', False, 9)

    for v in g:
        for w in v.get_connections():
            vid = v.get_address()
            wid = w.get_address()
            print( '( %s , %s, %3d)'  % ( vid, wid, v.get_speed(w)))

    for v in g:
        print ('g.vert_dict[%s]=%s' %(v.get_address(), g.vert_dict[v.get_address()]))