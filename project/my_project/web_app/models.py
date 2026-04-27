from django.db import models

class Marketplace(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание", default='')  
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фотография")
    price = models.IntegerField(verbose_name="Цена")
    email = models.EmailField(verbose_name="Email продавца", default = "")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)  

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"