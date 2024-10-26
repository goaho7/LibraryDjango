from django.db import models


class Author(models.Model):
    """Автор"""

    full_name = models.CharField(max_length=150)

    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    biography = models.TextField(verbose_name="Биография", null=True, blank=True)
    tags = models.ManyToManyField(
        "Tag",
        verbose_name="Тег",
        related_name="authors",
    )

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ("full_name",)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=250,
    )
    publication_date = models.DateField(verbose_name="Дата публикации")
    genre = models.CharField(
        verbose_name="Жанр",
        max_length=100,
    )
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    author = models.ForeignKey(
        Author,
        verbose_name="Автор книги",
        related_name="books",
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField(
        "Tag",
        verbose_name="Тег",
        related_name="books",
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ("-title",)

    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    name = models.CharField("Название", max_length=50, unique=True)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ("name",)

    def __str__(self):
        return self.name
