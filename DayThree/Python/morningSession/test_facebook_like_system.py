from unittest import TestCase
import facebook_like_system

class test_facebook_like_system(TestCase):
    
    def test_that_no_one_likes_post(self):
        likes = []
        actual = facebook_like_system.facebook_likes(likes)
        expected = 0;
        self.assertEqual(actual, expected)
        
    def test_that_one_person_liked_post(self):
        likes = ["Peter"]
        actual = facebook_like_system.facebook_likes(likes)
        expected = 1;
        self.assertEqual(actual, expected)
        
    def test_that_two_persons_liked_post(self):
        likes = ["Peter", "Alex"]
        actual = facebook_like_system.facebook_likes(likes)
        expected = 2;
        self.assertEqual(actual, expected)
        
    def test_that_three_persons_liked_post(self):
        likes = ["Max", "John", "Mark"]
        actual = facebook_like_system.facebook_likes(likes)
        expected = 3;
        self.assertEqual(actual, expected)
        
    def test_that_three_persons_liked_post(self):
        likes = ["Alex", "Jacob", "Mark", "Max"]
        actual = facebook_like_system.facebook_likes(likes)
        expected = 4;
        self.assertEqual(actual, expected)
        
    
