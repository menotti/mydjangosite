import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Publicado recentemente?'
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Pessoa(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    data_de_nascimento = models.DateField()
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    sexo = models.CharField(max_length=1, choices=SEXO, null=True)
    def __str__(self):
        return self.nome

    @admin.display(
        ordering='data_de_nascimento',
        description='idade',
    )
    def idade(self):
        now = timezone.now()
        return int(now.strftime('%Y')) - int(self.data_de_nascimento.strftime('%Y'))

class Parentesco(models.Model):
    parentesco = models.CharField(max_length=100) 
    def __str__(self):
        return self.parentesco

class Dependente(models.Model):
    titular = models.ForeignKey(Pessoa, related_name='titular', on_delete=models.CASCADE)
    dependente = models.ForeignKey(Pessoa, related_name='dependente', on_delete=models.CASCADE)
    relacao = models.ForeignKey(Parentesco, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.titular) + str(self.relacao) + str(self.dependente)

