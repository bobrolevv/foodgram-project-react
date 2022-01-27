# from django.db import models
# from django.contrib.auth.models import User
#
#
# class userProfile(models.Model):
#     email = models.EmailField(
#         max_length=254,)
#
#     username = models.OneToOneField(
#         User,
#         max_length=150,
#         on_delete=models.CASCADE,
#         related_name="profile")
#
#     first_name = models.CharField(
#         max_length=150,
#         )
#
#     last_name = models.CharField(
#         max_length=150,
#         )
#
#     description = models.TextField(
#         blank=True,
#         null=True)
#     location = models.CharField(
#         max_length=30,
#         blank=True)
#     date_joined = models.DateTimeField(
#         auto_now_add=True)
#     updated_on = models.DateTimeField(
#         auto_now=True)
#     is_organizer=models.BooleanField(
#         default=False)
#
#     def __str__(self):
#         return self.user.username