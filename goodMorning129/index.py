# -*- coding: utf8 -*-
import csv
import random

def main_handler(event, context):
    # 读取CSV文件
    with open("goldenSentence.csv", newline='', encoding='utf-8') as csvfile:
        reader = list(csv.DictReader(csvfile))
        # 获取CSV文件的行数
        num_rows = len(reader)
        # 随机生成一个索引
        random_index = random.randint(0, num_rows - 1)
        # 获取对应索引的文本行
        random_text = reader[random_index]["sentence"]
        return {"content": random_text}
