# 빅맥을 통한 일물일가의 법칙의 신뢰성 판단

## (1) 용어 설명
● 일물일가의 법칙 : 동일한 재화의 가격이 어느 곳에서나 같은 가치를 가진다는 법칙이다. 예를 들어 금괴라는 재화가 미국에서는 500원, 한국에서는 100원이라고 가정한다면 이를 이용하여 한국에서 금괴를 사서 미국에 파는 방식으로 이윤을 취할 것이다. 그렇다면 구매되는 한국의 금괴 가격은 점점 올라가고 판매되는 미국의 금괴 가격은 점점 떨어지게 되어, 결국 금괴라는 재화의 가격은 미국과 한국 두 시장에서 동일하게 맞추어 진다는 이론이다.  
  
● 빅맥 지수(Bigmac Index) : 일물일가의 법칙에 따라, 동일한 가치를 지닌 빅맥이라는 재화를 서로 다른 화폐로 평가한 것이다.  
  
● 맥잡 지수(Macjob Index) : 각 나라의 최저시급을 빅맥의 가격으로 나누어 계산한다. 선진국의 경우 빅맥 가격은 높지만 시급도 높고, 후진국의 경우 빅맥 가격은 낮지만 시급도 낮아 균등하게 맞춰질 가능성이 크다.

## (2) 주제 선정 이유
  자본주의를 살아가면서 나는 경제 분야, 특히 돈을 만지는 것에 관심이 많았다. 따라서 자연스레 데이터 분석의 주제를 선정하는 것에 경제 분야를 떠올리게 되었다. 경제에 대한 주제가 무엇이 있을까 고민하며 맥도날드에서 빅맥을 먹다가, 옛날 고등학교 공부 중 알게 된 빅맥지수에 대해 떠올리게 되었다.   
    
  맥도날드는 대부분의 나라에 있다. 따라서 각 나라의 맥도날드가 빅맥을 전세계에 판매하기 위해서는 그 나라의 환율을 고려하여 빅맥의 가격을 조정해야한다. 일물일가의 법칙에 따르면 빅맥은 모든 나라에서 같은 가치를 가져야 한다. 하지만 현실적으로 이는 불가능하다고 생각되는데, 과연 빅맥지수가 신뢰 가능한 경제 지표인지, 일물일가의 법칙이 현실에서 적용될 수 있는 법칙인지 의문이 생겨 이 주제를 선정하게 되었다. 

## (3) 가설 정의
  맥도날드는 전 세계에서 6개 나라를 뺀 모든 나라에 점포를 두고 있는 세계적인 기업이다. 맥도날드는 음식을 팔 때에 각 나라의 경제수준, 즉 각 나라에서 통용되는 화폐의 가치를 고려해야 한다. 따라서 각 나라 별 빅맥의 가격에 차이가 발생할 것이다.  
    
  한 물건에는 하나의 가격만 존재한다는 일물일가의 법칙에 따르면, 빅맥이 모든 나라에서 같은 가치를 가진다. 따라서 각 나라의 빅맥의 가격은 각 화폐의 환율을 따를 것이다. 예를 들어 현재 빅맥이 미국에서 1달러라면 한국에서는 1157원일 것이다.  
  
  이처럼 각 나라의 빅맥 가격이 각 화폐의 환율을 따른다면, 한국의 빅맥 가격(원)/미국의 빅맥 가격(달러) = 한국의 명목환율(원/달러) 이 될 것이고 다른 나라의 화폐도 이처럼 명목환율을 계산할 수 있을 것이다.

  오차율을 구할 나라는 영국, 한국, 캐나다, 오스트레일리아, 일본, 아르헨티나, 브라질, 러시아, 중국, 인도네시아 10개국이고 2001년부터 2010년까지 10년간의 자료를 구했다.
  
  연도별, 국가별 명목환율과 실제 환율을 비교하여 오차율을 구한다. 그리고 이 오차율을 통해 빅맥지수가 과연 신뢰할 수 있는 지표인지 구함으로써 일물일가의 법칙의 신뢰성을 판단해본다.

## (4) 인터넷을 통한 데이터 획득
http://bigmacindex.org 에서 구할 수 있는 자료가 표 형태로 되있음을 파악했다. 따라서 pandas 모듈의 read_html을 사용하여 각 연도 별로 정리된 표를 획득할 수 있었다.

pandas로 html의 [0]번째를 읽어오는 것은 그 웹페이지의 첫번째 표를 Dataframe, 즉 표의 형태로 가져오는 것을 의미한다.
따라서 이를 그대로 <연도>.csv 파일에 저장해주었다.

```python
import pandas as pd
import csv


# Crawling Start

#2001
data_file_2001 = pd.read_html('http://bigmacindex.org/2001-big-mac-index.html', flavor='html5lib')
data_file=data_file_2001[0]

data_file.to_csv("2001.csv", mode='w', header=False)

#2002
data_file_2002 = pd.read_html('http://bigmacindex.org/2002-big-mac-index.html', flavor='html5lib')
data_file=data_file_2002[0]

data_file.to_csv("2002.csv", mode='w', header=False)

#2003
data_file_2003 = pd.read_html('http://bigmacindex.org/2003-big-mac-index.html', flavor='html5lib')
data_file=data_file_2003[0]

data_file.to_csv("2003.csv", mode='w', header=False)

#2004
data_file_2004 = pd.read_html('http://bigmacindex.org/2004-big-mac-index.html', flavor='html5lib')
data_file=data_file_2004[0]

data_file.to_csv("2004.csv", mode='w', header=False)

#2005
data_file_2005 = pd.read_html('http://bigmacindex.org/2005-big-mac-index.html', flavor='html5lib')
data_file=data_file_2005[0]

data_file.to_csv("2005.csv", mode='w', header=False)

#2006
data_file_2006 = pd.read_html('http://bigmacindex.org/2006-big-mac-index.html', flavor='html5lib')
data_file=data_file_2006[0]

data_file.to_csv("2006.csv", mode='w', header=False)

#2007
data_file_2007 = pd.read_html('http://bigmacindex.org/2007-big-mac-index.html', flavor='html5lib')
data_file=data_file_2007[0]

data_file.to_csv("2007.csv", mode='w', header=False)

#2008
data_file_2008 = pd.read_html('http://bigmacindex.org/2008-big-mac-index.html', flavor='html5lib')
data_file=data_file_2008[0]

data_file.to_csv("2008.csv", mode='w', header=False)

#2009
data_file_2009 = pd.read_html('http://bigmacindex.org/2009-big-mac-index.html', flavor='html5lib')
data_file=data_file_2009[0]

data_file.to_csv("2009.csv", mode='w', header=False)

#2010
data_file_2010 = pd.read_html('http://bigmacindex.org/2010-big-mac-index.html', flavor='html5lib')
data_file=data_file_2010[0]

data_file.to_csv("2010.csv", mode='w', header=False)

# Crawling End
```

## (5) 분석을 위한 데이터의 가공
연도별 자료에서 우리가 필요한 건 앞에서 정한 10개국의 빅맥가격, 화폐 환율, 그리고 그 연도의 미국의 빅맥 가격이다. 따라서 웹에서 크롤링한 표에서 원하는 행과 열만 뽑아 새로운 csv 파일을 만들었다.

아래는 2001년의 데이터를 가공한 예시이다.

1. 가공을 시작하기 전, 미리 10개국과 미국의 국가 이름을 아이템으로 가지는 리스트 wanted_country를 선언했다.  

```python
wanted_country=["Britain", "South Korea", "Canada", "Japan", "Australia", "Argentina", "Brazil", "Russia", "China", "Indonesia", "United States"] #1

```

2. csv모듈의 reader를 통해 2001.csv 파일의 각 행을 fileMatrix 리스트에 append 시켜주었다.


```python
fileMatrix = []
fileMatrix_2=[]

with open("2001.csv", 'r') as fileRead:

    csvFirst = csv.reader(fileRead)

    for lineContent in csvFirst: #2
        fileMatrix.append(lineContent)

    for i in range(len(fileMatrix)): 
        fileMatrix[i]=fileMatrix[i][1:4] #3
        if fileMatrix[i][0] in wanted_country: #4
            fileMatrix_2.append(fileMatrix[i])

```


3. fileMatrix의 아이템인 csv파일의 각 행에서, 내가 필요한 데이터인 국가 이름, 현지 빅맥 가격, 환율만을 남기도록 수정했다.


4. fileMatrix의 각 행을 for문으로 읽어나가면서, 리스트의 첫 아이템인 국가 이름이 wanted_country안에 있는지 if문으로 판단해서 원하는 국가의 데이터만 추출하여 fileMatrix_2 리스트에 append 시켜준다.


```python
    for i in range(len(fileMatrix)): 
        fileMatrix[i]=fileMatrix[i][1:4] #3
        if fileMatrix[i][0] in wanted_country: #4
            fileMatrix_2.append(fileMatrix[i])

```




5. fileMatrix_2의 아이템들을 csv모듈의 writerow를 사용하여 2001_P.csv파일의 각 행에 넣어준다.

```python
with open("2001_P.csv", 'w', newline='') as fileWrite:

    csvSecond=csv.writer(fileWrite)

    for i in range(len(fileMatrix_2)):
        csvSecond.writerow(fileMatrix_2[i]) #5

```

6. 위 1~5번을 연도별로 반복해준다.

## (6) 분석 결과 도출
새롭게 만든 csv파일을 바탕으로 연도별 각 나라의 환율 오차율을 구하여 이를 csv파일로 만들었다. 이를 연도별 각 나라의 오차율 차트, 국가별 각 연도의 오차율 차트를 통해 데이터를 정리하고 시각화해보았다.

### 오차율 계산하기
1. exchange 클래스를 만들어준다. 이 클래스는 멤버 attribute로 현지의 빅맥 가격, 미국의 빅맥 가격, 실제 환율을 가지고 있다. 함수로는 실제 환율을 기준으로 가짜 환율의 오차율을 계산해주는 errorRate 함수가 있다.

아래는 2001년의 국가 별 오차율을 계산한 예시이다.

```python
class exchange: #1
    def __init__(self, givenPL, givenPU, exRateR):
        self.price_Local=givenPL
        self.price_USA=givenPU
        self.exchange_Real=exRateR
        self.exchange_Fake=givenPL/givenPU

    def errorRate(self):
        return (self.exchange_Fake-self.exchange_Real)/self.exchange_Real*100
```

2. errorRate, errorRate_<연도> 리스트를 선언하고 errorRate_<연도>리스트의 아이템으로 <연도>를 추가한다. 이는 csv파일을 보았을 때 구분하기 쉽게 하기 위해서이다.

```python
errorRate=[]; fileMatrix=[]; errorRate_2001=[2001] #2
```

3. <연도_P>.csv파일의 각 행을 읽어와 fileMatrix에 append한다. 이때 미국에 대한 정보가 있는 행은 <연도_P>.csv의 마지막 행이다. 이는 10개국과 미국의 영어 이름을 A-Z순서로 나열했을 때 미국이 가장 마지막에 있기 때문이다.

```python
with open("2001_P.csv", 'r') as fileRead: #3
    csvFile = csv.reader(fileRead)
    for lineContent in csvFile:
        fileMatrix.append(lineContent)
```

4. exchange 클래스의 객체 ToDo를 선언하고, ToDo.errorRate()를 errorRate에 append한다. for문으로 그 연도에서의 각 국가별 오차율을 모두 append 시켜준다.

```python
for i in range(lenfileMatrix-1): #4
    ToDo=exchange(float(fileMatrix[i][1]), price_in_USA, float(fileMatrix[i][2]))
    errorRate_2001.append(ToDo.errorRate())
```

5. 이를 2001년부터 2010년까지의 10개 데이터에 반복시킨다.

...

6. csv모듈의 writerow를 이용해서 errorRate의 아이템을 Error Rate.csv 파일의 각 행에 넣어준다.

```python
with open('Error Rate.csv', 'w', newline='') as fileWrite: #6
    csvWrite=csv.writer(fileWrite)
    for i in range(len(errorRate)):
        csvWrite.writerow(errorRate[i])
```

### 국가별 각 연도의 오차율 차트
1. A-Z 순서별로, 각 나라에 1번부터 10번까지 번호를 매기는 which_Country 함수를 만든다.

```python
def which_Country(countryInput): #1
    if countryInput == "Argentina":
        return 1
    elif countryInput == "Australia":
        return 2
    elif countryInput == "Brazil":
        return 3
    elif countryInput == "Britain":
        return 4
    elif countryInput == "Canada":
        return 5
    elif countryInput == "China":
        return 6
    elif countryInput == "Indonesia":
        return 7
    elif countryInput == "Japan":
        return 8
    elif countryInput == "Russia":
        return 9
    elif countryInput == "South Korea":
        return 10
```

2. 사용자에게 국가 이름을 입력받고, whilch_Country함수를 통해 국가 번호를 매겨준다.

```python
countryInput=input("Country : ") #2
countryNum=which_Country(countryInput)
```

3. Error Rate.csv파일의 각 행을 fileMatrix 리스트에 append한다.

```python
fileMatrix = [] #3
with open('Error Rate.csv', 'r') as fileRead:
    csvFirst=csv.reader(fileRead)
    for i in csvFirst:
        fileMatrix.append(i)
```


4. 그래프의 X축인 연도는 x_year 리스트를 선언하고 아이템으로 각 연도를 넣어준다.

```python
x_year=['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010'] #4
```


5. 그래프의 Y축인 오차율은 fileMatrix의 countryNum번째 행을 가지고 와서 y_rate 리스트에 넣어준다.

```python
y_rate=[] #5
for i in range(10):
    y_rate.append(float(fileMatrix[i][countryNum]))
```


6. matplotlib 모듈을 이용하여 그래프를 그려준다.

```python
N_of_groups = len(x_year) #6
index = np.arange(N_of_groups)

plt.bar(index, y_rate, tick_label=x_year, align='center')

plt.xlabel('Year')
plt.ylabel('Error Rate (%) ')
plt.title('Error Rate of '+countryInput)
plt.xlim( -1, N_of_groups)
plt.ylim( -100, 100)
fig = plt.gcf()
plt.show()

bar_width = 0.2
opacity = 0.5

plt.bar(index, y_rate, bar_width, tick_label=x_year, align='center',alpha=opacity, color='#AA2848', label='country')
```


7. 이 그래프를 Chart_<국가 이름>.png파일로 저장한다.

```python
fig.savefig("Chart_"+countryInput+".png") #7
```


### 연도별 각 국가의 오차율 차트
1. 사용자에게 연도를 입력받는다.

```python
yearInput=int(input("Year : ")) #1
```

2. Error Rate.csv파일의 각 행을 fileMatrix 리스트에 append한다.

```python
fileMatrix = [] #2
with open('Error Rate.csv', 'r') as fileRead:
    csvFirst=csv.reader(fileRead)
    for i in csvFirst:
        fileMatrix.append(i)
```

3. 그래프의 X축인 국가 이름은 A-Z 순서대로 x_country 리스트의 아이템으로 넣어준다.

```python
x_country=['ARG', 'AUS', 'BRA', 'BRI', 'CAN','CHI', 'IND', 'JAP', 'RUS', 'KOR'] #3
```

4. 그래프트의 Y축인 오차율은 fileMatrix리스트의 yearInput-2001번째 행의 아이템을 읽는다. 이때 각 행의 가장 첫 아이템인 연도는 제외하고 읽어나간다.

```python
y_rate=[] #4
for i in range(len(fileMatrix[yearInput-2000])-1):
    y_rate.append(float(fileMatrix[yearInput-2000][i+1]))

```

5. matplotlib 모듈을 이용하여 그래프를 그려준다.

```python
N_of_groups = len(x_country) #5
index = np.arange(N_of_groups)

plt.bar(index, y_rate, tick_label=x_country, align='center')

plt.xlabel('Country')
plt.ylabel('Error Rate (%) ')
plt.title('Error Rate in '+str(yearInput))
plt.xlim( -1, N_of_groups)
plt.ylim( -100, 100)
fig = plt.gcf()
plt.show()

bar_width = 0.2
opacity = 0.5

plt.bar(index, y_rate, bar_width, tick_label=x_country, align='center',alpha=opacity, color='b', label='year')
```

