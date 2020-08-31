from django.db import models


class Education(models.Model):
    course = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.course


class Grade(models.Model):
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    grade = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.education) + " - " + self.name


class Work(models.Model):
    job_title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.job_title + " @ " + self.location


class Basic(models.Model):
    type = models.CharField(max_length=200)
    data = models.CharField(max_length=200)

    def __str__(self):
        return self.type
