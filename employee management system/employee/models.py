from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    designation = models.CharField(max_length=30, null=False, blank=False)
    salary = models.IntegerField(null=True, blank=True)

    user = models.OneToOneField(User, on_delete='models.CASCADE')

    class Meta:
        db_table = "Profile_Info"
        ordering = ("-salary",)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


@receiver(post_save, sender=User)
def user_is_created(sender, instance, created, **kwargs):
    print(created)
    if created:
        Profile.objects.create(user=instance)
        # instance.profile
    else:
        instance.profile.save()


