from email import message
from django.shortcuts import render, redirect
from climbing_ligue.forms import AddRouteForm, AddUserRouteForm, UpdateEdition
from climbing_ligue.models import Route, User_routes, Active_edition
from django.contrib import messages
import operator
from members.models import Member

# Create your views here.


# -----------------------------------------------------------------------------------------



def test(request):
    return render(request, 'test.html', {

    })



# -----------------------------------------------------------------------------------------



def add_user_route_view(request):

    if request.POST:
        form = AddUserRouteForm(request.POST)
        if form.is_valid():
            u = User_routes.objects.create(
                user_name = request.user,
                user_routes = form.cleaned_data['user_routes']
            )
            messages.success(request, ('Udało się dodać nową drogę!'))
            return redirect('add_user_route')
        else:
            messages.success(request, ('Nie udało się dodać nowej drogi!'))
            return redirect('add_user_route')
    else:
        form = AddUserRouteForm()

    current_edition = Active_edition.objects.filter(current_edition=True).values_list('edition', flat=True)
    for current_edition_value in current_edition:
        current_edition_value = current_edition_value

    all_routes = Route.objects.all()
    all_routes_filter = all_routes.filter(edition=current_edition_value)

    all_users = Member.objects.all()
    all_users_filter = all_users.filter(username=request.user.username)

    return render(request, 'add_user_route.html', {
        'form':form,
        'current_edition_value':current_edition_value,
        'all_routes_filter':all_routes_filter,
        'all_users_filter':all_users_filter,
    })



# -----------------------------------------------------------------------------------------



def user_home(request):

# ----- LISTA WSZYSTKICH DRÓG -------------------------------------------------------------
    
    current_edition = Active_edition.objects.filter(current_edition=True).values_list('edition', flat=True)
    for current_edition_value in current_edition:
        current_edition_value = current_edition_value

    all_route_list = Route.objects.all().order_by('-edition', 'round', 'points')


# ----- LISTA WSZYSTKICH DRÓG UŻYTKOWNIKA ------------------------------------------------------------
    user_routes = User_routes.objects.all()
    user_routes_filter = user_routes.filter(user_name=request.user)


# ----- AKTUALNA PUNKTACJA ----------------------------------------------------------------
    i = 0
    current_points = 0
    
    for route in user_routes_filter:
        if route.user_routes.edition == current_edition_value:
            current_points = i + route.user_routes.points
            i = current_points


    return render(request, 'user_home.html', {
        'all_route_list':all_route_list,
        'filter':user_routes_filter,
        'current_points':current_points,
        'current_edition_value':current_edition_value
    })



# -----------------------------------------------------------------------------------------



def update_edition_view(request):
    all_editions = Active_edition.objects.all()

    return render(request, 'update_edition.html', {
        'all_editions':all_editions,
    })



# -----------------------------------------------------------------------------------------



def add_route_view(request):
 
    if request.POST:
        form = AddRouteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Udało się dodać nową drogę!'))
            return redirect('add_route')
        else:
            messages.success(request, ('Nie udało się dodać nowej drogi!'))
            return redirect('add_route')
    else:
        form = AddRouteForm()

    route_list = Route.objects.all().order_by('-edition', 'round', 'points')
    
    return render(request, 'add_route.html', {
        'add_route_form':form,
        'route_list':route_list
        })



# -----------------------------------------------------------------------------------------



def home(request):
    
    all_users = Member.objects.all()
    user_routes = User_routes.objects.all()

    username = request.user.username

    points_dict = {}
    
    for user in all_users:
        i = 0
        user_routes_filter = user_routes.filter(user_name=user)    
        for route in user_routes_filter:
            points = route.user_routes.points
            current_points = i + points
            i = current_points
            
        points_dict[user]=i
        
    sorted_points = sorted(points_dict.items(), key=operator.itemgetter(1), reverse=True)

    print(sorted_points)

    return render(request, 'home.html', {
    'sorted_points':sorted_points, 
    'user':username
    })