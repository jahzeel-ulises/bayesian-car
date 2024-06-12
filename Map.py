import random
import msvcrt

class Map():
    def __init__(self,map) -> None:
        """
        Constructor of class Map.

        Parameters
        -------------
        map: array-like
            Map with index values 0 or 1.
        """
        self.map_ = map
    
    def random_pos(self):
        """Return a random empty position"""
        x = random.randint(1,len(self.map_[0])-2)
        y = random.randint(1,len(self.map_)-2)
        if self.map_[y][x] != 1:
            return (y,x)
        else:
            return self.random_pos()

    def create_zone(self):
        """
        Creates the target zone.

        Retuns
        --------
        self:
            Self with the target zone.
        """

        x = random.randint(0,len(self.map_[0])-1)
        y = random.randint(0,len(self.map_)-1)

        for i in range(-1,2,1):
            for j in range(-1,2,1):
                if self.map_[y+j][x+i] == 1:
                    return self.create_zone()
    
        self.zone_ = (y-1,x-1)
        return self