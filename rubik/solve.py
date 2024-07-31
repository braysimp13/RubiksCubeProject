'''
Created on: 9/18/2022

@Author: Brayden Simpson
'''
#Function used to solve Rubik's Cube (Currently only applicable to Down-Cross and before.

import rubik.cube as cube
from rubik.rotate import downC
import rubik.rotate as rotate
import hashlib
import random


def _solve(parms):
    """Return rotates needed to solve input cube"""
    result = {} 
    # Gets the code inputed by used
    encodedCube = parms.get('cube',None) 
    # Checks if the parameters have the cube and if it is valid 
    if(not 'cube' in parms.keys()):
        return {'status': 'error: Cube parameter does not exist'}
    cubeValidity = cube.Cube.isCubeValid(None,encodedCube)
    if(not cubeValidity['validity']):
        result['status'] = cubeValidity['status']
        return result
    originalCube = encodedCube
    # Automatically what the rotation dictionary holds
    rotations = {}
    rotations['cube'] = encodedCube
    rotations['rotations'] = ''
    rotations['status'] = 'ok'
    # Checks if we have been given a cube that already is to a DownCross
    if(not checkIfDownCrossDone(encodedCube)):
        rotations = doDownCross(encodedCube)
        if(rotations['status'] != 'ok'):
            return rotations
        encodedCube = rotations['cube']
    # Checks if a bottom layer needs to be completed
    if(not checkIfBottomDone(encodedCube)):
        rotations = doBottomLayer(encodedCube, rotations)
        if(rotations['status'] != 'ok'):
            return rotations
        encodedCube = rotations['cube']  
    if(not checkIfMiddleDone(encodedCube)):
        #rotations = doMiddleLayer(encodedCube, rotations)
        rotations = doMiddleLayer(encodedCube, rotations)
        if(rotations['status'] != 'ok'):
            return rotations
        encodedCube = rotations['cube']
    if(not checkIfTopCrossDone(encodedCube)):
        rotations = solveTopCross(encodedCube, rotations)
        if(rotations['status'] != 'ok'):
            return rotations
        encodedCube = rotations['cube']    
    if(not checkIfTopDone(encodedCube)):
        rotations = solveTopSide(encodedCube, rotations)
        if(rotations['status'] != 'ok'):
            return rotations
    if(not isTopCornersSolved(encodedCube)):
        rotations = solveTopCorners(rotations)
        if(rotations['status'] != 'ok'):
            return rotations
    if(not checkIfFullCubeDone(encodedCube)):
        rotations = solveFullCube(rotations)
        if(rotations['status'] != 'ok'):
            return rotations
    # Returns the rotations needed to complete this iteration. Provides a token that is the way to decode the cube
    # Makes the token for the cube
    sha256Hash = hashlib.sha256()
    stringToEncode = str(originalCube) + str(rotations['rotations'])
    sha256Hash.update(stringToEncode.encode())
    fullToken = sha256Hash.hexdigest()
    index = random.randint(0,len(fullToken)-9)
    # Used to get last 8 digits of token
    num = index + 8
    fullToken = fullToken[index:num:1]
    rotations['token'] = fullToken
    del rotations['cube']
    return rotations
    
def doDownCross(cube):
    bottomColor = cube[49]
    rotations = solveDaisy(cube)
    downCrossSolved = solveDownCross(rotations['cube'],rotations['rotations'],bottomColor)
    
    # Grabs the rotation solution and final cube
    rotations['rotations'] = downCrossSolved[0]
    rotations['cube'] = downCrossSolved[1]
    
    # Used to make sure Down Cross occurred. Should have no errors thrown if cube valid
    if(not checkIfDownCrossDone(rotations['cube'])):
        return fixRotation(rotations,'the bottom cross')
        
    rotations['status'] = 'ok'
    return rotations

# Used to complete bottom layer. Calls bottom layer solve function and determines if it actually did it correctyl
def doBottomLayer(cube, rotations):
    bottomLayerSolved = solve_Bottom(rotations['cube'], rotations['rotations'])
    rotations['rotations'] = bottomLayerSolved['rotations']
    rotations['cube'] = bottomLayerSolved['cube']
        
    if(not checkIfBottomDone(rotations['cube'])):
        return fixRotation(rotations,'the bottom layer')
    
    rotations['status'] = 'ok'
    return rotations

# Manually checks values to see if the down-cross is done yet.
def checkIfDownCrossDone(cube):
    if(cube[48] == cube[46] == cube[50] == cube[52] == cube[49]):
        if((cube[7] == cube[4]) and (cube[34] == cube[31]) and (cube[16] == cube[13]) and (cube[22] == cube[25])):
            return True
        else:
            return False
    else:
        return False   
# Checks if the bottom layer is done
def checkIfBottomDone(cube):
    if(cube[48] == cube[46] == cube[50] == cube[52] == cube[51] == cube[53] == cube[47] == cube[45] == cube[49]):
        if((cube[33] == cube[35] == cube[31]) and (cube[4] == cube[6] == cube[8]) and (cube[13] == cube[15] == cube[17]) and (cube[22] == cube[24] == cube[26])):
            return True
        else:
            return False
    return False
# Checks if the daisy has been complete by manual indexes        
def checkIfDaisy(cube, bottomMiddle):
    if(cube[39] == cube[43] == cube[41] == cube[37] == bottomMiddle):
        return True 
    return False

