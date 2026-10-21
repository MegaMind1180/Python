import math


def get_player_pos() -> tuple:
    while True:
        coordinates = input("Enter new coordinates as floats in format 'x,y,z': ")
        lst = coordinates.split(",")
        if len(lst) != 3:
            print("Invalid syntax")
            continue    
        validco = []
        error_occurred = False
        for pos in lst:
            val = pos.strip()
            try:
                validco.append(float(val))
            except ValueError:
                print(f"Error on parameter '{val}': could not convert string to float: '{val}'")
                error_occurred = True
                break
                
        if error_occurred:
            continue
            
        return tuple(validco)


if __name__ == "__main__":
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    
    x1, y1, z1 = pos1
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    
    dist_to_center = math.sqrt(x1**2 + y1**2 + z1**2)
    print(f"Distance to center: {round(dist_to_center, 4)}")
    print()
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    
    x2, y2, z2 = pos2
    dist_between = math.sqrt(
        (x2 - x1)**2 + 
        (y2 - y1)**2 + 
        (z2 - z1)**2
    )
    print(f"Distance between the 2 sets of coordinates: {round(dist_between, 4)}")
