from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone
from django.utils.safestring import mark_safe 
from markdown_deux import markdown
import uuid

def upload_path_img(instance, filename):
    return "bookapp/images/%s/%s" %(instance.id, filename)
def upload_path_audio(instance, filename):
    return "bookapp/audio/%s/%s" %(instance.id, filename)     
 
# 북앱 파일 업로드 경로
# 이미지
def upload_path_main_author_img(instance, filename):
    return "bookapp/images/main_author/%s/%s" %(instance.id, filename)
def upload_path_annotator_img(instance, filename):
    return "bookapp/images/annotator/%s/%s" %(instance.id, filename)
def upload_path_main_translator_img(instance, filename):
    return "bookapp/images/main_translator/%s/%s" %(instance.id, filename)
def upload_path_cover_img(instance, filename):
    return "bookapp/images/cover/%s/%s" %(instance.id, filename)
def upload_path_preview_img(instance, filename):
    return "bookapp/images/preview/%s/%s" %(instance.id, filename)
# 파일/부록자료
def upload_path_file(instance, filename):
    return "bookapp/files/%s/%s" %(instance.id, filename) 


class Publication_BW(models.Model):
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    
    # 마크다운을 위한 스트링 변환                          
    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.main_author_profile, 
                          self.main_translator_profile,
                          self.annotator_profile,
                          self.co_writer_profile,
                          self.introduction,
                          self.table_of_contents,
                          self.errata
                          )  

# 기록파트 ==============================
    # 1. 북정보 작성자
    draftsman = models.CharField(blank=True, null=True,default='', max_length=100, verbose_name='북정보 작성자 이름', help_text='')
    # 2. 북정보 생성일
    created_date = models.DateTimeField(default=timezone.now)
    # 3. 북정보 수정일
    re_draft_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    def publish(self):
        self.re_draft_date = timezone.now()
        self.save()
        
# 저자파트 ==============================    
    # 1.1. 주 저자이름
    main_author = models.CharField(blank=True, null=True, default='', max_length=100, verbose_name='주저자 이름', help_text='')
    # 1.2. 주 저자 약력
    main_author_profile = models.TextField(blank=True, null=True, default='', verbose_name='주저자 약력', help_text='')
    def get_markdown_main_author_profile(self):
        main_author_profile = self.main_author_profile
        markdown_main_author_profile = markdown(main_author_profile)
        return mark_safe(markdown_main_author_profile)        
    # 1.3. 주 저자 이미지
    main_author_img = models.ImageField(upload_to=upload_path_main_author_img, blank=True, null=True, default='', 
                              height_field='height_field', 
                              width_field='width_field',
                              verbose_name='주저자-사진', help_text='' )
    # 2.1. 주석자 이름
    annotator = models.CharField(blank=True, null=True, default='', max_length=100, verbose_name='주석자 이름', help_text='')
    # 2.2. 주석자 약력
    annotator_profile = models.TextField(blank=True, null=True, default='', verbose_name='주석자 약력', help_text='')
    def get_markdown_annotator_profile(self):
        annotator_profile = self.annotator_profile
        markdown_annotator_profile = markdown(annotator_profile)
        return mark_safe(markdown_annotator_profile)        
    # 2.3. 주석자 이미지
    annotator_img = models.ImageField(upload_to=upload_path_main_author_img, blank=True, null=True, default='',
                              height_field='height_field', 
                              width_field='width_field',
                              verbose_name='주석자-사진', help_text='' )
    # 3.1. 주 번역자 이름
    main_translator = models.CharField(blank=True, null=True, default='', max_length=100, verbose_name='주번역자 이름', help_text='')
    # 3.2. 주 번역자 약력
    main_translator_profile = models.TextField(blank=True, null=True, default='', verbose_name='주번역자 약력', help_text='')
    def get_markdown_main_translator_profile(self):
        main_translator_profile = self.main_translator_profile
        markdown_main_translator_profile = markdown(main_translator_profile)
        return mark_safe(markdown_main_translator_profile)        
    # 3.3. 주 번역자 이미지
    main_translator_img = models.ImageField(upload_to=upload_path_main_translator_img, blank=True, null=True, default='',
                              height_field='height_field', 
                              width_field='width_field',
                              verbose_name='주번역자-사진', help_text='' )
    # 4.1. 다중저자-목록
    co_author = models.CharField(blank=True, null=True, default='', max_length=300, verbose_name='다중저자-목록', help_text='')
    # 4.2. 다중역자-목록
    co_translator = models.CharField(blank=True, null=True, default='', max_length=300, verbose_name='다중역자-목록', help_text='')
    # 4.3. 다중 저자/역자 - 약력
    co_writer_profile = models.TextField(blank=True, null=True, default='', verbose_name='다중 저자/역자 - 약력', help_text='')
    def get_markdown_co_writer_profile(self):
        co_writer_profile = self.co_writer_profile
        markdown_co_writer_profile = markdown(co_writer_profile)
        return mark_safe(markdown_co_writer_profile)
    
