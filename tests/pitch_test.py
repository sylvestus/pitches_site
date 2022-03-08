import unittest
from app.models import Pitch,User,Comments

class TestPitch(unittest.TestCase):
    """
    This class will test our pitch class model.
    """

    def setUp(self):
        """
        Setup function that is run before every test.
        """
        self.new_user = User(username = "silvano")
        self.new_pitch = Pitch(pitch_title = "dating", user = self.new_user)

    def tearDown(self):
        """
        Tear down function that will clean the lists after every test
        """
        Pitch.query.delete()
        User.query.delete()
        Comments.query.delete()

    def test_instance(self):
        """
        Test instance class for testing wether instance are actaully instance of our classes.
        """
        self.assertTrue(isinstance(self.new_pitch, Pitch))

    def test_init(self):
        """
        Test init function to test if object are being initialized corectly.
        """

        self.assertEquals(self.new_pitch.title, "dating")

    def test_save_pitch(self):
        """
        Save function to test if our instances are being saved into the database.
        """
        self.new_pitch.save_pitch()
        pitches = Pitch.query.all()
        self.assertTrue(len(pitches) > 0)

    def test_relationship_user(self):
        """
        Relationship  function test if there is a relationship between user class and the comment made.
        """
        user = self.new_pitch.user.username
        self.assertTrue(user == "silvano")