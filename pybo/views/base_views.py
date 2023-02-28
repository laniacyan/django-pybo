from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Question


def index(request):
    """
    pybo 목록출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    # 조회
    question_list = Question.objects.order_by('-create_date') #전체 목록
    # 페이징처리
    paginator = Paginator(question_list, 10)    # 페이지당 10개씩 보여주기. question_list => 전체목록
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}

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









