#Create an array of 20 elements for 20 parking slots
#Initialize all elements to 0 
#Use 1 to specify if a slot is taken
#If a slot is free from left to right, a car can enter to park
#To leave a slot, specify the slot number where it was parked.
#Display parking status after each action of available space and filled space

import random

def get_parking_slot():
    available_parking_slots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    

    return available_parking_slots
      
print(get_parking_slot())


def get_parking_occupied():
    occupied_parking_slots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    occupied_parking_slots[0] = 1
    occupied_parking_slots[1] = 1
    occupied_parking_slots[2] = 1
    occupied_parking_slots[3] = 1
    occupied_parking_slots[4] = 1
    occupied_parking_slots[5] = 1
    occupied_parking_slots[6] = 1
    occupied_parking_slots[7] = 1
    occupied_parking_slots[8] = 1                                                                  
    

    return occupied_parking_slots
      
print(get_parking_occupied())


def get_parking_available():
    available_parking_slots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    available_parking_slots[0] = 0
    available_parking_slots[1] = 1
    available_parking_slots[2] = 0
    available_parking_slots[3] = 1
    available_parking_slots[4] = 1
    available_parking_slots[5] = 0
    available_parking_slots[6] = 1
    available_parking_slots[7] = 1
    available_parking_slots[8] = 1                                                                  
    

    return available_parking_slots
      
print(get_parking_available())
