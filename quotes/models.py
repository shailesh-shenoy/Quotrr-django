from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Personality(models.Model):
    personality_name = models.CharField(
        "Influential Person", unique=True, max_length=100
    )
    slug = models.SlugField(blank=True, unique=True, max_length=100)
    info = models.TextField("Information")
    trivia = models.TextField("Trivia")

    def __str__(self):
        return self.personality_name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.personality_name)

        super(Personality, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "personalities"
