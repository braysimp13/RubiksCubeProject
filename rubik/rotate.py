import rubik.cube as rubik
import rubik.cube as cube
import re

#
# Class: rotate
# Used to rotate cube in desired direction
# Input: Parameter dictionary that contains the cube and direction to be rotated. This is not validated to be correct.
# Output: Either error for invalid parameters or a valid rotated cube.
#

def _rotate(parms): 
    # Checks if the dir parameter is either not there, empty, or set to none. It defaults those to a front clockwise turn
    if((not 'dir' in parms.keys()) or (parms['dir'] == None) or (len(parms['dir']) == 0)):
        directions = 'F'
    else:
        # takes in the parameters correctly
        directions = parms['dir']
    
    # Brings in the cube correctly. Checks that the parameter actually exists
    if(not 'cube' in parms.keys()):
        return {'status': 'error: Cube parameter does not exist'} 
           
    encodedCube = parms['cube']
    
    # Checks for direction and cube validity
    dirValidity = cube.Cube.isDirValid(None,directions)
    cubeValidity = cube.Cube.isCubeValid(None,encodedCube)
    
    # Uses the validation from above to actually make sure nothing is wrong
    if(cubeValidity['validity'] and dirValidity['validity']):
        # Goes through each direction in the directions and performs a rotation
        for direction in directions:
            encodedCube = rotateCube(encodedCube, direction)
            
        # Returns the cube rotated correctly
        return {'cube': encodedCube, 'status': 'ok'}
    else:
        # Checks which validity needs to be returned as an error
        if(not cubeValidity['validity']):
            return {'status': cubeValidity['status']}
        else:
            return {'status': dirValidity['status']}
 

# Rotates the cube in provided direction
def rotateCube(cube, direction):
    # Function dictionary used to call specific rotate function by its accompanied character
    d = {'F': frontC,'f': frontCC,'R': rightC,'r': rightCC,'B': backC,'b': backCC,'L': leftC,'l': leftCC,'U': upC,'u': upCC,'D': downC,'d': downCC}
    rotateCube = d[direction](cube)
    
    # Returns rotated cube
    return rotateCube

# Rotates front clockwise
def frontC(cube):
    """Used to do Front Clockwise"""
    # Defines the side pieces that are along the side that will be rotated in their correct order
    sideNums = [42,43,44,9,12,15,47,46,45,35,32,29]
    # Defines the face pieces that are along the side that will be rotated in their correct order.
    faceOrder = [1,2,3,6,9,8,7,4]
    # Passes the side numbers and face numbers and returns the correct rotation
    return rotateSide(cube, sideNums, faceOrder)
              
def frontCC(cube):
    """Used to do Front Counter-Clockwise"""
    # Defines the side pieces that are along the side that will be rotated in their correct order
    sideNums = [44,43,42,29,32,35,45,46,47,15,12,9]
    # Defines the face pieces that are along the side that will be rotated in their correct order.
    faceOrder = [1,4,7,8,9,6,3,2]
    # Passes the side numbers and face numbers and returns the correct rotation
    return rotateSide(cube, sideNums, faceOrder)
def rightC(cube):
    """Used to do Right Clockwise"""
    # Defines the side pieces that are along the side that will be rotated in their correct order
    sideNums = [44,41,38,18,21,24,53,50,47,8,5,2]
    # Defines the face pieces that are along the side that will be rotated in their correct order.
    faceOrder = [10,11,12,15,18,17,16,13]
    # Passes the side numbers and face numbers and returns the correct rotation
    return rotateSide(cube, sideNums, faceOrder)
def rightCC(cube):
    """Used to do Right Counter-Clockwise"""
    # Defines the side pieces that are along the side that will be rotated in their correct order
    sideNums = [38,41,44,2,5,8,47,50,53,24,21,18]
    # Defines the face pieces that are along the side that will be rotated in their correct order.
    faceOrder = [10,13,16,17,18,15,12,11]
    # Passes the side numbers and face numbers and returns the correct rotation
    return rotateSide(cube, sideNums, faceOrder)
def backC(cube):
    """Used to do Back Clockwise"""
    # Defines the side pieces that are along the side that will be rotated in their correct order
    sideNums = [38,37,36,27,30,33,51,52,53,17,14,11]
    # Defines the face pieces that are along the side that will be rotated in their correct order.
    faceOrder = [19,20,21,24,27,26,25,22]
    # Passes the side numbers and face numbers and returns the correct rotation
    return rotateSide(cube, sideNums, faceOrder)
def backCC(cube):
    """Used to do Back Counter-Clockwise"""
    # Defines the side pieces that are along the side that will be rotated in their correct order
    sideNums = [36,37,38,11,14,17,53,52,51,33,30,27]
    # Defines the face pieces that are along the side that will be rotated in their correct order.
    faceOrder = [19,22,25,26,27,24,21,20]
    # Passes the side numbers and face numbers and returns the correct rotation
    return rotateSide(cube, sideNums, faceOrder)
