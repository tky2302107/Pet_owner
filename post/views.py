from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from post.forms import PostForm
from post.models import PostInfo
  
# 投稿画面表示、投稿情報保存
class PostPageView(LoginRequiredMixin, CreateView):
<<<<<<< HEAD
    template_name = '../templates/post/test_post.html'
=======
    template_name = '../templates/post/post.html'
    login_url = '/login/'
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
    model = PostInfo
    form_class = PostForm
    success_url = reverse_lazy('post:posts_completed')
      
    def form_valid(self, form):
        form.instance.account_id = self.request.user
        return super().form_valid(form)

# 投稿完了画面表示
class PostCompletePageView(TemplateView):
<<<<<<< HEAD
    template_name = '../templates/post/test_completed.html'

# 投稿検索画面表示
class PostSearchPageView(ListView):
    template_name = '../templates/post/test_search.html'
=======
    template_name = '../templates/post/post_completed.html'
    login_url = '/login/'

# 投稿検索画面表示
class PostSearchPageView(ListView):
    template_name = '../templates/post/post_search.html'
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
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
<<<<<<< HEAD
    template_name = '../templates/post/test_detail.html' # テンプレート
=======
    template_name = '../templates/post/post_detail.html' # テンプレート
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
    context_object_name = 'post'

# 投稿削除画面表示
class PostDeletePageView(LoginRequiredMixin, DeleteView):
    model = PostInfo
<<<<<<< HEAD
    template_name = '../templates/post/test_confirm_delete.html'
=======
    template_name = '../templates/post/post_delete.html'
    login_url = '/login/'
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
    context_object_name = 'post'
    success_url = reverse_lazy('post:posts_delete_completed')

# 投稿削除完了画面表示
class PostDeleteCompletePageView(TemplateView):
<<<<<<< HEAD
    template_name = '../templates/post/test_delete_complete.html'

# 投稿履歴画面表示
class PostHistoryPageView(LoginRequiredMixin, ListView):
    template_name = '../templates/post/test_history.html'
=======
    template_name = '../templates/post/post_delete_complete.html'
    login_url = '/login/'

# 投稿履歴画面表示
class PostHistoryPageView(LoginRequiredMixin, ListView):
    template_name = '../templates/post/post_history.html'
    login_url = '/login/'
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
    model = PostInfo # 投稿情報モデル
    context_object_name = 'posts' # コンテキスト名
    
    def get_queryset(self, **kwargs): # モデルから情報を取得
        queryset = super().get_queryset(**kwargs) # 全取得
        
        user_id = self.request.user.id # ログイン中のユーザーのIDを取得
        queryset = queryset.filter(account_id=user_id).order_by('-post_date') # 完全一致検索、投稿降順で並び替え
        
        return queryset
    
    
# 投稿編集画面表示
class PostUpdatePageView(LoginRequiredMixin, UpdateView):
    model = PostInfo
    form_class = PostForm
<<<<<<< HEAD
    template_name = '../templates/post/test_update.html'
=======
    login_url = '/login/'
    template_name = '../templates/post/post_update.html'
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
    
    def get_success_url(self):
        return reverse('post:posts_detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        form.instance.account_id = self.request.user
        return super().form_valid(form)