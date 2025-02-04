from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from . import models, forms
from django.shortcuts import redirect, render
from contents.models import NoticeList
from django.http import HttpResponseRedirect
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
    # success_url = reverse_lazy('chat:buffer')
    # fields = (
    #     "field",
    # )
    def get_success_url(self):
        return reverse_lazy("chat:create_buffer",kwargs={"pk":self.request.user.id})

    def form_valid(self, form):
        form.instance.set_host(self.request.user)
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super(CreateRoom, self).get_form_kwargs()
        kwargs['user_id'] = self.request.user.id
        return kwargs

    # def post(self):
    #     # kwargs = super(CreateRoom, self).get_form_kwargs()
    #     # kwargs['create_room_url'] = self.kwargs['pk']
    #     return redirect("chat:buffer", pk=self.kwargs['pk'])
    

 
    

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
    # success_url = reverse_lazy('chat:index') 

    def get_form_kwargs(self):
        kwargs = super(UpdateView, self).get_form_kwargs()
        kwargs['user_id'] = self.request.user.id
        return kwargs

    def get_success_url(self, **kwargs):
        return reverse_lazy("chat:update_buffer",kwargs={"pk":self.kwargs["pk"]})


# チャットルームの削除
"""
class DeleteRoom(LoginRequiredMixin, OnlyRoomHostMixin, DeleteView):
    model = models.Room
    success_url = reverse_lazy('chat:index')
    # def get_success_url(self):
    #     return reverse_lazy("chat:delete_buffer",kwargs={"pk":self.request.user.id})

    def get(self, request, *args, **kwargs):
        # ignore direct access    
        # print("rpk:"+str(self.kwargs["room.pk"]))
        return self.handle_no_permission()
""" 
    # def get_queryset(self):
    #     # url= request.POST["url"]
    #     # print(self.kwargs["pk"])
    #     m1 = int(models.Room.objects.order_by("-created_at").filter(host_id=self.request.user.id).values()[0]["id"])
    #     print("削除")
    #     userlist = list(models.Room.objects.get(id=m1).participants.filter().values())
    #     newul = []
    #     cr = str(list(models.Room.objects.filter(id=m1).values())[0]["name"])
    #     for i in range(len(userlist)):
    #         newul.append(userlist[i]["id"])
    #     print('削除処理中')
        
        
    #     for i in range(len(newul)):
    #         chknl=list(NoticeList.objects.filter(target=newul[i],text="チャットルーム「"+str(cr)+"」が解散しました。").values())
    #     print("chknl: "+str(chknl))
    #     print("newnl: "+str(chknl))

    #     if chknl == [] :
    #         print("削除中断")
    #     else:
    #         for j in range(len(newul)):
    #             Notice = NoticeList(
    #                 target=newul[j],
    #                 title="チャットルーム解散のお知らせ",
    #                 text="チャットルーム「"+str(cr)+"」が解散しました。",
    #                 )
    #             Notice.save()
    #         print("削除終了")
            
    #     return super().get_queryset()
        
    

    # def post(self, request, *args, **kwargs):


# 修正部分：チャットルームへの参加可否を判断するMixinを追加
class OnlyAssignedUserMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        room = self.get_object()

        return room.is_assigned(self.request.user)

# チャットルームへの入室\
class EnterRoom(LoginRequiredMixin, OnlyAssignedUserMixin, DetailView):
    model = models.Room
    template_name = 'chat/chat_room.html'
    login_url = '/login/'
    context_object_name = 'room'

class CreateBufferView(TemplateView):
    template_name = "chat/buffer.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["url"] = self.kwargs["pk"]
        return context
    

    def post(self, request, *args, **kwargs):
        url= request.POST["url"]
        print(self.kwargs["pk"])
        m1 = int(models.Room.objects.order_by("-created_at").filter(host_id=url).values()[0]["id"])
        print("作成")
        userlist = list(models.Room.objects.get(id=m1).participants.filter().values())
        newul = []
        for i in range(len(userlist)):
            newul.append(userlist[i]["id"])

        cr = str(list(models.Room.objects.filter(id=m1).values())[0]["name"])
        for j in range(len(newul)):
            Notice = NoticeList(
                target=newul[j],
                title="チャットルーム招待のお知らせ",
                text="チャットルーム「"+str(cr)+"」に招待されました。",
                )
            Notice.save()
        return redirect('chat:index')


class UpdateBufferView(TemplateView):
    template_name = "chat/buffer.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["url"] = self.kwargs["pk"]
        return context
    
    def post(self, request, *args, **kwargs):
        url= request.POST["url"]
        print("更新")
        model1 = models.Room.objects.get(id=int(url))
        # print(model1)
        userlist = list(model1.participants.filter().values())
        newul = []
        # print(userlist)
        for i in range(len(userlist)):
            newul.append(userlist[i]["id"])

        cr = str(list(models.Room.objects.filter(id=int(url)).values())[0]["name"])
        for j in range(len(newul)):
            Notice = NoticeList(
                target=newul[j],
                title="チャットルーム更新のお知らせ",
                text="チャットルーム「"+str(cr)+"」で情報が更新されました。\n更新によって、ルーム名やユーザー人数が変更されている場合があります。",
                )
            Notice.save()
        return redirect('chat:index')
    
    
    
class DeleteView(TemplateView,LoginRequiredMixin, OnlyRoomHostMixin, ):
    template_name = "chat/delete_buffer.html"
    def get_context_data(self, **kwargs):
        
        m1=self.kwargs["pk"]
        # print("削除")
        userlist = list(models.Room.objects.get(id=m1).participants.filter().values())
        newul = []
        cr = str(list(models.Room.objects.filter(id=m1).values())[0]["name"])
        for i in range(len(userlist)):
            newul.append(userlist[i]["id"])
        # print('削除処理中')
        
        
        for i in range(len(newul)):
            chknl=list(NoticeList.objects.filter(target=newul[i],text="チャットルーム「"+str(cr)+"」が解散しました。").values())
        # print("chknl: "+str(chknl))
        # print("newnl: "+str(chknl))

        for j in range(len(newul)):
            Notice = NoticeList(
                target=newul[j],
                title="チャットルーム解散のお知らせ",
                text="チャットルーム「"+str(cr)+"」が解散しました。",
                )
            Notice.save()
        # print("削除終了")
            
    
        
        
        # print("削除")
        context = super().get_context_data(**kwargs)
        context["room"] = self.kwargs["pk"]
        models.Room.objects.get(id=int(self.kwargs["pk"])).delete()
        return context
    

    def post(self, request, *args, **kwargs):
        return redirect('chat:index')
    
# 動かないときはNoticeをnlに変える