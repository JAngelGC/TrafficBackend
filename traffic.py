# Tools
import numpy as np
import random
from functools import reduce

# Mesa framework
from mesa import Agent, Model
from mesa.space import ContinuousSpace
from mesa.time import RandomActivation, SimultaneousActivation

# File imports
from data import dataStreets
from data import dataCars
from data import dataSetStreets


class TrafficLight(Agent):
    def __init__(self, model: Model, pos, state, time, direction):
        super().__init__(model.next_id(), model)
        self.pos = pos
        self.state = state
        self.time = time
        self.direction = direction
        # self.group = 3    1
        

    def step(self):
        self.time = self.time + 1

        if (self.state == "Green"):
            if (self.time == 24):
                self.time = 0
                self.state = "Yellow"
                
        if (self.state == "Yellow"):
            if (self.time == 6):
                self.time = 0
                self.state = "Red"
                
        if (self.state == "Red"):
            if (self.time == 200):
                self.time = 0
                self.state = "Green"

    # Set groups [DEPRECATED]
    # def set_group(self, n):
    #     self.group = n
    
            

class Street(Agent):
    def __init__(self, model: Model, start, end, direction, traffic_light):
        super().__init__(model.next_id(), model)
        self.start = start
        self.end = end
        self.traffic_light = traffic_light
        self.direction = direction
        self.nextStreet = { "right": None, "forward": None, "left": None }

    def setStreet(self, nextStreet):
        self.nextStreet = {"left": nextStreet[0],
                            "forward": nextStreet[1],
                            "right": nextStreet[2]
                            }



class Car(Agent):
    def __init__(self, model: Model, pos, speed, street: Street):
        super().__init__(model.next_id(), model)
        self.pos = pos
        self.speed = speed
        self.old_speed = speed
        self.street = street
        self.stop = False

        self.direction = street.direction
        self.turnAvailable = False


        self.get_new_turn()


    def get_new_turn(self):
        # possibleTurns =  for street in ["right", "left", "forward"] if self.street.nextStreet[street] != None

        possibleTurns = []
        # for turn in self.street.nextStreet:
        for turn in ["left", "forward", "right"]:
            # print("T: ", turn)
            if self.street.nextStreet[turn]:
                possibleTurns.append(turn)
                
        self.next_street = random.choice(possibleTurns)



    def change_lane(self):
        self.street = self.street.nextStreet[self.next_street]
        self.get_new_turn()


    def car_advance(self):
        if self.stop == False:
            self.speed = self.old_speed
            new_pos = np.array(self.pos) + np.array([0.5, 0.5]) * self.speed
            self.model.space.move_agent(self, new_pos)


    def step(self):

        # print("speed: ", self.speed)
        # print("direction: ", self.direction)
        # print("street direction: ", self.street.direction)

        traffic_light = self.street.traffic_light
                
        distance_from_start = reduce(lambda acc, current: acc + current, np.subtract(self.street.start, self.pos))
        distance_from_end = reduce(lambda acc, current: acc + current, np.subtract(self.street.end, self.pos))



        speed_radius = 4.5
        speed = abs(self.speed[0] + (self.speed[1]))

        # # FIX: Kinda works
        if (0 <= speed <= 1): speed_radius = 5
        elif (1 < speed <= 3): speed_radius = 7
        else: speed_radius = speed + 5
        
        # speed_radius = reduce(lambda acc, current: acc + current, np.subtract(self.street.end, self.pos))
        # print(self.unique_id, "   ", speed_radius)



        neighbor_cars = [n for n in self.model.space.get_neighbors(self.pos, radius = speed_radius, include_center = False) if isinstance(n, Car) and n.street == self.street and n != self]
        ahead_cars = [n for n in neighbor_cars if np.less(self.pos, n.pos).any()]


        # If driving in "opposite" direction: Invert the sign & Get cars ahead of me
        if (self.street.direction == "left" or self.street.direction == "down"):
            distance_from_end = -distance_from_end
            ahead_cars = [n for n in neighbor_cars if np.greater(self.pos, n.pos).any()]

        # print("DISTANCIA: ", distance_from_end)




        # If within range of traffic light (end of the street)
        # if (2.5 <= distance_from_end <= 7.5):
        if (7 <= distance_from_end <= 10):
            if (traffic_light.state == "Red"):
                # print("-------------------")
                self.stop = True
                # self.speed = [0, 0]
            elif (traffic_light.state == "Green" or traffic_light.state == "Yellow"):
                self.stop = False
                self.car_advance()
            else:
                self.stop = False
                self.car_advance()


        # If cars in front of me
        elif ahead_cars:
            # print("AHEAD CARS: ", len(ahead_cars))
            closest_car = min(ahead_cars, key=lambda n:
                reduce(lambda acc, current: acc + current, abs(np.subtract(self.pos, n.pos))))

            # print("CLOSEST CARS: ", closest_car.unique_id)
            # Check distance with closest_car
            # if closest_car.speed == [0, 0]:
            if closest_car.stop == True:
                # self.speed = [0, 0]
                self.stop = True

            else:
                self.old_speed = closest_car.speed
                self.stop = False
                self.car_advance()

        
        # if self.next_street == "right":
            

        # MAKING A TURN
        # elif (0 <= distance_from_end <= 3 or 0<=distance_from_start<=3 ):
        elif ((self.next_street == "right" and 1.75 <= distance_from_end <= 3.25) or (self.next_street == "left" and -3.25 <= distance_from_end <= -1.75) or (self.next_street == "forward" and -1.75 <= distance_from_end <= 1.75)):
            # print("TIME TO MAKE A TURN")
            # print("OLD STREET: ", self.street.end)
            self.stop = False
            self.car_advance()
            self.change_lane()
            self.direction = self.street.direction
            # print("NEW STREET: ", self.street.end)

            # print("NEW STREET: ", self.street.start, "-", self.street.end, "  ", self.street.nextStreet)
            
            if(self.street.direction == "left"):
                self.old_speed = [-1*speed, 0]
                self.speed = [-1*speed, 0]

            if(self.street.direction == "right"):
                self.old_speed = [1*speed, 0]
                self.speed = [1*speed, 0]

            if(self.street.direction == "up"):
                self.old_speed = [0, 1*speed]
                self.speed = [0, 1*speed]

            if(self.street.direction == "down"):
                self.old_speed = [0, -1*speed]
                self.speed = [0, -1*speed]


        else:
            self.stop = False
            self.car_advance()





        


