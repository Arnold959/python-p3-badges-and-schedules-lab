def badge_maker(name):    
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return ["Hello, my name is "+name+"."for name in names]

# Enumarate function
# This is the easiest method. 
# The first variable in the iteration points to the index of the item and the second variable points to the current list item.

def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {i+1}!" for i, name in enumerate (names)]

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)
    
    for badge in badges:
        print(badge)
    for room in rooms:
        print(room)   
