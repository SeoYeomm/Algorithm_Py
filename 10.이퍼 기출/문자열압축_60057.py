import sys

def solution(s):
    answer = set()

    if len(s) == 1:
        return 1

    for i in range(1, len(s)+1):
        txt = s[:i]        # 검사할 부분 문자열
        cnt = 1            # 부분 문자열과 같은 문자열의 개수
        pre = ''           # 검사하기 전 문자들을 담는 str

        for j in range(i, len(s)+i, i): # 부분 문자열 길이만큼 이동하며 압축 진행 
            if txt == s[j:j+i]:
                cnt += 1
            
            else: # 문자열 반복 X
                if cnt != 1:
                    pre += str(cnt) + txt
                else:
                    pre += txt
                    
                # 다음 부분 문자열로 이동하기 위해 txt 갱신, cnt 초기화 
                txt = s[j:j+i]
                cnt = 1

        answer.add(len(pre))

    return min(answer)

