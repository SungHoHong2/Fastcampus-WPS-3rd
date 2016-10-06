# Django tutorial

> 구글 번역  
> <https://www.google.co.kr/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&ved=0ahUKEwidoImx_8TPAhVNwmMKHc26BEYQFgg3MAE&url=https%3A%2F%2Fchrome.google.com%2Fwebstore%2Fdetail%2Fgoogle-translate%2Faapbdbdomjkkjkaonfhkkikfgjllcleb%3Fhl%3Dko&usg=AFQjCNHLwS6zA90piXJu9pcjrJKjRafFvA&sig2=d6ISHxE2p0gO9YKgQwafJw>

### django-tutorial 폴더 생성

`mkdir django-tutorial`  

폴더 안으로 이동  
`cd django-tutorial`

가상환경 생성  
`pyenv virtualenv 3.4.3 tutorial`

가상환경을 적용 (django-tutorial폴더 내에서)  
`pyenv local tutorial`

장고 설치  
`pip install django`

> 선택사항 (pip 업그레이드)  
> pip install --upgrade pip

설치된 패키지 확인
`pip list`

```
(tutorial) ➜  django-tutorial git:(master) pip list
Django (1.10.2)
pip (8.1.2)
setuptools (12.0.5)
```

> 오래된 django버전 업그레이드  
> pip install django --upgrade  
> **(성환님 지적) --upgrade의 위치는 상관없다**

polls 애플리케이션 생성  
`python manage.py startapp polls`

Pycharm에 가상환경 세팅  
Preferences -> Project interpreter -> Add local -> /usr/local/var/pyenv/versions/tutorial

> 리눅스는 ~/.pyenv/versions/tutorial
