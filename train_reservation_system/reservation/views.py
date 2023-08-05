# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reservation, Cabin, Seat

def home(request):
    return render(request, 'index.html')

def check_seat_availability(request):
    num_members = int(request.GET.get('num_members', 0))
    if num_members <= 0:
        return  redirect("error_msg", msg='Invalid Number of members provided')

    available_cabins = []
    for cabin in Cabin.objects.all():
        reservations_in_cabin = Reservation.objects.filter(cabin=cabin)
        total_occupied_seats = sum(reservation.num_members for reservation in reservations_in_cabin)
        total_available_seats = 10 - total_occupied_seats  # Assuming each cabin has 10 seats
        if total_available_seats >= num_members:
            available_cabins.append(cabin)


    context = {
        'available_cabins': available_cabins,
        'num_members' : num_members
    }

    return render(request, 'reservation_form.html', context)

def select_cabin(request, cabin_name, num_members):
    num_members = int(num_members)
    print("cabin_name", cabin_name)
    if num_members <= 0:
        return  redirect("error_msg", msg='Invalid Number of members provided')

    reservations_in_cabin = Reservation.objects.filter(cabin=cabin_name)
    occupied_seats = sum(reservation.num_members for reservation in reservations_in_cabin)
    total_available_seats = 10 - occupied_seats  # Assuming each cabin has 10 seats
    if total_available_seats >= num_members:
        cabin = Cabin.objects.get(id=cabin_name)
        reservation = Reservation.objects.create(num_members=num_members,
                                                 cabin=cabin)

        # Assign seats to the reservation
        for i in range(num_members):
            seat_number = occupied_seats + i + 1
            seat = Seat.objects.create(seat_number=seat_number, cabin=cabin)
            reservation.seats.add(seat)

        seats = reservation.seats.all()
        total_fare = cabin.fare*num_members
        context = {
            'reservation_id' : reservation.reservation_id,
            'preferred_cabin': cabin.name,
            'seats' : seats,
            'total_fare': total_fare,
        }

        return render(request, 'select_cabin.html', context)
    else:
        return redirect("error_msg", msg='Multiple Reloads')

def make_payment(request, total_fare):
    return render(request, 'payment_page.html', {'total_fare': total_fare})

def error_msg(request, msg):
    return render(request, 'error_page.html', {'message':msg})