def leftC(cube):
    """Used to do Left Clockwise"""
    # Defines the side pieces that are along the side that will be rotated in their correct order
    sideNums = [36,39,42,0,3,6,45,48,51,26,23,20]
    # Defines the face pieces that are along the side that will be rotated in their correct order.
    faceOrder = [28,29,30,33,36,35,34,31]
    # Passes the side numbers and face numbers and returns the correct rotation
    return rotateSide(cube, sideNums, faceOrder)
def leftCC(cube):
    """Used to do Left Counter-Clockwise"""
    sideNums = [42,39,36,20,23,26,51,48,45,6,3,0]
    faceOrder = [28,31,34,35,36,33,30,29]
    return rotateSide(cube, sideNums, faceOrder)
def upC(cube):
    """Used to do Up Clockwise"""
    # Defines the side pieces that are along the side that will be rotated in their correct order
    sideNums = [2,1,0,29,28,27,20,19,18,11,10,9]
    # Defines the face pieces that are along the side that will be rotated in their correct order.
    faceOrder = [37,38,39,42,45,44,43,40]
    # Passes the side numbers and face numbers and returns the correct rotation
    return rotateSide(cube, sideNums, faceOrder)
def upCC(cube):
    """Used to do Up Counter-Clockwise"""
    # Defines the side pieces that are along the side that will be rotated in their correct order
    sideNums = [0,1,2,9,10,11,18,19,20,27,28,29]
    # Defines the face pieces that are along the side that will be rotated in their correct order.
    faceOrder = [37,40,43,44,45,42,39,38]
    # Passes the side numbers and face numbers and returns the correct rotation
    return rotateSide(cube, sideNums, faceOrder)
def downC(cube):
    """Used to do Down Clockwise"""
    # Defines the side pieces that are along the side that will be rotated in their correct order
    sideNums = [6,7,8,15,16,17,24,25,26,33,34,35]
    # Defines the face pieces that are along the side that will be rotated in their correct order.
    faceOrder = [46,47,48,51,54,53,52,49]
    # Passes the side numbers and face numbers and returns the correct rotation
    return rotateSide(cube, sideNums, faceOrder)
def downCC(cube):
    """Used to do Down Counter-Clockwise"""
    # Defines the side pieces that are along the side that will be rotated in their correct order
    sideNums = [8,7,6,35,34,33,26,25,24,17,16,15]
    # Defines the face pieces that are along the side that will be rotated in their correct order.
    faceOrder = [46,49,52,53,54,51,48,47]
    # Passes the side numbers and face numbers and returns the correct rotation
    return rotateSide(cube, sideNums, faceOrder)
    
def rotateSide(cube, sideNums, faceOrder):
    # Takes the cube string and makes it an array
    cubeArr = list(cube)
    
    # Used to track in while loop
    count = 0
    # Used to track when in sideNums we are at
    currSide = 0
    
    # Gets the first face needed to rotate and stores as the current
    c1 = cubeArr[sideNums[currSide]]
    c2 = cubeArr[sideNums[currSide + 1]]
    c3 = cubeArr[sideNums[currSide + 2]] 
    
    # Brings the end of the arrays side to the front 
    cubeArr[sideNums[currSide]] = cubeArr[sideNums[9]]    
    cubeArr[sideNums[currSide + 1]] = cubeArr[sideNums[10]]        
    cubeArr[sideNums[currSide + 2]] = cubeArr[sideNums[11]]              
    
    currSide = 3
    
    # Iterates through rest of cube
    while count < 3:
        # Stores previous values at current location
        p1 = cubeArr[sideNums[currSide]]
        p2 = cubeArr[sideNums[currSide+1]]
        p3 = cubeArr[sideNums[currSide+2]]
         
        # Sets previous value to current rotated values   
        cubeArr[sideNums[currSide]]  = c1
        cubeArr[sideNums[currSide+1]] = c2
        cubeArr[sideNums[currSide+2]] = c3
           
        # Sets previous values so they can be rotated properly 
        c1 = p1
        c2 = p2
        c3 = p3
          
        # Increments variables  
        currSide = currSide + 3
        count = count + 1
    
    # Array to store list of face values in the order they will rotate (clockwise counter-clockwise)
    snakedFace = []
    
    # Goes through face array and appends the value from the cube to it
    for num in faceOrder:
        snakedFace.append(cubeArr[num-1])
    
    # Gets the length of the face rotation
    length = len(snakedFace) - 1

    count = 0
    # While loop used to shift the face array over 2, which account for the face rotation
    while(count < 2):
        for _ in range(0,length):
            shift = snakedFace.pop(0)
            snakedFace.append(shift)
        count = count + 1
    
    i = 0
    # Puts the correct values into their locations within the cube array
    while(i < len(snakedFace)):
        cubeArr[faceOrder[i]-1] = snakedFace[i]
        i= i + 1
        
    # Makes the array a string and returns    
    return ''.join(cubeArr)
    


        