# Performs rotations that are given in from a rotation string. Add to previous rotations that hvae been.
def performRotations(cube, rotationsNeeded, rotationsOccured):
    for rotation in rotationsNeeded:
        cube = rotate.rotateCube(cube, rotation)
        rotationsOccured.append(rotation)
    returnArray = [cube, rotationsOccured]    
    return returnArray

# Way to rotate if multiple rotations need to be performed to move a vlaue onto top face
def faceRotations_MultipleMoves(cube, bottomVal, rotations, count, directions):
    # Does the first rotations to move value into correct position on face
    cube = rotate.rotateCube(cube, directions['rotations'][0])
    rotations.append(directions['rotations'][0])
    
    # Logic to select which index the value is in currently
    if (directions['index'] == 1 or directions['index'] == 2):
        currNum = directions['faceVals'][count][1]
    else:
        currNum = directions['faceVals'][count][3]
        
    # Does an upper rotation to line the top face with the side where the value needed to rotate on is
    rotationsNeeded = upperRotationsNeeded(cube, currNum, bottomVal)
    
    # Performs the rotations for upper face and returns the cube and rotations
    returnArray = performRotations(cube, rotationsNeeded,rotations)
    rotations = returnArray[1]
    cube = returnArray[0]
    
    # Rotates side value onto top of the face
    cube = rotate.rotateCube(cube, directions['rotations'][1])
    rotations.append(directions['rotations'][1])
    return cube, rotations

# Rotates value onto top face if it is already in an optimal position
def faceRotations_OneMove(cube, bottomVal, rotations, count, directions):
    # Checks which index the value is on to know where to rotate top face
    if (directions['index'] == 1 or directions['index'] == 2):
        currNum = directions['faceVals'][count][1]
    else:
        currNum = directions['faceVals'][count][3]
        
    # Figures out what rotations are needed to perform to move upper face to correct position
    rotationsNeeded = upperRotationsNeeded(cube, currNum, bottomVal)
    returnArray = performRotations(cube, rotationsNeeded,rotations)
    rotations = returnArray[1]
    cube = returnArray[0]
    
    # Rotates value onto the top of the face
    cube = rotate.rotateCube(cube, directions['rotations'][0])
    rotations.append(directions['rotations'][0])
    return cube, rotations

# Solves the daisy on top of the cube
def solveDaisy(cube):
    # Values that have the color of the bottom middle and the top values for daisy
    topFace = [39,43,41,37]
    bottomVal = cube[49]
    rotations= []    
    # Iterates until the cube is not a daisy anymore
    while(not checkIfDaisy(cube, bottomVal)):
        # Count to determine what side we are on
        count = 0     
        # Used to rotate upper face if there are no possible rotations to do in current loop.
        rotationOccur = False
        # Iterates through the middle values of top face
        for side in topFace:
            # Checks if the current value we are looking at on the top face is the correct value yet
            if(cube[side] != bottomVal):
                # Gets if there are any values to rotate straight onto the top face.
                directions = checkSide(cube, bottomVal, count)                
                # Checks if there are any rotations to actually be done
                if(directions != ''):
                    # Checks that the rotations have occurred
                    rotationOccur = True                                       
                    # Performs the rotations we have determined are necessary
                    returnArray = performRotations(cube,directions,rotations)                 
                    # Returns the rotations that have occurred
                    rotations = returnArray[1]
                    cube = returnArray[0]
                    count += 1                  
                    # Breaks current loop to go to next value
                    continue                               
                # Checks if the current values face it is attached to has a needed value
                directions = faceContainsVal(cube, count, bottomVal)                                
                # Checks if we should do a rotation
                if(directions != ''):
                    # Makes sure program knows a rotation has occurred
                    rotationOccur = True
                    count, cube, rotations = doFaceRotations(cube, directions, rotations, count, bottomVal)
                    continue
            count += 1          
        # If no rotations have occurred, perform an upper face rotation 
        if(not rotationOccur):
            cube = rotate.rotateCube(cube,'U')
            rotations.append('U')   
    result = makeRotationsReturn(rotations, cube)
    return result
def doFaceRotations(cube, directions, rotations, count, bottomVal):
     # If we need to do multiple rotations, pass to multiple face rotation function
    if(len(directions['rotations']) == 2):
        cube, rotations = faceRotations_MultipleMoves(cube, bottomVal, rotations, count, directions)
        count += 1
        # Does rotations that the value is already in an optimal location
    else:
        cube, rotations = faceRotations_OneMove(cube, bottomVal, rotations, count, directions)
        count += 1                
    return count, cube, rotations
def makeRotationsReturn(rotations,cube):
    rotationsForArray = ''   
    # Moves rotations into a string
    for rotation in rotations:
        rotationsForArray += rotation   
    result = {}   
    # Returns the needed information in a dictionary
    result['rotations'] = rotationsForArray
    result['status'] = 'ok'
    result['cube'] = cube
    return result
