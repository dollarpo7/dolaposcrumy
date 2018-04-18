from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import ScrumyGoals, ScrumyUser, ScrumyStatus
from .forms import AddUser, AddTask, EditTask
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User, Group
from django.views.generic import ListView, CreateView, DeleteView

# Create your views here.
class GoalsListView(ListView):
    model = ScrumyGoals
    template_name ='dolaposcrumy/home_page.html'


# def home_page(request):
#     scrumy_goals = ScrumyGoals.objects.all()
#     return render(request, 'dolaposcrumy/home_page.html', {'scrumy_goals':scrumy_goals})


@login_required
def add_user(request):
    if request.method == "POST":
        form = AddUser(request.POST)
        if form.is_valid():
            addUser = form.save(commit=False)
            addUser.save()
            return redirect('/')
    else:
        form = AddUser()
        return render(request, 'dolaposcrumy/add_user.html', {'form': form})


class GoalCreateView(CreateView, LoginRequiredMixin):
    model = ScrumyGoals
    template_name = 'dolaposcrumy/add_task.html'
    fields = '__all__'


# @login_required
# def add_task(request):
#     if request.method == "POST":
#         form = AddTask(request.POST)
#         if form.is_valid():
#             addTask = form.save(commit=False)
#             addTask.save()
#             return redirect('/')
#     else:
#
#         form= AddTask()
#         return render(request, 'dolaposcrumy/add_task.html', {'form': form})

# def home(request):
#
#     a = ScrumyGoals.objects.all().filter(task_category='daily goals')
#     a = get_object_or_404(ScrumyGoals, task_category='daily goals')
#     return render(request, 'registration/login.html', {'a': a })
#
#

# @login_required
# @user_passes_test(lambda u: u.groups.filter(name='Regular').count() == 0, login_url=None, redirect_field_name='/')
# def edit_task(request, pk):
#     addTask = get_object_or_404(ScrumyGoals, pk=pk)
#     if request.method == "POST":
#         form = AddTask(request.POST, instance=addTask)
#         if form.is_valid():
#             addTask = form.save(commit=False)
#             addTask.save()
#             return redirect('/', pk=addTask.pk)
#
#     else:
#         form = AddTask(instance=addTask)
#         return render(request, 'dolaposcrumy/add_task.html', {'form': form})

# class GoalsUpdateView(UpdateView):
#     model = ScrumyGoals
#     template_name = 'dolaposcrumy/edit_task.html'
#     fields = '__all__'

@login_required()
def edit_task(request, pk):
    # addTask = get_object_or_404(ScrumyGoals, pk=pk)
    if request.method == "POST":
        active_user = request.user
        active_user_group = Group.objects.get(user = active_user)
        task = ScrumyGoals.objects.get(pk = pk)
        if request.POST.get("status_id_id") == "WT":
            task.status_id_id = 4
            task.save()
            return redirect("/")

        elif request.POST.get("status_id_id") == "DT":
            task.status_id_id = 5
            task.save()
            return redirect("/")

        elif request.POST.get("status_id_id") == "V":
            Regular = Group.objects.get(pk = 1)
            if active_user_group.pk == Regular.pk:
                return render(request, "dolaposcrumy/denied.html")
            else:
                task.status_id_id = 6
                task.save()
                return redirect("/")

        elif request.POST.get("status_id_id") == "D":
            Regular = Group.objects.get(pk = 1)
            if active_user_group.pk == Regular.pk:
                return render(request, "dolaposcrumy/denied.html")
            else:
                task.status_id_id = 7
                task.save()
                return redirect("/")
    else:
        # form = AddTask(instance=addTask)
        return render(request, 'dolaposcrumy/edit_task.html', )

class DeleteGoalView(DeleteView, LoginRequiredMixin):
    model = ScrumyGoals
    template_name = 'dolaposcrumy/delete_task.html'
    success_url = reverse_lazy('dolaposcrumy:home')


