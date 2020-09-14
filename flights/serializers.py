from rest_framework import serializers
from flights.models import Flight, Booking

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'destination', 'time','price']

class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight','date','id']
