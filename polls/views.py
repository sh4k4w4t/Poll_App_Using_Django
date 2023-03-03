# app name = 'polls'
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CreatePollForm
from .models import Poll


def home(request):
    poll = Poll.objects.all()
    context = {'poll': poll}
    return render(request, 'polls/home.html', context)


def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
    context = {'form': form}
    return render(request, 'polls/create.html', context)


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':
        selected_option = request.POST["poll"]
        if selected_option == "option_one":
            poll.option_one_count += 1
        elif selected_option == "option_two":
            poll.option_two_count += 1
        elif selected_option == "option_three":
            poll.option_three_count += 1
        else:
            return HttpResponse(400, "invalid form")
        poll.save()
        return redirect('results', poll_id)
    context = {'poll': poll}
    return render(request, 'polls/vote.html', context)


def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {'poll': poll}
    return render(request, 'polls/results.html', context)
