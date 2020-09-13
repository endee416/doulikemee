from django import forms
from .models import destinations

answer1=[
('option1',  "red"),
('option2',  'blue'),
('option3', 'black'),
('option4',  'white')
]

answer2=[
('option1',  "introvert"),
('option2',  'extrovert'),
('option3', 'ambivert'),
('option4',  'just sad')
]

answer3=[
('option1',  "19"),
('option2',  '20'),
('option3', '21'),
('option4',  '22')
]

answer4=[
('option1',  "straight"),
('option2',  'gay'),
('option3', 'bisexual'),
('option4',  'asexual')
]

answers=[answer1, answer2, answer3, answer4]


class CHOICES(forms.Form):
    NUMS=forms.ChoiceField(widget=forms.RadioSelect(choices=answers))