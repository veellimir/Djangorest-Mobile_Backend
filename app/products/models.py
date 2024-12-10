from django.db import models

from mixins.base_meta_str import StrMixin


class CardItem(StrMixin, models.Model):
    name = models.CharField(max_length=100, verbose_name="Название товара")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to="media/card_items/", blank=False, null=False, verbose_name="Изображение")
    is_available = models.BooleanField(default=True, verbose_name="Доступен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"