from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='укажите название блога')
    description = models.TextField(blank=True, verbose_name='укажите описание блога')
    image = models.ImageField(upload_to='blog/', verbose_name='загрузите фото')
    GENRE_BLOG = (
        ('Информационные технологии', 'Информационные технологии'),
        ('Исскуственный интелект', 'Исскуственный интелект'),
        ('Бизнес и работа в IT сфере', 'Бизнес и работа в IT сфере')
    )
    genre_blog = models.CharField(max_length=100, choices=GENRE_BLOG, verbose_name='укажите жанр')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

    def __str__(self):
        return self.title


