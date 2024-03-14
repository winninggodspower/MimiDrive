from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import requests
from .models import Car, Feature

# Create your views here.
def home(request):
    context = {
        'cars': Car.objects.all(),
        'features': Feature.objects.all(),
    }
    return render(request, 'index.html', context)

def collection(request):
    context = {
        'cars': Car.objects.all(),
        'features': Feature.objects.all(),
    }
    return render(request, 'collection.html', context)

def search(request):
    query = request.GET.get('q')
    cars = Car.objects.filter(title__icontains=query)

    context = {
        'cars': cars,
        'features': Feature.objects.all(),
        'query': query
    }
    return render(request, 'collection.html', context)


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'car_detail.html', {'car': car})

def populate_car_data(request):
    endpoint_url = "https://random-data-api.com/api/v3/projects/3f90c755-811c-46b2-a5a3-9832b28201c8?api_key=k2ybkF3X3SKZlJYrKQp5bQ"

    # Fetch data from the endpoint
    response = requests.get(endpoint_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract JSON data from the response
        car_data = response.json()

        # Create a new Car object using the fetched data
        new_car = Car(
            make=car_data['car_make'],
            model=car_data['car_model'],
            title=f"{car_data['car_make']} {car_data['car_model']}",
            fuel_type=car_data['fuel_type'],
            year=car_data['car_year'],
            description=car_data['car_description'],
            price=car_data['car_price'] * 1000000,
            main_image=car_data['image_url'],
            transmision=car_data['transmission']
        )

        # Save the new Car object to the database
        new_car.save()

        return HttpResponse("Car data successfully fetched and saved to the database.")
    else:
        return HttpResponse("Failed to fetch car data from the endpoint.")