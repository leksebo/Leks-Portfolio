from django.db import models
from django.core.exceptions import ValidationError
from tinymce.models import HTMLField

def validate_json_data(value):
    """Custom validator for JSON fields"""
    if not isinstance(value, (dict, list)):
        raise ValidationError("Value must be a JSON object or array")

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Full Name")
    description = HTMLField(verbose_name="Description")
    role = models.CharField(max_length=100, verbose_name="Role")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Personal Information"
        verbose_name_plural = "Personal Information"

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Project Title")
    description = HTMLField(verbose_name="Project Description")
    link = models.URLField(verbose_name="Project Link")
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True,
        help_text="Upload project images here",
        verbose_name="Project Image"
    )
    is_featured = models.BooleanField(default=False, verbose_name="Featured Project")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['-is_featured', 'title']
