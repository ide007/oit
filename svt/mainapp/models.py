from django.db import models


class Category(models.Model):
    objects = None
    name = models.CharField(
        max_length=64,
        verbose_name='Категория',
        unique=True,
    )

    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )

    created = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Location(models.Model):
    objects = None
    name = models.CharField(
        max_length=64,
        verbose_name='Расположение',
        unique=True,
    )

    description = models.TextField(
        verbose_name='Адрес расроложения',
        blank=True,
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'Расположение'
        verbose_name_plural = 'Адреса расположения'


class Model(models.Model):
    objects = None
    inventory_number = models.CharField(max_length=64,
                                        verbose_name='инвентарный номер',
                                        unique=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL,
                                 null=True, default=0)
    serial_number = models.CharField(max_length=64,
                                     verbose_name='серийный номер',
                                     blank=True, null=True)

    name = models.CharField(max_length=128, verbose_name='Модель')

    shot_desc = models.CharField(
        verbose_name='коментарий',
        max_length=252,
        blank=True
    )

    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='История',
    )

    @staticmethod
    def get_items():
        return Model.objects.filter(
            quantity__gte=1
        ).order_by('category', 'name')

    def __str__(self):
        return f'{self.name} ({self.category.name})'

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

