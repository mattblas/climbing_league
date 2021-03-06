from django import forms
from django.forms import ModelForm
from climbing_ligue.models import Route, User_routes, Active_edition, User_Group, Active_round
from django.db import connection

# FORMULARZ NOWEJ EDYCJI
class NewEditionForm(ModelForm):
    edition = forms.IntegerField(required=True, label='Edycja', min_value=1)

    class Meta:
        model = Active_edition
        fields = ['edition']

# ----- FORMULARZ AKTUALIZACJI GRUPY -----
class UserGroupForm(ModelForm):

    user_group_choices = (
        ('Początkujący', 'Początkujący'),
        ('Średniozaawansowani', 'Średniozaawansowani'),
        ('Pro', 'Pro'),
        ('Masters', 'Masters'),
    )

    user_group = forms.ChoiceField(choices=user_group_choices, required=True, label='Grupa')

    class Meta:
        model = User_Group
        fields = ['user_group']

# FORMULARZ NOWEJ DROGI UŻYTKOWNIKA
def table_exists(table_name):
    all_tables = connection.introspection.table_names()
    if table_name in all_tables:
        return True
    else:
        return False

def get_current_edition():
    if table_exists('climbing_ligue_active_edition'):
        current_edition = list(Active_edition.objects.filter(current_edition=True).values_list('edition', flat=True))
        if current_edition:
            return current_edition[0]
        else:
            return None
    else:
        return None

def get_current_round():
    if table_exists('climbing_ligue_active_round'):
        current_round = list(Active_round.objects.filter(current_round=True).values_list('round', flat=True))
        if current_round:
            return current_round[0]
        else:
            return None
    else:
        return None

class AddUserRouteForm(ModelForm):
    #user_routes = forms.ModelChoiceField(queryset=Route.objects.all().filter(edition=get_current_edition()))
    user_routes_001 = forms.ModelChoiceField(queryset=Route.objects.all().filter(edition=get_current_edition()).filter(round=get_current_round()).filter(route_group='Początkujący'))
    user_routes_002 = forms.ModelChoiceField(queryset=Route.objects.all().filter(edition=get_current_edition()).filter(round=get_current_round()).filter(route_group='Średniozaawansowani'))
    user_routes_003 = forms.ModelChoiceField(queryset=Route.objects.all().filter(edition=get_current_edition()).filter(round=get_current_round()).filter(route_group='Pro'))
    user_routes_004 = forms.ModelChoiceField(queryset=Route.objects.all().filter(edition=get_current_edition()).filter(round=get_current_round()).filter(route_group='Masters'))

    class Meta:
        model = User_routes
        fields = ['user_routes_001', 'user_routes_002', 'user_routes_003', 'user_routes_004']

# FORMULARZ DLA NOWEJ DROGI
class AddRouteForm(ModelForm):
    route_grade_choices = (
        ('4A', '4A'),
        ('4B', '4B'),
        ('4C', '4C'),
        ('5A', '5A'),
        ('5B', '5B'),
        ('5C', '5C'),
        ('6A', '6A'),
        ('6A+', '6A+'),
        ('6B', '6B'),
        ('6B+', '6B+'),
        ('6C', '6C'),
        ('6C+', '6C+'),
        ('7A', '7A'),
        ('7A+', '7A+'),
        ('7B', '7B'),
        ('7B+', '7B+'),
        ('7C', '7C'),
        ('7C+', '7C+'),
        ('8A', '8A'),
        ('8A+', '8A+'),
        ('8B', '8B'),
        ('8B+', '8B+'),
        ('8C', '8C'),
    )

    points_choices = (
        (0.5, '0,5'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (4.5, '4,5'),
        (5, '5'),
        (5.5, '5,5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (8.5, '8,5'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
        (13, '13'),
        (14, '14'),
        (15, '15'),

    )

    round_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', 'Finał'),
    )

    route_group_choices = (
        ('Początkujący', 'Początkujący'),
        ('Średniozaawansowani', 'Średniozaawansowani'),
        ('Pro', 'Pro'),
        ('Masters', 'Masters'),
    )

    route_name = forms.CharField(max_length=60, required=True, label='Nazwa drogi')
    route_grade = forms.ChoiceField(choices=route_grade_choices, label='Trudność', required=True)
    points = forms.ChoiceField(choices=points_choices, label='Punkty', required=True)
    edition = forms.IntegerField(required=True, label='Edycja', min_value=1)
    round = forms.ChoiceField(choices=round_choices, required=True, label='Runda')
    route_group = forms.ChoiceField(choices=route_group_choices, required=True, label='Grupa')

    class Meta:
        model = Route
        fields = ('route_name', 'route_grade', 'points', 'edition', 'round', 'route_group')


class AddUserRouteForm001(ModelForm):
    user_routes = forms.ModelChoiceField(queryset=Route.objects.all().filter(edition=get_current_edition()).filter(round=get_current_round()).filter(route_group='Początkujący'))

    class Meta:
        model = User_routes
        fields = ['user_routes']


class AddUserRouteForm002(ModelForm):
    user_routes = forms.ModelChoiceField(queryset=Route.objects.all().filter(edition=get_current_edition()).filter(
        round=get_current_round()).filter(route_group='Średniozaawansowani'))

    class Meta:
        model = User_routes
        fields = ['user_routes']


class AddUserRouteForm003(ModelForm):
    user_routes = forms.ModelChoiceField(
        queryset=Route.objects.all().filter(edition=get_current_edition()).filter(round=get_current_round()).filter(
            route_group='Pro'))

    class Meta:
        model = User_routes
        fields = ['user_routes']


class AddUserRouteForm004(ModelForm):
    user_routes = forms.ModelChoiceField(
        queryset=Route.objects.all().filter(edition=get_current_edition()).filter(round=get_current_round()).filter(
            route_group='Masters'))

    class Meta:
        model = User_routes
        fields = ['user_routes']