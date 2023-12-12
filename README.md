# Aggressive-Driving-Detection-Using-SUMO

## Introduction
SUMO를 이용한 공격 차량 탐지 시스템

8차선 왕복도로로 구성되며 공격 차량은 과속을 하는 차량 그리고 잦은 차선변경을 하는 차량들로 구성된다.

공격 차량들을 쉽게 구분하기 위하여 붉은색으로 나타냈으며 정상 주행 차량들의 경우 초록생으로 나타내었다.

과속 차량의 경우 vType 태그의 maxSpeed 옵션을 정상 주행 차량들에 비해서 높에 설정하였고 차선 변경 차량의 경우 lcPushy옵션 을 1로 설정하였다.
## RUN SUMO
```bash
netconvert -c cloud.netccfg
pyhon3 exe_sumo.py
```


## SUMO를 이용한 공격 차량 탐지 예시
- 과속 차량 탐지 예시


- 잦은 차선변경 차량 탐지 예시
