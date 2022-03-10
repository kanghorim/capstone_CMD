from django.urls import path
from django.conf.urls import url
from django.conf import settings
from . import views
from . import views_drive
from . import views_business
from django.conf.urls.static import static
from django.conf import settings

app_name = 'pybo'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('team/', views.mainpage, name='mainpage'),
    path('intro_detail/', views.intro_detail, name='intro_detail'),
    # path('book/',views.book_list,name = "book_list"),
    # path('book/upload/',views.upload_book,name = "upload_book"),
    # <--------------- 지도 관련 ---------------- >
    path('map/', views.map, name='map'),
    path('new_map/', views.new_map, name='new_map'),
    # path('landing/', views.landing, name="landing"),
    # <--------------- 공용차량운행일지 관련 ---------------- >
    # path('intro/', views.intro, name='intro'),
    path('drive_list/', views_drive.CMD_index, name='CMD_index'),
    path('drive_list/<int:cmd_question_id>/', views_drive.CMD_detail, name='CMD_detail'),
    path('drive_list/answer/create/<int:cmd_question_id>/', views_drive.CMD_answer_create, name='CMD_answer_create'),
    path('drive_list/question/create/', views_drive.CMD_question_create, name='CMD_question_create'),
    path('drive_list/question/modify/<int:cmd_question_id>', views_drive.cmd_question_modify,
         name='CMD_question_modify'),
    path('drive_list/question/delete/<int:cmd_question_id>', views_drive.cmd_question_delete,
         name='CMD_question_delete'),
    path('static/', views.static, name='static'),
    path('', views.intro, name='intro'),

    # <--------------- 직원등록 --------------------->

    path('apply/', views_business.employee_apply, name='employee'),
    path('apply/<int:business_list_id>/', views_business.employee_detail, name='employee_detail'),
    path('apply/apply_create', views_business.employee_create, name='employee_create'),
    path('apply/modify/<int:business_list_id>', views_business.employee_modify, name='employee_modify'),
    path('apply/delete/<int:business_list_id>/', views_business.employee_delete, name='employee_delete'),
    # <---------------- 공용차량 등록관련 화면 ------------------->
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
    # path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