# Checks if the side contains the desired value in it to rotate to the daisy
def checkSide(cube, bottomVal, count):
    sideVals = [ [3,48,23],[12,46,32],[21,50,5],[30,52,14]]   
    rotations = [ {1:'l',2:'ll',3:'L'}, {1:'f',2:'ff',3:'F'},
            {1:'r',2:'rr',3:'R'},{1:'b',2:'bb',3:'B'}]    
    currSide = sideVals[count]
    index = 1
    for val in currSide:
        if(cube[val] == bottomVal):
            # Returns rotation pattern if there is any
            return rotations[count][index]
        index += 1
    return ''

# Chekcs if the face has the desired value in it to rotate to the daisy
def faceContainsVal(cube, count, bottomVal):
    faceValues = [[28,32,34,30],[1,5,7,3],[10,14,16,12],[19,23,25,21]]   
    rotations = [{1:'LF',2:'F',3:'Lb',4:'b'},{1:'FR',2:'R',3:'Fl',4:'l'},
                 {1:'RB',2:'B',3:'Rf',4:'f'},{1:'BL',2:'L',3:'Br',4:'r'} ]   
    currFace = faceValues[count]
    index = 1
    for val in currFace:
        if(cube[val] == bottomVal):
            # Returns rotation pattern if there is any
            return {'rotations': rotations[count][index], 'arr': rotations, 'faceVals': faceValues, 'index':index}
        index += 1
    return ''

# Used to determine what upper rotations are needed to put the desired space in its location
def upperRotationsNeeded(cube, currentMiddleNumber, bottomVal):
    sides = {3:39,5:41,12:43,14:37,21:41,23:39,30:37,32:43}
    sideOrder = {39:{'arr':[39,43,37,41],39:'',43:'U', 37:'u',41:'uu'},43:{'arr':[43,39,41,37],43:'',39:'u',41:'U',37:'uu'},
        41:{'arr':[41,43,37,39],41:'',43:'u',37:'U',39:'uu'},37:{'arr':[37,39,41,43],37:'',39:'U',41:'u',43:'uu'}}   
    # Checks what value is the place to transform to
    transformToThisMiddle = sides[currentMiddleNumber]    
    for currentLook in sideOrder[transformToThisMiddle]['arr']:
        # Checks what is the first value to need to be rotated to the middle
        if(cube[currentLook] != bottomVal):
            # Returns proper rotation if any (There should always be)
            return sideOrder[transformToThisMiddle][currentLook]    
    return ''  

# Used to solve the down cross
def solveDownCross(cube, rotations, bottomColor):
    # Function dictionary to have all face rotations to move to the bottom face
    functionDictionary = {'FF':FrontFaceDown, 'RF':RightFaceDown, 'BF':BackFaceDown, 'LF':LeftFaceDown}
    functionKeys = ['FF','RF','BF','LF']  
    # Goes through functions and calls them with the cube, previous rotations  
    for function in functionKeys:
        returnArray = functionDictionary[function](cube, rotations, bottomColor)
        rotations = returnArray[0]
        cube = returnArray[1]    
    return returnArray

# Used to determine the rotation needed to move to bottom cross
def determineRotations(rotation, topNum, topNums, cube, rotations, currRotation, middle, upperMiddle,bottomColor):
        # Checks if the 
        if(cube[upperMiddle] == cube[middle] and (cube[topNum] == bottomColor)):
            for direction in currRotation:
                # Performs the rotation that is needed since value is already in place
                cube = rotate.rotateCube(cube, direction)
            rotations += currRotation
        else:
            for topNum in topNums:
                # Finds where the value that needs to be move to bottom and performs movement to put in position
                if((cube[topNum] == cube[middle]) and (cube[rotation[topNum][1]] == bottomColor)):
                    # Does rotations for the face
                    for direction in rotation[topNum][0]:
                        cube = rotate.rotateCube(cube, direction)
                    rotations += rotation[topNum][0]
                    break
        returnArray = [rotations, cube]
        return returnArray  
    
# Proper rotation order for Front Face to go to bottom cross    
def FrontFaceDown(cube,rotations,bottomColor):
    topNums = [10,19,28]
    rotation = {10:['UFF',41],19:['UUFF',37],28:['uFF',39]}
    return determineRotations(rotation, 43, topNums, cube, rotations, 'FF', 4, 1, bottomColor)

# Proper rotation order for Right Face to go to bottom cross   
def RightFaceDown(cube,rotations,bottomColor):
    topNums = [1,19,28]
    rotation = {1:['uRR',43],19:['URR',37],28:['UURR',39]}  
    return determineRotations(rotation, 41, topNums, cube, rotations, 'RR', 13, 10, bottomColor)  

# Proper rotation order for Back Face to go to bottom cross   
def BackFaceDown(cube,rotations,bottomColor):  
    topNums = [10,1,28]
    rotation = {10:['uBB',41],1:['uuBB',43],28:['UBB',39]}
    return determineRotations(rotation, 37, topNums, cube, rotations, 'BB', 22, 19, bottomColor)

# Proper rotation order for LEft Face to go to bottom cross   
def LeftFaceDown(cube,rotations,bottomColor):
    topNums = [1,10,19]
    rotation = {1:['ULL',43], 10:['UULL',41],19:['uLL',37]} 
    return determineRotations(rotation, 39, topNums, cube, rotations, 'LL', 31, 28, bottomColor)

