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

        Steps:
        1. Create a work
        2. Modify random attributes
        3. Remove a work that is reserved / lended

        Test some with incorrect data and verify that the work will not be changed and will throw a warning as a result.
        """

    def test_work_checking(self):
        """
        Test to check if a work can be checked out and checked into a library

        Steps (Use provided work):
        1. Check out a work
        2. Check in a work
        """

    def test_work_move_library(self):
        """
        Test to check if the work can be moved from one library to another

        Steps (Use provided work and libraries):
        1. Move a work from a library to another
        2. Make sure that work is not in its original library and is in fact in the new library.
        3. Make sure that the ID of the work updated successfully
        """


class TestUsers(TestCase):
    def test_user_modification(self):
        """
        Test creating, modifying and deleting a User

        Steps:
        1. Create a user
        2. Modify a user data
        3. Delete a user

        Test some with incorrect data and verify that the user will not be changed and will throw a warning as a result.
        """

    def test_user_authentication(self):
        """
        Test user authentication
        For normal users
        For Admins

        Steps (Do this for each type of user):
        1. Authenticate with correct credentials
        2. Verify if the user is logged in
        3. Log out
        4. Authenticate with invalid credentials
        5. Verify if the user is logged in
        6. Try to make a user action (reserve a work)
        7. Try to log out

        Normal user:
        8. test if restricted (admin and employee actions) are unavailable

        Employee user:
        8. verify specific restricted actions are authorised and/or blocked

        Admin user:
        8. Verify if can run restricted actions and normal actions 
        """

    def test_user_promoting(self):
        """
        Test user promotion to a different state (Employee, Admin, etc)

        Steps:
        1. Create base User
        2. Upgrade it for each level (Each level needs the user to have some requirements by default)
        """

    def test_user_check_work(self):
        """
        Test user access to different works. (Work can be in a 'staging' area where they are not accessible)
        note: define staging area and its properties
        Steps (For every access right):
        1. Access a work that is public
        2. Access "restricted" work
        """

    def test_user_get_recommended(self):
        """
        Test getting recommended books.

        Step:
        1. Create new user
        2. Check out the recommended works (should be random, different types)

        Steps (For 3 random work types):
        1. Check out 10 work of one type
        2. Check out the recommended works (should of given types)
        :return:
        """
    
    def test_user_deletion(self):
        """
        test what happens if we delete a user and the result to it's corresponding items
        
        1. Create a normal user
        2. Create comments to a random book
        3. Delete User
        4. Check state of the comment
        
        5. Create admin account
        6. Create library under admin supervisation
        7. delete admin account
        8. Check state of library (in accordance to the use case predefined)
            8.1 Might raise the test of what happens if we delete a library
        """


class TestLibrary(TestCase):
    def test_library_modification(self):
        """
        Test Library creation, deletion and modification

        Steps:
        0. Create admin account who will supervise library
        1. Create library
        2. Modify library
        3. Delete library
        4. Check if linked books are somewhere in the db (should be handled by the SQL but not sure)

        Test some with incorrect data and verify that the library will not be changed and will throw a warning as a result.
        """

    def test_library_add_work(self):
        """
        Test adding and removing works from a library

        Steps:
        1. Add a work
        2. Remove work

        Test some with incorrect data and verify that the library will not be changed and will throw a warning as a result.
        """

    def test_library_get_top_works(self):
        """
        Test getting top works from a library

        Steps:
        1. Create library
        2. Check out the top works (should be random)

        Steps:
        1. Check out and check back in multiple random works multiple times
        2. Check out the top works (should correspond to the works that have been checked out the most)
        :return:
        """


class TestComment(TestCase):
    def test_comment_add(self):
        """
        Test adding a comment on a work

        Steps:
        1. Add a normal comment
        2. Add a comment with bad words (Should not be accepted)
            2.1 Define bad word. 
        3. Add a comment with html tags / script (Should not be accepted) or should be cleaned
        """

    def test_command_remove(self):
        """
        Test removing a comment

        Steps:
        1. Add a normal comment
        2. Remove it
        """