# 메이커 파트 ==============================
    # 1. 편집자
    editor = models.CharField(blank=True, null=True, default='', max_length=100, verbose_name='편집자', help_text='')
    # 2. 제작사
    production_company = models.CharField(blank=True, null=True, default='', max_length=100, verbose_name='제작사', help_text='')
    # 3. 발행자
    publisher = models.CharField(blank=True, null=True, default='', max_length=100, verbose_name='발행자', help_text='')
    # 4. 출판사
    publishing_company = models.CharField(blank=True, null=True, default='', max_length=100, verbose_name='출판사', help_text='')
    # 5. 후원자
    contributor = models.CharField(blank=True, null=True, default='', max_length=200, verbose_name='후원자', help_text='')
    # 6. 기여자
    helper = models.CharField(blank=True, null=True, default='', max_length=200, verbose_name='기여자', help_text='')
    # 7. 판권소유자
    copyright_holder = models.CharField(blank=True, null=True, default='', max_length=100, verbose_name='판권소유자', help_text='')
    # 8. 삽화가
    illustrator = models.CharField(blank=True, null=True, default='', max_length=100, verbose_name='삽화가', help_text='')
                              
# 서지정보 파트 ==============================
    # 1. 출판일
    published_date = models.DateTimeField(blank=True, null=True, default='', max_length=100, verbose_name='출판일', help_text='')
    # 2. 페이지수
    page_num = models.IntegerField(blank=True, null=True, default=1, verbose_name='페이지수', help_text='')
    # 3. ISBN
    isbn = models.CharField(blank=True, null=True, default='', max_length=100, verbose_name='ISBN', help_text='')
    # 4. 개정일
    revised_date = models.DateTimeField(blank=True, null=True, default='', max_length=100, verbose_name='개정일', help_text='')
    # 5. 판형
    edition = models.IntegerField(blank=True, null=True, default=1,  verbose_name='판형', help_text='')
    # 6. 쇄
    printing  = models.IntegerField(blank=True, null=True, default=1, verbose_name='쇄', help_text='')

# 책 제목 파트 ==============================
    # 1. 컬렉션 제목
    collection_title = models.CharField(blank=True, null=True, default='', max_length=200, verbose_name='컬렉션 제목', help_text='')
    # 2. 주제목
    main_title = models.CharField(blank=True, null=True, default='', max_length=200, verbose_name='주제목', help_text='')
    # 3. 부제목
    sub_title = models.CharField(blank=True, null=True, default='', max_length=200, verbose_name='부제목', help_text='')
    # 4. 권번호
    volume  = models.IntegerField(blank=True, null=True, default=1, verbose_name='권번호', help_text='')

