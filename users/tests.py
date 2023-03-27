from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.com", password="user")
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="user")

    def test_create_staff(self):
        User = get_user_model()
        staff_user = User.objects.create_staff(email="staff@user.com", password="staff")
        self.assertEqual(staff_user.email, "staff@user.com")
        self.assertTrue(staff_user.is_active)
        self.assertTrue(staff_user.is_staff)
        self.assertFalse(staff_user.is_superuser)
        try:
            self.assertIsNone(staff_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_staff(
                email="staff@user.com", password="staff", is_staff=False)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.com", password="admin")
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com", password="admin", is_superuser=False)