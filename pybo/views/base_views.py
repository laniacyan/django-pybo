from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from ..models import Question
from django.db.models import Q, Count



def index(request):
    """
    pybo 목록출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')
    so = request.GET.get('so', 'recent')    # 정렬 기준

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:   # recent
        question_list = Question.objects.order_by('-create_date')

    # 조회
    # question_list = Question.objects.order_by('-create_date') #전체 목록
    # question_list = Question.objects.order_by('-author__username') # 이름순으로 검색

    # 검색
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |      # 제목 검색
            Q(content__icontains=kw) |      # 내용 검색
            Q(author__username__icontains=kw) |     # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)   # 답글 글쓴이 검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(question_list, 10)    # 페이지당 10개씩 보여주기. question_list => 전체목록
    page_obj = paginator.get_page(page)

    context = {
        'kw': kw,
        'page': page,
        'so': so,
        'question_list': page_obj
        }

    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)


    # question.answer_set.create(content=request.POST.get('content'),
    #             create_date=timezone.now())

    # return redirect('pybo:detail', question_id=question_id)
    # print(request.method)
    # print(request.GET)      # dict
    # print(request.POST)     # dict

    # content = request.POST['content']           # 1) 키가 없으면, 예외 발생
    # print('[content]', content)

    # content = request.POST.get('content', '')       # 2) 키가 없으면, None 리턴


    # print('get(content)', content)









