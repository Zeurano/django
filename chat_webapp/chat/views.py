from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from .forms import MessageForm, UserForm, MessageEditForm, CommentForm, CommentEditForm
from .models import Message, User, Comment


def register(request):
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      user = form.save()
      request.session['user_id'] = user.id
      return redirect('chat')
  else:
    form = UserForm()
  return render(request, 'register.html', {'form': form})


def chat(request):
  user_id = request.session.get('user_id')
  
  user = User.objects.get(id=user_id) if user_id else None
  messages = Message.objects.all().order_by('-timestamp')
  comments = Comment.objects.all().order_by('-timestamp')
  form = MessageForm()
  comment_form = CommentForm()

  if request.method == 'POST':
    if not user:
      return redirect('register')


  if request.method == 'POST':
    # Handle message editing
    if 'edit_message_id' in request.POST:
      message_id = request.POST['edit_message_id']
      message = get_object_or_404(Message, id=message_id)
      if message.user == user:
        form = MessageEditForm(request.POST, instance=message)
        if form.is_valid():
          form.save()
          return redirect('chat')

    # Handle message deleting
    elif 'delete_message_id' in request.POST:
      message_id = request.POST['delete_message_id']
      message = get_object_or_404(Message, id=message_id)
      if message.user == user:
        message.delete()
        return redirect('chat')

    
  
      
    elif 'comment_edit_id' in request.POST:
      comment_id = request.POST['comment_edit_id']
      comment = get_object_or_404(Comment, id=comment_id)
      if comment.user == user:
        form = CommentEditForm(request.POST, instance=comment)
        if form.is_valid():
          form.save()
          return redirect('chat')
    
    elif 'delete_comment_id' in request.POST:
              comment_id = request.POST['delete_comment_id']
              comment = get_object_or_404(Comment, id=comment_id)
              if comment.user == user:
                comment.delete()
                return redirect('chat')
        
            # Handle new message
    elif 'comment_idd' in request.POST:
      form = CommentForm(request.POST)
      if form.is_valid():
        comment = form.save(commit=False)
        comment.user = user
        comment.save()
        return redirect('chat')

    elif 'create_message' in request.POST:
      form = MessageForm(request.POST)
      if form.is_valid():
        message = form.save(commit=False)
        message.user = user
        message.save()
        return redirect('chat')
      
  else:
    form = MessageForm()

  

  return render(
      request,
      'chat.html',
      {
          'messages': messages,
          'comments': comments,
          'form': form,
          'comment_form': comment_form,
          'user': user,
      },
  )