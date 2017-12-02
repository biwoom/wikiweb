# wiki 설치와 배포-AWS-Ubuntu16.04-Nginx-Gunicorn-2



## AWS 인스턴스 생성

1. Ubuntu 16.04 선택
2. Security 설정 : All traffic / anywhere 설정
3. 기존 퍼블릭키 설정  




## 터미널을 통해 아마존 서버 접속

퍼블릭키가 있는 폴더에서 터미널 실행 후

```
chmod 400 DjangoServer.pem
# 예시 각기 다름
ssh -i "DjangoServer.pem" ubuntu@ec2-52-78-3-167.ap-northeast-2.compute.amazonaws.com
```

퍼니오 가상서버호스팅 접속

```
# ssh root@[기본도메인] -p [SSH포트]

$ ssh root@dm1505382855865.fun25.co.kr -p 17901
```

iwinv 호스팅 접속

```
ssh root@115.68.219.229 -p 22
#:  root 비밀번호: B5TPWHLR
```



## 리눅스 apt-get 업데이트

현재 디렉토리 /home/ubuntu

```
$ sudo apt-get update
```



## 파이썬 설치

- python3

```
$ sudo apt-get install python3
$ sudo apt-get install python3-pip
$ sudo apt-get install python3-dev
$ sudo apt-get install python3-setuptools
```



## Django-wiki 오리지널 라이브러리 Pillow (PIL Fork) 설치1

```
#: Pillow (PIL Fork)설치 - 파이썬 이미지 처리 패키지

#: 1. 가상환경 아닌 전역에서 설치
sudo apt-get install libjpeg8 libjpeg-dev libpng12-0 libpng12-dev

#: 가상환경 설정 후 Pillow 설치
#: 2. 가상환경에서 설치
(wikivenv) $ pip install Pillow==3.4.0
#: 또는
(wikivenv) $ pip install Pillow==4.0.0
```



## 작업 디렉토리 생성

```
$ mkdir wikiproject
$ cd wikiproject

$ mkdir wikiconfig
$ cd wikiconfig

$ mkdir gunicorn
$ mkdir supervisor
$ mkdir nginx

$ cd /home/ubuntu/wikiproject/wikiconfig/gunicorn 
$ mkdir logs
$ mkdir run

$ cd /home/ubuntu/wikiproject/wikiconfig/nginx
$ mkdir logs
```



## 파이썬 가상환경 설치 및 설정

- virtualenv

```
sudo apt-get install python-virtualenv
virtualenv --python=python3 wikivenv
```

- 가상환경 실행 

```
$ source wikivenv/bin/activate

#: 2. 가상환경에서 설치
(wikivenv) $ pip install Pillow==3.4.0
#: 또는
(wikivenv) $ pip install Pillow==4.0.0
```

- 가상환경 종료 명령어

```
(wikivenv) $ deactivate
```



## Django-wiki 오리지널 라이브러리 설치2


> 가상환경 실행 후 설치

```
(wikivenv) $ pip install wiki==0.2.4

#: 1. 패키지에 Pillow 버전확인 4.0.0 또는 3.4.0이 아니면 기존 버전 제거하고 명기한 버전으로 재설치(최신버전에서 png이미지파일 업로드 오류 발생함)

#: 패키지 제거 명령어 
(wikivenv) $ pip uninstall Pillow   
#: 패키지 설치 명령어
(wikivenv) $ pip install Pillow==4.0.0
```

> [venv : 가상환경] 내부 lib > python3 > site-packages 디렉토리에 필수라이브러리들 설치됨



## Django-wiki 수정본 설치

```
#: 1. git 에서 기본 코드 받기(git저장소 코드에는 db가 빠져있음)
(wikivenv) $ cd /home/ubuntu/wikiproject
(wikivenv) $ git clone https://github.com/biwoom/wikiweb.git

#: 2. 파일질라 등의 FTP를 통해 db 업로드하기
(db 업로드 디렉토리) wiki_site/db/wiki_database.db
#: db 파일은 테스트 서버에서 다운로드 할 것.
#: ftp 접속 설정
#: host: 115.68.219.229
#: 사용자 : root
#: 비밀번호 : B5TPWHLR
```

