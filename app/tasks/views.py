from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from ctfboard.config import *
import os
import yaml
from tasks.models import Submit, Hint
from teams.models import Team
from django.utils.timezone import now
from tasks.utils import generate_scoreboard


def get_task(team, slug):
    TASKS_PATH = COMPETITIONS[team.competition]["tasks_folder"]

    if not os.path.exists(os.path.join(TASKS_PATH, slug)):
        raise Http404()

    task = yaml.load(open(os.path.join(TASKS_PATH, slug, "config.yml"), encoding="utf-8").read())
    task["solutions"] = Submit.objects.filter(success=True, task=slug).count()
    task["solved"] = Submit.objects.filter(success=True, task=slug, team=team).count() > 0

    return task


def login(request):
    error = False
    if request.session.get("team", None) is not None:
        return redirect("/")
    if request.method == "POST":
        teams = Team.objects.filter(
            login=request.POST.get("login", ""),
            password=request.POST.get("password", "")
        )
        if len(teams) == 1:
            team = teams[0]
            request.session["team"] = team.id
            return redirect("/")
        error = True
    return render(request, "login.html", {"error": error})


def logout(request):
    request.session["team"] = None
    return redirect("/")


def show_tasks(request):
    if request.session.get("team", None) is None:
        return redirect("/login/")
    team = get_object_or_404(Team, id=int(request.session["team"]))
    
    if now() < COMPETITIONS[team.competition]["start_time"]:
        return render(request, "not_started.html", {
            "competition_name": COMPETITIONS[team.competition]["full_name"],
            "team": team,
            "scoreboard_path": os.path.join(BOARDS_URL, team.competition),
            "time1": now(),
            "time2": COMPETITIONS[team.competition]["start_time"],
            "delta": now() - COMPETITIONS[team.competition]["start_time"]
        })

    tasks = []
    for task in os.listdir(COMPETITIONS[team.competition]["tasks_folder"]):
        if not task.startswith(".") and os.path.isdir(os.path.join(COMPETITIONS[team.competition]["tasks_folder"], task)):
            tasks.append(get_task(team, task))

    return render(request, "tasks.html", {
        "competition_name": COMPETITIONS[team.competition]["full_name"],
        "team": team,
        "tasks": tasks,
        "scoreboard_path": os.path.join(BOARDS_URL, team.competition)
    })


def show_task(request, slug):
    if request.session.get("team", None) is None:
        return redirect("/login/")
    team = get_object_or_404(Team, id=int(request.session["team"]))

    task = get_task(team, slug)
    wrong = False
    if request.method == "POST":
        flag = request.POST.get("flag", "")
        correct = flag.lower().strip() == task["flags"][0]["text"].lower().strip()
        Submit(
            task=slug,
            team=team,
            text=flag,
            success=correct
        ).save()
        if correct and not task["solved"]:
            #team.score += task["points"]
            #team.last_submit = now()
            #team.save()
            task["solved"] = True
            task["solutions"] += 1
            generate_scoreboard(team.competition)
        else:
            wrong = True

    return render(request, "task.html", {
        "competition_name": COMPETITIONS[team.competition]["full_name"],
        "team": team,
        "task": task,
        "scoreboard_path": os.path.join(BOARDS_URL, team.competition),
        "wrong": wrong,
        "main_block_attr": "main-block-task"
    })
