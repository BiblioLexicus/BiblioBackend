import datetime

from django.test import TestCase

from .models import *


# Create your tests here.
class TestWorks(TestCase):
    library = LibrariesData(
        schedules="",
        postal_code="",
        library_website="",
        phone_address="",
        library_name="Library 1",
    )
    work = WorkList(
        name_works="Work 1",
        author_name="Author 1",
        publication_date=datetime.date.today().strftime("%Y-%m-%d"),
        edition_house="",
        length=120,
        resume="A short description of the work",
        genre="aa",
        state="",
        copy_number=1,
        type_work="qq",
        price=12.1,
    )
    user = UserList(
        password_hash="",
        name="User",
        first_name="1",
        date_birth=datetime.date.today(),
        fees=0,
        email="user@one.com",
        adresse_postale="",
        expiration_subscription=datetime.date.today() + datetime.timedelta(days=30),
        permissions="",
        related_library_id="",
    )

    def test_work_modification(self):
        """
        Test a work creation, deletion and modification
        """

    def test_work_checking(self):
        """
        Test to check if a work can be checked out and checked into a library
        """

    def test_work_move_library(self):
        """
        Test to check if the work can be moved from one library to another
        """


class TestUsers(TestCase):
    def test_user_modification(self):
        """
        Test creating, modifying and deleting a User
        """

    def test_user_authentication(self):
        """
        Test user authentication
        For normal users
        For Admins
        """

    def test_user_promoting(self):
        """
        Test user promotion to a different state (Employee, Admin, etc)
        """

    def test_user_check_work(self):
        """
        Test user access to different works. (Work can be in a 'staging' area where they are not accessible)
        """


class TestLibrary(TestCase):
    def test_library_modification(self):
        """
        Test Library creation, deletion and modification
        """

    def test_library_add_work(self):
        """
        Test adding and removing works from a library
        """
