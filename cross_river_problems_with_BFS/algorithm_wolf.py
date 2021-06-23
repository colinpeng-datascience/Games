# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 01:17:48 2021

@author: YiWei
"""


class State :
    def __init__(self, location_man,location_wolf, location_sheep, location_cabbage, parent):
        self.man = location_man
        self.wolf = location_wolf
        self.sheep = location_sheep
        self.cabbage = location_cabbage
        self.parent = parent
        
    def is_valid(self):
        goat_eats_cabbage = (self.sheep == self.cabbage and self.man != self.sheep)
        wolf_eats_goat = (self.wolf == self.sheep and self.man != self.wolf)
        invalid = goat_eats_cabbage or wolf_eats_goat
        
        return not invalid
    
    def is_goal(self):
        return (self.sheep == self.cabbage == self.wolf == self.man == 'B')
    
    def get_next(self):
        next_states = []
        if self.man == 'A':
            other_side = 'B'
        else :
            other_side = 'A'
            
        # move man
        moved_man = State(other_side,self.wolf,self.sheep,self.cabbage,self)
        if moved_man.is_valid():    
            next_states.append(moved_man)
        # move man and wolf
        if self.man == self.wolf:
            moved_wolf = State(other_side,other_side,self.sheep,self.cabbage,self)
            if moved_wolf.is_valid():
                next_states.append(moved_wolf)
        #move man and sheep
        if self.man == self.sheep:
            moved_sheep = State(other_side,self.wolf,other_side,self.cabbage,self)
            if moved_sheep.is_valid():
                next_states.append(moved_sheep)
        #move man and cabbage
        if self.man == self.cabbage:
            moved_cabbage = State(other_side,self.wolf,self.sheep,other_side,self)
            if moved_cabbage.is_valid():
                next_states.append(moved_cabbage)
                
        return next_states
    
    def __eq__(self, other):
        return self.sheep == other.sheep and self.wolf == other.wolf and self.cabbage == other.cabbage and self.man == other.man
    
    def __hash__(self):
        return hash(self.man + self.wolf + self.sheep + self.cabbage)
    
    def __str__(self):
        a_side = ""
        b_side = ""
        
        if self.man == 'A':
            a_side  = a_side + " man "
        else:
            b_side = b_side + " man "
            
        if self.wolf == 'A':
            a_side  = a_side + " wolf "
        else:
            b_side = b_side + " wolf "
            
        if self.sheep == 'A':
            a_side  = a_side + " sheep "
        else:
            b_side = b_side + " sheep "
            
        if self.cabbage == 'A':
            a_side  = a_side + " cabbage "
        else:
            b_side = b_side + " cabbage "
            
        return '%30s ~~~ %s' % (a_side,b_side)
            
def breadth_first_search(start):
    queue = [start]
    discovered = set([start])
    
    while len(queue) != 0:
        this_state = queue.pop(0)

        if this_state.is_goal():
            path = []
            while this_state is not None:
                path.insert(0, this_state)
                this_state = this_state.parent
            return path

        for next_state in this_state.get_next():
            if next_state not in discovered:
                discovered.add(next_state)
                queue.append(next_state)
                
                




start = State('A','A','A','A',None)
path = breadth_first_search(start)

for this_state in path:
    print(str(this_state))
    