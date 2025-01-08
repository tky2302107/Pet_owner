from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    # 定期実行設定↓
    def ready(self):
        from .ap_scheduler import start
        start()