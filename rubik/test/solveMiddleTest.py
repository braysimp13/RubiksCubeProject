import unittest
import rubik.solve as solve
import rubik.rotate as rotate

'''
Created on Oct 16, 2022

@author: brayd
'''

class solveBottomTest(unittest.TestCase):
    def test_solve_001_IsMiddleComplete(self):
        cube = 'yggrrrrrroyrgggggggyyooooooobrbbbbbbboyyyrbyywwwwwwwww'
        
        self.assertEqual(True, solve.checkIfMiddleDone(cube))
        
    def test_solve_002_checkForAFrontFaceTop(self):
        cube = 'ooygoroooryrbbybbbyyobrrrrrbggygrgggyoboygybgwwwwwwwww'
        placeFrom = 1 
        placeTo = 5
        
        expectedResult = 'bgygoooooryobbybbbbbybrrrrrggyygrgggoryyyorogwwwwwwwww'
        
        result,rotations = solve.rotate_immediate_rotation(cube, placeFrom, placeTo, '')
        
        self.assertEqual(expectedResult, result)
        
    def test_solve_003_checkForAFrontFaceTop(self):
        cube = 'rgoygggggyyooooooobyybbbbbbrybrrrrrrgoygybyrgwwwwwwwww'
        placeFrom = 1 
        placeTo = 3
        
        expectedResult = 'rygggggggygyoooooogrobbbbbbbybrrrrrryyooyyybrwwwwwwwww'
        
        result,rotations = solve.rotate_immediate_rotation(cube, placeFrom, placeTo, '')
        
        self.assertEqual(expectedResult, result)
        
    def test_solve_004_checkForARightFaceTop(self):
        cube = 'bggygrgggooygoroooryrbbybbbyyobrrrrrbggoybyoywwwwwwwww'
        placeFrom = 10 
        placeTo = 14
        
        expectedResult = 'ggyygrgggbgygoooooryobbybbbbbybrrrrryogryooyrwwwwwwwww'
        
        result,rotations = solve.rotate_immediate_rotation(cube, placeFrom, placeTo, '')
        
        self.assertEqual(expectedResult, result)
        
    def test_solve_005_checkForARightFaceTop(self):
        cube = 'rybrrrrrrrgoygggggyyooooooobyybbbbbbybgoyrggywwwwwwwww'
        placeFrom = 10 
        placeTo = 12
        
        expectedResult = 'bybrrrrrrrygggggggygyoooooogrobbbbbboyryybyoywwwwwwwww'
        
        result,rotations = solve.rotate_immediate_rotation(cube, placeFrom, placeTo, '')
        
        self.assertEqual(expectedResult, result)
        
    def test_solve_006_checkForABackFaceTop(self):
        cube = 'yyobrrrrrbggygrgggooygoroooryrbbybbbgbygyoboywwwwwwwww'
        placeFrom = 19 
        placeTo = 23
        
        expectedResult = 'bbybrrrrrggyygrgggbgygoooooryobbybbbgoroyyyrowwwwwwwww'
        
        result,rotations = solve.rotate_immediate_rotation(cube, placeFrom, placeTo, '')
        
        self.assertEqual(expectedResult, result)
        
    def test_solve_007_checkForABackFaceTop(self):
        cube = 'byybbbbbbrybrrrrrrrgoygggggyyooooooogrybygyogwwwwwwwww'
        placeFrom = 19 
        placeTo = 21
        
        expectedResult = 'grobbbbbbbybrrrrrrrygggggggygyoooooorbyyyooyywwwwwwwww'
        
        result,rotations = solve.rotate_immediate_rotation(cube, placeFrom, placeTo, '')
        
        self.assertEqual(expectedResult, result)
        
    def test_solve_008_checkForALeftFaceTop(self):
        cube = 'ryrbbybbbyyobrrrrrbggygrgggooygoroooyoybyoggbwwwwwwwww'
        placeFrom = 28 
        placeTo = 32
        
        expectedResult = 'ryobbybbbbbybrrrrrggyygrgggbgygoooooryooyrgoywwwwwwwww'
        
        result,rotations = solve.rotate_immediate_rotation(cube, placeFrom, placeTo, '')
        
        self.assertEqual(expectedResult, result)
        
    def test_solve_009_checkForALeftFaceTop(self):
        cube = 'yyooooooobyybbbbbbrybrrrrrrrgoygggggyggryogbywwwwwwwww'
        placeFrom = 28 
        placeTo = 30
        
        expectedResult = 'ygyoooooogrobbbbbbbybrrrrrrrygggggggyoybyyryowwwwwwwww'
        
        result,rotations = solve.rotate_immediate_rotation(cube, placeFrom, placeTo, '')
        
        self.assertEqual(expectedResult, result)
        
    def test_solve_010_findCorrectMoves(self):
        cube = 'rryyrrrrroogggggggyggooooooobbbbbbbbyyrryyyybwwwwwwwww'
        
        expectedResult = {}
        expectedResult["found"] = True
        expectedResult["placeFrom"] = 28
        expectedResult['placeTo'] = 32
        
        result = solve.check_for_immediate_rotation(cube)
        
        self.assertEqual(expectedResult["found"], result["found"])
        self.assertEqual(expectedResult["placeFrom"], result["placeFrom"])
        self.assertEqual(expectedResult["placeTo"], result["placeTo"])
        
    def test_solve_011_findCorrectMoves(self):
        cube = 'oogyrrrrryggggggggobboooooorrybbbbbbyryyyybyrwwwwwwwww'
        
        expectedResult = {}
        expectedResult["found"] = True
        expectedResult["placeFrom"] = 19
        expectedResult['placeTo'] = 32
        
        result = solve.check_for_immediate_rotation(cube)
        
        self.assertEqual(expectedResult["found"], result["found"])
        self.assertEqual(expectedResult["placeFrom"], result["placeFrom"])
        self.assertEqual(expectedResult["placeTo"], result["placeTo"])
        
    def test_solve_012_findCorrectMoves(self):
        cube = 'yggyrrrrrobbggggggrryoooooooogbbbbbbbyyyyrryywwwwwwwww'
        
        expectedResult = {}
        expectedResult["found"] = True
        expectedResult["placeFrom"] = 10
        expectedResult['placeTo'] = 32
        
        result = solve.check_for_immediate_rotation(cube)
        
        self.assertEqual(expectedResult["found"], result["found"])
        self.assertEqual(expectedResult["placeFrom"], result["placeFrom"])
        self.assertEqual(expectedResult["placeTo"], result["placeTo"])
        
    def test_solve_013_findCorrectMoves(self):
        cube = 'obbyrrrrrrryggggggoogooooooyggbbbbbbrybyyyyrywwwwwwwww'
        
        expectedResult = {}
        expectedResult["found"] = True
        expectedResult["placeFrom"] = 1
        expectedResult['placeTo'] = 32
        
        result = solve.check_for_immediate_rotation(cube)
        
        self.assertEqual(expectedResult["found"], result["found"])
        self.assertEqual(expectedResult["placeFrom"], result["placeFrom"])
        self.assertEqual(expectedResult["placeTo"], result["placeTo"])
        
    def test_solve_014_movementRotation(self):
        cube = 'ryyrooooogyybbbbbbroyrrgrrroybogggggbygbygyrowwwwwwwww'
        
        expectedResult = {}
        expectedResult["found"] = True
        expectedResult["placeFrom"] = 1 
        expectedResult["placeTo"] = 3
        
        result = solve.check_for_possible_rotation(cube)
        
        self.assertEqual(expectedResult["found"], result["found"])
        self.assertEqual(expectedResult["placeFrom"], result["placeFrom"])
        self.assertEqual(expectedResult["placeTo"], result["placeTo"])
        
    def test_solve_015_movementRotation(self):
        cube = 'gyybbbbbbroyrrgrrroybogggggryyroooooybbryyoggwwwwwwwww'
        
        expectedResult = {}
        expectedResult["found"] = True
        expectedResult["placeFrom"] = 10 
        expectedResult["placeTo"] = 14
        
        result = solve.check_for_possible_rotation(cube)
        
        self.assertEqual(expectedResult["found"], result["found"])
        self.assertEqual(expectedResult["placeFrom"], result["placeFrom"])
        self.assertEqual(expectedResult["placeTo"], result["placeTo"])
        
    def test_solve_016_solveMiddle(self):
        input = {}
        input['cube'] = 'byrrbbywwwoyyroowobrrgggwrwgbowowbygygrrybyggobboworyg'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfMiddleDone(result['cube']))
        
    def test_solve_017_solveMiddle(self):
        input = {}
        input['cube'] = 'ywoobbrorybowrbbyogybygwbrrwybgogywwrrwoyrooggbyrwgggw'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfMiddleDone(result['cube']))
        
    def test_solve_018_solveMiddle(self):
        input = {}
        input['cube'] = 'grggbrybowrygrobywrgowgyboybrwooyobbywgbywryorowwwbggr'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfMiddleDone(result['cube']))
        
    def test_solve_019_solveMiddle(self):
        input = {}
        input['cube'] = 'byrgbowrggyybrrwbobwgggybgbooogowryoybrwyoybygwrrwrwow'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfMiddleDone(result['cube']))
        
    def test_solve_020_solveMiddle(self):
        input = {}
        input['cube'] = 'brogbwobbbyogryywrgorggrgowgwwyorboyygwoybowygrrywbrbw'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfMiddleDone(result['cube']))
        
        
    