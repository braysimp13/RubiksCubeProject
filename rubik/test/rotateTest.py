import unittest
import rubik.rotate as rotate

class RotateTest(unittest.TestCase):
    #Test number lists and Descriptions
    # Cube tests:
    # 001: Testing for character count of rubik string
    # 002: Testing if the characters in the cube string are valid
    # 003: Testing if the values in the middle of each face are unique
    # 004:Checking that the program can catch an invalid directional string
    # 005: Checking that the program can identify that the empty directional string is not invalid
    # 006: Checking to see that the program can catch that the a value of None is not invalid
    # 007: Checking to see that the program can catch that the lack of a direction key is not invalid
    # 008: Checking that the parameters actually has a cube parameter within it.
    #
    # Rotate tests:
    # 001: Checking to see that the program can do a front clockwise rotation
    # 002: Checking to see that the program can do a front counter-clockwise rotation
    # 003: Checking to see if the program can do a right clockwise rotation.
    # 004: Checking to see that the program can do a right counter-clockwise rotation
    # 005: Checking to see that program can do a back clockwise rotation
    # 006: Checking to see that the program can do a back counter-clockwise rotation
    # 007: Checking to see that the program can do a left clockwise rotation.
    # 008: Checking to see that the program can do a left counter-clockwise rotation
    # 009: Checking to see that the program can do an up clockwise rotation.
    # 010: Checking to see that the program can do an up counter-clockwise rotation.
    # 011: Checking to see that the program can do a down clockwise rotation.
    # 012: Checking to see that the program can do a down counter-clockwise rotation.
    
    def setUp(self):
        pass


    def tearDown(self):
        pass 
    #Cube validity tests
    
    #test is for checking the validity of a cube that does not have 54 characters
    def test_cube_001_CubeStringLengthTest(self):
        input = {}
        input['op'] = 'rotate'
        input['cube'] = 'ygrwbgyggbobrryrrwobrggrgwywrorbbggwwbyybwwooyowboo'
        input['dir'] = 'F'
        
        expected = {}
        expected['cube'] = 'ygrwbgyggbobrryrrwobrggrgwywrorbbggwwbyybwwooyowboo'
        expected['status'] = 'error: Cube is invalid.'
        
        actualResult = rotate._rotate(input)
        self.assertEqual(expected.get('status'), actualResult.get('status'))
      
    #test is used to check if the actual characters in the Rubik string are valid  
    def test_cube_002_CubeCharacterValidity(self):
        input = {}
        input['op'] = 'rotate'
        input['cube'] = 'gowrgwrwygybgyooybybygbryywrbobwgowbgyoorgwwrwrgbrobrr'
        input['dir'] = 'F'
        
        expected = {}
        expected['status'] = 'error: Cube is invalid.'
        
        actualResult = rotate._rotate(input)
        self.assertEqual(expected.get('status'), actualResult.get('status'))
    
    #test is used to check the values in the middle of each face are unique
    def test_cube_003_ValidMiddle(self):
        input = {}
        input['op'] = 'rotate'
        input['cube'] = 'gowrbwrwygyggyooybybygbryywrbobwgowbgyoorgwwrwrgboobrr'
        input['dir'] = 'F'
        
        expected = {}
        expected['status'] = 'error: Rubik string does have unique middle colors for each face of the cube.'
        
        actualResult = rotate._rotate(input)
        self.assertEqual(expected.get('status'), actualResult.get('status'))
        
    #test is used to check that the direction is valid. This is to check that it is either a string or an empty string that has valid rotational directions
    #this specific passes a wrong direction
    def test_cube_004_ValidDirectionalString(self):
        
        input = {}
        input['op'] = 'rotate'
        input['cube'] = 'gowrgwrwygybgyooybybygbryywrbobwgowbgyoorgwwrwrgboobrr'
        input['dir'] = 'q'
        
        expected = {}
        expected['status'] = 'error: Direction string contains an invalid character'
        
        actualResult = rotate._rotate(input)
        self.assertEqual(expected.get('status'), actualResult.get('status'))
    
    #Tests if the dir key is left to be an empty string. It still should rotate as a Front Clockwise.
    def test_cube_005_EmptyDirectionalString(self):
        input = {}
        input['op'] = 'rotate'
        input['cube'] = 'gowrgwrwygybgyooybybygbryywrbobwgowbgyoorgwwrwrgboobrr'
        input['dir'] = ''
        
        expected = {}
        expected['cube'] = 'gowrgwrwygybgyooybybygbryywrbobwgowbgyoorgwwrwrgboobrr'
        expected['status'] = 'ok'
        
        actualResult = rotate._rotate(input)
        self.assertEqual(expected.get('status'), actualResult.get('status'))
        
    #Tests if the dir key is left to be none. It still should rotate as a Front Clockwise.
    def test_cube_006_NoDirectionalString(self):
        input = {}
        input['op'] = 'rotate'
        input['cube'] = 'gowrgwrwygybgyooybybygbryywrbobwgowbgyoorgwwrwrgboobrr'
        input['dir'] = None
        
        expected = {}
        expected['cube'] = 'gowrgwrwygybgyooybybygbryywrbobwgowbgyoorgwwrwrgboobrr'
        expected['status'] = 'ok'
        
        actualResult = rotate._rotate(input)
        self.assertEqual(expected.get('status'), actualResult.get('status'))
        
    #Tests if the user forgets to add a direction. It should still automatically. It still should rotate as a Front Clockwise.
    def test_cube_007_NoDirectionalKey(self):
        input = {}
        input['op'] = 'rotate'
        input['cube'] = 'gowrgwrwygybgyooybybygbryywrbobwgowbgyoorgwwrwrgboobrr'
        
        expected = {}
        expected['cube'] = 'gowrgwrwygybgyooybybygbryywrbobwgowbgyoorgwwrwrgboobrr'
        expected['status'] = 'ok'
        
        actualResult = rotate._rotate(input)
        self.assertEqual(expected.get('status'), actualResult.get('status'))
        
    def test_cube_008_NoCubeKey(self):
        input = {}
        input['op'] = 'rotate'
        
        expected = {}
        expected['status'] = 'error: Cube parameter does not exist'
        
        actualResult = rotate._rotate(input)
        self.assertEqual(expected.get('status'), actualResult.get('status'))
        
    # Rotation Tests

    #Tests if the cube is able to do a forward clockwise rotation
    def test_rotate_001_FrontClockwise(self):
        input = {}
        input['op'] = 'rotate'
        input['cube'] = 'yygowobworggborbyywwwwybgyyryorrwbgrbboggogbwygwrboorr'
        input['dir'] = 'F'       
        
        expected = {}
        expected['cube'] = 'boywwyooggggborwyywwwwybgyyryyrrgbgwbboggorwobbrrboorr'
        expected['status'] = 'ok'
        
        actualResult = rotate._rotate(input)
        self.assertEqual(expected.get('cube'), actualResult.get('cube'))
        self.assertEqual(expected.get('status'), actualResult.get('status'))
        
    def test_rotate_002_FrontCounterClockwise(self):
        input = {}
        input['op'] = 'rotate'
        input['cube'] = 'rryyyborbrgyobwyrggywowooowbbgygrbybobowrwwggybrgowrgw'
        input['dir'] = 'f'       
        
        expected = {}
        expected['cube'] = 'ybbryrryorgybbwyrggywowooowbbgyggbywobowrwroygrbgowrgw'
        expected['status'] = 'ok'
        
        actualResult = rotate._rotate(input)
        self.assertEqual(expected.get('cube'), actualResult.get('cube'))
        self.assertEqual(expected.get('status'), actualResult.get('status'))
    
    def test_rotate_003_rightClockwise(self):
        input = {}
        input['op'] = 'rotate'
        input['cube'] = 'oywgwrrowogywgbboygbwwyrrgyggbbbwbogryoorywrgybrwoyorb'
        input['dir'] = 'R'       
        
        expected = {}
        expected['cube'] = 'oyrgwyrobbwooggybygbwyyrogyggbbbwbogryworrwrwybrwoworg'
        expected['status'] = 'ok'
        
        actualResult = rotate._rotate(input)
        self.assertEqual(expected.get('cube'), actualResult.get('cube'))
        self.assertEqual(expected.get('status'), actualResult.get('status'))
        
    def test_rotate_004_rightCounterClockwise(self):
        input = {}
        input['op'] = 'rotate'
        input['cube'] = 'woyryrybgoywwgorwbgyywwwwowgyggbgbybogrrooogbrrybrbrbo'
        input['dir'] = 'r'       
        
        expected = {}
        expected['cube'] = 'worryoybbwobygwowroyybwwyowgyggbgbybogwrowoggrrybrrrbg'
        expected['status'] = 'ok'
        
        actualResult = rotate._rotate(input)
        self.assertEqual(expected.get('cube'), actualResult.get('cube'))
        self.assertEqual(expected.get('status'), actualResult.get('status'))
        
    def test_rotate_005_backClockwise(self):
        input = {}
        input['op'] = 'rotate'
        input['cube'] = 'rwbroggooybbygwworobgorbwgroobrbygryywwgwyyrorbggyywwb'
        input['dir'] = 'B'       
        
        expected = {}
        expected['cube'] = 'rwbroggooybbygwwowwoogrbrbgwobwbyyrybwrgwyyrorbggyyorg'
        expected['status'] = 'ok'
        
        actualResult = rotate._rotate(input)
        self.assertEqual(expected.get('cube'), actualResult.get('cube'))
        self.assertEqual(expected.get('status'), actualResult.get('status'))
        
        
    def test_rotate_006_backCounterClockwise(self):
        input = {}
        input['op'] = 'rotate'
        input['cube'] = 'oogrbgroywoorwbggywrowgbrbwyyyyywbgwgyborgbbogwryowrrb'
        input['dir'] = 'b'       
        
        expected = {}
        expected['cube'] = 'oogrbgroywogrwyggbobwrgbwwrryyrywbgwbyyorgbbogwryowybo'
        expected['status'] = 'ok'
        
        actualResult = rotate._rotate(input)
        self.assertEqual(expected.get('cube'), actualResult.get('cube'))
        self.assertEqual(expected.get('status'), actualResult.get('status'))
    
    def test_rotate_007_leftClockwise(self):
        input = {}
        input['op'] = 'rotate'
        input['cube'] = 'orwbrbbybbbgowryoyywrwogogowgwoyryywgorrgwgyorbrgbybwg'
        input['dir'] = 'L'       
        
        expected = {}
        expected['cube'] = 'grwrrbgybbbgowryoyywbwogogryowyygwrwoorggwryoobrbbybwg'
        expected['status'] = 'ok'
        
        actualResult = rotate._rotate(input)
        self.assertEqual(expected.get('cube'), actualResult.get('cube'))
        self.assertEqual(expected.get('status'), actualResult.get('status'))
        
    def test_rotate_008_leftCounterClockwise(self):
        input = {}
        input['op'] = 'rotate'
        input['cube'] = 'orwbrbbybbbgowryoyywrwogogowgwoyryywgorrgwgyorbrgbybwg'
        input['dir'] = 'l'       
        
        expected = {}
        expected['cube'] = 'rrwgrbbybbbgowryoyywgworoggwrwgyywoyoorbgwbyoobrgbyrwg'
        expected['status'] = 'ok'
        
        actualResult = rotate._rotate(input)
        self.assertEqual(expected.get('cube'), actualResult.get('cube'))
        self.assertEqual(expected.get('status'), actualResult.get('status'))
        
    def test_rotate_009_upClockwise(self):
        input = {}
        input['op'] = 'rotate'
        input['cube'] = 'orgyoygororrrgbboybworrwgboggbgbgyyrwbwowgwwywwyoybbyr'
        input['dir'] = 'U'       
        
        expected = {}
        expected['cube'] = 'orryoygorbworgbboyggbrrwgboorggbgyyrwowwwbygwwwyoybbyr'
        expected['status'] = 'ok'
        
        actualResult = rotate._rotate(input)
        self.assertEqual(expected.get('cube'), actualResult.get('cube'))
        self.assertEqual(expected.get('status'), actualResult.get('status'))
      
    def test_rotate_010_upCounterClockwise(self):
        input = {}
        input['op'] = 'rotate'
        input['cube'] = 'orgyoygororrrgbboybworrwgboggbgbgyyrwbwowgwwywwyoybbyr'
        input['dir'] = 'u'       
        
        expected = {}
        expected['cube'] = 'ggbyoygororgrgbboyorrrrwgbobwogbgyyrwgybwwwowwwyoybbyr'
        expected['status'] = 'ok'
        
        actualResult = rotate._rotate(input)
        self.assertEqual(expected.get('cube'), actualResult.get('cube'))
        self.assertEqual(expected.get('status'), actualResult.get('status'))
        
    def test_rotate_011_downClockwise(self):
        input = {}
        input['op'] = 'rotate'
        input['cube'] = 'yrbooywgyrywgggoobgwwwrwogwbygbbybooorrbwrrbygrgwybroy'
        input['dir'] = 'D'       
        
        expected = {}
        expected['cube'] = 'yrbooyboorywgggwgygwwwrwoobbygbbyogworrbwrrbyrwgoyrybg'
        expected['status'] = 'ok'
        
        actualResult = rotate._rotate(input)
        self.assertEqual(expected.get('cube'), actualResult.get('cube'))
        self.assertEqual(expected.get('status'), actualResult.get('status'))
    
    def test_rotate_012_downCounterClockwise(self):
        input = {}
        input['op'] = 'rotate'
        input['cube'] = 'yrbooywgyrywgggoobgwwwrwogwbygbbybooorrbwrrbygrgwybroy'
        input['dir'] = 'd'       
        
        expected = {}
        expected['cube'] = 'yrbooyoobrywgggogwgwwwrwboobygbbywgyorrbwrrbygbyryogwr'
        expected['status'] = 'ok'
        
        actualResult = rotate._rotate(input)
        self.assertEqual(expected.get('cube'), actualResult.get('cube'))
        self.assertEqual(expected.get('status'), actualResult.get('status'))
    
