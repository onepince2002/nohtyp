from django.conf.urls import url # 匯入url函式，需要用它來映對到URL視窗

from . import views # 匯入views模組，其中句點是讓python從目前的urls.py模組所在的資料夾中匯入視窗

urlpatterns = [
    url(r'^$', views.index, name='index'), # 此函式接受三個引數來處理，第一個引數是正規表示式，第二個引數指定要呼叫的函式視窗，第三個引數把這個URL模式的名稱指定為index
]