from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Board, Topic, Post
from .forms import NewTopicForm
# from user_contacts.new_contact_form import ContactForm



def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})

# def new_topic(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     user = User.objects.first()  # TODO: get the currently logged in user
#     if request.method == 'POST':
#         form = NewTopicForm(request.POST)
#         if form.is_valid():
#             topic = form.save()
#             return redirect('board_topics', pk=board.pk)
#     else:
#         form = NewTopicForm()
#     return render(request, 'new_topic.html', {'form': form})
