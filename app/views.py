from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.messages.api import success
from django.http.response import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.http import Http404
from .models import Entries, Post, Game, Profile, Aside
from django.views import generic
from django.contrib import messages
from .forms import (
    CustomUserCreationForm,
    EntriesForm,
    GamesForm,
    NewsForm,
    ProfileForm,
    EmailForm,
)
from django.db.models import Q
from django.views.generic.edit import FormView, UpdateView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django import forms
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.decorators.csrf import csrf_exempt

# Home
def main(request):
    posts = Entries.objects.all()
    page = request.GET.get("page", 1)
    search = request.GET.get("search")

    if search:
        posts = Entries.objects.filter(Q(title__icontains=search)).distinct()

    try:
        paginator = Paginator(posts, 8)
        posts = paginator.page(page)
    except:
        raise Http404

    data = {"entity": posts, "paginator": paginator}
    return render(request, "main.html", data)


# Aside
def aside(request):
    post = aside.objects.all()
    context = {"post": post}
    return render(request, "other/aside.html", context)


# HomeDetails
def entries_detail(request, id):
    posts = get_object_or_404(Entries, id=id)
    context = {"posts": posts}
    return render(request, "other/entries_detail.html", context)


# Games
def games(request):
    posts = Game.objects.all()
    page = request.GET.get("page", 1)
    search = request.GET.get("search")

    if search:
        posts = Game.objects.filter(Q(title__icontains=search)).distinct()

    try:
        paginator = Paginator(posts, 20)
        posts = paginator.page(page)

    except:
        raise Http404
    data = {"entity": posts, "paginator": paginator}
    return render(request, "games.html", data)


# GamesDetails
def game_detail(request, id):
    posts = get_object_or_404(Game, id=id)
    context = {"posts": posts}
    return render(request, "other/game_detail.html", context)


# VistNews
def news(request):
    posts = Post.objects.all()
    page = request.GET.get("page", 1)
    search = request.GET.get("search")

    if search:
        posts = Post.objects.filter(Q(title__icontains=search)).distinct()
    try:
        paginator = Paginator(posts, 6)
        posts = paginator.page(page)
    except:
        raise Http404

    data = {"entity": posts, "paginator": paginator}
    return render(request, "other/news.html", data)


# VistNewsDetails
def news_detail(request, id):
    posts = get_object_or_404(Post, id=id)
    context = {"posts": posts}
    return render(request, "other/news_detail.html", context)


# Donate
def donate(request):
    return render(request, "other/donate.html")


# ProfileUsers
@method_decorator(login_required, name="dispatch")
@method_decorator(csrf_exempt, name="dispatch")
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy("profile")
    template_name = "registration/profile_form.html"

    def get_object(self):
        try:
            return Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            return Profile.objects.create(user=self.request.user)


# EmailProfileChange
@method_decorator(login_required, name="dispatch")
@method_decorator(csrf_exempt, name="dispatch")
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy("profile")
    template_name = "registration/profile_email_form.html"

    def get_object(self):
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        form.fields["email"].widget = forms.EmailInput(
            attrs={"class": "form-control mb-2", "placeholder": "Email"}
        )
        return form


# Terms
def terms(request):
    return render(request, "other/terms.html")


# ADMIN PANEL


# Admin
@permission_required("app.admin_interface")
def admin(request):
    return render(request, "admin/admin_panel.html")


# AddEntries
@permission_required("add_entries")
def add_entries(request):
    data = {"form": EntriesForm()}

    if request.method == "POST":
        form = EntriesForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Save")
        else:
            data["form"] = form

    return render(request, "admin/add_entries.html", data)


# AddGames
@permission_required("add_games")
def add_games(request):
    data = {"form": GamesForm()}

    if request.method == "POST":
        form = GamesForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Save")
        else:
            data["form"] = form

    return render(request, "admin/add_games.html", data)


# AddNews
@permission_required("add_news")
def add_news(request):
    data = {"form": NewsForm()}

    if request.method == "POST":
        form = NewsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Save")
        else:
            data["form"] = form

    return render(request, "admin/add_news.html", data)


# login


# UsersRegister
@csrf_exempt
def sign_up(request):
    data = {"form": CustomUserCreationForm()}

    if request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"],
            )
            login(request, user)
            messages.success(request, "You Joined Successfully")
            return redirect(to="main")
        data["form"] = form

    return render(request, "registration/sign_up.html", data)