# Used to implement logic of solving bottom layer. Loops until done
def solve_Bottom(cube, rotations):
    functions = {"Top" : solveToTop, "Bottom": solveToBottom, "TopFace": solveToTopFace}
    # Loops until done
    while(not checkIfBottomDone(cube)):
        # Finds where the index with the most priority is
        place = checkWhereWantedColor(cube, cube[49])

        if(place[0] == False):
            rotated = doRandomRotation(cube)
            cube = rotated[0]['cube']
            rotations += rotated[1]
        else:  
            # Rotates according to function array above and index
            rotated = functions[place[0]](cube, place[1])
            cube = rotated[0]['cube']            
             # Adds rotation to previous rotations
            rotations += rotated[1] 
    # Returns finished result
    result = {'cube' : cube , 'rotations' : rotations}
    return result

def doRandomRotation(cube):
    places = {4:[6,8],
              13:[15,17],
              22:[24,26],
              31:[33,35]
            }
    middles = [4,13,22,31]
    rotations = {6:'luL',8:'RUr',15:'fuF',17:'BUb',24:'ruR',26:'LUl',33:'buB',35:'FUf'}
    for middle in middles:
        for num in places.get(middle):
            if(not cube[num] == cube[middle]):
                input = {}
                input['op'] = 'rotate'
                input['cube'] = cube
                input['dir'] = rotations.get(num)
                result = rotate._rotate(input)
                return [result, input['dir']]
# Goes through and checks if the value is needed top, bottom, or top face. Goes in order of how close it is to bottom layer
def checkWhereWantedColor(cube, bottomColor):
    topCheck = checkTop(cube, bottomColor)
    if(topCheck[0]):
        return ["Top",topCheck[1]]
    bottomCheck = checkBottom(cube, bottomColor)
    if(bottomCheck[0]):
        return ["Bottom", bottomCheck[1]]
    topFaceCheck = checkTopFace(cube, bottomColor)
    if(topFaceCheck[0]):
        return ["TopFace", topFaceCheck[1]]  
    return [False]

# Checks if the value is in the top layer
def checkTop(cube, color):
    arr = [0,2,9,11,18,20,27,29]
    for num in arr:
        if(cube[num] == color):
            return [True, num]
    return [False]

# Checks if the value is on the bottom layer
def checkBottom(cube, color):
    arr = [6,8,15,17,24,26,33,35]
    for num in arr:
        if(cube[num] == color):
            return [True, num]
    return [False]

# Checks if the value is on the top face.
def checkTopFace(cube, color):
    arr = [36, 38, 42, 44]  
    for num in arr:
        if(cube[num] == color):
            return [True, num]
    return [False]

# Used to move a value from the top corners of the face to the bottom face
def solveToTop(cube,num):
    # Corners and the values that are attached to them on the corner
    dict = {0: 29, 2: 9, 9: 2, 11:18, 18:11, 20:27, 27:20, 29:0}    
    # All of the corresponding rotations to where it needs to go with the value to rotate properly
    middleNumDict = {4: {29: 'uRUr', 9: 'UluL', 2 : 'RUr', 18 :'UUluL', 11 : 'URUr', 27:'uluL', 20:'uuRur', 0:'luL'},
                     13: {29: 'uuBUb', 9: 'fuF', 2 : 'uBUb', 18 :'UBUb', 11 : 'BUb', 27:'uufuF', 20:'UBUb', 0:'ufuF'},
                     22: {29: 'ULUl', 9: 'uruR', 2 : 'uuLUl', 18 :'ruR', 11 : 'uLUl', 27:'UruR', 20:'Lul', 0:'UUruR'},
                     31: {29: 'FUf', 9: 'UUbuB', 2 : 'UFUf', 18 :'ubuB', 11 : 'UUFUf', 27:'buB', 20:'uFuf', 0:'UbuB'}}
    middleNums = [4,13,22,31]
    colorToFind = dict.get(num)
    
    # Finds corresponding middle number and does the rotation
    for middlenum in middleNums:
        if(cube[colorToFind] == cube[middlenum]):
            input = {}
            input['op'] = 'rotate'
            input['cube'] = cube
            temp = middleNumDict.get(middlenum)
            input['dir'] = temp.get(colorToFind)
            result = rotate._rotate(input)
            return [result, input['dir']] 
    return {}
# Used to move a value from the bottom layer to the top layer of the cube
def solveToBottom(cube,num):
    # Corresponding corners and roations needed
    correspondingCorner = {6:45, 8:47, 15:47,17:53, 24:53,26:51,33:51,35:45}
    correspondingRotation = {47:{8:'fuF',15:'RUr'},
                             53:{17:'ruR', 24:'BUb'},
                             51:{26:'buB', 33:'LUl'},
                             45:{6:'FUf',35:'luL'}   }
    # Finds corresponding rotation to corner that it is in the bottom and rotates to move to top layer
    input = {}
    input['op'] = 'rotate'
    input['cube'] = cube
    input['dir'] = correspondingRotation[correspondingCorner.get(num)].get(num)
    result = rotate._rotate(input)   
    return [result, input['dir']]

