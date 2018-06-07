from json import dump
from teams.models import Team
from ctfboard.config import BOARDS_ROOT
import os


def generate_scoreboard(competition):
    teams = Team.objects.filter(competition=competition).order_by('-score', 'last_submit')
    response = []
    for team in teams:
        response.append((team.name, team.city, team.score))
    with open(os.path.join(BOARDS_ROOT, competition + ".json"), "w") as f:
        dump(response, f)
