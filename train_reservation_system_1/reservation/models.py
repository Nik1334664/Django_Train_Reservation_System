from django.db import models
import uuid

class Cabin(models.Model):
    name = models.CharField(max_length=100)
    fare = models.PositiveIntegerField()

    def __str__(self):
        return self.name

# models.py
class Seat(models.Model):
    seat_number = models.PositiveIntegerField()
    cabin = models.ForeignKey(Cabin, on_delete=models.CASCADE)

    def __str__(self):
        return f'Seat Number: {self.seat_number}, Cabin: {self.cabin}'


class Reservation(models.Model):
    reservation_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
 #   family_name = models.CharField(max_length=100)
    num_members = models.PositiveIntegerField()
    cabin = models.ForeignKey(Cabin, on_delete=models.CASCADE)
    seats = models.ManyToManyField('Seat', related_name='reservations')

    def __str__(self):
        return f"Cabin {self.cabin.name}, Reservation ID {self.reservation_id}"
