from django.db import models

# Create your models here.
from django.utils import timezone
from django.utils.safestring import mark_safe 
from markdown_deux import markdown

def upload_path_img(instance, filename):
    return "dictapp/images/%s/%s" %(instance.id, filename)
    
def upload_path_file(instance, filename):
    return "dictapp/files/%s/%s" %(instance.id, filename)    
    
def upload_path_audio(instance, filename):
    return "dictapp/audio/%s/%s" %(instance.id, filename)     
    
class Dict(models.Model):
    author = models.ForeignKey('auth.User')
    
    # 티벳어 단어 표제어 필드
    title = models.CharField(max_length=200, verbose_name='티벳어 표제어', help_text='')
    
    # 단어 설명 필드(품사/한국어 표제어/의미/용례/어원)
    text = models.TextField(blank=True, null=True, verbose_name='단어설명', help_text='')
    def __str__(self):
        return self.title
    
    def get_markdown(self):
        text = self.text
        markdown_text = markdown(text)
        return mark_safe(markdown_text)        
    
    # 티벳어 사진자료(이미지) 필드 
    image = models.ImageField(upload_to=upload_path_img, blank=True, null=True, 
                              height_field='height_field', 
                              width_field='width_field',
                              verbose_name='사진자료', help_text=''
                              )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
     
    # 파일 필드 
    file = models.FileField(upload_to=upload_path_file, blank=True, null=True, verbose_name='파일', help_text='')
    def get_filename(self):
        filename = str(self.file.name)
        filename_str = filename.split('/')
        return filename_str[3]
    
    # 티벳어 발음 오디오 필드 
    audio = models.FileField(upload_to=upload_path_audio, blank=True, null=True, verbose_name='티벳어 발음 오디오', help_text='')
    
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    # 티벳어 동사 미래형 필드
    ti_future_tense = models.CharField(blank=True, null=True, max_length=200, verbose_name='동사-미래형', help_text='')
    
    # 티벳어 동사 현재형 필드
    ti_present_tense = models.CharField(blank=True, null=True, max_length=200, verbose_name='동사-현재형', help_text='')
    
    # 티벳어 동사 과거형 필드
    ti_past_tense = models.CharField(blank=True, null=True, max_length=200, verbose_name='동사-과거형', help_text='')
    
    # 티벳어 동사 명령형 필드
    ti_imperative = models.CharField(blank=True, null=True, max_length=200, verbose_name='동사-명령형', help_text='' )
    
    # 티벳어 동의어 필드
    ti_synonym = models.CharField(blank=True, null=True, max_length=200, verbose_name='동의어', help_text='')
    
    # 티벳어 유의어 필드
    ti_thesaurus = models.CharField(blank=True, null=True, max_length=200, verbose_name='유의어', help_text='')
    
    # 티벳어 반의어 필드
    ti_antonym = models.CharField(blank=True, null=True, max_length=200, verbose_name='반의어', help_text='')
    
    # 티벳어 높임말 필드
    ti_honorific = models.CharField(blank=True, null=True, max_length=200, verbose_name='높임말', help_text='')
    
    # 티벳어 낮춤말 필드
    ti_humble_terms = models.CharField(blank=True, null=True, max_length=200, verbose_name='낮춤말', help_text='')
    
    # 한국어 표제어 필드
    ti_korean_entry = models.CharField(blank=True, null=True, max_length=200, verbose_name='한국어 표제어', help_text='')
    
    # 범어 표제어 필드
    ti_sanskrit_entry = models.CharField(blank=True, null=True, max_length=200, verbose_name='산스끄리뜨', help_text='')
    
    # 빨리어 표제어 필드
    ti_pali_entry = models.CharField(blank=True, null=True, max_length=200, verbose_name='빨리어', help_text='')
    
    # 한문 표제어 필드
    ti_classical_chinese_entry = models.CharField(blank=True, null=True, max_length=200, verbose_name='한문', help_text='')
    
    # 영어 표제어 필드
    ti_english_entry = models.CharField(blank=True, null=True, max_length=200, verbose_name='영어', help_text='')
    
    # 티벳어-와일리 필드
    ti_wylie = models.CharField(blank=True, null=True, max_length=200, verbose_name='티벳어 와일리표기', help_text='')
    
    # 단어 분류 필드    
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    CLASSIFICATION = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    classification = models.CharField(
        max_length=2,
        choices=CLASSIFICATION,
        default=FRESHMAN,
        verbose_name='단어 분류', help_text=''
    ) 
    
    # 불교 단어 분류 필드   
    Bu_Sutra = '《경장》'
    Bu_Vinaya = '《율장》'
    Bu_Shastra = '《논장》'
    Bu_Treatise = '《주석》'
    Bu_Chant_of_praising = '《찬가》'
    Bu_Letter = '《서신》'
    Bu_Poem = '《시문》'
    Bu_History = '《역사》'
    Bu_Fable = '《우화》'
    Bu_Person = '《인명》'
    Bu_Location = '《지명》'
    Bu_Ceremony = '《의례》'
    Bu_Cloth = '《복식》'
    Bu_Temple = '《사원》'
    
    BU_CLASSIFICATION = (
        (Bu_Sutra, '《경장》'),
        (Bu_Vinaya, '《율장》'),
        (Bu_Shastra, '《논장》'),
        (Bu_Treatise, '《주석》'),
        (Bu_Chant_of_praising, '《찬가》'),
        (Bu_Letter, '《서신》'),
        (Bu_Poem, '《시문》'),
        (Bu_History, '《역사》'),
        (Bu_Fable, '《우화》'),
        (Bu_Person, '《인명》'),
        (Bu_Location, '《지명》'),
        (Bu_Ceremony, '《의례》'),
        (Bu_Cloth, '《복식》'),
        (Bu_Temple, '《사원》'),
    )
    bu_classification = models.CharField(
        max_length=10,
        choices=BU_CLASSIFICATION,
        default=FRESHMAN,
        verbose_name='불교 단어 분류', help_text=''
    ) 
          