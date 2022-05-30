from django.db import models
from datetime import datetime, timedelta, timezone
from accounts.models import User
# Create your models here.

class Board(models.Model): # models 안의 Model (이미 구현되어있는 장고의 모델 기능 사용) 을 상속해서 만들어짐
    # 데이터베이스 테이블의 열들을 선언 + 데이터 형식과 함께
    title = models.CharField(max_length=200)
    content = models.TextField()
    file = models.FileField(default="", blank=True, null=True, upload_to='board_photo') 
    # file = models.file
    # 비어있어도 되고, null값이어도 된다
    # settings.py 에 MEDIA파일을 올리는 위치도 지정해줌 
    # upload_to 라는 거는 /media/board_photo 라는폴더가 생겨서 이안에 모든 파일들이 저장된다는 소리


    date = models.DateTimeField(auto_now_add=True) #자동으로 지금 시간 추가
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    # 외래키에서 어떤 테이블을 참조할지
    #  on_delete : 외래키가 바라보는 테이블의 값이 삭제될 때 수행할 방법을 지정,
    # user가 삭제되었을 때 board들은 어떻게할 것인가?
    # CASCADE: 유저가 삭제되면 해당 유저를 참조하는 게시물도 삭제하십시오 

    def __str__(self):
        return self.title

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.date
        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.date.date()
            return str(time.days) + '일 전'
        else:
            return False

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True) #자동으로 지금 시간 추가
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Board, on_delete=models.CASCADE)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True,  related_name='+')
    # 대댓글을 구현하기 위해서 자기자신을 참조 -> 기준이 되는 부모의 댓글 참조하기 때문에 self( 댓글 참조)로 지정

    def __str__(self):
        return self.comment

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.date
        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.date.date()
            return str(time.days) + '일 전'
        else:
            return False
