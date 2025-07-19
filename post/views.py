from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Comment
from django.contrib.auth.decorators import login_required

def post_detail(request, pk):
    post = get_object_or_404(News, pk=pk)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_text = request.POST.get('text')
            if comment_text:
                Comment.objects.create(
                    news=post,
                    user=request.user,
                    text=comment_text
                )
                return redirect('get-detail', pk=pk)
        else:
            return redirect('get-login')

    return render(request, 'blog.html', {
        'post': post,
        'comments': comments,
    })
