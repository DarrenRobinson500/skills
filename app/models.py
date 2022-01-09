from django.db import models
import datetime
from datetime import datetime, timedelta, date


class Role_Level(models.Model):
    role_level = models.CharField('Description', max_length=255,null=True, blank=True)
    def __str__(self):
        if self.role_level is None:
            result = "Not provided"
        else:
            result = self.role_level
        return result

class People(models.Model):
    name = models.CharField('Name',max_length= 50,null=True,blank=True)
    manager = models.ForeignKey("self",null=True,blank=True,on_delete = models.SET_NULL)
    role = models.CharField('Role',max_length= 255,null=True,blank=True)
    role_level = models.ForeignKey(Role_Level, blank=True, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        if self.name is None:
            result = "No name"
        else:
            result = self.name
        return result
    def level(self):
        levels = Role_Level.objects.all()
        result = 1
        if self.role_level == levels[1]: result = 2
        if self.role_level == levels[2]: result = 3
        if self.role_level == levels[3]: result = 4
        return result

class Skill_Cat(models.Model):
    category = models.CharField('Description', max_length=255,null=True, blank=True)
    sub_category = models.CharField('Description', max_length=255,null=True, blank=True)
    score1 = models.FloatField(null=True)
    score2 = models.FloatField(null=True)
    score3 = models.FloatField(null=True)
    score4 = models.FloatField(null=True)
    to_develop = models.CharField(max_length=1000,null=True,blank=True)
    required = models.BooleanField(default=False)
    target = models.CharField('Description', max_length=255,null=True, blank=True)
    def __str__(self):
        if self.sub_category is None:
            result = "No category"
        else:
            result = self.sub_category
        return result

class Skill_Level(models.Model):
    level = models.CharField('Description', max_length=255,null=True, blank=True)
    def __str__(self):
        if self.level is None:
            result = "Not provided"
        else:
            result = self.level
        return result

class Skill(models.Model):
    sub_category = models.ForeignKey(Skill_Cat, blank=True, null=True, on_delete=models.SET_NULL)
    role_level = models.ForeignKey(Role_Level, blank=True, null=True, on_delete=models.SET_NULL)
    question = models.CharField(max_length=500,null=True, blank=True)
    score_temp = models.IntegerField(null=True)
    text0_temp = models.CharField(max_length=255,null=True, blank=True)
    text1_temp = models.CharField(max_length=255,null=True, blank=True)
    text2_temp = models.CharField(max_length=255,null=True, blank=True)
    text3_temp = models.CharField(max_length=255,null=True, blank=True)
    text4_temp = models.CharField(max_length=255,null=True, blank=True)
    text5_temp = models.CharField(max_length=255,null=True, blank=True)
    def __str__(self):
        return self.question
    def level(self):
        levels = Role_Level.objects.all()
        result = 1
        if self.role_level == levels[1]: result = 2
        if self.role_level == levels[2]: result = 3
        if self.role_level == levels[3]: result = 4
        return result

class Score(models.Model):
    SCORE_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    skill = models.ForeignKey(Skill, blank=True, null=True, on_delete=models.SET_NULL)
    person = models.ForeignKey(People, blank=True, null=True, on_delete=models.SET_NULL)
    score = models.IntegerField(null=True,choices=SCORE_CHOICES)
    def __str__(self):
        result = ""
        if self.person.name is not None:
            result = self.person.name
        if self.skill is not None:
            result += " " + self.skill.question
        if self.score is not None:
            result += " " + str(self.score)

        return result

class Target(models.Model):
    sub_cat = models.ForeignKey(Skill_Cat, blank=True, null=True, on_delete=models.SET_NULL,related_name='sub_cat')
    person = models.ForeignKey(People, blank=True, null=True, on_delete=models.SET_NULL)
    target = models.ForeignKey(Skill_Level, blank=True, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.target.level

class Colour(models.Model):
    name = models.CharField(max_length=40,null=True)
    active = models.BooleanField(default=False,null=True)
    nav = models.CharField(max_length=10,null=True)
    primary_dark = models.CharField(max_length=10,null=True)
    primary_light = models.CharField(max_length=10,null=True)
    secondary_dark = models.CharField(max_length=10,null=True)
    secondary_light = models.CharField(max_length=10,null=True)

class File(models.Model):
    name = models.CharField(max_length=100)
    document = models.FileField(upload_to='files')
    def __str__(self):
        return self.name
    def delete(self, *args, **kwargs):
        self.document.delete()
        super().delete(*args, **kwargs)

TYPES = [("Group","Group"), ("Person","Person"), ("Objective","Objective"), ("Story","Story"), ("Issue","Issue"), ("ToDo","ToDo"), ("Report","Report"), ("Reminder","Reminder"), ("Meeting","Meeting"), ("Holiday", "Holiday"), ("Medical", "Medical"),("Grateful","Grateful"),("Life","Life"),]
TYPES_ORDER = {"Group":0, "Person":1, "Objective":2, "Issue":3, "ToDo":4, "Report":6, "Reminder":5, "Meeting":7, "Story":8, "Holiday":9, "Medical":10, }
STATUS = [("Not asked","Not asked"), ("Requested and Open","Requested and Open"), ("Complete","Complete"), ]

class Note(models.Model):
    name = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True, blank=True)
    actions = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=64,null=True,choices=TYPES)
    parent = models.ForeignKey("self", related_name='parent_rn', blank=True, null=True, on_delete=models.SET_NULL,)
    level = models.IntegerField(null=True)
    date = models.DateField(null=True, blank=True)
    status = models.TextField(null=True, blank=True, default="Not asked", choices=STATUS)

    created_by = models.CharField(max_length=255, null=True, blank=True)
    time_changed = models.DateTimeField(null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        if self.date is not None and self.type != "Person":
            result = self.name + " (" + self.date.strftime('%d %b %Y') + ")"
        elif self.name is None:
            return self.description
        else:
            result = self.name
        if self.time_changed is not None:
            result += " [" + str(self.time_changed.strftime('%d %b %Y')) + "]"
        return result

    def children(self):
        children = Note.objects.filter(parent=self).order_by('-time_changed')
        children = sorted(children, key=lambda t: t.type_order())
        return children

    def type_x(self):
        if self.type == "Person": return ""
        if self.type is None: return ""
        return "[" + self.type + "]"

    def type_order(self):
        return TYPES_ORDER[self.type]

    def has_children(self):
        if self.children is None: return False
        return True

    def full_name(self):
        parent = self.parent
        name = self.name
        while parent is not None:
            name = parent.name + "/" + name
            parent = parent.parent
        return name

    def calendar_date(self):
        if self.type != "Person": return self.date
        bday = self.date
        current_year = date.today().year
        bday_this_year = date(current_year, bday.month, bday.day)
        bday_next_year = date(current_year + 1, bday.month, bday.day)
        if date.today() > bday_this_year: return bday_next_year
        else: return bday_this_year
