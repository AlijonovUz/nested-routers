from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
