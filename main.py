import jieba
import random

with open('answer.txt', 'r', encoding="utf-8") as f:
 answer = f.read().split("\n")

with open('Time.txt', 'r', encoding="utf-8") as f:
 Time = f.read().split("\n")
 startTime=Time[0:len(Time)-1]
 endTime=Time[1:]

for answer,startTime,endTime in zip(answer,startTime,endTime):

 seg_list = list(jieba.cut(answer, cut_all=False))
 print("{")
 print('"text": "",')
 print('"answer": '+'"'+answer+'",')
 print('"choices": '+str(random.sample(seg_list,len(seg_list)))+',')
 print('"startTime":'+str(startTime)+',')
 print('"endTime":'+str(endTime)+',')
 print('},')