from django.db import models

def car_images_path(instance, filename):
    # Generate file path for car images
    return f'car_images/{instance.make}_{instance.model}/{filename}'

class Car(models.Model):
    FUEL_TYPE_CHOICES = (
        ('Gasoline', 'Gasoline'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
        ('Other', 'Other'),
    )

    # Choices for transmission type
    TRANSMISSION_CHOICES = (
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    )

    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    description = models.TextField()
    fuel_type = models.CharField(max_length=50, choices=FUEL_TYPE_CHOICES)
    transmission = models.CharField(max_length=50, choices=TRANSMISSION_CHOICES)
    front_image = models.ImageField(upload_to=car_images_path, blank=True, null=True)
    back_image = models.ImageField(upload_to=car_images_path, blank=True, null=True)
    side_image = models.ImageField(upload_to=car_images_path, blank=True, null=True)
    interior_image = models.ImageField(upload_to=car_images_path, blank=True, null=True)
    engine_bay_image = models.ImageField(upload_to=car_images_path, blank=True, null=True)
    trunk_image = models.ImageField(upload_to=car_images_path, blank=True, null=True)
    main_image = models.URLField(max_length=200)
    features = models.ManyToManyField('Feature', blank=True, null=True)

    def __str__(self):
        return f"{self.make} {self.model}"


class Feature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name