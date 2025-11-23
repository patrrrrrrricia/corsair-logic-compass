from django.db import models


class Instruction(models.Model):
    DIRECTION_CHOICES = [
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
        ('north_east', 'North-East'),
        ('north_west', 'North-West'),
        ('south_east', 'South-East'),
        ('south_west', 'South-West'),
    ]

    direction = models.CharField(max_length=20, choices=DIRECTION_CHOICES)
    distance = models.PositiveIntegerField()
    description = models.TextField()
    previous_instruction = models.OneToOneField(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        unique=True
    )
    risk_level = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.distance} miles {self.direction}"

    def get_svg_path(self):
        svg_paths = {
            'north': 'M12 2L15 7H9L12 2Z',
            'south': 'M12 22L9 17H15L12 22Z',
            'east': 'M22 12L17 15V9L22 12Z',
            'west': 'M2 12L7 15V9L2 12Z',
            'north_east': 'M17 3L21 7L14 14L10 10L17 3Z',
            'north_west': 'M7 3L3 7L10 14L14 10L7 3Z',
            'south_east': 'M17 21L21 17L14 10L10 14L17 21Z',
            'south_west': 'M7 21L3 17L10 10L14 14L7 21Z',
        }
        return svg_paths.get(self.direction, '')