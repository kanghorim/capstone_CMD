from django import forms
from pybo.models import Question,Answer,CMD_Question,CMD_Answer,business_apply




class business_applyform(forms.ModelForm):
    class Meta:
        model = business_apply
        fields = ['name','email','Living','gender','Phone','assign_num','office']
        labels = {
            'name': '이름',
            'email': '이메일',
            'Phone': '핸드폰 번호',
            'assign_num' : '부여받은 사번',
            'gender': '성별',
            'Living': '주소지',
            'office':'직위'
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['Car_num','bussiness_num','Car_variety','Car_manager']
        labels = {

            'Car_num':'차량번호',
            'Car_variety':'차량종류',
            'Car_manager':'차량책임자',
            'bussiness_num': '사번'
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class CMD_QuestionForm(forms.ModelForm):
    class Meta:
        model = CMD_Question
        fields = [ 'Car_num','bussiness_num','bussiness_manager','start_date','pdf',
                   'start_pos','destination_pos','depart_date','arrive_date','Lat','Long']

        labels = {
            'Car_num':'선택차량번호',
            'bussiness_num':'사번',
            'bussiness_manager':'운행 책임자',
            'start_pos':'출발위치',
            'destination_pos':'도착위치',
            'start_date':'운행날짜',
            'depart_date':'출발시간',
            'arrive_date':'도착시간',
            'Lat':'위도',
            'Long':'경도'
        }

class CMD_AnswerForm(forms.ModelForm):
    class Meta:
        model = CMD_Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }


