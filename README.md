# Aggressive-Driving-Detection-Using-SUMO

## Introduction
SUMO를 이용한 공격 차량 탐지 시스템

8차선 왕복도로로 구성되며 각 도로에는 정상 주행 차량과 공격 운전 차량들이 함께 주행한다. 

공격 운전 차량에는 과속차량과 잦은 차선변경을 하는 차량들이 있다.

공격 운전 차량들을 쉽게 구분하기 위하여 붉은색으로 나타냈으며 정상 주행 차량들의 경우 초록색으로 나타내었다.

과속 차량의 경우 vType 태그의 maxSpeed 옵션을 정상 주행 차량들에 비해서 높게 설정하였고 차선 변경 차량의 경우 lcPushy 옵션값을 1로 설정하여 잦은 차선변경을 수행하도록 하였다.
## RUN SUMO
```bash
netconvert -c cloud.netccfg
python3 exe_sumo.py
```


## SUMO를 이용한 공격 차량 탐지 예시
- ### 과속 차량 탐지 예시
<img width="80%" src="https://github.com/jyk122121/Aggressive-Driving-Detection-Using-SUMO/assets/97593741/63b348c2-8287-4bcc-955a-bdd4a810c1ec" />


- ### 잦은 차선변경 차량 탐지 예시
<img width="80%" src="https://github.com/jyk122121/Aggressive-Driving-Detection-Using-SUMO/assets/97593741/5356bc21-78fa-4410-9a1f-e0174a08c90f" />
