from django.db import models


class Presentation(models.Model):
    CLASS_CHOICES = [
        ("5", "5 класс"),
        ("6", "6 класс"),
        ("7", "7 класс"),
        ("8", "8 класс"),
        ("9", "9 класс"),
        ("10", "10 класс"),
        ("11", "11 класс"),
    ]

    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    school_class = models.CharField(
        max_length=2,
        choices=CLASS_CHOICES,
        default="5",
        verbose_name="Класс",
    )
    file = models.FileField(upload_to="presentations/", verbose_name="Файл презентации")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_school_class_display()})"

    class Meta:
        verbose_name = "Презентация"
        verbose_name_plural = "Презентации"
