from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, View, ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from post.forms import PostForm
from post.models import PostInfo

# 投稿画面表示、投稿情報保存
class PostPageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)
        
        return render(request, '../templates/post/test_post.html', {'form': form})
    
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
    template_name = '../templates/post/test_search.html'
    model = PostInfo # 投稿情報モデル
    context_object_name = 'posts' # コンテキスト名
    
    def get_queryset(self, **kwargs): # モデルから情報を取得
        queryset = super().get_queryset(**kwargs) # 全取得
        
        keyword = self.request.GET.get('keyword') # 検索ワード取得
        if keyword is not None:
            queryset = queryset.filter(post__icontains=keyword) # 部分一致で検索
            
        queryset = queryset.order_by('-post_date') # 投稿降順で並び替え
        
        return queryset

# 投稿詳細画面表示
class PostDetailPageView(DetailView):
    model = PostInfo # 投稿情報モデル
    template_name = '../templates/post/test_detail.html' # テンプレート
    context_object_name = 'post'

# 投稿削除画面表示
class PostDeletePageView(LoginRequiredMixin, DeleteView):
    model = PostInfo
    template_name = '../templates/post/test_confirm_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post:posts_delete_completed')

# 投稿削除完了画面表示
class PostDeleteCompletePageView(TemplateView):
    template_name = '../templates/post/test_delete_complete.html'

# 投稿履歴画面表示
class PostHistoryPageView(LoginRequiredMixin, ListView):
    template_name = '../templates/post/test_history.html'
    model = PostInfo # 投稿情報モデル
    context_object_name = 'posts' # コンテキスト名
    
    def get_queryset(self, **kwargs): # モデルから情報を取得
        queryset = super().get_queryset(**kwargs) # 全取得
        
        user_id = self.request.user.id # ログイン中のユーザーのIDを取得
        queryset = queryset.filter(account_id=user_id).order_by('-post_date') # 完全一致検索、投稿降順で並び替え
        
        return queryset