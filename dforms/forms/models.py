from django.db import models


class Users(models.Model):
    username = models.TextField(max_length=50)
    password = models.TextField(max_length=256)


class Form(models.Model):
    name = models.TextField(max_length=256)
    owner_id = models.ForeignKey(Users, on_delete=models.CASCADE)


class Question(models.Model):
    question_text = models.CharField(max_length=100)
    is_open_question = False
    form_id = models.ForeignKey(Form, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text


class Answers(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)


class Choice(models.Model):  # to do pytan zamknietych
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    answer_id = models.ForeignKey(Answers, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text


class OpenQuestionAnswers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_id = models.ForeignKey(Answers, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)

