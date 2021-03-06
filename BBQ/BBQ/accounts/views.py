from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.conf import settings

from BBQ.accounts.forms import SignUpForm, LoginForm
from BBQ.search import search


@login_required
def home(request, results=None, jscode=None):
    if results == None:
        print(settings.GOOGLE_MAPS_API_KEY)
        context = {
            "APIKEY": settings.GOOGLE_MAPS_API_KEY
        }
        return render(request, 'home.html', context)
    else:
        latitude = -25.363
        longitude = 131.044
        context = {
            "APIKEY": settings.GOOGLE_MAPS_API_KEY,
            "results": results,
            "latitude": latitude,
            "longitude": longitude,
            "jscode": jscode
        }
        return render(request, 'home.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            
            lastname = form.cleaned_data.get('last_name')
            firstname = form.cleaned_data.get('first_name')
            email = form.cleaned_data.get('email')
            # username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            re_password = form.cleaned_data.get('password2')
            if raw_password == re_password:
                user = None
                try:
                    user = User.objects.get(username=email)
                except Exception as e:
                    pass
                if user != None:
                    return redirect('home') #should report user alerady exist
                user = User.objects.create_user(username=email, password=raw_password, last_name=lastname, first_name=firstname)
                login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_page(request,template_name):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            if user != None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('home') #should report bad user info
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_page(request,next_page):
    logout(request)
    return redirect('home')

def pulledpork_search(request):
    api_key = settings.YELP_API_KEY
    lat = 89
    lng = -62
    if request.method == "POST":
        lat = request.POST['lat']
        lng = request.POST['lng']
        term = request.POST['term']
        print("Looking for: "+ term)
    results, jscode = search (api_key, lat, lng, term)
    # if request.method == "GET":
    #     print("happy days are here again something soemthing")
    #     latitude = request.GET.get('lat')
    #     longitude = request.GET.get('lng')
    # print (type(results))
    return home(request, results, jscode)

# def brisket_search(request):
#     api_key = settings.YELP_API_KEY
#     lat = 89
#     lng = -62
#     if request.method == "POST":
#         lat = request.POST['lat']
#         lng = request.POST['lng']
#         term = request.POST['term']
#     results, jscode = search (api_key, lat, lng, term)
#     return home(request, results, jscode)

# def chickenquarter_search(request):
#     api_key = settings.YELP_API_KEY
#     lat = 89
#     lng = -62
#     if request.method == "POST":
#         lat = request.POST['lat']
#         lng = request.POST['lng']
#     results, jscode = search (api_key, lat, lng)
#     return home(request, results, jscode)
    