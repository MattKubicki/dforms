from django.db import models


class Users(models.Model):
    username = models.TextField(max_length=50)
    password = models.TextField(max_length=256)


class Form(models.Model):
    name = models.TextField(max_length=256)
    owner_id = models.ForeignKey(Users, on_delete=models.CASCADE)


class Questions(models.Model):
    question_text = models.CharField(max_length=100)
    is_open_question = False
    form_id = models.ForeignKey(Form, on_delete=models.CASCADE)
# id chyyyba kmini samo sadzac po przykładach

    def __str__(self):
        return self.question_text


class Choice(models.Model):  # to do pytan zamknietych
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


class OpenQuestionAnswers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    user = models.ForeignKey(Questions, on_delete=models.CASCADE)

    choice_text = models.CharField(max_length=200)


class Answers(models.Model):
    pass
