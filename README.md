# PredictSignLanguage_DNN
## Sign language recognition using LeapMotion, DNN
### Leapmotion을 활용하여 손동작에 대한 입력 값을 얻고 그 입력값을 학습하여 만든 DNN 모델
1. 립모션을 이용하여 손가락 동작에 대한 반환값을 전처리한다.
#####      Leapmotion을 활용하였을때, 반환되는 값은 총 192개 (반환되는 값은 립모션 공식 홈페이지 참조)
##### -Leapmotion API (https://developerarchive.leapmotion.com/documentation/python/devguide/Leap_Overview.html#hands)
2. 전처리한 결과값을 Python pandas module을 이용하여 csv 파일로 저장한다
##### Leapmotion에서 제공하는 sample.py 파일에 내가 필요한 값들을 전처리하여 엑셀 파일로 저장
3. csv 파일을 학습시킨다.
##### tensorflow 모듈을 이용
4. middle_present.py 파일은 학습한 모델을 불러와서 입력한 손동작이 어떠한 손동작인지 알려주는 파일
-----------------------------------------------------------------
### DNN model that obtains input value for hand gesture by using Leapmotion and learns input value
1. Use Leapmotion to preprocess the return value for the finger gesture.
##### When using Leapmotion, the total value returned is 192 (refer to the lip motion official website for the returned value)
##### -Leapmotion API (https://developerarchive.leapmotion.com/documentation/python/devguide/Leap_Overview.html#hands)
2. Save the preprocessed result as csv file using Python pandas module
##### Pre-process the values in the sample.py file provided by Leapmotion and save it as an Excel file
3. Train the csv file.
##### Using Tensorflow Module
4. The middle_present.py file is a file that imports the trained model and tells what type of hand gestures are entered.
