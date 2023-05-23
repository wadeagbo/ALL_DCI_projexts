from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from .models import UserProfile

@receiver(user_signed_up)
def create_user_profile(request, **kwargs):
    UserProfile.objects.create(user = kwargs.get('user'))