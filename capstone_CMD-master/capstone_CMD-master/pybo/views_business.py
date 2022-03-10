from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404,redirect
from .forms import business_applyform
from django.utils import timezone
from .models import business_apply
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def employee_apply(request):

    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    # 조회
    business_list = business_apply.objects.order_by('-create_date')
    if kw:
        business_list = business_list.filter(
            Q(name__icontains=kw)   # 제목검색
            # Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            # Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()
    paginator = Paginator(business_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'business_list': page_obj, 'page': page, 'kw': kw}
    return render(request,'pybo/apply_form.html',context)

def employee_detail(request,business_list_id):
    business_list = get_object_or_404(business_apply, pk=business_list_id)
    context = {'business_list': business_list}
    return render(request, 'pybo/apply_detail.html', context)


@login_required(login_url='common:login')
def employee_create(request):

    if request.method == 'POST':
        form = business_applyform(request.POST)
        if form.is_valid():
            employee_question = form.save(commit=False)
            employee_question.create_date = timezone.now()
            employee_question.author = request.user
            employee_question.save()
            return redirect('pybo:employee')
    else:
        form = business_applyform()
    context = {'form': form}
    return render(request, 'pybo/apply_create.html', context)

@login_required(login_url='common:login')
def employee_modify(request, business_list_id):
    business = get_object_or_404(business_apply, pk=business_list_id)
    if request.user != business.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:employee_detail', business_list_id=business.id)

    if request.method == "POST":
        form = business_applyform(request.POST, instance=business)
        if form.is_valid():
            business = form.save(commit=False)
            business.author = request.user
            business.modify_date = timezone.now()  # 수정일시 저장
            business.save()
            return redirect('pybo:employee_detail', business_list_id=business.id)
    else:
        form = business_applyform(instance=business)
    context = {'form': form}
    return render(request, 'pybo/apply_create.html', context)


@login_required(login_url='common:login')
def employee_delete(request, business_list_id):
    business = get_object_or_404(business_apply, pk=business_list_id)
    if request.user != business.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:employee_detail', business_list_id=business.id)
    business.delete()
    return redirect('pybo:employee')

