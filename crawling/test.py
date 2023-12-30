def remove_certification(text):
    # 찾을 문자열
    certification_string = "[한국관광 품질인증/Korea Quality]"

    # 문자열에서 인증 부분 제거
    result = text.replace(certification_string, "").strip()

    return result

# 테스트
name = "가경재 [한국관광 품질인증/Korea Quality]"
modified_name = remove_certification(name)

print("원래 이름:", name)
print("수정된 이름:", modified_name)