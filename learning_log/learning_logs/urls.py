from django.conf.urls import url # 匯入url函式，需要用它來映對到URL視窗
from django.urls import path

from . import views # 匯入views模組，其中句點是讓python從目前的urls.py模組所在的資料夾中匯入視窗


# urlpatterns = [
#     url(r'^$', views.index, name='index'), # 此函式接受三個引數來處理，第一個引數是正規表示式，第二個引數指定要呼叫的函式視窗，第三個引數把這個URL模式的名稱指定為index
# ]


app_name='learning_logs'
urlpatterns=[
    path('',views.index,name='index'),
    # 顯示所有主題
    path('topics/',views.topics,name='topics'),
    # 顯示個別主題
    path('<int:topic_id>/',views.topic,name='topic'),
]
