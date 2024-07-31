import unittest
import rubik.solve as solve
import rubik.rotate as rotate

class solveBottomCrossTest(unittest.TestCase):
    #Test Lists (Iteration 2)
    # 001: Ensure that the cube is validated for cube length
    # 002 Ensure that the cube is validated for color sequences
    # 003 Ensure that the cube is validated for middle colors
    # 004: Check that function gets rotations to daisy
    # 005: Check that the function does rotations to front face being rotated down to downward-cross.
    # 006: Check that the function does rotations to Right face being rotated down to downward-cross.
    # 007: Check that the function does rotations to Left face being rotated down to downward-cross.
    # 008: Check that the function does rotations to Right face being rotated down to downward-cross.
    # 009: Check that the function does rotations to correctly make Rubik's cube downward-cross
    
    def test_solve_001_Validation(self):
        input = {}
        input['op'] = 'solve'
        input['cube'] = 'fsfs'
        
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
        
    def test_solve_004_isAlreadyInCross(self):
        input = {}
        input['op'] = 'solve'
        input['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        
        expected = {}
        expected['status'] = 'ok'
        expected['rotations'] = ''
        
        actualResult = solve._solve(input)
        self.assertEqual(expected.get('status'), actualResult.get('status'))
        self.assertEqual(expected.get('rotations'), actualResult.get('rotations'))
        
    def test_solve_005_getDaisy(self):
        input = {}
        input['op'] = 'solve'
        input['cube'] = 'ooowbrrgywobwrggygwgbwgryywrwybobgywyrroybbybgorbwgoro'
        
        expected = {}
        expected['status'] = 'ok'
        expected['rotations'] = 'lfrb'
        
        actualResult = solve.solveDaisy(input['cube'])
        self.assertEqual(expected.get('status'), actualResult.get('status'))
        self.assertEqual(expected.get('rotations'), actualResult.get('rotations'))
        
    def test_solve_006_solveFFDown(self):
        input = {}
        input['cube'] = 'ggbggowrowowyogyorgboobrbbggrygryrybwwrwywowroybbwbyry'
        input['op'] = 'solve'
        
        expected = {}
        expected['status'] = 'ok'
        expected['rotations'] = 'FF'
        
        rotations = ''
        actualResult = solve.FrontFaceDown(input['cube'], rotations, input['cube'][49])

        self.assertEqual(expected.get('rotations'), actualResult[0])
        
    def test_solve_007_solveRFDown(self):
        input = {}
        input['cube'] = 'orwoggbggbowyogyorgboobrbbggrygryrywwwrwywbyorwobwbyry'
        input['op'] = 'solve'
        
        expected = {}
        expected['rotations'] = 'ok'
        expected['rotations'] = 'RR'
        
        rotations = ''
        actualResult = solve.RightFaceDown(input['cube'], rotations, input['cube'][49])

        self.assertEqual(expected.get('rotations'), actualResult[0])
        
    def test_solve_008_solveBFDown(self):
        input = {}
        input['cube'] = 'orbogobggroygoywobgbogbrwbggrygryrywwwowybbyyrwrbwwyro'
        input['op'] = 'solve'
        
        expected = {}
        expected['status'] = 'ok'
        expected['rotations'] = 'BB'
        
        rotations = ''
        actualResult = solve.BackFaceDown(input['cube'], rotations, input['cube'][49])

        self.assertEqual(expected.get('rotations'), actualResult[0])

    
    def test_solve_009_solveLFDown(self):
        input = {}
        input['cube'] = 'bryogobggorbgogwogrorrbgobggbwyryyywybyryyowbrwrbwwoww'
        input['op'] = 'solve'
        
        expected = {}
        expected['status'] = 'ok'
        expected['rotations'] = 'ULL'
        
        rotations = ''
        actualResult = solve.LeftFaceDown(input['cube'], rotations, input['cube'][49])

        self.assertEqual(expected.get('rotations'), actualResult[0])
        
    def test_solve_010_solveCube(self):
        input = {}
        input['cube'] = 'ooowbrrgywobwrggygwgbwgryywrwybobgywyrroybbybgorbwgoro'
        input['op'] = 'solve'
        
        expected = {}
        expected['status'] = 'ok'
        expected['rotations'] = 'lfrbuFFRRBBLL'
        
        actualResult = solve._solve(input)
        self.assertEqual(expected.get('rotations'), actualResult.get('rotations'))
    
    def test_solve_011_TestCube000(self):
        input = {}
        input['cube'] = 'grwbowwwogoorywbobbyyyryrwgwgooggrryrbgrbbwbrooyywgbgy'
        input['op'] = 'solve'
    
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['cube'] = input.get('cube')
        rotateInput['dir'] = actualResult.get('rotations')
        rotateInput['op'] = 'rotate'
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfDownCrossDone(result.get('cube')))
        
    def test_solve_012_TestCube010(self):
        input = {}
        input['cube'] = 'owrwbgyrrybbogboyyyrborrgwrowggwogbbwogbogbywwywyygorr'
        input['op'] = 'solve'
    
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['cube'] = input.get('cube')
        rotateInput['dir'] = actualResult.get('rotations')
        rotateInput['op'] = 'rotate'
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfDownCrossDone(result.get('cube')))
    
    def test_solve_013_TestCube020(self):
        input = {}
        input['cube'] = 'bbwyrwbggrgyboowgybrwwbgryrbbgygryrwgooywryooobrwywgoo'
        input['op'] = 'solve'
    
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['cube'] = input.get('cube')
        rotateInput['dir'] = actualResult.get('rotations')
        rotateInput['op'] = 'rotate'
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfDownCrossDone(result.get('cube')))
    
    def test_solve_014_TestCube030(self):
        input = {}
        input['cube'] = 'gbrorybbobgobwggoogwyoybrwgbwwwoyyryoryggyrrwworgbrwyb'
        input['op'] = 'solve'
    
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['cube'] = input.get('cube')
        rotateInput['dir'] = actualResult.get('rotations')
        rotateInput['op'] = 'rotate'
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfDownCrossDone(result.get('cube')))    
    def test_solve_015_TestCube040(self):
        input = {}
        input['cube'] = 'wbygwwyogryybbwwrgbyogooryygrgbroroobrwwgwbgobrryygwbo'
        input['op'] = 'solve'
    
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['cube'] = input.get('cube')
        rotateInput['dir'] = actualResult.get('rotations')
        rotateInput['op'] = 'rotate'
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfDownCrossDone(result.get('cube')))
    
    def test_solve_016_TestCube050(self):
        input = {}
        input['cube'] = 'yyorbgybrwbrwrogoygyowgrggobbbgwbwybrgowoyrwbwoyryrgow'
        input['op'] = 'solve'
    
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['cube'] = input.get('cube')
        rotateInput['dir'] = actualResult.get('rotations')
        rotateInput['op'] = 'rotate'
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfDownCrossDone(result.get('cube')))
    
    def test_solve_017_TestCube060(self):
        input = {}
        input['cube'] = 'wybwyrbyyoobgwwrggrwwbbbobwryyrgorygbrgroboowoggwroygy'
        input['op'] = 'solve'
    
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['cube'] = input.get('cube')
        rotateInput['dir'] = actualResult.get('rotations')
        rotateInput['op'] = 'rotate'
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfDownCrossDone(result.get('cube')))
    
    def test_solve_018_TestCube070(self):
        input = {}
        input['cube'] = 'ygowwowrygbgggbrybowrrywgrbboggrbworyrywbgbywoyoyobrow'
        input['op'] = 'solve'
    
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['cube'] = input.get('cube')
        rotateInput['dir'] = actualResult.get('rotations')
        rotateInput['op'] = 'rotate'
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfDownCrossDone(result.get('cube')))
    
    def test_solve_019_TestCube080(self):
        input = {}
        input['cube'] = 'ogwybgbyrgygborwrowbbgwowwygybwggboryoyorwrwrgborybory'
        input['op'] = 'solve'
    
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['cube'] = input.get('cube')
        rotateInput['dir'] = actualResult.get('rotations')
        rotateInput['op'] = 'rotate'
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfDownCrossDone(result.get('cube')))
    
    def test_solve_020_TestCube090(self):
        input = {}
        input['cube'] = 'wwgorgyyboworyyogbwbgbbwgobrgryobygwywrogryorbrwbwygro'
        input['op'] = 'solve'
    
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['cube'] = input.get('cube')
        rotateInput['dir'] = actualResult.get('rotations')
        rotateInput['op'] = 'rotate'
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfDownCrossDone(result.get('cube')))