from django.db import models


class Article(models.Model):
    CATEGORY_CHOICES = [
        ("achievement", "إنجازات"),
        ("training", "تدريب"),
        ("initiative", "مبادرات"),
        ("partnership", "شراكات"),
    ]

    title = models.CharField(max_length=250)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    summary = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to="news_images/", blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title