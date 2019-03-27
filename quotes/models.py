from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Personality(models.Model):
    personality_name = models.CharField(
        "Influential Person", unique=True, max_length=100
    )
    slug = models.SlugField("Slug", blank=True, unique=True, max_length=100)
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


class Quote(models.Model):
    personality = models.ForeignKey(
        Personality, on_delete=models.SET_NULL, blank=True, null=True
    )
    quote_text = models.TextField("Quote")
    quote_slug = models.SlugField("Slug", blank=True, unique=True, max_length=255)

    def __str__(self):
        return self.quote_text

    def save(self, *args, **kwargs):
        if not self.id:
            self.quote_slug = slugify(self.quote_text)[:255]

        super(Quote, self).save(*args, **kwargs)