> 나의 django-wiki 수정본의 깃허브에서 프로젝트 디렉토리로 코드 복제
>
> sudo 명령어를 앞에 넣으면 루트사용자가 아닐때는 파일수정이 어려워짐.
>
> git 을 이용할 때는 sudo 명령어 뺄것. 



## 데이터베이스 초기화

```
(wikivenv) $ cd wikiweb
(wikivenv) $ python manage.py makemigrations
(wikivenv) $ python manage.py migrate
```



## 정적파일(static) 구성

```
# 테스트서버에서만 할 것. **배포서버**에는 생략 할 것.
(wikivenv) $ python manage.py collectstatic
```




## 장고 테스트 서버 실행

```
(wikivenv) $  python manage.py runserver 0.0.0.0:8080
```



## Gunicorn 서버 설치

```
(wikivenv) $  pip install gunicorn
(wikivenv) $  cd wikiweb

(wikivenv) $  gunicorn wiki_site.wsgi:application --bind 0.0.0.0:8001
# 또는 아래 명령어로 테스트 둘다 같은 명령어임
(wikivenv) $  gunicorn --bind 0.0.0.0:8000 wiki_site.wsgi
# 호스팅 업체별로 이용가능한 포트를 명시한 경우가 있으니 주의하여 포트번호를 적용할 것.
```



## Gunicorn 옵션 스크립트 설정

이제 포트 8001을 사용하여 서버의 공개 IP에서 gunicorn에 액세스 할 수 있습니다. 이제 gunicorn을 장고 응용 프로그램에 더 유용하게 만들려면 옵션을 구성해야합니다. 이를 위해 gunicorn.bash라는 bash 스크립트를 작성하십시오. 원하는대로 파일 이름을 변경할 수 있습니다.

- gunicorn 스크립트 생성

```
# 주의 ! sudo 붙이지 말것. 
# 현재 디렉토리 : /home/ubuntu/wikiproject/wikiconfig/gunicorn
(wikivenv) $  cd /home/ubuntu/wikiproject/wikiconfig/gunicorn
(wikivenv) $  nano /home/ubuntu/wikiproject/wikiconfig/gunicorn/gunicorn_start.bash
```

- gunicorn_start.bash 파일에 추가

```
#!/bin/bash

NAME="wikiweb"                                   # Name of the application
DJANGODIR=/home/ubuntu/wikiproject/wikiweb               # Django project directory
SOCKFILE=/home/ubuntu/wikiproject/wikiconfig/gunicorn/run/gunicorn.sock  # we will communicte using this unix socket
USER=ubuntu                                         # the user to run as
GROUP=ubuntu                                        # the group to run as
NUM_WORKERS=3                                       # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=wiki_site.settings      # which settings file should Django use
DJANGO_WSGI_MODULE=wiki_site.wsgi              # WSGI module name
echo "Starting $NAME as `whoami`"

# Activate the virtual environment

cd $DJANGODIR
source /home/ubuntu/wikiproject/wikivenv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
```

- 스크립트를 실행가능하도록 설정

```
(wikivenv) $  sudo chmod u+x gunicorn_start.bash
```
- 실행

```
(wikivenv) $  ./gunicorn_start.bash
```



## supervisor 설치

이제 관리자를 설정하여 애플리케이션을 감독 할 수있는 시간입니다. 시스템이 재부팅되거나 응용 프로그램이 예기치 않게 종료되면 감독자가 재시작을 처리합니다. 이를 위해 먼저 supervisor를 설치하십시오.

```
sudo apt-get install supervisor
```



supervisor를 통해 프로그램을 감독하려면 /etc/supervisor/conf.d/ 디렉토리에 해당 프로그램의 구성 파일을 만들어야합니다. 우리의 Django 애플리케이션을 위해서 wikiweb.conf를 작성합니다.

```
(wikivenv) $  nano /home/ubuntu/wikiproject/wikiconfig/supervisor/wikiweb.conf
```

- wikiweb.conf 파일에 작성

