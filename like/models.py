from django.db import models



# Create your models here.
class destinations:
    question: str
    name: str
    option1: str
    option2: str
    option3: str
    option4: str



answer1=[
('option1',  "red"),
('option2',  'blue'),
('option3', 'black'),
('option4',  'white')
]


class credentials4(models.Model):
    username=models.CharField(max_length=50, null=True, blank=True)
    password=models.IntegerField(null=True, default=True)
    favcolor=models.CharField(max_length=50, null=True, blank=True )
    sociallife=models.CharField(max_length=50 , null=True, blank=True)
    age=models.CharField(max_length=50, null=True, blank=True)
    sexuality=models.CharField(max_length=50, null=True, blank=True)
    fullname=models.CharField(max_length=50, null=True, blank=True)
    birthday=models.CharField(max_length=50, null=True, blank=True)
    rstatus=models.CharField(max_length=50, null=True, blank=True)
    dept=models.CharField(max_length=50, null=True, blank=True)
    favmeal=models.CharField(max_length=50, null=True, blank=True)
    siblings=models.CharField(max_length=50, null=True, blank=True)
    tvshow=models.CharField(max_length=50, null=True, blank=True)
    hometown=models.CharField(max_length=50, null=True, blank=True)
    priedu=models.CharField(max_length=50, null=True, blank=True)
    secedu=models.CharField(max_length=50, null=True, blank=True)
    sports=models.CharField(max_length=50, null=True, blank=True)
    hobby=models.CharField(max_length=50, null=True, blank=True)
    church=models.CharField(max_length=50, null=True, blank=True)
    anime=models.CharField(max_length=50, null=True, blank=True)
    favanime=models.CharField(max_length=50, null=True, blank=True)
    personality=models.CharField(max_length=50, null=True, blank=True)
    otherpersonality=models.CharField(max_length=50, null=True, blank=True)
    clientname=models.CharField(max_length=50, null=True, default=True)
    imagetogether=models.ImageField(upload_to='pics')


    
