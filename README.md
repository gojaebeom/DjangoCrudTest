##### 기본적인 crud를 연습 프로젝트

** python이 설치되었다는 가정하에 진행 <br>
** github에 올라와있는 파일들은 참고용으로만 이용 <br>
** 직접 만들어 보는것이 목표 <br>

## 가상환경 , django 프로젝트 설정 및 생성
django project를 진행하려면 django가 설치되어 있어야 함 <br>
하지만 기본적으로 **python**으로 개발을 할 땐 가상환경을 만들어놓고 프로젝트를 진행 <br>
가상환경이 필요한 이유는 [이곳](https://windybay.net/post/13/) 에서 참고하시면 좋다. <br>

### virtualenv 다운로드
가상환경을 생성하기 위해 여러 방법이 있지만 이번 예제에서는 `virtualenv` 라는 모듈을 다운 받아 사용<br>
```shell script
pip install virtualenv
```
<br>
가상환경 파일은 프로젝트 밖, 또는 안에서 포함하는 방법 모두 상관이 없음 <br>
하지만 본인이 찾아본 예제들은 대부분 프로젝트의 내부에 venv 폴더를 두었기 때문에 따라감

### django 프로젝트 폴더 생성
장고 프로젝트 폴더를 하나 생성<br>
이름은 `django-crud` 로 진행.<br>

<br>
그리고 생성한 폴더 내부로 들어와 
../django-crud > 위치에서 명령창을 통해 다운받았던 가상환경 모듈을 사용하여 가상환경 파일을 만들어주기

```
virtualenv venv
```

그리고 
```
# 윈도우
venv\Scripts\activate.bat

# 맥 
source venv/Scripts/activate
```
를 입력<br>


명령창 입력줄 옆에 `(venv)` 표시가 뜬다면 가상환경을 실행한 상태라는 뜻 <br>


이제 가상환경 내부에서 장고를 깔아주면 된다.
```
pip install django
```

해당 명령어로 장고를 깔았다면  
이제 장고 프로젝트를 시작할 수 있게된다.
