from django.views.generic import TemplateView,ListView
from django.contrib.auth.views import LoginView, LogoutView
from .models import User

class Index(TemplateView):
    template_name = 'accounts/index.html'

class LoginPage(LoginView):
    template_name = 'accounts/login.html'

class LogoutPage(LogoutView):
    template_name = 'accounts/logout.html'
    
class MainPage(TemplateView):
    template_name = 'main.html'
    
class ExchangePoint(TemplateView):
    template_name = 'accounts/p1.html'
    model = User
    # def get_queryset(self):
    #     return super().get_queryset()
    # nl = User.objects.filter(id=1)


    def get(self, request, **kwargs):
        ctx = {
            'points': self.request.user.points
        }
        print("ctx"+str(ctx))
        return self.render_to_response(ctx)
    
class ExchangePointComplete(TemplateView):
    template_name = 'accounts/p2.html'
    # model = User
    
    # def get(self, request, **kwargs):
    #     global ctxii
    #     ctxii = {
    #         'points': self.request.user.points
    #     }
    #     print("ctx"+str(ctxii))
    #     return ctxii
    # if ctxii == 0:
    #     pass
    # else:
    #     ctxii+=1
    #     User.points = 0
    #     User.save()

    