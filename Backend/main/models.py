# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# TODO check that all classes are well generated - will do after that it has been merged to Dev

# TODO: check que la db a du sens(celle django) avec ce que on veut. Point de discussion: doit-on viser la base de
# données la plus petite ou quelque chose de cohérent (penser à la taille des fields, ne serait-ce pas mieux de
# prendre des fields plus grand mais logique, genre 100, 128, 200 ou 256)


class Comments(models.Model):
    id_comments = models.IntegerField(
        db_column="ID_Comments", primary_key=True
    )  # Field name made lowercase.
    id_works = models.ForeignKey(
        "WorkList", models.DO_NOTHING, db_column="ID_Works"
    )  # Field name made lowercase.
    id_users = models.ForeignKey(
        User, models.DO_NOTHING, db_column="id"
    )  # Field name made lowercase.
    release_date = models.DateTimeField(
        db_column="Release_Date"
    )  # Field name made lowercase.
    comment_text = models.TextField(
        db_column="Comment_Text"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Comments"
        unique_together = (("id_comments", "id_works", "id_users"),)


class LibrariesData(models.Model):
    id_users = models.ForeignKey(
        User, models.DO_NOTHING, db_column="id"
    )  # Field name made lowercase.
    schedules = models.CharField(
        db_column="Schedules", max_length=11
    )  # Field name made lowercase.
    postal_code = models.CharField(
        db_column="Postal_Code", max_length=6
    )  # Field name made lowercase.
    library_website = models.CharField(
        db_column="Library_Website", max_length=45
    )  # Field name made lowercase.
    phone_address = models.CharField(
        db_column="Phone_Address", max_length=14
    )  # Field name made lowercase.
    library_name = models.CharField(
        db_column="Library_Name", max_length=45, blank=True, null=True
    )  # Field name made lowercase.
    id_library = models.CharField(
        db_column="ID_Library", primary_key=True, max_length=2
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Libraries_Data"


class LoanedWorks(models.Model):
    id_works = models.OneToOneField(
        "WorkList", models.DO_NOTHING, db_column="ID_Works", primary_key=True
    )  # Field name made lowercase.
    end_loan_date = models.DateField(
        db_column="End_Loan_Date"
    )  # Field name made lowercase.
    id_users = models.ForeignKey(
        User, models.DO_NOTHING, db_column="id"
    )  # Field name made lowercase.
    #binary ou boolean? question avec arpad voir ce qui se passe
    work_lost = models.BinaryField(
        db_column="Work_Lost"
    )  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = "Loaned_Works"
        unique_together = (("id_works", "id_users"),)


# extends user class fourni par django, @arpad si tu veux voir ce qui est la dedans vas dans le server, mariadb -u
# /DB_ADMIN_BL demande a Charles le password (ou autre façon quelconque, trouve le .env si tu peux ;) )
# use bibliolexicusdb
# SELECT * FROM AUTH.user
# note: c case sensitive, so fais attention
# note: one to one relationship with user, sera plus facile. Réécriture des test nécessaire mais bon.
class LibraryUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Field name made lowercase.
    date_birth = models.DateField(db_column="Date_Birth")  # Field name made lowercase.
    fees = models.DecimalField(
        db_column="Fees", max_digits=10, decimal_places=4, default=0.0)  # Field name made lowercase.
    """email = models.CharField(
        db_column="Email", unique=True, max_length=320
    )  # Field name made lowercase."""
    addresse_postale = models.CharField(
        db_column="Addresse_Postale", max_length=6
    )  # Field name made lowercase.
    expiration_subscription = models.DateField(
        db_column="Expiration_Subscription"
    )  # Field name made lowercase.
    permissions = models.CharField(
        db_column="Permissions", max_length=2, default="OO"
    )  # Field name made lowercase.
    related_library_id = models.CharField(
        db_column="Related_Library_ID", max_length=2, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "User_List"


# hooks sur la création d'un utilisateur, je crois. One to one relationship SQL,
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        LibraryUserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def saver_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class WorkList(models.Model):
    id_works = models.CharField(
        db_column="ID_Works", primary_key=True, max_length=20
    )  # Field name made lowercase.
    name_works = models.CharField(
        db_column="Name_Works", max_length=50
    )  # Field name made lowercase.
    author_name = models.CharField(
        db_column="Author_Name", max_length=250
    )  # Field name made lowercase.
    publication_date = models.DateField(
        db_column="Publication_Date"
    )  # Field name made lowercase.
    edition_house = models.CharField(
        db_column="Edition_House", max_length=45
    )  # Field name made lowercase.
    length = models.PositiveIntegerField(
        db_column="Length"
    )  # Field name made lowercase.
    resume = models.CharField(
        db_column="Resume", max_length=2000
    )  # Field name made lowercase.
    genre = models.CharField(
        db_column="Genre", max_length=2
    )  # Field name made lowercase.
    language = models.CharField(
        db_column="Language", max_length=18
    )  # Field name made lowercase.
    state = models.BinaryField(
        db_column="State"
    )  # Field name made lowercase. This field type is a guess.
    copy_number = models.PositiveIntegerField(
        db_column="Copy_Number"
    )  # Field name made lowercase.
    type_work = models.CharField(
        db_column="Type_Work", max_length=2
    )  # Field name made lowercase.
    price = models.DecimalField(
        db_column="Price", max_digits=5, decimal_places=3
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Work_List"
