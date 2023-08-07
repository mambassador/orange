from django.contrib.auth.forms import forms, AuthenticationForm, UserCreationForm
from blog.models import User, Post, Comment
from .models import Contact


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-input"}))
    password = forms.PasswordInput(attrs={"class": "form-input"})


class UserSignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
            }
        )
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
        ]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "description",
            "photo",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["email"].widget.attrs.update({"class": "form-control"})
        self.fields["first_name"].widget.attrs.update({"class": "form-control"})
        self.fields["last_name"].widget.attrs.update({"class": "form-control"})
        self.fields["description"].widget.attrs.update({"class": "form-control"})
        self.fields["photo"].widget.attrs.update({"class": "form-control"})


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "text", "photo", "is_published"]
        publish = forms.BooleanField(label="Publish now", required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update({"class": "form-control"})
        self.fields["description"].widget.attrs.update({"class": "form-control"})
        self.fields["text"].widget = forms.Textarea(attrs={"class": "form-control"})
        self.fields["photo"].widget.attrs.update({"class": "form-control"})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["author", "text"]
        widgets = {
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)  # Get the request object
        super().__init__(*args, **kwargs)

        if self.request and self.request.user.is_authenticated:
            full_name = self.request.user.get_full_name()
            self.fields["author"].initial = full_name
            self.fields["author"].widget.attrs["readonly"] = True
        else:
            self.fields["author"].initial = "Anonymous User"
            self.fields["author"].widget.attrs["readonly"] = False


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "email", "message"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control"}),
        }
