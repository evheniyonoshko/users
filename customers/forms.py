from django import forms
from customers.models import User, Courses, Customers
from users import settings

STATUS_CHOICES = (
    (False, "Inactive"),
    (True, "Active")
)

class UserAdminForm(forms.ModelForm):
    user_permissions = forms.SelectMultiple(
        attrs={
            'class': 'select2'
        }
    )

    class Meta:
        model = User
        exclude = ('last_login', 'password')



class CreateUserForm(forms.ModelForm):
    name = forms.CharField(
        label='Name',
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'Name'}),
        required=True,
    )

    email = forms.EmailField(
        label='E-Mail',
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'tinyperson@gmail.com'}),
        required=True,
    )

    phone = forms.CharField(
        label='Phone',
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'Phone'}),
        required=False
    )
    mobile_phone = forms.CharField(
        label='Mobile Phone',
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'Mobile Phone'}),
        required=False
    )

    status = forms.ChoiceField(
        label='Status',
        choices = STATUS_CHOICES)


    class Meta:
        model = Customers
        fields = ('name', 'email', 'phone', 'mobile_phone', 'status')


class CreateCoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ('name', 'code')


class ChangeUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        courses_choices = [(None,'Select course...')]
        for courses in Courses.objects.all():
            if courses.name:
                courses_choices.append((courses.name, courses.name))
        self.fields['courses'].choices = courses_choices

    name = forms.CharField(
        label='Name',
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'Name',
                                      'class': 'w3-gray',
                                      'readonly':'readonly'}),
        required=True,
    )

    email = forms.EmailField(
        label='E-Mail',
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'tinyperson@gmail.com'}),
        required=True,
    )

    phone = forms.CharField(
        label='Phone',
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'Phone'}),
        required=False
    )
    mobile_phone = forms.CharField(
        label='Mobile Phone',
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'Mobile Phone'}),
        required=False
    )

    status = forms.ChoiceField(
        label='Status',
        choices = STATUS_CHOICES)

    courses = forms.ChoiceField(
        label='Courses',
        required=False,
        widget=forms.Select(attrs={'class':'select-btn',
                                   'style': 'display:none;'})
    )

    class Meta:
        model = Customers
        fields = ('name', 'email', 'phone', 'mobile_phone', 'status', 'courses')