# Solves when there is a value on the top of the cube we want move to a face
def solveToTopFace(cube,num):
    # List of corresponding rotations to places it could be on the top
    correspondingRotationToCorner = {36:{45:'uluL',47:'uuRUr',51:'LUl',53:'UruR'},
                                     38:{45:'uuluL',47:'URUr',51:'uLUl',53:'ruR'},
                                     42:{45:'luL',47:'uRUr',51:'ULUl',53:'uuruR'},
                                     44:{45:'UluL',47:'RUr',51:'uuLUl',53:'uruR'}}
    # finds an empty corner and then finds the rotation in the dictionary
    openMiddleNum = findEmptyCorner(cube)
    neededRotation = correspondingRotationToCorner.get(num).get(openMiddleNum)
    input = {}
    input['op'] = 'rotate'
    input['cube'] = cube
    input['dir'] = neededRotation
    # Rotates cube effectively
    result = rotate._rotate(input)
    return [result, input['dir']]
 
# Finds a corner that a value can be moved to on the bottom
def findEmptyCorner(cube):
    # Corner values for bottom
    cornerArr = [45, 47, 51, 53]
    # Searches through and finds the corner
    for cornerNum in cornerArr:
        if(cube[cornerNum] != cube[49]):
            return cornerNum

# Function used to facilitate the solving of the middle layer.
def doMiddleLayer(cube, rotations): 
    # Throws the cube and rotations to a solve function
    middleLayerSolved = solve_middle(rotations['cube'], rotations['rotations'])
    
    # Gets the updated cube and rotations list into output array
    rotations['rotations'] = middleLayerSolved['rotations']
    rotations['cube'] = middleLayerSolved['cube']
    
    # Ensures that the cube is actually solved properly. Throws error if not       
    if(not checkIfMiddleDone(rotations['cube'])):
        return fixRotation(rotations,'the middle layer')  
    
    # Returns the cube and rotations along with the status
    rotations['status'] = 'ok'
    return rotations 

# Used to loop while the middle layer isn't done. Checks for rotations to be done      
def solve_middle(cube, rotations):
    # Loops while middle layer is not done 
    while(not checkIfMiddleDone(cube)):
        # Checks for an immediate top piece that can be put on the sides. 
        result = check_for_immediate_rotation(cube)
        if(result.get('found')):
            # Rotates the piece into the proper place if it has been found
            cube,rotations = rotate_immediate_rotation(cube, result.get('placeFrom'), result.get('placeTo'), rotations)
            continue   
        
        # Checks for random rotation that can move into place and does it    
        result = check_for_possible_rotation(cube)
        cube,rotations = rotate_regular_rotation(cube, result.get('placeTo'), rotations)   
    
    # Returns reuslt once done
    result = {'cube' : cube, 'rotations' : rotations}
    return result

# Checks if the middle layer is done. Returns false if not. Returns true if it is
def checkIfMiddleDone(cube):
    if((cube[3] == cube[4] == cube[5]) and (cube[12] == cube[13] == cube[14]) and (cube[21] == cube[22] == cube[23]) and (cube[30] == cube[31] == cube[32])):
        return True
    return False

# Checking for a top piece that can be moved into the middle layer immediately
def check_for_immediate_rotation(cube):    
    # Slots on the side and corresponding middle pieces and side pieces
    openSpots = [3,5,12,14,21,23,30,32]
    spotMapping = {3:[32,4,31], 5:[12,4,13], 12:[5,13,4], 14:[21,13,22], 21:[14,22,13], 23:[30,22,31], 30:[23,31,22], 32:[3,31,4]}
    
    # Sets variables that will be returned in case nothing is found
    placeFrom = -1
    placeTo = -1
    found = False
    
    # Goes through all side spots. If it finds a spot that does not equal the middle piece on one of them it goes into a function to find a top piece
    for spot in openSpots:
        currArray = spotMapping.get(spot)
        if(cube[spot] != cube[currArray[1]] or cube[currArray[0]] != cube[currArray[2]]):
            placeFrom, placeTo = checkForTopPieceMatch(cube, spot, currArray[0], currArray[1], currArray[2])
            # If it did not find a top piece continue
            if(placeFrom == -1 and placeTo == -1):
                continue 
            else:
                found = True
                break 
            
    # Returns the result whether it is good or bad
    result = {'found' : found, 'placeFrom' : placeFrom, 'placeTo' : placeTo}    
    return result

# Checks for a matching top piece to a side piece we are looking at
def checkForTopPieceMatch(cube, spot1, spot2, middleSpot1, middleSpot2):
    # Top pieces
    pieces = [[1,43],[19,37],[10,41], [28,39]] 
    
    # Corresponding side pieces to the middle spots we have  
    knowWhichSide = {4:{13:5,31:3},
        13:{4:12,22:14},
        22:{13:21,31:23},
        31:{22:30,4:32}}
    
    # Loops through top pieces on the cube
    for piece in pieces:
        # Checks if the piece matches a specific middle area or not. Returns the top piece to middle side that matches
        if(cube[piece[0]] == cube[middleSpot1] and cube[piece[1]] == cube[middleSpot2]):
            pieceTo = knowWhichSide.get(middleSpot1).get(middleSpot2)
            return piece[0], pieceTo
        elif (cube[piece[0]] == cube[middleSpot2] and cube[piece[1]] == cube[middleSpot1]):
            pieceTo = knowWhichSide.get(middleSpot2).get(middleSpot1)
            return piece[0], pieceTo           
    return -1,-1  

