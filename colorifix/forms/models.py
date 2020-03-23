from django.db import models

# Create your models here.
class Forms(models.Model):
    unique_id = models.IntegerField()
    unique_id.primary_key = True
    name = models.CharField(max_length=200, null=False)
    label = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=500, null=False)

    def get_parameters(self):
        return Parameters.objects.filter(form_id=self.unique_id)

    parameters = property(get_parameters)

    def __str__(self):
        return self.label

class Parameters(models.Model):
    unique_id = models.IntegerField()
    unique_id.primary_key = True
    name = models.CharField(max_length=200, null=False)
    label = models.CharField(max_length=200, null=False)
    param_type = models.CharField(max_length=200, null=False)
    form = models.ForeignKey(Forms, on_delete=models.CASCADE)

    def get_options(self):
        return Options.objects.filter(param_id=self.unique_id)

    options = property(get_options)

    def __str__(self):
        return self.name

class Options(models.Model):
    unique_id = models.IntegerField()
    unique_id.primary_key = True
    name = models.CharField(max_length=200, null=False)
    param = models.ForeignKey(Parameters, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Values(models.Model):
    unique_id = models.IntegerField()
    unique_id.primary_key = True
    form = models.ForeignKey(Forms, on_delete=models.PROTECT)
    param = models.ForeignKey(Parameters, on_delete=models.PROTECT)
    value = models.CharField(max_length=500)
