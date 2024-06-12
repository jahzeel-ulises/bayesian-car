import math

class Car():
    def __init__(self,position:tuple[int,int],dir:int) -> None:
        """
        Constructor of class Car.

        Parameters
        -------------
        position: tuple[int,int]
            Position of the car in the map.
        dir: int[0,3]
            Direction of the car, must be between 0-3
        """
        self.position_ = position
        self.dir_ = dir%4

    def _get_distance(self,map,step:int,axis:int):
        """
        Returns distances of the obstacles in one direction.

        Parameters
        -----------
        map: Map
            Object Map.
        step: int
        axis: int
            Axis of the obstacle.
        """
        distance = 0
        x = self.position_[1]
        y = self.position_[0]
        i = 0
        while map.map_[y][x] != 1 and i !=15:
            if axis == 0:
                x += step
            else:
                y+= step
            distance += 1
            i += 1
        return distance


    def get_distances(self,map):
        """
        Returns distances of the obstacles in three different directions.

        Parameters
        -----------
        map: Map
            Object Map.
        """
        distance = [0,0,0]
        if self.dir_ == 0:
            distance[0] = self._get_distance(map,-1,0)
            distance[1] = self._get_distance(map,-1,1)
            distance[2] = self._get_distance(map,1,0)
        elif self.dir_ == 1:
            distance[0] = self._get_distance(map,-1,1)
            distance[1] = self._get_distance(map,1,0)
            distance[2] = self._get_distance(map,1,1)
        elif self.dir_ == 2:
            distance[0] = self._get_distance(map,1,0)
            distance[1] = self._get_distance(map,1,1)
            distance[2] = self._get_distance(map,-1,0)
        else:
            distance[0] = self._get_distance(map,1,1)
            distance[1] = self._get_distance(map,-1,0)
            distance[2] = self._get_distance(map,-1,1)

        return distance

            
    def get_manhatan(self,map):
        return (((map.zone_[0]+1)-self.position_[0]),((map.zone_[1]+1)-self.position_[1]))  
        
    def get_angle(self,map):
        """
        Returns the angle betweem the car and the target zone.

        Parameters
        -----------
        map: Map
            Object Map
        
        Returns
        -----------
        float:
            Angle in radians.    
        """
        try:
            
            value = math.atan2(((map.zone_[0]+1)-self.position_[0]),((map.zone_[1]+1)-self.position_[1]))
            if value >= 0:
                return value
            else:
                return value + 2*math.pi
        except:
            return math.pi/2

    def get_position(self):
        """
        Returns car position in the map.
        
        Returns
        -----------
        tuple[int,int]
            Position of the car.
        """
        return self.position_

    def update_position(self):
        """
        Update de position of the car acording to the direction of the car.

        Returns
        ----------------
        self:
            Self with the position updated.
        """
        if self.dir_ == 0:
            self.position_ = (self.position_[0]-1,self.position_[1])
        elif self.dir_ == 1:
            self.position_ = (self.position_[0],self.position_[1]+1)
        elif self.dir_ == 2:
            self.position_ = (self.position_[0]+1,self.position_[1])
        else:
            self.position_ = (self.position_[0],self.position_[1]-1)
        return self

    def update_dir(self,dir:int):
        """
        Update dir acording the dir parameter.

        Parameters
        -----------
        dir: int -1,1

        Returns
        -----------
        self:
            Self with the direction updated.
        """
        self.dir_ = (self.dir_+dir)%4
        return self