```
[program:wikiweb]
command = /home/ubuntu/wikiproject/wikiconfig/gunicorn/gunicorn_start.bash                  ; Command to start app
user = ubuntu                                                ; User to run as
stdout_logfile = /home/ubuntu/wikiproject/wikiconfig/gunicorn/logs/gunicorn_supervisor.log   ; Where to write log messages
redirect_stderr = true                                       ; Save stderr in the same log
environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8              ; Set UTF-8 as default encoding
```

- wikiweb.conf 파일 복사
 ```
sudo ln -s /home/ubuntu/wikiproject/wikiconfig/supervisor/wikiweb.conf /etc/supervisor/conf.d/wikiweb.conf
 ```

위의 파일에서 언급했듯이 로그는 /home/ubuntu/logs/gunicorn_supervisor.log에 저장 될 것이므로이 디렉토리와 파일을 만들어야합니다.

- 로그파일 생성

```
(wikivenv) $  touch /home/ubuntu/wikiproject/wikiconfig/gunicorn/logs/gunicorn_supervisor.log
```

이 작업이 끝나면 감독자에게 구성 파일을 다시 읽도록 요청하고 새로 업데이트 된 구성 파일이 추가되도록합니다.

Ubuntu 버전확인 :

```
$ lsb_release -a  
# 또는 
$ cat /etc/issue
```

Ubuntu 14.04 일 경우 :

```
$ sudo supervisorctl reread
wikiweb: available

$ sudo supervisorctl update
wikiweb: added process group
```

Ubuntu 16.04 일 경우 :

```
$ sudo systemctl restart supervisor
$ sudo systemctl enable supervisor
```


- 상태점검 :

```
(wikivenv) $  sudo supervisorctl status wikiweb
wikiweb                  RUNNING  pid 24768, uptime 0:00:10
```
- 비활성화 :

```
(wikivenv) $  sudo supervisorctl stop wikiweb
wiki_site: stopped
```
- 재시작 :

```
(wikivenv) $  sudo supervisorctl restart wikiweb
```



## Nginx 설치

Nginx는 우리의 어플리케이션을위한 서버의 역할을 할 것입니다. 

```
(wikivenv) $  sudo apt-get install nginx
```

브라우저로 도메인 접속시 Welcome to nginx! 표시됨.



이제 우리는 / etc / nginx / sites-available / 디렉토리에있는 애플리케이션 용 설정 파일을 생성해야합니다. 이 후에는 / etc / nginx / sites-enabled 디렉토리에 심볼릭 링크를 만들어야합니다. 하나씩 차례대로 할 수 있습니다. 먼저 구성 파일을 만듭니다.

```
(wikivenv) $  nano /home/ubuntu/wikiproject/wikiconfig/nginx/wikiweb.conf
```

- wikiweb.conf 파일에 추가

```
upstream wikiweb_server {
  # fail_timeout=0 means we always retry an upstream even if it failed
  # to return a good HTTP response (in case the Unicorn master nukes a
  # single worker for timing out).
  server unix:/home/ubuntu/wikiproject/wikiconfig/gunicorn/run/gunicorn.sock fail_timeout=0;
}

server {

    listen   80;
    server_name wikiweb;

    client_max_body_size 4G;
    access_log /home/ubuntu/wikiproject/wikiconfig/nginx/logs/nginx-access.log;
    error_log /home/ubuntu/wikiproject/wikiconfig/nginx/logs/nginx-error.log;

    location /static/ {
        root   /home/ubuntu/wikiproject/wikiweb/wiki_site/;
    }

    location /media/ {
        root   /home/ubuntu/wikiproject/wikiweb/wiki_site/;
    }

    location / {

        # an HTTP header important enough to have its own Wikipedia entry:
        #   http://en.wikipedia.org/wiki/X-Forwarded-For
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;


        # enable this if and only if you use HTTPS, this helps Rack
        # set the proper protocol for doing redirects:
        # proxy_set_header X-Forwarded-Proto https;

        # pass the Host: header from the client right along so redirects
        # can be set properly within the Rack application
        proxy_set_header Host $http_host;

        # we don't want nginx trying to do something clever with
        # redirects, we set the Host: header above already.
        proxy_redirect off;

        # set "proxy_buffering off" *only* for Rainbows! when doing
        # Comet/long-poll stuff.  It's also safe to set if you're
        # using only serving fast clients with Unicorn + nginx.
        # Otherwise you _want_ nginx to buffer responses to slow
        # clients, really.
        # proxy_buffering off;

        # Try to serve static files from nginx, no point in making an
        # *application* server like Unicorn/Rainbows! serve static files.
        if (!-f $request_filename) {
            proxy_pass http://wikiweb_server;
            break;
        }
    }

    # Error pages
    error_page 500 502 503 504 /500.html;
    location = /500.html {
        root /home/ubuntu/wikiproject/wikiweb/wiki_site/templates/;
    }
}
```

