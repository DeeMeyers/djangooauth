from django.test import TestCase
from ..models import Goal

class GoalTest(TestCase):

    def setUp(self):
        Goal.objects.create(
            current='4',
            previous='2',
            goal='5',
        )
    
    def testGoal(self):
        testObj = Goal.objects.get(current='4')
        self.assertEqual(
            testObj.test(), (4,2,5)
            )