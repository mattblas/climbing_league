import operator

from django.contrib import messages
from django.shortcuts import render, redirect

from climbing_ligue.forms import AddRouteForm, AddUserRouteForm, UserGroupForm, NewEditionForm
from climbing_ligue.models import Route, User_routes, Active_edition, User_Group
from members.models import Member
from django.db.models import Max

# Create your views here.


# -----------------------------------------------------------------------------------------


def test(request):
    username = request.user

    #GET ACTIVE EDITION
    current_edition_filter = Active_edition.objects.filter(current_edition=True).values_list('edition', flat=True)
    current_edition = list(current_edition_filter)
    current_edition_value = current_edition[0]

    #GET USER GROUP
    usergroup_filter = User_Group.objects.filter(user_name=username)
    for x in usergroup_filter:
        usergroup_value = x.user_group

    #GET USER GENDER
    usergender_filter = Member.objects.filter(username=username)
    for x in usergender_filter:
        usergender_value = x.gender

    #RETURN USER'S POINTS FILTERED BY: GENDER, EDITION, GROUP ------ FIX BUGS
    user_routes = User_routes.objects.filter(user_routes__edition=current_edition_value, user_routes__route_group=usergroup_value)
    all_users = Member.objects.filter(gender=usergender_value)

    points_dict = {}

    for user in all_users:
        i = 0
        user_routes_filter = user_routes.filter(user_name=user)
        for route in user_routes_filter:
            points = route.user_routes.points
            current_points = i + points
            i = current_points

        points_dict[user] = i

    sorted_points = sorted(points_dict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'test.html', {
        'username': username,
        'current_edition_value': current_edition_value,
        'usergroup_value': usergroup_value,
        'usergender_value': usergender_value,
        'sorted_points': sorted_points,
    })


# -----------------------------------------------------------------------------------------

def add_new_edition_view(request):
    if request.POST:
        form = NewEditionForm(request.POST)
        if form.is_valid():
            u = Active_edition.objects.create(
                current_edition=False,
                edition=form.cleaned_data['edition']
            )
            messages.success(request, ('Udało się dodać nową edycję!'))
            return redirect('add_new_edition')
        else:
            messages.success(request, ('Nie udało się dodać nowej edycji!'))
            return redirect('add_new_edition')
    else:
        form = NewEditionForm()

    return render(request, 'add_new_edition.html', {
        'form': form
    })

# -----------------------------------------------------------------------------------------


def add_user_route_view(request):
    current_edition_filter = Active_edition.objects.filter(current_edition=True).values_list('edition', flat=True)
    current_edition = list(current_edition_filter)
    current_edition_value = current_edition[0]

    usergroups = User_Group.objects.filter(user_name = request.user)

    max_user_edition = usergroups.aggregate(Max('edition'))
    max_user_edition_value = max_user_edition['edition__max']

    if max_user_edition_value is not None:
        max_user_edition_value = max_user_edition['edition__max']
    else:
        max_user_edition_value = 0

    if max_user_edition_value >= current_edition_value:
        if request.POST:
            form = AddUserRouteForm(request.POST)
            if form.is_valid():
                u = User_routes.objects.create(
                    user_name=request.user,
                    user_routes=form.cleaned_data['user_routes']
                )
                messages.success(request, ('Udało się dodać nową drogę!'))
                return redirect('add_user_route')
            else:
                messages.success(request, ('Nie udało się dodać nowej drogi!'))
                return redirect('add_user_route')
        else:
            form = AddUserRouteForm()
    else:
        if request.POST:
            form = UserGroupForm(request.POST)
            if form.is_valid():
                u = User_Group.objects.create(
                    user_name=request.user,
                    edition=current_edition_value,
                    user_group=form.cleaned_data['user_group']
                    )
                messages.success(request, ('Udało się aktualizować Twoją grupę!'))
                return redirect('add_user_route')
            else:
                messages.success(request, ('Nie udało się aktualizować Twojej grupy!'))
                return redirect('add_user_route')
        else:
            form = UserGroupForm()

    return render(request, 'add_user_route.html', {
        'form': form,
        'current_edition_value': current_edition_value,
        'max_user_edition_value': max_user_edition_value,
    })


# -----------------------------------------------------------------------------------------


def user_home(request):
    # ----- LISTA WSZYSTKICH DRÓG -------------------------------------------------------------

    current_edition_filter = Active_edition.objects.filter(current_edition=True).values_list('edition', flat=True)
    current_edition = list(current_edition_filter)
    current_edition_value = current_edition[0]

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
        'all_route_list': all_route_list,
        'filter': user_routes_filter,
        'current_points': current_points,
        'current_edition_value': current_edition_value
    })


# -----------------------------------------------------------------------------------------


def update_edition_view(request):
    edition_list = Active_edition.objects.all()
    if request.method == "POST":
        id_list = request.POST.getlist('boxes')
        edition_list.update(current_edition=False)
        for x in id_list:
            Active_edition.objects.filter(pk=int(x)).update(current_edition=True)

        messages.success(request, ('Udało się zaktualizować edycję!'))
        return redirect('update_edition')

    return render(request, 'update_edition.html', {
        'edition_list': edition_list
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
        'add_route_form': form,
        'route_list': route_list
    })


# -----------------------------------------------------------------------------------------


def home(request):
    all_users = Member.objects.all()
    user_routes = User_routes.objects.all()
    user_group = User_Group.objects.all()
    current_edition_filter = Active_edition.objects.filter(current_edition=True).values_list('edition', flat=True)
    current_edition = list(current_edition_filter)
    if current_edition:
        current_edition_value = current_edition[0]
    else:
        current_edition_value = 0
    username = request.user.username

    points_dict = {}

    for user in all_users:
        i = 0
        user_routes_filter = user_routes.filter(user_name=user)
        for route in user_routes_filter:
            points = route.user_routes.points
            current_points = i + points
            i = current_points

        points_dict[user] = i

    sorted_points = sorted(points_dict.items(), key=operator.itemgetter(1), reverse=True)

    # print(sorted_points)

    return render(request, 'home.html', {
        'sorted_points': sorted_points,
        'user': username,
        'all_users': all_users,
        'user_group': user_group,
        'current_edition_value': current_edition_value,
    })
