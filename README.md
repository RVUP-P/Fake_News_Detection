# Fake_News_Detection PJ
---------------------------------------
### 2024 한양대 정보공학
### 인공지능1 정철현교수님(inbass@hanyang.ac.kr)
### 고현주(6817), 이신영(6644), 전민규(4475), 조일경(4239)
---------------------------------------

### ■■ 기본 모델(Ref Project)
### Ref Project(Model) : https://github.com/Abhradipta/Fake-News-Detection
#### [기본 모델]
#### nltk의 stopwords + ‘from, subject, re, edu, use’ 제거, 3개 이하 단어 제거
#### sklearn의 train_test_split로 훈련 데이터와 테스트 데이터 8:2 분할
#### nltk의 word_tokenize로 텍스트 데이터를 정수 인덱스의 시퀀스로 변환, padding도 추가
#### Bi-Directional RNN and LSTM로 모델 Building
#### batch_size = 64, validation_split = 0.1, epochs = 5로 Training
#### 각 예측 값이 0.95보다 큰 경우만 긍정적 예측으로 분류

---------------------------------------

### ■■ 성능 개선을 위한 시도 
#### ■ 전처리/모델 개선
#### [추가]
#### nltk의 WordNetLemmatizer
#### GloVe 100차원 벡터로 임베딩 매트릭스 생성
#### Functional API로 모델 정의 + Keras의 attention 레이어 사용
#### Sequential API로 모델 정의 + 직접 정의한 SelfAttention 클래스 사용(Query, Key, Value를 Dense 레이어로 정의하고, Softmax를 적용하여 어텐션 스코어를 계산한 후, Context Vector를 구함)

---------------------------------------

### ■■ 성능 개선 시도별 ACC (기존 제공 data 학습결과 )
![image](https://github.com/RVUP-P/Fake_News_Detection/assets/101576044/e2e8fbf4-5d5e-4e65-a432-46cf8b93aed2)



### ■■ 성능 개선 시도별 ACC (Crawling/ChatGPT 생성 data 학습결과)

![image](https://github.com/RVUP-P/Fake_News_Detection/assets/101576044/d11825d2-a258-4a06-b007-19a87b885404)


---------------------------------------
### ■■ Project Report (국제 표준 ISO/IEC TS 4213:2022에 따른 Report)
![image](https://github.com/RVUP-P/fake_news_detect/assets/101576044/396bce6f-4901-408a-a9b1-7b021a720805)


---------------------------------------

### ■■ 데이터 셋 구성 
#### -기본 제공 데이터 셋 
#### -Fake & True : 44898 row
#### -추가 데이터 셋 
#### -Crawling(time) & Generated Fake News(GPT3.5) : 11133 row 

#### True 분포 / Fake 분포
![image](https://github.com/RVUP-P/fake_news_detect/assets/101576044/21fbb6f3-f1ef-464d-bbbe-34ec588cae69)
![image](https://github.com/RVUP-P/fake_news_detect/assets/101576044/17b61f9d-d88f-428e-a680-5cbe79778e44)

#### Crawling(Time) 분포 / Generated News(GPT3.5) 분포 
![image](https://github.com/RVUP-P/Fake_News_Detection/assets/101576044/41ccb496-1525-41ef-88b5-d4d8d809dba6)
![image](https://github.com/RVUP-P/Fake_News_Detection/assets/101576044/96d5698c-d719-49a5-9f9f-545f8eb98f93)



#### ■ Crawling(Time) 방법 
#### Time지에서 politics 뉴스기사를 Crawling하여 data 수집 
#### -> 뉴스 기사 본문의 길이가 일정치 않음(수백~수만)
#### -> 기존에 제공된 fake/true data set의 뉴스기사길이 분포를 참고하여 본문의 길이가 800~4000자인 기사만 수집
####
#### ■ Generated Fake News(GPT3.5) 방법 
#### ChatGPT API를 활용하여 Fake News를 생성 (ChatGPT3.5Turbo)
#### 1.API를 사용하지 않는 경우에는 생성도 느리고 또 긴 뉴스기사를 중복없이 작성하기 어려움이 있었음. 
#### 2.API에서도 프롬포팅을 다회 진행 해봤을 때, 특정 주제에 한정된 뉴스 기사 생성이 쉽지 않았음.
#### -> Time지에서 크롤링한 뉴스 기사의 제목을 활용하여 해당 제목에 맞게 가짜 뉴스를 생성해달라고 프롬포팅실시 
#### -> 단, 기존과 동일한 기사 제목을 가지고  News생성시 기사 원문에 너무 똑같아질 것을 고려하여 기존의 뉴스제목을 참고하여 제목을 재생성하고 생성된 새로운 기사 제목을 가지고 뉴스기사 본문을 작성하도록 진행 
#### -> Max Token 수를 조정하여 기존에 제공된 Fake/True 뉴스기사와 비슷한 기사 본문 길이를 확보함.
---------------------------------------
#### ■ 생성된 Fake News 샘플 평가 (GPT-4) 
-> Crawling한 News와 생성한 Fake News 구분이 어렵다는 평가 
![image](https://github.com/RVUP-P/fake_news_detect/assets/101576044/6ee148af-64c1-46b9-81b8-a81d7f25eae0)


#### ■ 기존에 제공된 Fake News 샘플 평가 (GPT-4) 
-> Fake News가 가짜 같다는 평가 
![image](https://github.com/RVUP-P/Fake_News_Detection/assets/101576044/6e2b2c41-6ab1-46b0-95f3-b33818f7a50e)




#### ■ 추가 API
#### API 사용료 : 8.59$
#### API 호출 : 11988 , 사용 Token : 4,474,000 
![image](https://github.com/RVUP-P/fake_news_detect/assets/101576044/38555fd2-c857-49c0-8fb6-10bb112cb0c7)
![image](https://github.com/RVUP-P/fake_news_detect/assets/101576044/97fcee81-25b5-45be-964c-2602b9297ad0)