# Looks for a side that has an empty side piece that can be given a regular rotation  
def check_for_possible_rotation(cube):
    openSpots = [3,5,12,14,21,23,30,32]
    topPiece = {3:[4,1],5:[4,1],12:[13,10],14:[13,10],21:[22,19],23:[22,19],30:[31,28],32:[31,28]}   
    found = False
    placeFrom = -1
    placeTo = -1
    for spot in openSpots:
        piece = topPiece.get(spot)
        if(cube[spot] != cube[piece[0]]):
            placeFrom = piece[1]
            placeTo = spot
            found = True
            break
    result = {'found' : found, 'placeFrom' : placeFrom, 'placeTo' : placeTo}
    return result

# Does a rotation based on the numbers given from the top piece rotation from before
def rotate_immediate_rotation(cube, placeFrom, placeTo,rotations):
    # Rotation type for a certain side piece
    rotationType = {3 : "FL", 5 : "FR", 12 : "RL", 14 : "RR", 
                    21 : "BL", 23 : "BR", 30 : "LL", 32 : "LR"}        
    # Rotations for specific sides
    pieceRotation = {"FL": 'ulULUFuf', "FR" : 'URurufUF', "RL" : 'ufUFURur', "RR" : 'UBuburUR',  "BL": 'urURUBub' , "BR" : 'ULulubUB', "LL" : 'ubUBULul', "LR" : 'UFufulUL'}       
    # Rotations that will get a certain top piece into position
    rotateToProper = {1 : {5:'', 3:'', 12:'u',14:'u', 21:'uu', 23: 'uu', 30:'U', 32:'U'},10:{5:'U', 3:'U', 12:'',14:'', 21:'u', 23: 'u', 30:'uu', 32:'uu'},
                  19:{5:'UU', 3:'UU', 12:'U',14:'U', 21:'', 23: '', 30:'u', 32:'u'},28:{5:'u', 3:'u', 12:'uu',14:'uu', 21:'U', 23: 'U', 30:'', 32:''}    }     
    # Gets the beginning rotations and specific rotation to move pieces  
    beginRotation = rotateToProper.get(placeFrom).get(placeTo)
    specificEndRotation = pieceRotation.get(rotationType.get(placeTo))     
    # Creates input hash and does the rotation. Returns new cube and added rotations
    needRotations = beginRotation + specificEndRotation
    result = doRotation(cube, needRotations)  
    rotations += needRotations
    return result['cube'],rotations

# Does a regular rotation based off of the side piece that is empty
def rotate_regular_rotation(cube, placeTo,rotations):
    # Rotation type based on a certain side
    rotationType = {3 : "FL", 5 : "FR", 12 : "RL", 14 : "RR", 21 : "BL", 23 : "BR", 30 : "LL", 32 : "LR"}     
    # Attached side piece to rotation type
    pieceRotation = {"FL": 'ulULUFuf', "FR" : 'URurufUF', "RL" : 'ufUFURur', "RR" : 'UBuburUR', "BL": 'urURUBub' , "BR" : 'ULulubUB', "LL" : 'ubUBULul', "LR" : 'UFufulUL'}     
    # Gets the specfic rotation and then does the rotation through the rotate function
    specificRotation = pieceRotation.get(rotationType.get(placeTo))   
    rotations += specificRotation
    result = doRotation(cube, specificRotation)
    # Returns new cube and new rotations string
    return result['cube'], rotations

# Used by middle layer functions to complete a rotation
def doRotation(cube, rotation):
    input = {}
    input['cube'] = cube
    input['op'] = 'rotate'
    input['dir'] = rotation
    result = rotate._rotate(input)
    return result

# Facilitates the solving of the top cross
def solveTopCross(cube, rotations):
    # Puts info into main solve top cross function that loops
    topCrossLayerSolved = solve_TopCross(rotations['cube'], rotations['rotations'])
    rotations['rotations'] = topCrossLayerSolved['rotations']
    rotations['cube'] = topCrossLayerSolved['cube']   
    # Makes sure we actually solved and errors if not
    if(not checkIfTopCrossDone(rotations['cube'])):
        return fixRotation(rotations,'the top cross')
    rotations['status'] = 'ok'
    return rotations
def solve_TopCross(cube, rotations):
    while(not checkIfTopCrossDone(cube)):
        if(isDot(cube)):
            cube, rotations = doPossibleDotRotation(cube, rotations)
        if(isL(cube)):
            cube, rotations = doPossibleLRotation(cube, rotations)
        if(isLine(cube)):
            cube, rotations = doPossibleLineRotation(cube, rotations)  
    return {'cube' : cube, 'rotations' : rotations}
# Does a dot rotation if it has been determined to do it
def doPossibleDotRotation(cube, rotations):
    result = doRotation(cube, 'FRUruf')
    rotations += 'FRUruf'
    cube = result['cube']
    return cube, rotations

# Does a L rotation if determined we want
def doPossibleLRotation(cube,rotations):
    # Pieces and rotations that form the L in the cross
    piecesToCheck = [[37,41],[41,43],[39,43],[37,39]]
    rotationTypes = {'3741':'LFUful', '4143':'FRUruf', '3943': 'LFUful', '3739':'FRUruf'}
    rotationNeed= ''
    # If we have the desired pattern, we pull it out, get the rotation, and perform it
    for pattern in piecesToCheck:
        if(cube[40] == cube[pattern[0]] == cube[pattern[1]]):
            pieces = str(pattern[0]) + str(pattern[1])
            rotationNeed = rotationTypes.get(pieces)
            break
    result = doRotation(cube, rotationNeed)
    rotations += rotationNeed
    return result['cube'], rotations

