from .models import Comment, Entries, Game, Post, Profile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import widgets
from django import forms


# CommentstoApp
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "body")


# FormToUsers
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# FormEntries
class EntriesForm(forms.ModelForm):
    class Meta:

        title = forms.CharField(min_length=3, max_length=50)
        model = Entries
        fields = [
            "title",
            "gender",
            "review",
            "description",
            "date",
            "content",
            "article",
            "url",
            "image",
            "miniature",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                    "placeholder": "Titulo de la entrada.",
                }
            ),
            "gender": forms.Select(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                }
            ),
            "review": forms.Select(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                }
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                    "placeholder": "Descripcion breve de 35 caracteres.",
                }
            ),
            "date": forms.SelectDateWidget(
                attrs={
                    "class": "bg-dark text-light mb-3",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control mb-3 bg-dark text-light",
                    "rows": 3,
                    "placeholder": "Recuerda las normas de entradas.",
                }
            ),
            "article": forms.Textarea(
                attrs={
                    "class": "form-control mb-3 bg-dark text-light",
                    "rows": 3,
                    "placeholder": "Recuerda las normas por articulos.",
                }
            ),
            "url": forms.URLInput(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                    "placeholder": "Codigo embed del video de la entrada.",
                }
            ),
            "image": forms.FileInput(
                attrs={
                    "class": "mb-3 bg-primary text-light",
                }
            ),
            "miniature": forms.FileInput(
                attrs={
                    "class": "mb-3 bg-danger text-light",
                }
            ),
        }


# FormGames
class GamesForm(forms.ModelForm):
    class Meta:

        title = forms.CharField(min_length=3, max_length=50)
        model = Game
        fields = [
            "title",
            "gb",
            "gender",
            "review",
            "description",
            "date",
            "content",
            "requirement",
            "requirementm",
            "requirementr",
            "screen1",
            "screen2",
            "screen3",
            "download1",
            "download2",
            "download3",
            "url",
            "image",
            "miniature",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                    "placeholder": "Titulo del juego.",
                }
            ),
            "gb": forms.NumberInput(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                }
            ),
            "gender": forms.Select(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                }
            ),
            "review": forms.Select(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                }
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                    "placeholder": "Descripcion breve de 35 caracteres.",
                }
            ),
            "date": forms.SelectDateWidget(
                attrs={
                    "class": "bg-dark text-light mb-3",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control mb-3 bg-dark text-light",
                    "rows": 3,
                    "placeholder": "Recuerda las normas de contenido.",
                }
            ),
            "requirement": forms.TextInput(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                    "placeholder": "Comenta un emoji.",
                }
            ),
            "requirementm": forms.Textarea(
                attrs={
                    "class": "form-control mb-3 bg-dark text-light",
                    "rows": 3,
                    "placeholder": "Recuerda de los requerimientos.",
                }
            ),
            "requirementr": forms.Textarea(
                attrs={
                    "class": "form-control mb-3 bg-dark text-light",
                    "rows": 3,
                    "placeholder": "Recuerda de los requerimientos.",
                }
            ),
            "screen1": forms.URLInput(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                    "placeholder": "Recuerda las normas por imagen.",
                }
            ),
            "screen2": forms.URLInput(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                    "placeholder": "Recuerda las normas por imagen.",
                }
            ),
            "screen3": forms.URLInput(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                    "placeholder": "Recuerda las normas por imagen.",
                }
            ),
            "download1": forms.URLInput(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                    "placeholder": "Recuerda las normas por botones de descargas.",
                }
            ),
            "download2": forms.URLInput(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                    "placeholder": "Recuerda las normas por botones de descargas.",
                }
            ),
            "download3": forms.URLInput(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                    "placeholder": "Recuerda las normas por botones de descargas.",
                }
            ),
            "url": forms.URLInput(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                    "placeholder": "Codigo embed del video del juego.",
                }
            ),
            "image": forms.FileInput(
                attrs={
                    "class": "mb-3 bg-primary text-light",
                }
            ),
            "miniature": forms.FileInput(
                attrs={
                    "class": "mb-3 bg-danger text-light",
                }
            ),
        }


# FormPost
class NewsForm(forms.ModelForm):
    class Meta:

        title = forms.CharField(min_length=3, max_length=50)
        model = Post
        fields = [
            "title",
            "author",
            "number",
            "description",
            "copiri",
            "content",
            "url",
            "image",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                    "placeholder": "Titulo del post.",
                }
            ),
            "author": forms.Select(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                }
            ),
            "number": forms.NumberInput(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                }
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                    "placeholder": "Descripcion breve de 35 caracteres.",
                }
            ),
            "copiri": forms.TextInput(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                    "placeholder": "Titulo del copyright",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control mb-3 bg-dark text-light",
                    "rows": 3,
                    "placeholder": "Recuerda las normas de contenido.",
                }
            ),
            "url": forms.URLInput(
                attrs={
                    "class": "mb-3 bg-dark text-light",
                    "placeholder": "Codigo embed del video del post.",
                }
            ),
            "image": forms.FileInput(
                attrs={
                    "class": "mb-3 bg-primary text-light",
                }
            ),
        }


# FormProfile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar", "bio", "link"]
        widgets = {
            "avatar": forms.ClearableFileInput(
                attrs={"class": "form-control-file mt-3"}
            ),
            "bio": forms.Textarea(
                attrs={
                    "class": "form-control mt-3",
                    "rows": 3,
                    "placeholder": "Biografia",
                }
            ),
            "link": forms.URLInput(
                attrs={"class": "form-control mt-3", "placeholder": "Enlace"}
            ),
        }


# EditEmailProfile
class EmailForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        help_text="It requires 254 Characters Maximum.",
    )

    class Meta:
        model = User
        fields = ["email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "email" in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError(
                    "The email is already registered !, use a new one."
                )
        return email
