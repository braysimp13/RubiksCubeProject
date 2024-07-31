import unittest
import rubik.solve as solve
import rubik.rotate as rotate

class solveTopTest(unittest.TestCase):
    def test_solve_001_checkIfTopCrossDone(self):
        cube = 'ywybbwogwgowororgrbobbgryrbygryorrygogoryybbowygbwwwwg'
        self.assertEqual(False, solve.checkIfTopCrossDone(cube))
        
    def test_solve_002_IdentifyDotRotation(self):
        cube = 'yyoooooooyyobbbbbbbyrrrrrrryygggggggbgybyorrgwwwwwwwww'
        self.assertEqual(True, solve.isDot(cube))
        
    def test_solve_003_IdentifyLRotation(self):
        cube = 'yrbrrrrrryggggggggoygooooooyyrbbbbbbrbyoyybyowwwwwwwww'
        self.assertEqual(True, solve.isL(cube))
        
    def test_solve_004_IdentifyLineRotation(self):
        cube = 'rbgbbbbbbyyorrrrrrygbggggggyyboooooooygryoyyrwwwwwwwww'
        self.assertEquals(True, solve.isLine(cube))
        
    def test_solve_005_DoDotRotation(self):
        cube = 'yyrooooooyyrbbbbbbgyorrrrrryybgggggggryoybogbwwwwwwwww'
        rotations = ''
        cube,rotations = solve.doPossibleDotRotation(cube, rotations)
        self.assertEquals(True, solve.isL(cube))
        
    def test_solve_006_DoLRotation(self):
        cube = 'ybygggggggoyooooooryrbbbbbbyybrrrrrrbggryyoyowwwwwwwww'
        rotations = ''
        cube,rotations = solve.doPossibleLRotation(cube, rotations)
        self.assertEqual(True, solve.isLine(cube))
        
    def test_solve_007_DoLineRotation(self):
        cube = 'yrorrrrrryyrggggggygooooooobygbbbbbbyyboybrygwwwwwwwww'
        rotations = ''
        cube,rotations = solve.doPossibleLineRotation(cube, rotations)
        self.assertEqual(True, solve.checkIfTopCrossDone(cube))
        
    def test_solve_008_solveTopCross(self):
        input = {}
        input['cube'] = 'bbbgbybbowwygryyrgrwwbgoygwowyyorrgogrgbyorrrwobowygwo'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfTopCrossDone(result['cube']))
    
    def test_solve_009_solveTopCross(self):
        input = {}
        input['cube'] = 'owyobbbbrgrgrrrgorwrrygwyooyyyboybbwbwogygbgorywowgwwg'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfTopCrossDone(result['cube']))
        
    def test_solve_010_solveTopCross(self):
        input = {}
        input['cube'] = 'ggwybbrgorborrrbwrbyowgbybggowoooyrywrygyyrybbwwgwoowg'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfTopCrossDone(result['cube']))
        
    def test_solve_011_solveTopCross(self):
        input = {}
        input['cube'] = 'gwwrbogoyorogrwryrbybbgryororwyowwwowbygybrggybbowgbyg'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfTopCrossDone(result['cube']))
        
    def test_solve_012_solveTopCross(self):
        input = {}
        input['cube'] = 'robgbgywrrwwyrywyoorrogbbobgggooroygybgwyrwgyobbrwbyww'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfTopCrossDone(result['cube']))
      
    def test_solve_013_checkForTopDown(self):
        cube = 'gryggggggbgyooooooobrbbbbbbgoyrrrrrryybyyyoyrwwwwwwwww'
        self.assertEqual(False,solve.checkIfTopDone(cube))  
        
    def test_solve_014_IdentifyCross(self):
        cube = 'gbrrrrrrryrbggggggygyooooooroybbbbbbgyoyyyoybwwwwwwwww'
        self.assertEquals(True, solve.isCross(cube))
        
    def test_solve_015_IdentityFish(self):
        cube = 'goyrrrrrrgryggggggbgyooooooobrbbbbbbbyryyyyyowwwwwwwww'
        self.assertEquals(True, solve.isFish(cube))
        
    def test_solve_016_rotateCross(self):
        cube = 'royrrrrrrgbrggggggyrbooooooygybbbbbboybyyygyowwwwwwwww'
        rotations = ''
        
        cube,rotations = solve.doCrossRotation(cube, rotations)
        
        self.assertEquals(True, solve.isFish(cube))
        
    def test_solve_017_rotateFish(self):
        cube = 'boyrrrrrrogyggggggrbgooooooorybbbbbbyygyyyrybwwwwwwwww'
        rotations = ''
        
        cube, rotations = solve.doFishRotation(cube, rotations)
        self.assertEqual(True, solve.checkIfTopDone(cube))
        
    def test_solve_018_rotateAbnormal(self):
        cube = 'oorrrrrrryryggggggobroooooogggbbbbbbyybyyyyybwwwwwwwww'
        rotations = ''
        
        cube, rotations = solve.doCrossRotation(cube, rotations)
        self.assertEqual(True, solve.isCross(cube))
        
    def test_solve_19_solveTop(self):
        input = {}
        input['cube'] = 'ryrwrorowywyygwbryororoyobwgwyrbgobwwgboybggbggrywbbog'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfTopDone(result['cube']))