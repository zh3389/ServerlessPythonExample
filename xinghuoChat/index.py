# pip install urllib3==1.26.15 -t .
# pip install spark_ai_python -t .
import json
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage

# 星火认知大模型Spark3.5 Max的URL值
SPARKAI_URL = 'wss://spark-api.xf-yun.com/v3.5/chat'
# 星火认知大模型调用秘钥信息
SPARKAI_APP_ID = ''
SPARKAI_API_SECRET = ''
SPARKAI_API_KEY = ''
# 星火认知大模型Spark3.5 Max的domain值
SPARKAI_DOMAIN = 'general'


def main_handler(event, context):
    # 从事件中提取消息内容
    user_message = event.get('message')

    # 初始化 Spark 模型
    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )

    # 构建消息并生成响应
    messages = [ChatMessage(
        role="user",
        content=user_message
    )]
    handler = ChunkPrintHandler()
    response = spark.generate([messages], callbacks=[handler])
    result = spark.generate([messages], callbacks=[handler])
    return {
        'statusCode': 200,
        'body': result.generations[0][0].text
    }


print(main_handler({"message": "你好！"}, None))
