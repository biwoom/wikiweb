from django import forms

from .models import Dict


# class DictForm(forms.ModelForm):

#     class Meta:
#         model = Dict
#         fields = (
#             # 티벳어 표제어
#             'title',
#             # 티벳어 한글 설명
#             'text',
#             # 티벳어 동사 과거형 필드
#             'ti_past_tense',
#             # 티벳어 동사 현재형 필드
#             'ti_present_tense',
#             # 티벳어 동사 미래형 필드
#             'ti_future_tense',
#             # 티벳어 동사 명령형 필드
#             'ti_imperative',
#             # 티벳어 동의어 필드
#             'ti_synonym',
#             # 티벳어 유의어 필드
#             'ti_thesaurus',
#             # 티벳어 반의어 필드
#             'ti_antonym',
#             # 티벳어 높임말 필드
#             'ti_honorific',
#             # 티벳어 낮춤말 필드
#             'ti_humble_terms',
#             # 한국어 표제어 필드
#             'ti_korean_entry',
#             # 범어 표제어 필드
#             'ti_sanskrit_entry',
#             # 빨리어 표제어 필드
#             'ti_pali_entry',
#             # 한문 표제어 필드
#             'ti_classical_chinese_entry',
#             # 영어 표제어 필드
#             'ti_english_entry',
#             # 티벳어-와일리 필드
#             'ti_wylie',
#             # 티벳어 이미지
#             'image', 
#             # 티벳어 발음 오디오
#             'audio',
#             )

class CommentForm(forms.Form):
    name = forms.CharField(label='Your name')
    url = forms.URLField(label='Your website', required=False)
    comment = forms.CharField()

class DictForm(forms.ModelForm):

    class Meta:
        model = Dict
        fields = (
            # 티벳어 표제어
            'title',
            # 티벳어-와일리 필드
            'ti_wylie',
            # 티벳어 한글 설명
            'text',
            # 티벳어 동사 과거형 필드
            'ti_past_tense',
            # 티벳어 동사 현재형 필드
            'ti_present_tense',
            # 티벳어 동사 미래형 필드
            'ti_future_tense',
            # 티벳어 동사 명령형 필드
            'ti_imperative',
            # 티벳어 동의어 필드
            'ti_synonym',
            # 티벳어 유의어 필드
            'ti_thesaurus',
            # 티벳어 반의어 필드
            'ti_antonym',
            # 티벳어 높임말 필드
            'ti_honorific',
            # 티벳어 낮춤말 필드
            'ti_humble_terms',
            # 한국어 표제어 필드
            'ti_korean_entry',
            # 범어 표제어 필드
            'ti_sanskrit_entry',
            # 빨리어 표제어 필드
            'ti_pali_entry',
            # 한문 표제어 필드
            'ti_classical_chinese_entry',
            # 영어 표제어 필드
            'ti_english_entry',
            # 티벳어 이미지
            'image', 
            # 티벳어 발음 오디오
            'audio',
            )            