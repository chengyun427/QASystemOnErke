#!/usr/bin/env python3
# coding: utf-8
# File: chatbot_graph.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-10-4

from question_classifier import *
from question_parser import *
from answer_search import *

'''问答类'''
class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = '您好，我是小勇医药智能助理，希望可以帮到您。祝您身体棒棒！'
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return answer
        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return answer
        else:
            return '\n'.join(final_answers)


if __name__ == '__main__':
    # 导入baiduyuyin识别函数（自己写的）
    import sys
    sys.path.append("..")
    from speech_recognition import baiduyuyin

    # 导入文字转语音相关包
    import pyttsx3
    engine = pyttsx3.init()     # 初始化
    voices = engine.getProperty('voices')


    handler = ChatBotGraph()
    while 1:
        # 1.语音识别，获取用户输入问题
        print('用户：', end='')
        # question = input('用户:')
        question = baiduyuyin.main()
        print(question)

        # 2.判断是否退出问答系统
        if '退出' in question:
            break

        # 3.调用问答系统
        answer = handler.chat_main(question)
        print('小勇:', answer)

        # 4.转语音读出
        engine.say(answer)
        engine.runAndWait()

