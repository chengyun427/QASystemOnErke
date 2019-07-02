# from pyspark import SparkContext
# import os
# import sys
# os.environ['SPARK_HOME'] = "C:\\Spark"
# os.environ['JAVA_HOME'] = "C:\\Program Files\\Java\\jdk1.8.0_191"
# os.environ["PYSPARK_PYTHON"]="D:\\Anaconda3\\envs\\tensorflow\\python.exe"
#
#
# sys.path.append("C:\\Spark\\python")
# sys.path.append("C:\\Spark\\python\\lib\\py4j-0.10.7-src.zip")
#
# sc = SparkContext('local')
# doc = sc.parallelize([['a','b','c'],['b','d','d']])
# words = doc.flatMap(lambda d:d).distinct().collect()
# word_dict = {w:i for w,i in zip(words,range(len(words)))}
# word_dict_b = sc.broadcast(word_dict)
#
# def wordCountPerDoc(d):
#     dict={}
#     wd = word_dict_b.value
#     for w in d:
#         if wd[w] in dict:
#             dict[wd[w]] +=1
#         else:
#             dict[wd[w]] = 1
#     return dict
# print(doc.map(wordCountPerDoc).collect())
# print("successful")







# 测试neo4j连接
from py2neo import Graph, Node, Relationship, NodeMatcher

graph = Graph(
            # host="127.0.0.1",  # neo4j 搭载服务器的ip地址，ifconfig可获取到
            # http_port=7474,  # neo4j 服务器监听的端口号
            "http://127.0.0.1:7474",
            username="neo4j",  # 数据库user name，如果没有更改过，应该是neo4j
            password="123456")
node = Node("Test_Class",name='姚明董事长',id='0001',age=65,location='上海')
graph.create(node)