- wikiweb.conf 파일 복사

```
(wikivenv) $  sudo ln -s /home/ubuntu/wikiproject/wikiconfig/nginx/wikiweb.conf /etc/nginx/sites-available/wikiweb.conf

(wikivenv) $  sudo ln -s /etc/nginx/sites-available/wikiweb.conf /etc/nginx/sites-enabled/wikiweb.conf
```

- 기존 default 파일 이름변경

```
(wikivenv) $  cd /etc/nginx/sites-available
(wikivenv) $  sudo mv default default-kjh
```

- nginx 재시작

```
(wikivenv) $  sudo service nginx restart
```



## 프로젝트 구성도(tree)

```
wikiproject
    ├── wikivenv 
    ├── wikiweb
    |   ├── wiki
    |   ├── wiki_site
    |   |    ├── __init__.py
    |   |    ├── settings
    |   |    ├── db
    |   |    ├── media
    |   |    ├── static
    |   |    ├── settings
    |   |    |    ├── base.py
    |   |    ├── templets
    |   |    ├── urls.py
    |   |    ├── wsgi.py
    |   |    ├── views.py
    |   ├── manage.py
    ├── wikiconfig
        ├── gunicorn
        |   ├── gunicorn_start.bash
        |   ├── logs
        |   |   ├── guncorn_supervisor.log
        |   ├── run
        |       ├── gunicorn.sock
        ├── nginx
        |   ├── logs
        |   ├── wikiweb.conf
        ├── supervisor
            ├── wikiweb.conf
```



## 프로젝트 개발과 배포과정 

>  개발 과정 

1. 정적파일 생성

  ```
  $ source wikivenv/bin/activate
  (wikivenv) $ cd wikiweb
  (wikivenv) $ python manage.py collectstatic
  ```

2. 테스트서버(Icloud9)를 통해 코드 변경 후 GIT업로드

     ```
     git status

           #: db가 포함되었다면,
           배포서버 $ git rm --cached -- wiki_site/db/wiki_database.db
           배포서버 $ git commit -m "git rm cached db"

     git status      
     git add --all .
     git status
     git commit -m "edit 메시지"
     git push
     ```

3. 배포서버(AWS)에서 GIT을 이용해 코드 다운로드

      ```
      #: AWS 서비스 ================
      #: DjangoServer.pem 디렉토리에서 터미널 시작
      $ local $ chmod 400 DjangoServer.pem
      $ local $ ssh -i "DjangoServer.pem" ubuntu@ec2-13-124-171-194.ap-northeast-2.compute.amazonaws.com

      #: iwinv 서비스 ================
      $ ssh root@115.68.219.229 -p 22
      #:  root 비밀번호: B5TPWHLR

      #: 배포서버 접속 후 ==============================================
      배포서버 $ cd /home/ubuntu/wikiproject/wikiweb

      #: db git에서 제외
      배포서버 $ git status

            #: db가 포함되었다면,
            배포서버 $ git rm --cached -- wiki_site/db/wiki_database.db
            배포서버 $ git commit -m "git rm cached db"
            
      배포서버 $ git status
      배포서버 $ git pull origin master

      #: db삭제. 특별한 경우가 아니면 사용하지 말것. 
        배포서버 $ sudo rm -f wiki_site/db/wiki_database.db
      ```


4. 배포서버에서 수퍼바이저 & nginx 재시작 

  ```
  배포서버 $ sudo supervisorctl restart wikiweb

  배포서버 $ sudo service nginx restart
  ```

5. wikivenv 하위 폴더에 대한 수정이 있을 경우 파일질라를 통해 해당파일 업로드

