from django.db import models

class FamilyUser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('姓名', max_length=20)
    age = models.IntegerField('年龄', default=0)
    gender = models.CharField('性别', max_length=20)

    class Meta:
        db_table = 'family_user'