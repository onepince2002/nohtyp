from django.db import models

# Create your models here.
class Topic(models.Model):
    text=models.CharField(max_length=100)
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text # 返回儲存在text屬性中的字串
		
# 以下為新增區塊
class Entry(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
 
    def __str__(self):
        return self.text		