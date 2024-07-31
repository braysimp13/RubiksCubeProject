import unittest
import rubik.solve as solve
import rubik.rotate as rotate

class solveFullTest(unittest.TestCase):
    # Failed Test case from Iteration 5
    def test_solve_001_ReviewTestCase(self):
        input = {}
        input['cube'] = 'yrwbyooygbrryoyorrwgogboogwbogbwwbyyrwygrwwoggrbwgbrby'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfTopDone(result['cube']))
        self.assertEqual(True, solve.checkIfBottomDone(result['cube']))
        
    def test_solve_002_isCubeDone(self):
        cube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        self.assertEqual(True, solve.checkIfFullCubeDone(cube))
        
    def test_solve_003_isTopCornerDone(self):
        cube = 'rbrrrrrrrgogggggggogooooooobrbbbbbbbyyyyyyyyywwwwwwwww'
        self.assertEqual(True, solve.isTopCornersSolved(cube))
        
    def test_solve_004_findCorrectTopCorner(self):
        cube = 'ggobbbbbbbbgrrrrrroobggggggrrrooooooyyyyyyyyywwwwwwwww'
        topCornerInfo = [13,[27,29]]
        
        self.assertEqual(topCornerInfo, solve.whereTopCorner(cube))
        
    def test_solve_005_rotateTopCorner(self):
        cube = 'ggobbbbbbbbgrrrrrroobggggggrrrooooooyyyyyyyyywwwwwwwww'
        rotations = ''
        topCornerInfo = [13,[27,29]]
        cube,rotations = solve.rotateTopCorner(cube, rotations,topCornerInfo)
        
        self.assertEqual(True, solve.isTopCornersSolved(cube))
        
    def test_solve_006_fullRotateTop(self):
        input = {}
        input['cube'] = 'rrooooooobbgbbbbbboorrrrrrrggbggggggyyyyyyyyywwwwwwwww'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.isTopCornersSolved(result['cube']))
        
    def test_solve_007_fullRotateTop(self):
        input = {}
        input['cube'] = 'rbgobobbbwbbgrwyyywoyggwogrooyroygrobbrwyrgyowwrywgwrg'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.isTopCornersSolved(result['cube']))
        
    def test_solve_008_fullRotateTop(self):
        input = {}
        input['cube'] = 'rbbbbyrgbyrgororrorgowgbgrbgoyoowwgywrwgywgyobwwywyoby'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.isTopCornersSolved(result['cube']))
        
    def test_solve_009_fullRotateTop(self):
        input = {}
        input['cube'] = 'owrbbowobgbwgrwrbwbyoggrryybrgwoyryoygogyoybygwwrwrbog'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.isTopCornersSolved(result['cube']))
        
    def test_solve_010_fullRotateTop(self):
        input = {}
        input['cube'] = 'yowrbygbobwgbrgwobrgrygbrbgywbroyywybrwryoogoroggwyoww'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.isTopCornersSolved(result['cube']))
        
    def test_solve_011_findAllignment(self):
        cube = 'rorbbbbbbgggrrrrrroboggggggbrbooooooyyyyyyyyywwwwwwwww'
        result = solve.whereTopLayerAlligned(cube)
        self.assertEqual(22,result[0])
        self.assertEqual(10,result[1])
        
    def test_solve_012_doAllingmentRotation(self):
        cube = 'brboooooororbbbbbbgggrrrrrroboggggggyyyyyyyyywwwwwwwww'
        result = solve.rotateToFull(cube,'',[31,19])
        self.assertEqual('orooooooobobbbbbbbrbrrrrrrrgggggggggyyyyyyyyywwwwwwwww', result[0])
        
    def test_solve_013_doAllignmentRotationToFull(self):
        cube = 'orooooooobobbbbbbbrbrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        result = solve.rotateToFull(cube, '', [31,28])
        self.assertEqual(True, solve.checkIfFullCubeDone(result[0]))
        
    def test_solve_014_doSolveFromInput(self):
        input = {}
        input['cube'] = 'yowrbygbobwgbrgwobrgrygbrbgywbroyywybrwryoogoroggwyoww'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfFullCubeDone(result['cube']))
    def test_solve_015_doSolveFromInput(self):
        input = {}
        input['cube'] = 'rwowboroyybryryboobwgrggwgbrbyrogwwywowryygbgbborwgoyg'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfFullCubeDone(result['cube']))
    def test_solve_016_doSolveFromInput(self):
        input = {}
        input['cube'] = 'wrryboorobrowroggrbwwbgyyyrgwgoobbywrgybygobwbwygwoyrg'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfFullCubeDone(result['cube']))
    def test_solve_017_doSolveFromInput(self):
        input = {}
        input['cube'] = 'gygobbygbrwwrrowgbrbgwgyyoywoyboggroowbyygorwbrowwyrbr'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfFullCubeDone(result['cube']))
    def test_solve_018_doSolveFromInput(self):
        input = {}
        input['cube'] = 'owbrbgoygwwbrrwywrobroggyowyowyoyrobbrwyyrggrybobwbggg'
        input['op'] = 'solve'
        
        actualResult = solve._solve(input)
        
        rotateInput = {}
        rotateInput['op'] = 'rotate'
        rotateInput['cube'] = input['cube']
        rotateInput['dir'] = actualResult['rotations']
        
        result = rotate._rotate(rotateInput)
        self.assertEqual(True, solve.checkIfFullCubeDone(result['cube']))
    
    def test_solve_019_checkError(self):
        rotations = {}
        rotations['cube'] = ''
        rotations['status'] = ''
        rotations['rotations'] = ''
        
        status = 'error : Unable to solve the top corners from this Rubiks cube'
        self.assertEqual(status,solve.fixRotation(rotations, 'the top corners').get('status'))