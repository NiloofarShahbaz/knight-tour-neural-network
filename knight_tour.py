import numpy as np

KNIGHT_MOVES = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]


class KnightTour:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = []
        for i in range(self.board_size[0]):
            temp = []
            for j in range(self.board_size[1]):
                temp.append(set())
            self.board.append(temp)
        self.neuron_vertices = []
        self.neuron_outputs = np.array([])
        self.neuron_states = np.array([])
        self.neuron_neighbours = []
        # print('------first-------')
        # self.print_board(self.board)

        self.init()

    def print_board(self, board):
        if len(board) == self.board_size[0]:
            for i in range(self.board_size[0]):
                print(board[i])
        else:
            m = 0
            strin = ''
            for i in range(0, len(board), 6):
                print(board[i: i+6])

    def init(self):
        neuron_num = 0
        for x1 in range(self.board_size[0]):
            for y1 in range(self.board_size[1]):
                # print('(x1, y1) = ',(x1, y1))
                i = x1 * self.board_size[1] + y1

                for (x2, y2) in self.find_neighbours((x1, y1)):
                    # print('(x2, y2) = ',(x2,y2))
                    j = x2 * self.board_size[1] + y2

                    if j > i:
                        self.board[x1][y1].add(neuron_num)
                        self.board[x2][y2].add(neuron_num)
                        # print('neuron Num = ', neuron_num)
                        self.neuron_vertices.append({(x1, y1), (x2, y2)})
                        neuron_num += 1
        # # exit()
        # print("----init-----")
        # print('board')
        # self.print_board(self.board)
        # print('vertices')
        # self.print_board(self.neuron_vertices)

        for i in range(len(self.neuron_vertices)):
            vertex1, vertex2 = self.neuron_vertices[i]
            neighbours = self.board[vertex1[0]][vertex1[1]].union(self.board[vertex2[0]][vertex2[1]]) - {i}
            self.neuron_neighbours.append(neighbours)

        # print('neighbours')
        # self.print_board(self.neuron_neighbours)

    def initialize_neurons(self):
        self.neuron_outputs = np.random.randint(2, size=(len(self.neuron_vertices)), dtype=np.int16)
        self.neuron_states = np.zeros((len(self.neuron_vertices)), dtype=np.int16)
        # print('states:')
        # print(self.neuron_states)
        # print('outputs')
        # print(self.neuron_outputs)

    def update_neurons(self):
        sum_of_neighbours = np.zeros((len(self.neuron_states)), dtype=np.int16)
        for i in range(len(self.neuron_neighbours)):
            sum_of_neighbours[i] = self.neuron_outputs[list(self.neuron_neighbours[i])].sum()

        next_state = self.neuron_states + 4 - sum_of_neighbours - self.neuron_outputs
        number_of_changes = np.count_nonzero(next_state != self.neuron_states)
        self.neuron_outputs[np.argwhere(next_state < 0).ravel()] = 0
        self.neuron_outputs[np.argwhere(next_state > 3).ravel()] = 1
        self.neuron_states = next_state
        number_of_active = len(self.neuron_outputs[self.neuron_outputs == 1])
        # print('____________________update________________________')
        # print('states:')
        # print(self.neuron_states)
        # print('output')
        # print(self.neuron_outputs)

        return number_of_active, number_of_changes

    def neural_network(self):
        even = False
        time = 0
        while True:
            print('_________initalize_neurons__________________________')
            self.initialize_neurons()
            n = 0
            while True:
                num_of_active, num_of_changes = self.update_neurons()
                print('__________________info__________________________')
                print('active', num_of_active, 'changes', num_of_changes)
                if num_of_changes == 0:
                    exit()
                    break
                if self.check_degree():
                    even = True
                    print('okay?')
                    break
                n += 1
                if n == 20:
                    break
            time += 1
            if even:
                if self.check_connected_components():
                    print('solution found!!')
                    return
                else:
                    even = False

    def check_connected_components(self):
        active_neuron_indices = np.argwhere(self.neuron_outputs == 1).ravel()
        connected = self.dfs_through_neurons(neuron=active_neuron_indices[0], active_neurons=active_neuron_indices)
        if connected:
            return True
        return False

    def dfs_through_neurons(self, neuron, active_neurons):
        active_neurons = np.setdiff1d(active_neurons, [neuron])
        active_neighbours = np.intersect1d(active_neurons, list(self.neuron_neighbours[neuron]))
        if len(active_neighbours) is 0:
            if len(active_neurons) is 0:
                return True
            else:
                return False
        return self.dfs_through_neurons(neuron=active_neighbours[0], active_neurons=active_neurons)

    def get_active_neurons_vertices(self):
        active_neuron_indices = np.argwhere(self.neuron_outputs == 1).ravel()
        active_neuron_vertices = []
        for i in active_neuron_indices:
            active_neuron_vertices.append(self.neuron_vertices[i])
        return active_neuron_vertices

    def check_degree(self):
        active_neuron_indices = np.argwhere(self.neuron_outputs == 1).ravel()
        degree = np.zeros((self.board_size[0], self.board_size[1]), dtype=np.int16)

        for i in active_neuron_indices:
            vertex1, vertex2 = self.neuron_vertices[i]
            degree[vertex1[0]][vertex1[1]] += 1
            degree[vertex2[0]][vertex2[1]] += 1
        # print('____________________check degree_______________________')
        # print(degree)
        if degree[degree != 2].size is 0:
            return True
        return False

    def find_neighbours(self, pos):
        neighbours = set()
        for (dx, dy) in KNIGHT_MOVES:
            new_x, new_y = pos[0]+dx, pos[1]+dy
            if 0 <= new_x < self.board_size[0] and 0 <= new_y < self.board_size[1]:
                neighbours.add((new_x, new_y))
        return neighbours

#
# tour = KnightTour((6, 6))
# tour.neural_network()


