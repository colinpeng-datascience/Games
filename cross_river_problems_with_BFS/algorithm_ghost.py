# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 01:17:48 2021

@author: YiWei
"""


class State :
    def __init__(self, man, ghost ,boat_side,parent):
        self.man = man #[side0_man_count, side1_man_count]
        self.ghost = ghost
        self.boat_side = boat_side
        self.parent = parent
        
    def is_valid(self):
        side1_safe = (self.man[0]>=self.ghost[0] or self.man[0] == 0)
        side2_safe = (self.man[1]>=self.ghost[1] or self.man[1] == 0)
        return  side1_safe and side2_safe
    
    def is_goal(self):
        return (self.man[1] == self.ghost[1] == 3)
    
    def get_next(self):
        next_states = []
        if self.boat_side == 1:
            this_side = 1
            other_side = 0
        else :
            this_side = 0
            other_side = 1
            
        # move 1 man
        if self.man[this_side] >= 1:
            new_man = self.man.copy()
            new_man[this_side] -= 1
            new_man[other_side] += 1
            moved_man = State(new_man ,self.ghost,other_side,self)
            if moved_man.is_valid():
                next_states.append(moved_man)
                
        # move 2 man
        if self.man[this_side] >= 2:
            new_man = self.man.copy()
            new_man[this_side] -= 2
            new_man[other_side] += 2
            moved_man = State(new_man ,self.ghost,other_side,self)
            if moved_man.is_valid():
                next_states.append(moved_man)
                
        # move 1 ghost
        if self.ghost[this_side] >= 1:
            new_ghost = self.ghost.copy()
            new_ghost[this_side] -= 1
            new_ghost[other_side] += 1
            moved_ghost = State(self.man ,new_ghost,other_side,self)
            if moved_ghost.is_valid():
                next_states.append(moved_ghost)
        # move 2 ghost
        if self.ghost[this_side] >= 2:
            new_ghost = self.ghost.copy()
            new_ghost[this_side] -= 2
            new_ghost[other_side] += 2
            moved_ghost = State(self.man ,new_ghost,other_side,self)
            if moved_ghost.is_valid():
                next_states.append(moved_ghost)
        # move 1 man 1 ghost
        if self.man[this_side] >= 1 and self.ghost[this_side] >= 1:
            new_man = self.man.copy()
            new_man[this_side] -= 1
            new_man[other_side] += 1
            new_ghost = self.ghost.copy()
            new_ghost[this_side] -= 1
            new_ghost[other_side] += 1
            
            moved = State(new_man ,new_ghost,other_side,self)
            if moved.is_valid():
                next_states.append(moved)
                
        return next_states
    
    def __eq__(self, other):
        return self.man == other.man and self.ghost == other.ghost and self.boat_side == other.boat_side
    
    def __hash__(self):
        return hash(str(self))
    
    def __str__(self):
        side_0 = ""
        side_1 = ""
        
        
        if self.boat_side == 0:
            side_0  = side_0 + " boat "
        else:
            side_1 = side_1 + " boat "
            
        for man in range(self.man[0]):
            side_0 = side_0 + " man "
        for man in range(self.man[1]):
            side_1 = side_1 + " man "
            
        for ghost in range(self.ghost[0]):
            side_0 = side_0 + " ghost "
        for ghost in range(self.ghost[1]):
            side_1 = side_1 + " ghost "
            
        return '%40s ~~~ %s' % (side_0,side_1)
            
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
 
man = [3,0]
ghost = [3,0]

start = State(man,ghost,0,None)
path = breadth_first_search(start)

for this_state in path:
    print(str(this_state))
    