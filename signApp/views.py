import bcrypt
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
# GET : 로그인 페이지 / POST : 로그인 요청
from signApp.forms import LoginForm


# GET : 로그인 페이지 / POST : 로그인 요청
def login(request):
    # POST : 로그인 요청 처리
    if request.POST:
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST['username']
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)
        print(user)
        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect('/posts')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'login.html', {'error': 'login false'})

    # GET : 로그인 페이지 응답
    return render(request, 'signApp/login.html')


# GET : 회원가입 페이지 / POST : 회원가입 요청
def join(request):
    # POST : if문 내의 작업을 실행
    if request.POST:
        # 해당 User 모델은 장고에서 기본으로 제공해준다 ..
        User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
        return redirect('/login')

    # GET : 회원가입 페이지 응답
    return render(request, 'signApp/join.html')