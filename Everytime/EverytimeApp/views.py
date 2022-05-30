from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Comment
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q


def landing(request):
    return render(request, 'landing.html')

def main(request):
    return render(request, 'main.html')

def free(request):
    # 지금까지 데이터베이스에 저장한 글 객체들을 모조리 다 불러오고 싶다!
    # 데이터베이스의 Board 객체들을 모두 보여주는 곳
    # posts = Board.objects.all()
    posts = Board.objects.filter().order_by('-date') ## 최신순부터 
    print(posts)
    paginator = Paginator(posts, 5) # 몇개씩 끊어서 보여줄거니?
    page_num = request.GET.get('page') 
    # 127.0.0.1:8000/free/?page=1
    # 127.0.0.1:8000/free/?page=2
    # 조회할 때 GET 요청을 사용
    # { page : 1} -> 딕셔너리 자료형 : 따라서 page 라는 키값에 해당하는 값을 받아오기 위해서 사용

    

    # 몇 페이지에 있는 객체들의 목록을 띄워줄건지?
    # 1번 페이지를 갖고오겠다!
    posts = paginator.get_page(page_num) 

    #freeBoardDefault 와 함께 이 데이터들을 가져가라! 딕셔너리 형태로! 
    return render(request, 'freeBoardDefault.html', {'posts':posts})

def graduate(request):
    return render(request, 'graduatedBoardDefault.html')

    # 게시판 글을 저장해주는 함수
def create(request):
    if(request.method == 'POST'): 
        post = Board()
        post.title = request.POST['title']
        post.content = request.POST['text']
        post.file = request.FILES.get('file')
        print()
        post.user = request.user
    
        # post.file = request.FILES['file']

    # new_blog.image = request.FILES.get('image') 이런식으로 
    # request.FILES.get() 메서드를 이용하면 get()에 전달한 키 값으로 
    # QueryDict에 해당하는 key와 value가 있는지 찾아서 key가 있는 경우에는 
    # key에 해당하는 value를 반환하고 key가 없으면 에러를 일으키지 않고 None을 반환한다고 한다. 
    # None이 반환되는 것은 'models.py'에 대비 해놨으므로 더이상 오류가 나지 않았다🥰
        
        ## request.POST xxxxx
        post.date = timezone.now()
        # post.user = request.user
        post.save() # 모델객체.save() 를 통해 모델 객체를 DB에 저장할 수 있음
        return redirect('free')
    else:
        return render(request, 'freeBoardDefault.html')

def detail(request, post_id):
    # post_id 번째 블로그 글을 DB로부터 가져와서
    post_detail = get_object_or_404(Board, pk=post_id)
    # pk 값을 이용해 특정 모델 객체 하나만 가져오기

    # blog_id 번째 블로그 글을 detail.html로 띄워주겠다
    return render(request, 'freeBoardDetail.html', {'post_detail':post_detail})

def update(request, post_id):
    post_detail = get_object_or_404(Board, pk=post_id)
    if request.method == "POST":
        post_detail.title = request.POST['title']
        post_detail.content = request.POST['content']
        post_detail.file = request.FILES.get('file')
        post_detail.date = timezone.now()
        post_detail.save()
        return redirect('/freeBoard/'+str(post_id),{'post_detail':post_detail})
    else:
        return render(request, 'freeBoardUpdate.html', {'post_detail':post_detail})

def delete(request, post_id):
    post = get_object_or_404(Board, pk=post_id)
    post.delete()
    return redirect('free')

# def search(request):
#     posts = Board.objects.all()
#     search = request.GET.get('search')
#     if search:
#         search_list = posts.filter(
#             Q(title__icontains = search) | #제목
#             Q(content_icontains = search) | #내용
#             Q(user__nickname__icontains = search) #글쓴이
#             )
#         paginator = Paginator(search_list,5)
#         page = request.GET.get('page')
#         posts = paginator.get_page(page)

#     return render(request, 'freeBoardDefault.html', {'posts':search_list})


    # if request.method == 'POST':
    #     searched = request.POST['keyword']  # 검색어   
    #     posts = Board.objects.filter(title__contains=searched)
    #     return redirect('free', {'posts':posts})
    # else:
    #     return redirect('free')


# 게시판 댓글을 작성해주는 함수
def createComment(request, post_id):
    if(request.method == 'POST'): 
        print(post_id)
        comment = Comment()
        comment.comment = request.POST['comment']
        comment.date = timezone.now()
        comment.user = request.user
        comment.post = get_object_or_404(Board, pk=post_id)
        # comment.post.comments = comment_count
        comment.save() # 모델객체.save() 를 통해 모델 객체를 DB에 저장할 수 있음
        # return redirect('detail', post_id)

        return redirect('detail', post_id)

# 게시판 대댓글을 작성해주는 함수
def createReply(request, post_id, comment_id):
    if(request.method == 'POST'): 
        comment = Comment()
        comment.comment = request.POST['comment']
        comment.date = timezone.now()
        comment.user = request.user
        comment.post = get_object_or_404(Board, pk=post_id)
        comment.reply = get_object_or_404(Comment, pk=comment_id)
        comment.save() 

        return redirect('detail', post_id)