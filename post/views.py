from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from post.forms import PostForm
from post.models import PostInfo

# 投稿画面表示、投稿情報保存
class PostPageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)
        
        return render(request, '../templates/post/test.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)
        
        if form.is_valid():
            post_data = PostInfo()
            post_data.account_id = request.user
            post_data.post = form.cleaned_data['post']
            if request.FILES: # 画像アップロード判定
                post_data.image = request.FILES.get('image')
                post_data.video = request.FILES.get('video')               
            post_data.save()
            return redirect('post:posts_completed')
        return render(request, '../templates/post/test.html', {'form': form})
    
# 投稿完了画面表示
class PostCompletePageView(TemplateView):
    template_name = '../templates/post/test_completed.html'

# 投稿検索画面表示
class PostSearchPageView(ListView):
    template_name = '../templates/post/test_s.html'
    model = PostInfo # 投稿情報モデル
    context_object_name = 'posts' # コンテキスト名
    
    def get_queryset(self, **kwargs): # モデルから情報を取得
        queryset = super().get_queryset(**kwargs) # 全取得
        
        keyword = self.request.GET.get('keyword') # 検索ワード取得
        if keyword is not None:
            queryset = queryset.filter(post__icontains=keyword) # 部分一致で検索
            
        queryset = queryset.order_by('-post_date') # 投稿降順で並び替え
        
        return queryset

class PostDetailPageView(ListView):
    template_name = '../templates/post/test_d.html'
    model = PostInfo
    context_object_name = 'post_detail' # コンテキスト名

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        
        # id = self.request.GET.get('id')
        id = self.kwargs.get('id')
        queryset = queryset.filter(id=id)
        
        return queryset