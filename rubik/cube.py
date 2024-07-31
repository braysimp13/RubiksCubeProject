import re
class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self):
        pass
    
    # Function to check the cube validity       
    def isCubeValid(self, cube):
        # Dictionary to track colors allowed in the cube
        count = {
            'g':9,
            'r':9,
            'b':9,
            'o':9,
            'w':9,
            'y':9
        }
        
        # Has the variables for the validity and satus
        validity = ""
        status = ""
        
        # Checks the length of the cube string to make sure it is valid
        if(len(cube) != 54):
            validity = False
            status = "error: Cube is invalid."
            return {'validity': validity,'status': status}
        
        # Goes through each color piece in the cube
        for piece in cube:
            # Checks that the string is in the color dictionary and it is able to be there
            if(piece in count.keys() and count[piece] != 0):
                # Decreases the count of the count
                count[piece] = count[piece] - 1
            else:
                # Throws an error stating the cube is not valid
                validity = False
                status = "error: Cube is invalid."
                return {'validity': validity,'status': status}
            
        # Splits the string into arrays of the face values
        arr = re.findall('.........?', cube)
        
        # Checks that the values in the middle of each face are unique
        seen = {}
        
        # This iterates each face of the cube to verify the middle of each side
        for side in arr:
            # Throws an error if we have seen the middle of the face yet
            if(side[4] in seen.keys()):
                validity = False
                status = "error: Rubik string does have unique middle colors for each face of the cube."
                return {'validity': validity,'status': status}
            else:
                seen[side[4]] = 1
        
        # If we have got through every check it is valid
        validity = True
        status = 'ok'
        return {'validity': validity,'status': status}
    
    # Checks if the direction parameter is correct
    def isDirValid(self, directions):
        # Dictionary that contains all valid directions
        d = ['F', 'f', 'R', 'r', 'B', 'b', 'L', 'l', 'U', 'u','D', 'd']
        
        # Loops through direction parameter and ensures that the string is made of valid directions
        for curr in directions:
            if(not (curr in d)):
                validity = False
                status = "error: Direction string contains an invalid character"
                return {'validity': validity,'status': status}
        return {'validity': True, 'status': 'ok'}
    
     