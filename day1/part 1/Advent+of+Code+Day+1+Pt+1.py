
# coding: utf-8

# In[82]:

# Advent of Code Day 1 Pt 1
#    Given a series of directions, find the taxi distance from the origin to the destination
#    This is defined as
#    for (p1, p2) and (q1, q2) d = |p1-q1| + |p2-q2| in a real vector space


# In[83]:

# Class definition
class EasterBunnyHQ:
    
    def __init__(self):
        # class variables
        self.direction_coords = []
        self.facing_direction = 'N'
        # Rules on how to modify tuples
        # Facing N/W:
        #    L = subtract
        #    R = add
        # Facing S/E:
        #    L = add
        #    R = subtract
        # Quadrants
        #    2 | 1
        #    -----
        #    3 | 4
        # as in standard geometry
        # move along a standard cartesian system
        
    def parse_input(self, input_string):
        """ look this was really lazy here """
        return input_string.split(', ')
    
    def calculate_tuples(self, given_directions):
        """ Establish a list of tuples representing coordinates
            that we can use to determine distance
        """
        for index in range(0, len(given_directions)):
            direction = given_directions[index]
            turn = direction[0]
            shift = int(direction[1:])
            if index > 0:
                prev_step = self.direction_coords[index - 1]
            else:
                prev_step = (0, 0)
            # Switch on current facing followed by shift direction
            if self.facing_direction == 'N':
                # shift old x
                new_y = prev_step[1]
                if turn == 'L':
                    new_x = prev_step[0] - shift
                    self.facing_direction = 'W'
                elif turn == 'R':
                    new_x = prev_step[0] + shift
                    self.facing_direction = 'E'
            elif self.facing_direction == 'E':
                # shift old y
                new_x = prev_step[0]
                if turn == 'L':
                    new_y = prev_step[1] + shift
                    self.facing_direction = 'N'
                elif turn == 'R':
                    new_y = prev_step[1] - shift
                    self.facing_direction = 'S'
            elif self.facing_direction == 'S':
                # shift old x
                new_y = prev_step[1]
                if turn == 'L':
                    new_x = prev_step[0] + shift
                    self.facing_direction = 'E'
                elif turn == 'R':
                    new_x = prev_step[0] - shift
                    self.facing_direction = 'W'
            elif self.facing_direction == 'W':
                # shift old y
                new_x = prev_step[0]
                if turn == 'L':
                    new_y = prev_step[1] - shift
                    self.facing_direction = 'S'
                elif turn == 'R':
                    new_y = prev_step[1] + shift
                    self.facing_direction = 'N'
            next_step = (new_x, new_y)
            self.direction_coords.append(next_step)
        return self.direction_coords
    
    def calculate_block_distance(self, coordinate_list):
        """ Distance from last point in the list to the origin """
        distance = abs(coordinate_list[-1][0] - 0) + abs(coordinate_list[-1][1] - 0)
        return distance


# In[84]:

obj = EasterBunnyHQ()
parsed = obj.parse_input('L1, L5, R1, R3, L4, L5, R5, R1, L2, L2, L3, R4, L2, R3, R1, L2, R5, R3, L4, R4, L3, R3, R3, L2, R1, L3, R2, L1, R4, L2, R4, L4, R5, L3, R1, R1, L1, L3, L2, R1, R3, R2, L1, R4, L4, R2, L189, L4, R5, R3, L1, R47, R4, R1, R3, L3, L3, L2, R70, L1, R4, R185, R5, L4, L5, R4, L1, L4, R5, L3, R2, R3, L5, L3, R5, L1, R5, L4, R1, R2, L2, L5, L2, R4, L3, R5, R1, L5, L4, L3, R4, L3, L4, L1, L5, L5, R5, L5, L2, L1, L2, L4, L1, L2, R3, R1, R1, L2, L5, R2, L3, L5, L4, L2, L1, L2, R3, L1, L4, R3, R3, L2, R5, L1, L3, L3, L3, L5, R5, R1, R2, L3, L2, R4, R1, R1, R3, R4, R3, L3, R3, L5, R2, L2, R4, R5, L4, L3, L1, L5, L1, R1, R2, L1, R3, R4, R5, R2, R3, L2, L1, L5')
coord_list = obj.calculate_tuples(parsed)
result = obj.calculate_block_distance(coord_list)
print('{0} blocks'.format(result))


# In[ ]:



