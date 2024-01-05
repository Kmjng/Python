#시리즈 만들어서 데이터프레임 만들기
import pandas as pd

lst_num = [1,2,3,4,5]
s1 = pd.core.series.Series(lst_num)
print(s1) #이렇게 하면 아래와 같이 출력된다.
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64
s2=pd.core.series.Series(['one','two','three','four','five'])
s3=pd.DataFrame(data=dict(num=s1, word=s2))
print(s3)