6. 이 그래프를 Chart_<연도>.png파일로 저장해준다.

```python
fig.savefig('Chart_'+str(yearInput)+'.png') #6
```

## (7) 분석 결과

 ### 연도별 차트
![Chart_2001.png](attachment:Chart_2001.png)
![Chart_2002.png](attachment:Chart_2002.png)
![Chart_2003.png](attachment:Chart_2003.png)
![Chart_2004.png](attachment:Chart_2004.png)
![Chart_2005.png](attachment:Chart_2005.png)
![Chart_2006.png](attachment:Chart_2006.png)
![Chart_2007.png](attachment:Chart_2007.png)
![Chart_2008.png](attachment:Chart_2008.png)
![Chart_2009.png](attachment:Chart_2009.png)
![Chart_2010.png](attachment:Chart_2010.png)

### 국가별 차트
![Chart_South%20Korea.png](attachment:Chart_South%20Korea.png)![Chart_Russia.png](attachment:Chart_Russia.png)![Chart_Japan.png](attachment:Chart_Japan.png)![Chart_Indonesia.png](attachment:Chart_Indonesia.png)![Chart_Canada.png](attachment:Chart_Canada.png)![Chart_Britain.png](attachment:Chart_Britain.png)![Chart_Brazil.png](attachment:Chart_Brazil.png)![Chart_Australia.png](attachment:Chart_Australia.png)![Chart_Argentina.png](attachment:Chart_Argentina.png)

내가 처음 예상한 것과 다른 결과가 나왔다.

첫번째로, 선진국과 후진국 간 차이이다. 나는 선진국은 양의 오차율을, 후진국은 음의 오차율을 보일 것이라고 생각했다. 그 이유는 선진국은 물가가 비싸기 때문에 자연스레 빅맥의 가격도 비싸지고, 후진국은 물가가 싸기 때문에 빅맥의 가격 또한 쌀것이라고 생각했다. 하지만 위 그래프를 보면 오차율의 양 음은 각 국가에 따라 비슷한 경향을 보이긴 하지만, 선진국과 후진국 간에 큰 차이는 발생하지 않았다. 오히려 2010년 그래프를 보면 아르헨티나가 영국보다 오차율이 큰 것을 확인할 수 있다. 따라서 선진국과 후진국이라는 이유만으로 무조건 양, 음의 오차율 차이가 발생하는 것은 아니었다.

두번째로, 연도별 성장의 차이이다. 나는 제안서에서, 한 두 나라 정도를 빼고는 모두 오차율의 성장을 보일 것이라 예측했다. 하지만 브라질처럼 대체로 평탄한 오차율의 성장을 거친 나라도 있었지만, 캐나다, 영국처럼 애매하게 바뀌는 나라들도 있었다. 

## (8) 결론

빅맥 지수와 맥잡 지수를 모두 분석해본 결과, 각 경제 지표에서 규칙성을 찾을 수 없었다. 또한 데이터 분석 이전에 예측했던 바와 다르게, 최저임금 이라는 요소 만으로는 특정할 수 없는 부분이 있었다. 따라서 일물일가의 법칙은 신뢰할 수 없는 법칙이다.

## (9) 참고 문헌
파이썬으로 데이터 주무르기(민형기)  
https://namu.wiki/w/%EB%B9%85%EB%A7%A5%EC%A7%80%EC%88%98    
https://medium.com/@whj2013123218/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EC%9B%B9%EC%97%90%EC%84%9C-%EB%8F%84%ED%91%9C-%ED%81%AC%EB%A1%A4%EB%A7%81%ED%95%98%EA%B8%B0-97bd7908b83a  
https://buttercoconut.xyz/74/  
https://codeday.me/ko/qa/20190316/25204.html  
https://m.blog.naver.com/PostView.nhn?blogId=real_77&logNo=221200151992&proxyReferer=https%3A%2F%2Fwww.google.com%2F  
https://iamaman.tistory.com/2086  
http://egloos.zum.com/nitraqu/v/4383287  
