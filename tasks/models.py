from django.db import models

# Create your models here.
COLORS = [
    ('gray', 'Gray'),
    ('blue', 'Blue'),
    ('purple', 'Purple'),
    ('red', 'Red'),
    ('green', 'Green'),
]


class Category(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200, choices=COLORS, default="gray")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'


class Task(models.Model):
    title           = models.CharField(max_length=115)
    extra_info      = models.CharField(max_length=300, blank=True)
    complete        = models.BooleanField(default=False)
    created         = models.DateTimeField(auto_now_add=True)
    # category        = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, blank=True)
    category        = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title