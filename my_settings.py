DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DATABASE 명',
        'USER': 'DB접속 계정명',
        'PASSWORD': 'DB접속용 비밀번호',
        'HOST': '실제 DB 주소',
        'PORT': '포트번호',
    }
}

SECRET = {
        'secret':'시크릿키',
}