from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from . import models, forms

# チャットルームの一覧作成
class Index(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = models.Room
    template_name = 'chat/index.html'
    context_object_name = 'room_ctx'
    pagenate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        form = forms.SearchForm(self.request.GET or None)
        keywords = form.get_keywords()

        return queryset.filtering(user=self.request.user, keywords=keywords)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # チャットルーム検索用のフォームを追加
        context['search_form'] = forms.SearchForm(self.request.GET or None)

        return context

# チャットルームの作成
class CreateRoom(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = models.Room
    template_name = 'chat/room_form.html'
    form_class = forms.RoomForm
    success_url = reverse_lazy('chat:index')

    def form_valid(self, form):
        form.instance.set_host(self.request.user)
        
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super(CreateRoom, self).get_form_kwargs()
        kwargs['user_id'] = self.request.user.id
        return kwargs

class OnlyRoomHostMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        room = self.get_object()

        return room.is_host(self.request.user)

# チャットルームの更新
class UpdateRoom(LoginRequiredMixin, OnlyRoomHostMixin, UpdateView):
    model = models.Room
    template_name = 'chat/room_form.html'
    login_url = '/login/'
    form_class = forms.RoomForm
    success_url = reverse_lazy('chat:index') 

    def get_form_kwargs(self):
        kwargs = super(UpdateView, self).get_form_kwargs()
        kwargs['user_id'] = self.request.user.id
        return kwargs


# チャットルームの削除
class DeleteRoom(LoginRequiredMixin, OnlyRoomHostMixin, DeleteView):
    model = models.Room
    success_url = reverse_lazy('chat:index')

    def get(self, request, *args, **kwargs):
        # ignore direct access
        return self.handle_no_permission()

# 修正部分：チャットルームへの参加可否を判断するMixinを追加
class OnlyAssignedUserMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        room = self.get_object()

        return room.is_assigned(self.request.user)

# チャットルームへの入室
class EnterRoom(LoginRequiredMixin, OnlyAssignedUserMixin, DetailView):
    model = models.Room
    template_name = 'chat/chat_room.html'
    login_url = '/login/'
    context_object_name = 'room'

# チャットルームの更新
# class UpdateRoom(CreateView):
#     model = models.Room
#     template_name = 'chat/room_form.html'
#     login_url = '/login/'
#     success_url = reverse_lazy('chat:index')

#     def get(self,request, **kwargs):

#     def post(self,request,*args, **kwargs):