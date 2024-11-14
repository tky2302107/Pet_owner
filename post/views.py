from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from post.forms import PostForm
from post.models import PostInfo

# 投稿画面表示
class PostPageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)
        
        return render(request, 'template/post/post.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)
        
        if form.is_valid():
            post_data = PostInfo()
            post_data.account_id = request.user
            post_data.post = form.cleaned_data['post']
            if request.FILES:
                post_data.image = request.FILES.get('image')
            post_data.save()
            return redirect('post_completed', post_data.pk)
        
        return render(request, 'template/post/post.html', {'form': form})
    
# 投稿検索画面表示
class PostSearchPageView(View):
    ''