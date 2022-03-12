from django.shortcuts import render
from django.views import generic
from .models import Comment
from django.http import HttpResponseRedirect

# Create your views here.
class IndexView (generic.ListView):
    template_name = 'commentapp/index.html'
    context_object_name = 'comment_list'
    def get_queryset(self):
        return Comment.objects.order_by('date_published')
    
class MyCommentView(generic.DetailView):
    template_name = 'commentapp/myComment.html'
    # context_object_name = 'myComment'
    model = Comment

    
# def createComment(request):
#     new_comment = Comment(request.body)
#     if (new_comment): 
#         new_comment.save()
#     return HttpResponseRedirect(reverse('commentapp:index', args=(comment.id)))
    