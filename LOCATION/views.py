from django.shortcuts import render, redirect
from LOCATION.MODELS.location import Location
from LOCATION.forms import TrackForm
from USERS.MODELS.user import CustomUser
import requests


def track_view(request):
    if request.method == 'POST':
        form = TrackForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            user = CustomUser.objects.filter(phone_number=phone_number).first()
            if user:
                location_data = fetch_location_data(phone_number)
                if location_data:
                    Location.objects.create(
                        user=user,
                        area=location_data['area'],
                        city=location_data['city'],
                        state=location_data['state'],
                        country=location_data['country']
                    )
                    locations = user.locations.order_by('-timestamp')
                    return render(request, 'USERS\TEMPLATES\LOCATION\track.html', {'locations': locations, 'phone_number': phone_number})
    else:
        form = TrackForm()
    return render(request, 'USERS\TEMPLATES\LOCATION\track.html', {'form': form})

def fetch_location_data(phone_number):
    API_URL = 'https://phonevalidation.abstractapi.com/v1/'
    API_KEY = ''

    try:
        response = requests.get(API_URL, params={'api_key': API_KEY, 'phone': phone_number})
        response.raise_for_status()
        data = response.json()
        return {
            'area': data.get('location'),
            'city': data.get('city'),
            'state': data.get('state'),
            'country': data.get('country')
        }
    except requests.RequestException as e:
        print(f"Error fetching location data: {e}")
        return None
