from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Works(models.Model):
    id = models.AutoField(primary_key=True)
    workid = models.ForeignKey("WorkTitle", on_delete=models.CASCADE)
    statusid = models.ForeignKey("WorkStatus", on_delete=models.CASCADE)
    priority = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)
    plan_date = models.DateTimeField(null=True)


class WorkTitle(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title


class WorkStatus(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.status
