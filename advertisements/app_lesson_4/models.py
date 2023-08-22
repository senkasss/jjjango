from django.db import models
from django.utils.html import format_html
class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Стоимость", max_digits = 10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text = "Если торг уместен, поставье 1. Если нет - 0.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)


    def created_date(self):
        from django.utils import timezone
        if self.created_at.date()== timezone.now().date:
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html('<span style = "color: green; font-weight: bold;">Сегодня в {}</span>', created_time)
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")



    def updated_date(self):
        from django.utils import timezone
        if self.created_at.date()== timezone.now().date:
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html('<span style = "color: blue; font-weight: bold;">Сегодня в {}</span>', created_time)
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
