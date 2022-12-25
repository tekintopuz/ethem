from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="username")
    password = forms.CharField(max_length=100, label="password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, label="username")
    name = forms.CharField(max_length=100, label="name")
    lastname = forms.CharField(max_length=100, label="lastname")
    email = forms.CharField(max_length=100, label="email")
    password = forms.CharField(max_length=100, label="password", widget=forms.PasswordInput)
    confPassword = forms.CharField(max_length=100, label="password", widget=forms.PasswordInput)
    choiceRole = (
        ("1", "Select1"),
        ("2", "S"),
        ("3", "Three"),
        ("4", "Four"),
        ("5", "Five"),
    )

    user_role = forms.ChoiceField(choices=choiceRole)
