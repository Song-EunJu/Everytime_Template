from django.db import models
from django.contrib.auth.models import AbstractUser
# AbstractUser vs AbstractBaseUser

# settings.py 등록
# 생성한 유저 모델을 인증을 위한 유저 모델로 사용하기 위해서는 아래와 같이 settings.py에 등록해줘야 합니다.

# django 유저모델을 커스터마이징했을때 발생하는 에러
# AbstractUser 를 상속받은 User모델을 새로 만들었으므로, 
# accounts 폴더에서 데이터가 migration 안됐다는 뜻

# 이 모델을 유저모델로 사용하기 위해 settings.py 에 추가적인 설정 필요

# ValueError: Dependency on app with no migrations: accounts
# accounts 폴더에서 데이터가 migration 안됐다는 뜻

class User(AbstractUser):
    nickname = models.CharField(max_length=20, default="")


