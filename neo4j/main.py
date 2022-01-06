from py2neo import Graph,Node,Relationship
import csv
import time
import sys
url='localhost'
username='neo4j'
password='password'
graph=Graph(host=url,user=username,password=password)
s0='match (n) delete (n)'
p0=graph.run(s0)
s1='LOAD CSV FROM "file:///datosb2.csv" AS line CREATE (:persona {id: line[0], state: line[1], month: line[2], year: line[3], countyBirths: line[4], stateBirths: line[5], county: line[6]})'
p1=graph.run(s1)
print("csv loaded")
seconds=10
################################################# select simple
start_time=time.time()
i=0
while True:
    s1='match (n:persona) where toInteger(n.id)=1244 return (n)'
    p1=graph.run(s1)
    i=i+1
    elapsed_time=time.time()
    tiempoTranscurrido=elapsed_time-start_time
    if tiempoTranscurrido>seconds:
        print("finished select simple")
        break
tiempo=i/seconds
print(tiempo)
################################################# select complejo
start_time=time.time()
i=0
while True:
    s1='match (n:persona) where toInteger(n.id)=1244 return (n)'
    p1=graph.run(s1)
    
    s2='match (n:persona) where toInteger(n.id)>1244 AND toInteger(n.id)<6000 return (n)'
    p2=graph.run(s2)
    
    s3='match (n:persona) where toInteger(n.id)>1244 AND toInteger(n.id)<6000 return sum(toInteger(n.month))'
    p3=graph.run(s3)
    s4='match (n:persona) where toInteger(n.id)>1244 AND toInteger(n.id)<6000 return (n) order by toInteger(n.month)'
    p4=graph.run(s4)
    i=i+1
    elapsed_time=time.time()
    tiempoTranscurrido=elapsed_time-start_time
    if tiempoTranscurrido>seconds:
        print("finished select complejo")
        break
tiempo=i/seconds
print(tiempo)
################################################# mixto
start_time=time.time()
i=0
while True:
    s1='match (n:persona) where toInteger(n.id)=1244 return (n)'
    p1=graph.run(s1)
    
    s2='match (n:persona) where toInteger(n.id)>1244 AND toInteger(n.id)<6000 return (n)'
    p2=graph.run(s2)
    s3='match (n:persona) where toInteger(n.id)=1244 set n.month=13 return (n)'
    p3=graph.run(s3)
    
    s4='match (n:persona) where toInteger(n.id)=1245 set n.mont=toInteger(n.month)+1 return (n)'
    p4=graph.run(s4)
    
    i=i+1
    elapsed_time=time.time()
    tiempoTranscurrido=elapsed_time-start_time
    if tiempoTranscurrido>seconds:
        print("finished mixto")
        break
tiempo=i/seconds
print(tiempo)
################################################# update
start_time=time.time()
i=0
while True:
    s1='match (n:persona) where toInteger(n.id)=1244 set n.month=13 return (n)'
    p1=graph.run(s1)
    
    s2='match (n:persona) where toInteger(n.id)=1245 set n.mont=toInteger(n.month)+1 return (n)'
    p2=graph.run(s2)
    
    i=i+1
    elapsed_time=time.time()
    tiempoTranscurrido=elapsed_time-start_time
    if tiempoTranscurrido>seconds:
        print("finished update")
        break
tiempo=i/seconds
print(tiempo)
################################################# create
start_time=time.time()
i=0
b=200000
while True:
    s1='create (n:persona{id:'+str(b)+',state:"02",month:"14",year:"2142",countyBirths:"20",stateBirths:"35",county:"52"}) return (n)'
    p1=graph.run(s1)
    b=b+1
    i=i+1
    elapsed_time=time.time()
    tiempoTranscurrido=elapsed_time-start_time
    if tiempoTranscurrido>seconds:
        print("finished update")
        break
tiempo=i/seconds
print(tiempo)
################################################# create
start_time=time.time()
i=0
b=200000
while True:
    s1='match (n:persona) where toInteger(n.id)='+str(b)+' delete (n)'
    p1=graph.run(s1)
    b=b+1
    i=i+1
    elapsed_time=time.time()
    tiempoTranscurrido=elapsed_time-start_time
    if tiempoTranscurrido>seconds:
        print("finished update")
        break
tiempo=i/seconds
print(tiempo)
