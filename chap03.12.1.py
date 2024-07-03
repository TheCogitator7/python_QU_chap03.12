#그룹 연산하기
#데이터를 특정 기준에 따라 그룹으로 나눈 후 처리하는 작업을 그룹 연산이라고 한다.
#그룹 연산은 일반적으로 3 단계 과정으로 이루어진다.

#분할(split) : 데이터를 특정 기준에 따라 분할
#적용(apply) : 데이터를 집계, 변환, 필터링하는 메서드 적용
#결합(conbine) : 적용의 결과를 하나로 결합

import seaborn as sns
from IPython.display import display

df=sns.load_dataset('penguins')

print(df.head())
print()
print()


#'species' 에 따라 데이터의 그룹을 나눠 주도록 하며,
#groupby() 메서드를 사용
df_group=df.groupby(['species'])

print(df_group)
print()
print()

print(df_group.head(2))
print()
print()

#groupby() 메서드 내에 기준이 되는 열을 입력하면 그룹 객체가 이루어진다.
#현재는 분할만 이루어진 상태이므로 데이터를 출력해도
#기존의 데이터프레임과는 크게 차이가 나지 않는다.

for key, group in df_group:
    print(key)
    display(group.head(2)) #from IPython.display import display module

print()
print()

     



