# fake_news_detect
---------------------------------------
### 2024 한양대 정보공학
### 인공지능1 정철현교수님 
### 고현주(6817), 이신영(6644), 전민규(4475), 조일경(4239)

---------------------------------------

### ■■ 기본 모델 
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

### ■■ 성능 개선 시도별 ACC

#### 1.기존 모델
#### Model Accuracy :  0.9582397844634036
#### True Positives (TP): 1042
#### False Positives (FP): 31

#### 2.Functional API로 모델 정의 + Keras의 attention 레이어 사용
#### Model Accuracy :  0.9582397844634036
True Positives (TP): 1041
False Positives (FP): 30

#### 3.Sequential API로 모델 정의 + 직접 정의한 SelfAttention 클래스 사용
Model Accuracy :  0.9568926807364168
True Positives (TP): 1041
False Positives (FP): 33

#### 4.Functional API로 모델 정의 + Keras의 attention 레이어 사용 + 전처리
Model Accuracy :  0.9164795689268074
True Positives (TP): 927
False Positives (FP): 9

#### 5.Sequential API로 모델 정의 + 직접 정의한 SelfAttention 클래스 사용 + 전처리
Model Accuracy :  0.9218679838347553
True Positives (TP): 948
False Positives (FP): 18

---------------------------------------

### ■■ 추가 데이터 셋 구성 
#### 기본 제공 데이터 셋 
#### Fake & True : 44898 row 
#### Crawling(time) & Generated News(GPT3.5) : 11133 row 

Fake 분포
![image](https://github.com/RVUP-P/fake_news_detect/assets/101576044/21fbb6f3-f1ef-464d-bbbe-34ec588cae69)
True 분포
![image](https://github.com/RVUP-P/fake_news_detect/assets/101576044/17b61f9d-d88f-428e-a680-5cbe79778e44)




