from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import QuestionForm, AnswerForm, CMD_QuestionForm, CMD_AnswerForm
from .models import CMD_Question, CMD_Answer
from django.db.models import Q


def CMD_index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    cmd_question_list = CMD_Question.objects.order_by('-create_date')
    if kw:
        cmd_question_list = cmd_question_list.filter(
            Q(Car_num__icontains=kw)  # 제목검색
            # Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            # Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()
    paginator = Paginator(cmd_question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'cmd_question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'pybo/drive_list.html', context)


def CMD_detail(request, cmd_question_id):
    cmd_question = get_object_or_404(CMD_Question, pk=cmd_question_id)
    context = {'cmd_question': cmd_question}
    return render(request, 'pybo/drive_detail.html', context)


def CMD_answer_create(request, cmd_question_id):
    cmd_question = get_object_or_404(CMD_Question, pk=cmd_question_id)
    if request.method == "POST":
        form = CMD_AnswerForm(request.POST)
        if form.is_valid():
            cmd_answer = form.save(commit=False)
            cmd_answer.create_date = timezone.now()
            cmd_answer.author = request.user
            cmd_answer.cmd_question = cmd_question
            cmd_answer.save()
            return redirect('pybo:CMD_detail', cmd_question_id=cmd_question.id)
    else:
        form = CMD_AnswerForm()
    context = {'cmd_question': cmd_question, 'form': form}
    return render(request, 'pybo/drive_detail.html', context)


def CMD_question_create(request):
    if request.method == 'POST':
        form = CMD_QuestionForm(request.POST,request.FILES)
        if form.is_valid():
            cmd_question = form.save(commit=False)
            cmd_question.create_date = timezone.now()
            cmd_question.author = request.user
            cmd_question.save()
            return redirect('pybo:CMD_index')
    else:
        form = CMD_QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form2.html', context)



@login_required(login_url='common:login')
def cmd_question_modify(request, cmd_question_id):
    cmd_question = get_object_or_404(CMD_Question, pk=cmd_question_id)
    if request.user != cmd_question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:CMD_detail', cmd_question_id=cmd_question.id)

    if request.method == "POST":
        form = CMD_QuestionForm(request.POST, instance=cmd_question)
        if form.is_valid():
            cmd_question = form.save(commit=False)
            cmd_question.author = request.user
            cmd_question.modify_date = timezone.now()  # 수정일시 저장
            cmd_question.save()
            return redirect('pybo:CMD_detail', cmd_question_id=cmd_question.id)
    else:
        form = QuestionForm(instance=cmd_question)
    context = {'form': form}
    return render(request, 'pybo/question_form2.html', context)



@login_required(login_url='common:login')
def cmd_question_delete(request, cmd_question_id):
    cmd_question = get_object_or_404(CMD_Question, pk=cmd_question_id)
    if request.user != cmd_question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:CMD_detail', cmd_question_id=cmd_question.id)
    cmd_question.delete()
    return redirect('pybo:CMD_index')
