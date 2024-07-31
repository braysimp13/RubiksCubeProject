import unittest
import rubik.solve as solve
import rubik.rotate as rotate

class solveBottomTest(unittest.TestCase):
    
    def test_solve_001_Validation(self):
        input = {}
        input['op'] = 'solve'
        input['cube'] = ''
        
        expected = {}
        expected['status'] = 'error: Cube is invalid.'
        
        actualResult = solve._solve(input)
        self.assertEqual(expected.get('status'), actualResult.get('status'))
        
    def test_solve_002_Validation(self):
        input = {}
        input['op'] = 'solve'
        input['cube'] = 'gowrgwrwygybgyooybybygbryywrbobwgowbgyoorgwwrwrgbrobrr'
        
        expected = {}
        expected['status'] = 'error: Cube is invalid.'
        
        actualResult = solve._solve(input)
        self.assertEqual(expected.get('status'), actualResult.get('status'))
        
    def test_solve_003_Validation(self):
        input = {}
        input['op'] = 'solve'
        input['cube'] = 'gowrbwrwygyggyooybybygbryywrbobwgowbgyoorgwwrwrgboobrr'
        
        expected = {}
        expected['status'] = 'error: Rubik string does have unique middle colors for each face of the cube.'
        
        actualResult = solve._solve(input)
        self.assertEqual(expected.get('status'), actualResult.get('status'))
        
    def test_solve_004_CheckIfBottomDone(self):
        input = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        self.assertEqual(True, solve.checkIfBottomDone(input))
    
    
    def test_solve_005_SolveBottomLayer(self):
        input = {}
        input['op'] = 'solve'
        input['cube'] = 'bbwyrwbggrgyboowgybrwwbgryrbbgygryrwgooywryooobrwywgoo'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfBottomDone(result['cube'])) 
        
    def test_solve_006_CheckTopMove(self):
        input = {}
        input['op'] = 'solve'
        input['cube'] = 'bbwbbybbbrrygrryrrgrrgggggggooooooooyyoyybyybwwrwwwwww'
        
        actualResult = solve._solve(input)
        
        solveCube = {}
        solveCube['op'] = 'rotate'
        solveCube['cube'] = 'bbwbbybbbrrygrryrrgrrgggggggooooooooyyoyybyybwwrwwwwww'
        solveCube['dir'] = actualResult['rotations']
        result = rotate._rotate(solveCube)
        self.assertEqual(True, solve.checkIfBottomDone(result['cube']))
    
        
    def test_solve_007_CheckBottomMove(self):
        input = {}
        input['op'] = 'solve'
        input['cube'] = 'rbybbybbroyyrrrwrrgorgggggggbbooooooyyoyygyrbwwbwwwwww'
        
        actualResult = solve._solve(input)
        
        solveCube = {}
        solveCube['op'] = 'rotate'
        solveCube['cube'] = 'rbybbybbroyyrrrwrrgorgggggggbbooooooyyoyygyrbwwbwwwwww'
        solveCube['dir'] = actualResult['rotations']
        result = rotate._rotate(solveCube)
        self.assertEqual(True, solve.checkIfBottomDone(result['cube']))
    
    def test_solve_008_CheckTopFaceMove(self):
        input = {}
        input['op'] = 'solve'
        input['cube'] = 'gbrbbrbbybyybrrrrrgroggggggborooooooyyoyygyywwwbwwwwww'
        
        actualResult = solve._solve(input)
        
        solveCube = {}
        solveCube['op'] = 'rotate'
        solveCube['cube'] = 'gbrbbrbbybyybrrrrrgroggggggborooooooyyoyygyywwwbwwwwww'
        solveCube['dir'] = actualResult['rotations']
        result = rotate._rotate(solveCube)
        self.assertEqual(True, solve.checkIfBottomDone(result['cube']))
        
    def test_solve_009_SolveBottomLayer(self):
        input = {}
        input['op'] = 'solve'
        input['cube'] = 'owbowrwyoogrgbgyyrybwoywybygbwggwobrrrbyoygrwbrborogwg'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfBottomDone(result['cube'])) 
        
    def test_solve_010_SolveBottomLayer(self):
        input = {}
        input['op'] = 'solve'
        input['cube'] = 'rgoybyrbobwyorobygggywgwobrbygrorwwgrrogygwoyyrwbwbbow'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfBottomDone(result['cube']))
        
    def test_solve_011_SolveBottomLayer(self):
        input = {}
        input['op'] = 'solve'
        input['cube'] = 'ryowgbwgwyorowrobywybbbygyryrbgygwooorgwowyoggrbgrwbbr'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfBottomDone(result['cube']))  
        
    def test_solve_012_SolveBottomLayer(self):
        input = {}
        input['op'] = 'solve'
        input['cube'] = 'wbygowyogoygrwwoggrrrbryygrboogywywbwbwbbrbybrywogrgoo'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfBottomDone(result['cube'])) 
        
    def test_solve_013_SolveBottomLayer(self):
        input = {}
        input['op'] = 'solve'
        input['cube'] = 'bgywrowrwgyoygbrywgbrworbwryoobboyrbbowgygywooggywbgrr'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfBottomDone(result['cube'])) 
        
    def test_solve_014_SolveBottomLayer(self):
        input = {}
        input['op'] = 'solve'
        input['cube'] = 'rgywwbgyrgggyoybwowgboyobrbwwybrborrryoogrgoowrywbgybw'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfBottomDone(result['cube'])) 
