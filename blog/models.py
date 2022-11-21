from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        ''' 와 str 이 없으면, 객체를 반환해주고, str이 있으면 str의 return값을 주네 __str__이 print(객체이름)과 같은 개념이야'''
        return f'[{self.pk}] {self.title}'
