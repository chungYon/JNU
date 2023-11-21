# JNU(재귀함수가 너무 어려워)
![ex_screenshot](./static/image/JUNicon.png)

>재귀함수를 공부하면서 재귀의 작동 과정에 대해 자세히 알고 싶었습니다.  
>그래서 여러 재귀함수를 매개변수에 따라 트리로 시각화하는 웹사이트를 제작해보았습니다.  
>팩토리얼, 피보나치 함수, 이분탐색, 하노이 탑 같은 잘 알려진 재귀 문제를 포함하여  
>백준 문제중 하나인 '1로 만들기' 까지 재귀함수 트리 분석이 가능합니다.  
>해당 웹 사이트를 통해 재귀함수의 작동 과정을 쉽게 이해하고  
>재귀 알고리즘 문제를 푸는데 도움이 되었으면 좋겠습니다.  

## 재귀함수가 어려운 이유?
>1. 왜 이렇게 동작하는지 순서를 이해하기 힘들다. (수많은 함수의 재귀 호출 속에서 꼬이는 나의 뇌)
>2. 프로그램의 큰 그림과 세부적인 요소가 동시에 요구 된다. (재귀함수가 언제 종료되야 할지.. 어떤 경우에 무슨 함수를 호출해야 할지 모르겠다)
>3. 간단해보였는데 복잡하네? (하노이의 이동 순서처럼 베이스 케이스와 호출 순서, 리턴하는 변수에 따라 결과가 달라짐.)
### 이러한 이유로 재귀함수를 트리로 시각화하는 사이트를 만들어보자고 계획함

# 개발 기간

# 멤버
박민서 :  
신지수 :  
이건민 :  
정윤하 :  

# 프로젝트 설명
## 구현 방법
+ 함수를 노드로 보고, 함수 안의 호출된 함수와의 관계를 부모-자식 관계로 본다 -> 트리 구조
+ flask python web framework로 웹과 py파일 연결
+ d3.js 라이브러리로 웹브라우저상에서 트리를 시각화
+ 재귀함수를 python에서 구동하며 노드 연결 정보를 담은 리스트를 json파일로 변환 -> 웹에 전송
## 사이트의 기능
#### main
>프로젝트의 이름 및 간단한 설명으로 사이트 소개
>'시작하기'버튼을 누르면 select로 넘어감
#### select
>총 5개의 항목을 선택 가능
1. 피보나치 함수
    + 매개변수 n을 입력받아 n 번째 피보나치 수열을 구함
2. 팩토리얼
    + 매개변수 n을 입력받아 1부터 n까지 모든 수를 곱한 값을 구함
3. 이분 탐색
    + 매개변수 n과 탐색을 수행할 리스트를 입력받아 정렬하여 n과 일치하는 인덱스 반환 (없으면 NONE)
4. 하노이 탑
    + 매개변수 n을 입력받아 원판의 개수를 정하고 각 원판의 이동 경로를 보여줌
5. 하나 만들기
    + 매개변수 n을 입력받아 n에서 1로 바꾸는 경우의 수를 구함
    + 1로 만드는 과정은 다음과 같다
       1. 2로 나눔
       2. 3으로 나눔
       3. 1을 뺌
+ 항목 선택 시 오른쪽에 사용 방법에 대한 도움말 나타남
    + 위의 '?'버튼을 누르면 도움말이 사라짐
+ 항목 선택 시 가운데에 예시 코드(파이썬) 나타남
    + 매개변수 n의 기능 나타냄
>매개변수를 입력하고 'submit'버튼을 누르면 선택한 항목에 맞는 recursion으로 넘어감
#### recursion
>선택한 항목과 입력받은 매개변수를 바탕으로 트리 구현
1. 각 노드(원) 안에서 일어나는 연산을 시각화
2. 각 노드를 링크(선)으로 연결한 것을 시각화
>https://chungyonta.pythonanywhere.com/
