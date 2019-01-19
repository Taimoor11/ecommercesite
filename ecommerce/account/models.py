from django.db import models
from django.conf import settings



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    customer_type = models.IntegerField(choices=((1, ('registered')),
                                                 (2, ('Non_registered'))),
                                        default=1)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)





class Address(models.Model):
    user_profile = models.ForeignKey(Profile, related_name='address', on_delete=models.CASCADE, null=True)
    address_line1 = models.CharField(max_length=60)
    address_line2 = models.CharField(max_length=60, blank=True)
    city = models.CharField(max_length=60)
    state = models.IntegerField(choices=((1, ('Capital')),
                                         (2, ('Punjab')),
                                         (3, ('Sindh')),
                                         (4, ('Balochistan')),
                                         (5, ('Kpk'))),
                                default=1)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=60)


    def __str__(self):
        return 'address for user profile {}'.format(self.user_profile)