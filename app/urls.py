from app.models import Profile
from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("<int:id>/entries-detail/", views.entries_detail, name="entries_detail"),
    path("games/", views.games, name="games"),
    path("<int:id>/game-detail/", views.game_detail, name="game_detail"),
    path("news/", views.news, name="news"),
    path("<int:id>/news-detail/", views.news_detail, name="news_detail"),
    # DONATIONS
    path("donate/", views.donate, name="donate"),
    # ADMIN PANEL
    path("admin-panel/", views.admin, name="admin_panel"),
    path("add-entries/", views.add_entries, name="add_entries"),
    path("add-games/", views.add_games, name="add_games"),
    path("add-news/", views.add_news, name="add_news"),
    # ACCOUNTS
    path("sign-up/", views.sign_up, name="sign_up"),
    path("accounts/profile/", views.ProfileUpdate.as_view(), name="profile"),
    path("profile/email/", views.EmailUpdate.as_view(), name="profile_email"),
    # TERMS
    path("terms/", views.terms, name="terms"),
]
