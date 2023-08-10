from django.db import models

class Skill(models.Model):
    # Создаём столбцы в таблице
    skill = models.CharField('Название скила', max_length=50, default='Не заполнено')
    opisanie = models.CharField('Краткое описание', max_length=250, default='Не заполнено')
    full_text = models.TextField('Примеры реализации')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.skill

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
