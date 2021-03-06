from django.db import models
from members.models import Member


# Create your models here.
# ----- MODEL AKTYWNYCH EDYCJI -----
class Active_round(models.Model):
    round = models.CharField(max_length=5, verbose_name='Runda')
    current_round = models.BooleanField(verbose_name='Bieżąca', default=False)

    def __str__(self):
        return str(self.round)

# ----- MODEL AKTYWNYCH EDYCJI -----
class Active_edition(models.Model):
    edition = models.IntegerField(verbose_name='Edycja', unique=True)
    current_edition = models.BooleanField(verbose_name='Bieżąca', default=False)

    def __str__(self):
        return str(self.edition)


# ----- MODEL DRÓG WSPINACZKOWYCH -----
class Route(models.Model):
    route_name = models.CharField(max_length=60, unique=False, verbose_name='Nazwa Drogi')
    route_grade = models.CharField(max_length=5, verbose_name='Wycena')
    points = models.FloatField(verbose_name='Punktacja')
    edition = models.IntegerField(verbose_name='Edycja', null=True)
    round = models.CharField(max_length=5, verbose_name='Runda')
    route_group = models.CharField(max_length=60, verbose_name='Grupa')
    add_date = models.DateTimeField(verbose_name='Data dodania', auto_now_add=True)

    REQUIRED_FIELDS = ['route_name', 'route_grade', 'points', 'edition', 'round', 'route_group']

    def __str__(self):
        return self.route_name


# ----- MODEL POKONANYCH DRÓG UŻYTKOWNIKA -----
class User_routes(models.Model):
    user_name = models.ForeignKey(Member, verbose_name=("User"), on_delete=models.CASCADE, null=True)
    user_routes = models.ForeignKey(Route, verbose_name=("Routes"), on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = ('user_name', 'user_routes',)
        # TU BĘDZIE PROBLEM JAK DROGA POJAWI SIĘ RÓWNIEŻ W INNEJ EDYCJI
        # TRZEBA NAPISAĆ validate_unique method
        # https://stackoverflow.com/questions/4440010/django-unique-together-with-foreign-keys


# ----- MODEL GRUPY UŻYTKOWNIKA -----
class User_Group(models.Model):
    user_name = models.ForeignKey(Member, verbose_name='User', on_delete=models.CASCADE, null=True)
    edition = models.IntegerField(verbose_name='Edycja')
    user_group = models.CharField(max_length=60, verbose_name='Grupa')

    def __str__(self):
        return self.user_group
