from django.db import models

from .consts import MAX_RATE

CATEGORY=(('SF/Fantasy','SF/ファンタジー'),('Robot','ロボット/メカ'),('Action/Battle','アクション/バトル'),('Comedy','コメディ/ギャグ'),('Love','恋愛/ラブコメ'),('Sports','スポーツ/競技'),('Horror/Suspense/Reasoning','ホラー/サスペンス/推理'),('History/War','戦争/歴史'),('Horror/Suspense/Reasoning','ホラー/サスペンス/推理'),('Aoharu','青春/ドラマ'),('Honobono','日常/ほのぼの'),('Other/Bridge','その他＆橋'))

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]

class Book(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField()
    thumbnail=models.ImageField(null=True, blank=False)
    category=models.CharField(
        max_length=100,
        choices=CATEGORY
        )
    
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title