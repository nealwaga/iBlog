import unittest
from app.models import Post

class PostTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the post class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_post = Post()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))