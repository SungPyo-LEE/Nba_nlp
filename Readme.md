## NBA 팀의 뉴스를 긁어서 자연어처리를 해보자.

1. NBA 각 팀의 Playoff 진출에 대해 언론을 통해 유사도를 구해보자.
2. Team_name <-> playoff 긍정인지, 부정인지 도출 해보자.

3. 방향이 바뀌었다.. 뉴스데이터에 가장 많이 이용하는 LDA 모델을 적용하여 각 토픽과 문서 분류를 해보자.

## 데이터 수집

1. 셀레니움으로 URL을 수집하고, Requests 라이브러리를 이용하여 뉴스 텍스트 데이터 수집.

## Training Model

1. LDA Training Model 이용

2. 핵심 토픽들 분류

3. 문서 분류 해보기

## 결과

(0, '0.027*"goal" + 0.025*"field" + 0.023*"percent" + 0.023*"defense"')
(1, '0.061*"privacy" + 0.047*"center" + 0.045*"warnermedia" + 0.028*"data"')
(2, '0.038*"odds" + 0.020*"article" + 0.017*"access" + 0.016*"blazers"')
(3, '0.021*"report" + 0.018*"contact" + 0.015*"standing" + 0.013*"friend"')
(4, '0.048*"rebotes" + 0.042*"asistencias" + 0.041*"puntos" + 0.027*"news"')
(5, '0.031*"sports" + 0.031*"black" + 0.022*"betting" + 0.014*"basketball"')
(6, '0.026*"thunder" + 0.023*"alexander" + 0.023*"gilgeous" + 0.016*"game"')
(7, '0.057*"nuggets" + 0.048*"thunder" + 0.034*"denver" + 0.028*"oklahoma"')
(8, '0.024*"wanted" + 0.022*"good" + 0.019*"said" + 0.018*"like"')
(9, '0.020*"left" + 0.017*"double" + 0.016*"durant" + 0.015*"kevin"')
(10, '0.034*"trade" + 0.025*"oklahoma" + 0.024*"city" + 0.022*"thunder"')
(11, '0.022*"avec" + 0.020*"drain" + 0.017*"adsbygoogle" + 0.016*"width"')
(12, '0.072*"warriors" + 0.026*"love" + 0.026*"bryant" + 0.026*"durant"')
(13, '0.055*"thunder" + 0.031*"city" + 0.028*"oklahoma" + 0.017*"quarter"')
(14, '0.062*"life" + 0.048*"twitter" + 0.035*"blowout" + 0.029*"critics"')
(15, '0.059*"cuarto" + 0.040*"marcador" + 0.039*"parcial" + 0.025*"resultado"')
(16, '0.045*"thunder" + 0.034*"oklahoma" + 0.032*"city" + 0.019*"spurs"')
(17, '0.018*"gallinari" + 0.012*"twitter" + 0.010*"doncic" + 0.010*"last"')
(18, '0.047*"points" + 0.027*"thunder" + 0.027*"game" + 0.027*"season"')
(19, '0.023*"history" + 0.018*"timberwolves" + 0.017*"january" + 0.015*"ahora"')

<h2> 현재 OKC의 트루에이스 길져스 알렉산더가 굉장히 높은 토픽을 가지고 있는 것을 확인 할 수 있다.  </h2>
<h2> 그 밖에도 듀란트가 자주 언급되는데 웨스트브룩이나 폴 조지는 자주 언급이 안 되나보다... </h2>

## 아쉬운 점.
당초 목적과 달라진 방향으로 작성하였지만, 재밌는 프로젝트였던 것 같다. 

각 팀별 뉴스를 정리한다던가, 얻는 뉴스데이터의 양을 늘리는 것도 좋은 경험이 될 것 같다!
 