from dataclasses import field
from django import forms
from django import forms
from django.forms import ChoiceField, ModelForm
from climbing_ligue.models import Route, User_routes, Active_edition
from members.models import Member
from django.utils.translation import gettext_lazy as _

# FORMULARZ AKTUALIZACJI EDYCJI
#--------------------------------------------------------------
class UpdateEdition(ModelForm):
    class Meta:
        model = Active_edition
        fields = '__all__'
#--------------------------------------------------------------

# FORMULARZ NOWEJ DROGI UŻYTKOWNIKA
#--------------------------------------------------------------
def get_current_edition():
    current_edition = Active_edition.objects.filter(current_edition=True).values_list('edition', flat=True)
    for current_edition_value in current_edition:
        current_edition_value = current_edition_value
    return current_edition_value

class AddUserRouteForm(ModelForm):

    user_routes = forms.ModelChoiceField(queryset=Route.objects.all().filter(edition=get_current_edition()))
    
    class Meta:
        model = User_routes
        fields = ('user_routes',)



#--------------------------------------------------------------

# FORMULARZ DLA NOWEJ DROGI
#--------------------------------------------------------------
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
        ('Final', 'Finał'),
    )

    route_group_choices = (
        ('Poczatkujacy', 'Początkujący'),
        ('Sredniozaawansowani', 'Średniozaawansowani'),
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
#--------------------------------------------------------------