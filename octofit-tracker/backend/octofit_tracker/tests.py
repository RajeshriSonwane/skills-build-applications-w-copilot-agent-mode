from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def setUp(self):
        User.objects.create(email="test@example.com", name="Test User", age=25)

    def test_user_creation(self):
        user = User.objects.get(email="test@example.com")
        self.assertEqual(user.name, "Test User")

class TeamModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(email="teamuser@example.com", name="Team User", age=30)
        team = Team.objects.create(name="Test Team")
        team.members.add(user)

    def test_team_creation(self):
        team = Team.objects.get(name="Test Team")
        self.assertEqual(team.name, "Test Team")

class ActivityModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(email="activityuser@example.com", name="Activity User", age=20)
        Activity.objects.create(user=user, activity_type="Running", duration=30, date="2025-04-11")

    def test_activity_creation(self):
        activity = Activity.objects.get(activity_type="Running")
        self.assertEqual(activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(email="leaderboarduser@example.com", name="Leaderboard User", age=22)
        Leaderboard.objects.create(user=user, score=100)

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.get(score=100)
        self.assertEqual(leaderboard.user.name, "Leaderboard User")

class WorkoutModelTest(TestCase):
    def setUp(self):
        Workout.objects.create(name="Yoga", description="Relaxing yoga session", duration=60)

    def test_workout_creation(self):
        workout = Workout.objects.get(name="Yoga")
        self.assertEqual(workout.duration, 60)