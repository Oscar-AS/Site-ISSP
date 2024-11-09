from django.contrib.auth.models import Group
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(m2m_changed, sender=User.groups.through)
def add_staff_status(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == 'post_add':
        group = Group.objects.get(name='publicateur')
        if group.pk in pk_set:
            instance.is_staff = True
            instance.save()
