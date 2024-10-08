# from django.db import models

# class Person(models.Model):
#     friends = models.CharField(max_length=255)

# class Group(models.Model):
#     name = models.CharField(max_length=255)
#     members = models.ManyToManyField(
#         Person,
#         through="Membership",
#         through_fields=("group", "person")
#     )


# class MemberShip(models.Model):
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     inviter = models.ForeignKey(
#         Person,
#         on_delete = models.CASCADE,
#         related_name = 'membership_invites',
#     )
#     invite_reason = models.CharField(max_length=64)