# Does a possible Line rotation
def doPossibleLineRotation(cube, rotations):
    # Pieces that form the Line on top
    piecesToCheck = [[37,43],[39,41]]
    rotationTypes = {'3743' : 'RBUbur', '3941': 'FRUruf'}
    rotationNeed = ''
    # Depending on which line formation, we determine which rotation and do it
    for pattern in piecesToCheck:
        if(cube[40] == cube[pattern[0]] == cube[pattern[1]]):
            pieces = str(pattern[0]) + str(pattern[1])
            rotationNeed = rotationTypes.get(pieces)
            break
    result = doRotation(cube, rotationNeed)
    rotations += rotationNeed
    return result['cube'], rotations
# Determines if the cube is a dot or not
def isDot(cube):
    numsToCheck = [39,37,41,43]
    count = 0
    for num in numsToCheck:
        if(cube[num] == cube[40] and count < 1): return False
        elif(cube[num] == cube[40]): count += 1
    return True
# Determines if we are currently in the L type of top face
def isL(cube):
    piecesToCheck = [[37,41],[41,43],[39,43],[37,39]]
    for pattern in piecesToCheck:
        if(cube[40] == cube[pattern[0]] == cube[pattern[1]]):return True
    return False

# Determines if we are currently in the line type of face
def isLine(cube):
    piecesToCheck = [[37,43],[39,41]]
    for pattern in piecesToCheck:
        if(cube[40] == cube[pattern[0]] == cube[pattern[1]]): return True
    return False

# Checks if the top cross is done at the time
def checkIfTopCrossDone(cube):
    if(cube[40] == cube[41] == cube[39] == cube[43] == cube[37]): return True
    return False
 
 # Checks if the top face is done at the time
def checkIfTopDone(cube): 
    if(checkIfTopCrossDone(cube) and (cube[40] == cube[44] == cube[42] == cube[38] == cube[36])): return True
    return False

# Facilitates the solving of the top face
def solveTopSide(cube,rotations):
    # Feeds info to other type of top side function
    topLayerSolved = solve_TopSide(rotations['cube'], rotations['rotations'])
    rotations['rotations'] = topLayerSolved['rotations']; rotations['cube'] = topLayerSolved['cube']
    # Ensures that the top side was actually rotated
    if(not checkIfTopDone(rotations['cube'])):
        return fixRotation(rotations,'the top side')
    rotations['status'] = 'ok'
    return rotations
    return cube, rotations
    
# Does the looping while we are trying to solve the top face
def solve_TopSide(cube,rotations):
    # Loops until the top face is done
    while(not checkIfTopDone(cube)):
        if(isFish(cube)):
            cube, rotations = doFishRotation(cube, rotations)
        else:
            cube, rotations = doCrossRotation(cube, rotations)
    return {'cube' : cube, 'rotations' : rotations}

# Checks if top face is a cross    
def isCross(cube):
    nums = [36, 38, 42, 44]
    for num in nums:
        if(cube[num] == cube[40]):
            return False
    return True

# Do cross rotation based on certain pieces  
def doCrossRotation(cube,rotations):
    indexesToLookAt = [2,29,20,11]
    rotationsToThese = {2:'U',29:'',20:'u', 11:'uu'}
    rotationsNeeded = ''
    # Checks for specific cross pattern along with side patterns and perform rotation
    for index in indexesToLookAt:
        if(cube[index] == cube[40]):
            rotationNeeded = str(rotationsToThese.get(index)) + 'RUrURUUr'
            break
    result = doRotation(cube, rotationNeeded)
    rotations += rotationNeeded
    return result['cube'],rotations

# Checks if current top face is a fish   
def isFish(cube):
    nums = [36, 38, 42, 44]
    count = 0
    for num in nums:
        if(cube[num] == cube[40] and count != 0):
            return False
        elif(cube[num] == cube[40]):
            count += 1
    
    if(count != 1):
        return False
    return True
# Does a fish rotation   
def doFishRotation(cube,rotations):
    nums = [36, 38,42,44]
    rotationsToThese = {36:'u', 38:'uu', 42:'', 44:'U'}
    # Uses fish patterns to determine which rotations need to be done
    for num in nums:
        if(cube[num] == cube[40]):
            rotationNeeded = str(rotationsToThese.get(num)) + 'RUrURUUr'
            break
    result = doRotation(cube, rotationNeeded)
    rotations += rotationNeeded
    return result['cube'],rotations
# Checks if cube is fully done. Uses other checks to confirm rest of cube is done.
def checkIfFullCubeDone(cube):
    if(checkIfBottomDone(cube) and (checkIfMiddleDone(cube)) and checkIfTopDone(cube) and isTopCornersSolved(cube)):
        if((cube[28] == cube[31]) and (cube[1] == cube[4]) and (cube[10] == cube[13]) and (cube[19] == cube[22])):
            return True
    return False
# Checks if the top corners are aligned correctly
def isTopCornersSolved(cube):
    if((cube[27] == cube[29]) and (cube[0] == cube[2]) and (cube[9] == cube[11]) and (cube[18] == cube[20])):
        return True
    return False
