# PredictSignLanguage_DNN
## Sign language recognition using LeapMotion, DNN
### 립모션을 활용하여 손동작에 대한 입력 값을 얻고 그 입력값을 학습하여 만든 DNN 모델
1. 립모션을 이용하여 손가락 동작에 대한 반환값을 전처리한다.
##### 립모션을 활용하였을때, 반환되는 값은 총 192개 (반환되는 값은 립모션 공식 홈페이지 참조)
##### -Leapmotion API (https://developerarchive.leapmotion.com/documentation/python/devguide/Leap_Overview.html#hands)
2. 전치리한 결과값을 Python pandas module을 이용하여 csv 파일로 저장한다
3. csv 파일을 학습시킨다.