class City(Model):
    def __init__(self):
        super().__init__()
        self.space = ContinuousSpace(100, 100, True)
        self.schedule = SimultaneousActivation(self)

        # Creating streets
        streets = []
        currentLight = None
        for dataStreet in dataStreets:
            if dataStreet["light"]["state"] == "White":
                currentLight = TrafficLight(self, [0, 0], "White", 0, None)
            else:
                currentLight = TrafficLight(self, dataStreet["light"]["pos"], dataStreet["light"]["state"], dataStreet["light"]["time"], dataStreet["direction"])
                
            currentStreet = Street(self, dataStreet["start"], dataStreet["end"], dataStreet["direction"], currentLight)
            
            # traffic_lights.append(currentLight)
            streets.append(currentStreet)
            
            self.space.place_agent(currentLight, currentLight.pos)
            self.schedule.add(currentLight)
        
            self.space.place_agent(currentStreet, currentStreet.start)
            self.schedule.add(currentStreet)

        for dataSetStreet in dataSetStreets:
            s1 = streets[dataSetStreet["info"][0]] if dataSetStreet["info"][0] != None else None 
            s2 = streets[dataSetStreet["info"][1]] if dataSetStreet["info"][1] != None else None 
            s3 = streets[dataSetStreet["info"][2]] if dataSetStreet["info"][2] != None else None 
            streets[dataSetStreet["id"]].setStreet([s1, s2, s3])
            
            # Set groups [DEPRECATED]
            # streets[dataSetStreet["id"]].traffic_light.set_group(len([s for s in [s1,s2,s3] if s != None]))
            # print(len([s for s in [s1,s2,s3] if s != None]))

        self.streets = streets
        
        # Creating cars
        for dataCar in dataCars:
            currentCar = Car(self, dataCar["pos"], dataCar["speed"], streets[dataCar["street"]])
            self.space.place_agent(currentCar, currentCar.pos)
            self.schedule.add(currentCar)

        

    def step(self):
        self.schedule.step()

    def getCars(self):
        cars = []
        for n in self.schedule.agents:
            if isinstance(n, Car):
                cars.append({"id": n.unique_id, "pos": [n.pos[0], n.pos[1]], "direction": n.direction})
        return cars

    def getStreets(self):
        streets = []
        for n in self.schedule.agents:
            if isinstance(n, Street):
                streets.append({"id": n.unique_id,
                                    "start": [n.start[0], n.start[1]],
                                    "end": [n.end[0], n.end[1]],
                                    "direction": n.direction
                                })
        return streets

    def getTrafficLights(self):
        lights = []
        for n in self.schedule.agents:
            if isinstance(n, TrafficLight) and n.state != "White":
                lights.append({"id": n.unique_id, "pos": [n.pos[0], n.pos[1]], "color": n.state, "direction": n.direction})
        return lights
