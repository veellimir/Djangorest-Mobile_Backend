from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название организации")
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="owned_organizations",
        verbose_name="Создатель"
    )
    members = models.ManyToManyField(
        User,
        related_name="organizations",
        verbose_name="Участники"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.members.filter(id=self.owner.id).exists():
            self.members.add(self.owner)


class OrganizationMembership(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата вступления")

    class Meta:
        unique_together = ('organization', 'user')
