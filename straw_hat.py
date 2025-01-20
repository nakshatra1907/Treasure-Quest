'''
    This file contains the class definition for the StrawHat class.
'''

from crewmate import CrewMate
from heap import Heap
from treasure import Treasure
def comp1(c1,c2):
    if c1.total_time<c2.total_time:
        return True
    return False

def comp2(t1,t2):
    p1=t1.arrival_time+t1.rem_size
    p2=t2.arrival_time+t2.rem_size
    if p1<p2:
        return True
    elif p1==p2:
        if t1.id<t2.id:
            return True
    return False


class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        # Write your code here
        arr=[]
        for i in range(m):
            s=CrewMate()
            arr.append(s)
        
        self.crew=Heap(comp1,arr)
    

        pass
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        
        # Write your code here
        root=self.crew.extract()

        root.treasures.append(treasure)
        if root.total_time<treasure.arrival_time:
            root.total_time=treasure.arrival_time+treasure.size
        else:
            root.total_time+=treasure.size
        self.crew.insert(root)
        


        
        
        pass
    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        l=[]
        for i in self.crew.heap:
            finished_treasures=[]
            t_heap=Heap(comp2,[])
            for tre in i.treasures:
                tre_=Treasure(tre.id,tre.size,tre.arrival_time)
                d=tre_.arrival_time-i.prev_processed
                while t_heap.size():
                    root=t_heap.extract()
                    if root.rem_size>d:
                        root.rem_size-=d
                        t_heap.insert(root)
                        break
                    else:
                        d-=root.rem_size
                        root.completion_time=i.prev_processed+root.rem_size
                        i.prev_processed+=root.rem_size
                        finished_treasures.append(root)
                i.prev_processed=tre_.arrival_time
                t_heap.insert(tre_)
            while t_heap.size():
                root=t_heap.extract()
                root.completion_time=i.prev_processed+root.rem_size
                i.prev_processed+=root.rem_size
                finished_treasures.append(root)
            l.extend(finished_treasures)
        l.sort(key=lambda t:t.id)
        return l

                    
        
        
        pass
    
    # You can add more methods if required