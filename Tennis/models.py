from django.db import models


# Create your models here.
class Player(models.Model):
    player_name = models.CharField(max_length=512)
    player_alias = models.CharField(max_length=256, blank=True)
    player_URL = models.CharField(max_length=1024)
    player_seed = models.CharField(max_length=3)
    player_img = models.FileField()

    def __str__(self):
        return self.player_name


class Tournament(models.Model):
    tournament_name = models.CharField(max_length=256)
    tournament_location = models.CharField(max_length=256, default=False)
    tournament_start_date = models.DateField()
    tournament_category = models.CharField(max_length=100)
    tournament_surface = models.CharField(max_length=256)
    tournament_draw = models.CharField(max_length=10)
    tournament_popularity = models.BooleanField(default=False)

    def __str__(self):
        return self.tournament_name


class Match(models.Model):
    match_nid = models.CharField(max_length=512)
    match_hour = models.CharField(max_length=100)
    match_round = models.CharField(max_length=100)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player1 = models.ManyToManyField(Player, related_name='player1')
    player2 = models.ManyToManyField(Player, related_name='player2')
    # PLAYER 1 SETS
    player1_set1 = models.IntegerField()
    player1_set2 = models.IntegerField()
    player1_set3 = models.IntegerField()
    player1_set4 = models.IntegerField()
    player1_set5 = models.IntegerField()
    # PLAYER 2 SETS
    player2_set1 = models.IntegerField()
    player2_set2 = models.IntegerField()
    player2_set3 = models.IntegerField()
    player2_set4 = models.IntegerField()
    player2_set5 = models.IntegerField()
    # GLOBAL
    player1_setTotal = models.IntegerField()
    player2_setTotal = models.IntegerField()
    total_games = models.IntegerField()

    def __str__(self):
        return self.match_nid