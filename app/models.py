from django.db import models

class Skill(models.Model):
    LEVEL_CHOICES = [(1, "Basic"), (2, "Developing"), (3, 3), (4, 4), (5, 5)]
    description = models.CharField('Description', max_length=255,null=True, blank=True)
    category = models.CharField('Category', max_length=255, null=True, blank=True)
    level = models.CharField('Level', max_length=255, null=True, blank=True, choices=LEVEL_CHOICES)
    def __str__(self):
        return self.description

class People(models.Model):
    name = models.CharField('Name',max_length= 50,null=True,blank=True)
    manager = models.ForeignKey("self",null=True,blank=True,on_delete = models.SET_NULL)
    role = models.CharField('Role',max_length= 255,null=True,blank=True)
    def __str__(self):
        return self.name

class Score(models.Model):
    SCORE_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    skill = models.ForeignKey(Skill, blank=True, null=True, on_delete=models.SET_NULL)
    person = models.ForeignKey(People, blank=True, null=True, on_delete=models.SET_NULL)
    score = models.IntegerField(null=True,choices=SCORE_CHOICES)
    def __str__(self):
        return self.person + self.competency

class File(models.Model):
    name = models.CharField(max_length=100)
    document = models.FileField(upload_to='files')
    def __str__(self):
        return self.name
    def delete(self, *args, **kwargs):
        self.document.delete()
        super().delete(*args, **kwargs)
