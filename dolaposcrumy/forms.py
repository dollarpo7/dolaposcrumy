from django import forms

from .models import ScrumyUser, ScrumyGoals, ScrumyStatus

class AddUser(forms.ModelForm):
    class Meta:
        model = ScrumyUser
        fields = ('userName','firstName','lastName')

# class StatusChoice(forms.ModelForm):
#     class Meta:
#         model = ScrumyStatus
#         fields = ('__all__')

class AddTask(forms.ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ('__all__')

class EditTask(forms.ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ('__all__')



# class MoveTask(forms.ModelForm):
#
#     class Meta:
#         model = ScrumyUser
#         fields = ('userName')