from django.db import models

class UserProfile(models.Model):
    '''
    UserProfile is to extend default User model.
    '''
    user = models.OneToOneField(User, related_name='profile')


with transaction.atomic():
    user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
           )

    UserProfile.objects.create(user=user)
