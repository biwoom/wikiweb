from django import forms

from .models import Publication_BW

class CommentForm(forms.Form):
    name = forms.CharField(label='Your name')
    url = forms.URLField(label='Your website', required=False)
    comment = forms.CharField()

# class Book_BWForm(forms.ModelForm):

#     class Meta:
#         model = Book_BW
#         fields = (
#             # 주저자
#             'text',
#             )            
# Textarea
class Publication_BW_Form(forms.ModelForm):

    class Meta:
        model = Publication_BW
        widgets = {'published_date': forms.TextInput(attrs={'id':'datepicker-1', 'class':'form-control'}),
                  'revised_date': forms.TextInput(attrs={'id':'datepicker-2', 'class':'form-control'}),
                  'errata_date': forms.TextInput(attrs={'id':'datepicker-3', 'class':'form-control'}),
        #         #저자파트
        #           'main_author': forms.TextInput(attrs={'class':'form-control'}),
                #   'main_author_profile': forms.Textarea(attrs={'class':'form-control'}),
        #         #   'main_author_img': forms.FileInput(attrs={'id':'form-file-1','class':'custom-file-input'}),
        #           'annotator': forms.TextInput(attrs={'class':'form-control'}),
                #   'annotator_profile': forms.Textarea(attrs={'class':'form-control'}),
        #         #   'annotator_img': forms.FileInput(attrs={'class':'custom-file-input'}),
        #           'main_translator': forms.TextInput(attrs={'class':'form-control'}),
        #           'main_translator_profile': forms.Textarea(attrs={'class':'form-control'}),
        #           'main_translator_img': forms.FileInput(attrs={'class':'custom-file-input'}),
        #           'co_author': forms.TextInput(attrs={'class':'form-control'}),
        #           'co_translator': forms.TextInput(attrs={'class':'form-control'}),
        #           'co_writer_profile': forms.Textarea(attrs={'class':'form-control'}),
        #         # 메이커파트
        #           'editor': forms.TextInput(attrs={'class':'form-control'}),
        #           'production_company': forms.TextInput(attrs={'class':'form-control'}),
        #           'publisher': forms.TextInput(attrs={'class':'form-control'}),
        #           'publishing_company': forms.TextInput(attrs={'class':'form-control'}),
        #           'contributor': forms.TextInput(attrs={'class':'form-control'}),
        #           'helper': forms.TextInput(attrs={'class':'form-control'}),
        #           'copyright_holder': forms.TextInput(attrs={'class':'form-control'}),
        #           'illustrator': forms.TextInput(attrs={'class':'form-control'}),
        #         # 서지정보파트
        #             'page_num': forms.NumberInput(attrs={'class':'form-control'}),
        #             'isbn': forms.TextInput(attrs={'class':'form-control'}),
        #             'edition': forms.NumberInput(attrs={'class':'form-control'}),
        #             'printing': forms.NumberInput(attrs={'class':'form-control'}),
        #         # 책제목파트
        #             'collection_title': forms.TextInput(attrs={'class':'form-control'}),
        #             'main_title': forms.TextInput(attrs={'class':'form-control'}),
        #             'sub_title': forms.TextInput(attrs={'class':'form-control'}),
        #             'volume': forms.NumberInput(attrs={'class':'form-control'}),
        #         # 책소개파트
        #             'introduction': forms.Textarea(attrs={'class':'form-control'}),
        #             'table_of_contents': forms.Textarea(attrs={'class':'form-control'}),
                    # 'cover_img': forms.FileInput(attrs={'class':'custom-file-input'}),
                    # 'preview_img_1': forms.FileInput(attrs={'class':'custom-file-input'}),
                    # 'preview_img_2': forms.FileInput(attrs={'class':'custom-file-input'}),
        #             # 'preview_img_3': forms.FileInput(attrs={'class':'custom-file-input'}),
        #             'subject': forms.TextInput(attrs={'class':'form-control'}),
        #             'topic_keyword': forms.TextInput(attrs={'class':'form-control'}),
        #         # 가격파트
        #             'price': forms.NumberInput(attrs={'class':'form-control'}),
        #             'selling_price': forms.NumberInput(attrs={'class':'form-control'}),
        #             'stock_num': forms.NumberInput(attrs={'class':'form-control'}),
        #             'sale_check': forms.RadioSelect(attrs={'class':'form-control','type':'radio'}),
        #             'our_bank': forms.TextInput(attrs={'class':'form-control'}),
        #         # 추가정보파트
        #             'errata': forms.Textarea(attrs={'class':'form-control'}),
        #             # 'supplement_file': forms.FileInput(attrs={'class':'custom-file-input'}),
        #             'video_url': forms.TextInput(attrs={'class':'form-control'}),
        #             'wiki_url': forms.TextInput(attrs={'class':'form-control'}),
        }
        fields = (
        # 기록파트 ==============================
            # 1. 북정보 작성자
            'draftsman',
            # 2. 북정보 생성일
            'created_date',
            # 3. 북정보 수정일
            're_draft_date',
                
        # 저자파트 ============================
            # 1.1. 주 저자이름
            'main_author',
            # 1.2. 주 저자 약력
            'main_author_profile',
            # 1.3. 주 저자 이미지
            # 'main_author_img',
            # 2.1. 주석자 이름
            # 'annotator',
            # 2.2. 주석자 약력
            # 'annotator_profile',
            # 2.3. 주석자 이미지
            # 'annotator_img',
            # 3.1. 주 번역자 이름
            'main_translator',
            # 3.2. 주 번역자 약력
            'main_translator_profile',
            # 3.3. 주 번역자 이미지
            # 'main_translator_img',
            # 4.1. 다중저자-목록
            # 'co_author',
            # 4.2. 다중역자-목록
            # 'co_translator',
            # 4.3. 다중 저자/역자 - 약력
            'co_writer_profile',
            
        # 메이커 파트 ==============================
            # 1. 편집자
            'editor',
            # 2. 제작사
            'production_company',
            # 3. 발행자
            'publisher',
            # 4. 출판사
            'publishing_company',
            # 5. 후원자
            'contributor',
            # 6. 기여자
            'helper',
            # 7. 판권소유자
            'copyright_holder',
            # 8. 삽화가
            'illustrator',
                                      
        # 서지정보 파트 ==============================
            # 1. 출판일
            'published_date',
            # 2. 페이지수
            'page_num',
            # 3. ISBN
            'isbn',
            # 4. 개정일
            'revised_date',
            # 5. 판형
            'edition',
            # 6. 쇄
            'printing',
        
        # 책 제목 파트 ==============================
            # 1. 컬렉션 제목
            'collection_title',
            # 2. 주제목
            'main_title',
            # 3. 부제목
            'sub_title',
            # 4. 권번호
            'volume',
        
        # 책 소개 파트 ==============================
            # 1. 책소개 - 책소개/추천사/보도자료
            'introduction',
            # 2. 목차 
            'table_of_contents',
            # 3. 표지_이미지
            'cover_img',
            # 4.1 책내용_미리보기_이미지1
            'preview_img_1',
            # 4.2 책내용_미리보기_이미지2
            'preview_img_2',
            # 4.3 책내용_미리보기_이미지3
            # 'preview_img_3',
            # 5. subject
            'subject',
            # 6. 토픽(주제) 키워드- 여러종류의 관련키워드 나열
            'topic_keyword',
        
        # 가격 파트 ==============================
            # 1. 정가
            'price',
            # 2. 판매가
            'selling_price',
            # 3. 재고수량
            'stock_num',
            # 4. 판매상태 - 판매중 / 준비중 / 절판
            'sale_check',
            # 5. 구입문의 - 입금은행정보
            'our_bank',
        
        # 추가 정보 파트 ==============================
            # 1. 오탈자(정정정보)
            'errata',
            # 2. 오탈자수정일
            'errata_date',
            # 3. 강의 동영상 유투브 URL
            'video_url',
            # 4. 관련문서 위키 URL
            'wiki_url',
            # 5. 부록자료-파일 필드 
            'supplement_file'
            )   
          