# Finds where the corners are that can be aligned.
def whereTopCorner(cube):
    cubeNums = [[0,2],[9,11],[18,20],[27,29]] 
    middleNums = [4,13,22,31]
    # Loops through middle nums and corners nums to find a corner pair that matches a middle
    for middle in middleNums:
        for nums in cubeNums:
            if(cube[middle] == cube[nums[0]] == cube[nums[1]]):
                return [middle,[nums[0],nums[1]]]
    return [-1,[-1,-1]]   
# Rotating the corner based on where it is and location
def rotateTopCorner(cube,rotations, topCornerInfo): 
    # rotations to move corner pair correct
    positionRotations = {
            0:{4:'',13:'u',22:'uu',31:'U'},
            9:{4:'U',13:'',22:'u',31:'uu'},
            18:{4:'uu',13:'U',22:'',31:'u'},
            27:{4:'u',13:'uu',22:'U',31:''}       
            }
    # Rotations to properly move the corner pair once it is aligned.
    middleRotations = {4:'fUBuFUb',13:'rULuRUl',22:'bUFuBUf',31:'lURuLUr'}
    # If there is no corner pair, do a front rotation
    if(topCornerInfo[0] == -1):
        result = doRotation(cube, 'lURuLUr')
        rotations += 'lURuLUr'
    else:
        # Gets rotation and does it
        firstRotation = positionRotations.get(topCornerInfo[1][0])
        firstRotation = firstRotation.get(topCornerInfo[0])
        middleRotation = middleRotations.get(topCornerInfo[0])
        tempRotation = firstRotation + middleRotation
        result = doRotation(cube, tempRotation)
        rotations += tempRotation
    # Rotates the fish rotation
    cube,rotations = doFishRotation(result['cube'],rotations)
    return cube, rotations
# Facilitates the solving of the top corner
def solve_TopCorners(cube, rotations):
    while(not isTopCornersSolved(cube)):
        topCornerInfo = whereTopCorner(cube)
        cube, rotations = rotateTopCorner(cube, rotations, topCornerInfo)
    result = {'cube':cube,'rotations':rotations}
    return result
# Facilitates the solving and error checking of the top corners
def solveTopCorners(rotations):
    topCornersSolved = solve_TopCorners(rotations['cube'], rotations['rotations'])
    rotations['rotations'] = topCornersSolved['rotations']
    rotations['cube'] = topCornersSolved['cube']    
    if(not isTopCornersSolved(rotations['cube'])):
        return fixRotation(rotations,'the top corners')
    rotations['status'] = 'ok'
    return rotations
# Checks where the top layer that is done ois
def whereTopLayerAlligned(cube):
    topLayers = [[0,1,2],[9,10,11],[18,19,20],[27,28,29]]
    middleNums = [4,13,22,31]
    # Goes through layer and middle nums to find where it is to rotate
    for layers in topLayers:
        for middleNum in middleNums:
            if(cube[middleNum] == cube[layers[0]] == cube[layers[1]] == cube[layers[2]]):
                return [middleNum,layers[1]]
    return [-1,-1]
# Does a rotation to eventually move to solved cube
def rotateToFull(cube,rotations, topInfo):
    # Rotations to move layer that is complete to correct position
    positionRotations = {
            1:{4:'',13:'u',22:'uu',31:'U'},
            10:{4:'U',13:'',22:'u',31:'uu'},
            19:{4:'uu',13:'U',22:'',31:'u'},
            28:{4:'u',13:'uu',22:'U',31:''}       
            }
    # Rotations across from the layer that is done
    middleRotations = {4:'BBUlRBBrLUBB',13:'LLUfBLLbFULL',22:'FFUrLFFlRUFF',31:'RRUbFRRfBURR'}
    #If there is no layer complete, do a random front rotation
    if(topInfo[0] == -1):
        result = doRotation(cube, middleRotations.get(22))
        rotations += middleRotations.get(22)
    else:
        # Do a rotation across from complete
        tempRotations = positionRotations.get(topInfo[1])
        tempRotations = tempRotations.get(topInfo[0])
        tempRotations = tempRotations + middleRotations.get(topInfo[0])
        result = doRotation(cube, tempRotations)
        rotations += tempRotations
    return result['cube'], rotations
# Facilitates the solving of the full cube
def solve_FullCube(cube, rotations):
    while(not checkIfFullCubeDone(cube)):
        layerInfo = whereTopLayerAlligned(cube)
        cube, rotations = rotateToFull(cube, rotations, layerInfo)
    result = {'cube':cube,'rotations':rotations}
    return result
# Facilitates the solving and error checking of full cube.
def solveFullCube(rotations):
    fullSolved = solve_FullCube(rotations['cube'], rotations['rotations'])
    rotations['rotations'] = fullSolved['rotations']
    rotations['cube'] = fullSolved['cube']    
    if(not checkIfFullCubeDone(rotations['cube'])):
        return fixRotation(rotations,'the full cube')
    rotations['status'] = 'ok'
    return rotations
# Removes rotations and cubes and does the correct error.
def fixRotation(rotations,type):
    rotations['status'] = 'error : Unable to solve ' + type + ' from this Rubiks cube'
    del rotations['cube']
    del rotations['rotations']
    return rotations