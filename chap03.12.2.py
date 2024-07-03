#그룹별 연산하기

import seaborn as sns
from IPython.display import display
import pandas as pd

df=sns.load_dataset('penguins')
print(df.head())
print()
print()

df_group=df.groupby(['species'])
print(df_group)
print()
print()


print(df_group.head(2))
print()
print()


#그룹의 칼럼별 평균

print(df_group['bill_length_mm'].mean())
print()

print(df_group['bill_depth_mm'].mean())
print()

print(df_group['flipper_length_mm'].mean())
print()

print(df_group['body_mass_g'].mean())
print()
print()

#'species' 와 'sex' 에 따른 평균을 구해보자
df_group_1=df.groupby(['species', 'sex'])

print(df_group_1['bill_length_mm'].mean())
print()

print(df_group_1['bill_depth_mm'].mean())
print()

print(df_group_1['flipper_length_mm'].mean())
print()

print(df_group_1['body_mass_g'].mean())
print()
print()


#집계 연산을 처리하는 함수를 사용자가 직접 만든 후
#그룹 객체에 적용하기 위해서는 agg() 메서드를 사용한다.
#예제로 최대값과 최소값의 차이를 계산하는 함수를 만든 후 적용해보면

def min_max(x):
    return x.max()-x.min()

print(df_group['bill_length_mm'].agg(min_max))
print()
print()


#agg() 메서드를 사용하면 한 번에 여러 개의 집계 연산을 처리할 수도 있다.

print(df_group['bill_length_mm'].agg(['max', 'min']))
print()

print(df_group['bill_depth_mm'].agg(['max', 'min']))
print()

print(df_group['flipper_length_mm'].agg(['max', 'min']))
print()

print(df_group['body_mass_g'].agg(['max', 'min']))
print()
print()



#각 열마다 다른 종류의 함수를 적용하면

#print(df_group['bill_length_mm'].agg({'bill_length_mm' : ['max', 'min']}))
#위 구문의 어떻게 고쳐야 에러가 안 날까???


#행 인덱스와 열 인덱스를 기준으로 할 경우
print(df_group['bill_length_mm'].transform('mean'))
print()
print()


#z-score 란 각 데이터의 값이 평균으로부터 얼마나 떨어져 있는지를 나타내는 수치로서
#각 원소를 평균으로 빼준 후 이를 표준편차로 나눈다.

def z_score(x):
    z=(x-x.mean()) / x.std()
    return(z)

print(df_group['bill_length_mm'].transform(z_score))
print()
print()


#apply() 메서드를 그룹 객체에 적용할 수 있다.

print(df_group['bill_length_mm'].apply(min)) #에러의 이유는?
print()
print()


print(df_group['bill_length_mm'].apply(z_score))
print()
print()

print(df_group['bill_length_mm'].mean())
print()
print()

print(df_group['bill_length_mm'].filter(lambda x : x.mean() >= 40))



