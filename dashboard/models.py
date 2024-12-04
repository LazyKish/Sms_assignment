from django.db import models
from twilio.rest import Client
# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.score >= 70:
            account_sid = 'ACfb13cb344027e7d0742e5f859957825b'
            auth_token = '9dfa523fbf28fabc7869c9ebb91467f4'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"HUE {self.name}, Utang nimo kay {self.score}",
                from_='+17754366033',
                to='+18777804236'
            )
        else:
            account_sid = 'ACfb13cb344027e7d0742e5f859957825b'
            auth_token = '9dfa523fbf28fabc7869c9ebb91467f4'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Pls {self.name}, gamay ra oh {self.score}. Ra",
                from_='+17754366033',
                to='+18777804236'
            )

        print(message.sid)
        return super().save(*args, **kwargs)