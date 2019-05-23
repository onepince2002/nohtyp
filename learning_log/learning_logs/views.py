from django.shortcuts import render

from .models import Topic # 匯入Topic模型

# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')


# 顯示所有主題
def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

# 顯示個別主題和它的entries
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)