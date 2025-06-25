from django.db import models


class FriendRequest(models.Model):

    from_who = models.ForeignKey('reg.Profile', related_name='sent_requests', on_delete=models.CASCADE)
    to_who = models.ForeignKey('reg.Profile', related_name='received_requests', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('from_who', 'to_who')

    def __str__(self):
        return f"{self.from_who.user.username} → {self.to_who.user.username}"