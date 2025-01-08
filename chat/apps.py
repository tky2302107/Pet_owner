from django.apps import AppConfig


class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'
    # 定期実行設定↓
    def ready(self):
        from .ap_scheduler import start
        start()