# 책 소개 파트 ==============================
    # 1. 책소개 - 책소개/추천사/보도자료
    introduction = models.TextField(blank=True, null=True, default='', verbose_name='책소개', help_text='')
    def get_markdown_introduction(self):
        introduction = self.introduction
        markdown_introduction = markdown(introduction)
        return mark_safe(markdown_introduction) 
    # 2. 목차 
    table_of_contents = models.TextField(blank=True, null=True, default='', verbose_name='목차', help_text='')
    def get_markdown_table_of_contents(self):
        table_of_contents = self.table_of_contents
        markdown_table_of_contents = markdown(table_of_contents)
        return mark_safe(markdown_table_of_contents)
    # 3. 표지_이미지
    cover_img = models.ImageField(upload_to=upload_path_cover_img, blank=True, null=True, default='',
                              height_field='height_field', 
                              width_field='width_field',
                              verbose_name='표지-사진', help_text='' )
    # 4.1 책내용_미리보기_이미지1
    preview_img_1 = models.ImageField(upload_to=upload_path_preview_img, blank=True, null=True, default='',
                              height_field='height_field', 
                              width_field='width_field',
                              verbose_name='책내용_미리보기_사진1', help_text='' )
    # 4.2 책내용_미리보기_이미지2
    preview_img_2 = models.ImageField(upload_to=upload_path_preview_img, blank=True, null=True, default='',
                              height_field='height_field', 
                              width_field='width_field',
                              verbose_name='책내용_미리보기_사진2', help_text='' )
    # 4.3 책내용_미리보기_이미지3
    preview_img_3 = models.ImageField(upload_to=upload_path_preview_img, blank=True, null=True, default='',
                              height_field='height_field', 
                              width_field='width_field',
                              verbose_name='책내용_미리보기_사진3', help_text='' )
    # 5. subject
    subject = models.CharField(blank=True, null=True, default='', max_length=100, verbose_name='분야', help_text='')
    # 6. 토픽(주제) 키워드- 여러종류의 관련키워드 나열
    topic_keyword = models.CharField(blank=True, null=True, default='', max_length=200, verbose_name='주제_키워드', help_text='')

# 가격 파트 ==============================
    # 1. 정가
    price  = models.IntegerField(blank=True, null=True, default=1, verbose_name='정가', help_text='')
    # 2. 할인 : 원래 판매가였으나 할인 필드로 교체
    selling_price  = models.CharField(blank=True, null=True, default=1, max_length=300, verbose_name='할인', help_text='')
    # 3. 배송료 : 원래 재고수량이었으나 배송료 필드로 교체
    stock_num  = models.CharField(blank=True, null=True, default=1, max_length=300, verbose_name='배송료', help_text='')
    # 4. 판매상태 - 판매중 / 준비중 / 절판    
    SALE_CHECK_LIST = (
    ('판매중', '판매중'),
    ('준비중', '준비중'),
    ('절판', '절판')
    )
    sale_check = models.CharField(
        max_length=10,
        choices=SALE_CHECK_LIST,
        default=SALE_CHECK_LIST[0],
        verbose_name='판매상태', help_text='') 
    # 5. 구입문의 - 입금은행정보
    our_bank = models.CharField(blank=True, null=True, default='', max_length=200, verbose_name='구입문의', help_text='')

# 추가 정보 파트 ==============================
    # 1. 오탈자(정정정보)
    errata = models.TextField(blank=True, null=True, default='', verbose_name='오탈자-정정정보', help_text='')
    def get_markdown_errata(self):
        errata = self.errata
        markdown_errata = markdown(errata)
        return mark_safe(markdown_errata)
    # 2. 오탈자수정일
    errata_date = models.DateTimeField(blank=True, null=True, default='', max_length=100, verbose_name='오탈자수정일', help_text='')
    # 3. 강의 동영상 유투브 URL
    video_url = models.CharField(blank=True, null=True, default='', max_length=1000, verbose_name="Vedio_URL")
    # 4. 관련문서 위키 URL
    wiki_url = models.CharField(blank=True, null=True, default='', max_length=1000, verbose_name="Wiki_URL")
    # 5. 무료 도서 다운로드  URL
    book_cloud_url = models.CharField(blank=True, null=True, default='', max_length=1000, verbose_name="Book_URL")
    # 6. 부록자료-파일 필드 
    supplement_file = models.FileField(upload_to=upload_path_file, verbose_name='부록자료', help_text='', blank=True, null=True, default='')
    def get_filename(self):
        filename = str(self.supplement_file.name)
        filename_str = filename.split('/')
        return filename_str[3]