from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
from postApp.models import Post


def post_list(request):  # 게시물 리스트
    # 게시물 리스트를 모델에서 받아옵니다.
    posts = Post.objects.all()
    # 게시물 리스트를 보여주면서 list.html 템플릿에 posts 값을 사용하기 위해 같이 넘겨줍니다.
    return render(request, 'postApp/list.html', context={'posts': posts})


def post_detail(request, id):  # 게시물 상세보기
    # 게시물 리스트에서 게시물을 클릭하게 되면 바로 post_detail 로 넘어오게 됩니다.
    # a 태그의 href=의 값으로 posts/{{ post.id }}를 보셨을 겁니다. 이값이 바로
    # post_detail 함수의  두번째로 id란 인자로 넘어 온것입니다.
    # id 에는 실제 게시물의 primary key 값이 담겨있습니다. 게시물의 고유번호로
    # 이제 이 값을 통해 특정한 게시물 목록중 이 고유번호와 매칭되는 특정 게시물만 가져올 수 있습니다.

    # Post 테이블의 목록중 id가 저희가 받아온 id와 일치하는 것을 가져오게 됩니다.
    # 그리고 그것을 사용하기 편하게 post 변수에 할당합니다.
    post = Post.objects.get(id=id)

    # 이제 상세보기 페이지를 보여주면서 저 특정 게시물을 템플릿에서 사용할 수 있게 가지고 가면됩니다.
    return render(request, 'postApp/detail.html', context={'post': post})


def post_create(request):  # 게시물 생성 페이지/ 생성하기
    if request.POST:
        # 만약 요청이 POST로 넘어왔다면, 넘어온 데이터를 사용하기 편하게 변수에 할당
        # 한번만 사용하는 경우 직접 ex) post.title = request.POST.get('title') 처럼 바로 사용해도 되지만
        # 나중에 사용할 일이 많아 질 수 있기 때문에 변수에 넣어서 사용하는 것이 좋습니다.
        title = request.POST.get('title')
        writer = request.POST.get('writer')
        content = request.POST.get('content')

        # 만들었던 Post 모델을 변수에 할당하고
        # 모델의 각 컬럼(레코드 또는 속성)들에 POST로 넘어오 값을 할당합니다.
        # 그리고 마지막 save() 메서드를 호출하여 실제 DB에 저장하는 작업을 진행합니다
        post = Post()
        post.title = title
        post.writer = writer
        post.content = content
        post.save()
        # 그리고 /posts url 로 redirect 시킵니다. /posts 요청은 post_list와 연결되어 있으므로 게시물 목록화면으로 돌아가게 됩니다.
        return redirect('/posts')

    # 요청이 POST가 아니라면 위의 if문을 타지 않았을 겁니다. 넘어온 요청은 GET 요청임으로
    # 단순히 게시물을 생성하는 화면을 보여주면 됩니다.
    return render(request, 'postApp/create.html')


def post_update(request, id):  # 게시물 수정 페이지/ 수정하기

    if request.POST:
        # post_create 함수와 비슷합니다. 하지만 다른 부분이 있죠.
        # 요청이 POST 로 넘어온다면 변수에 할당합니다.
        title = request.POST.get('title')
        writer = request.POST.get('writer')
        content = request.POST.get('content')

        # 이 부분은 생성하는 부분과는 다릅니다. 새로운 객체를 만들지 않고,
        # Post 테이블의 목록중 넘어온 id와 매칭되는 특정 포스트를 가져옵니다.
        # 그리고 그 post 의 값들을 넘어온 값들로 덮어쓰는 것이죠
        # 작업이 끝나면 save 메서드를 호출하여 DB를 수정합니다.
        # 그리고 이번엔 게시물 목록이아닌, 상세보기 페이지로 넘깁니다 (이부분은 설계의 차이입니다)
        post = Post.objects.get(id=id)
        post.title = title
        post.writer = writer
        post.content = content
        post.save()
        return redirect('/posts/'+str(id))

    # 만약 POST요청이 아닌 GET요청으로 왔다면 위의 과정은 생략되고 수정 페이지를 보여주게 됩니다.
    # 수정페이지는 생성과 다르게 수정해야하기 때문에 원래 데이터베이스에 있는 값을 가져와서 보여줘야합니다
    # 그리고 그 값을 html단에서 사용자가 수정하여 다시 post 요청을 하게 되면 이번엔 이부분이 실행이 되는 것이
    # 아닌 위의 if문 내부의 로직이 실행되겠죠.
    # (사실 밑의 구문 post = Post.objects.get(id=id) 은 if문에도 똑같은 부분이 있기때문에 중복되는 부분입니다
    # 중복을 처리하는 것은 crud에 익숙해지면 그때 바꿔서 보여드리겠습니다.
    post = Post.objects.get(id=id)
    return render(request, 'postApp/edit.html', context={'post': post})


def post_delete(request, id):  # 게시물 삭제
    # 게시물 삭제는 의외로 단순합니다
    # 물론 이렇게 구현하게 되면 다른사람이 무작위로 게시물을 삭제하는 등 보안에 취약하게 되지만
    # 예제상 그냥 진행하겠습니다.

    # GET으로 넘어온 요청의 id 값을 통해 해당하는 id값의 post를 삭제합니다
    post = Post.objects.get(id=id)
    post.delete()

    # 그리고 게시물 목록으로 redirect 시킵니다.
    return redirect('/posts')
