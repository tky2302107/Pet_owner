from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

# 投稿画面表示
class PostPageView(TemplateView):
    template_name = 'post.html'

# 投稿情報更新
class UpdatePostInfo(CreateView):
    template_name = ''