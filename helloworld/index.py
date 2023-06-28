# -*- coding: utf8 -*-
import json
import requests
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.scf.v20180416 import scf_client, models

def main(event, context):
    try:
        body = event['body']
        if isinstance(body, str):
            body = json.loads(body)
            body = json.loads(body)
        action = body['action']

        if action == 'register':
            # 实现用户注册功能
            return "register success..."

        elif action == 'login':
            # 实现用户登录功能
            return "login success..."

        elif action == 'update_profile':
            # 实现个人信息更新功能
            return "update_profile success..."

        elif action == 'list_users':
            # 实现用户列表功能
            return ["1", "2", "3"]

        elif action == 'approve_permission':
            # 实现用户权限审批功能
            response = requests.get("https://api.apiopen.top/api/sentences")
            data = json.loads(response.text)
            sentences = data['result']
            # for sentence in sentences:
            #     print(sentence['english'])
            # return "approve_permission success..."
            return sentences

        elif action == 'log_user_action':
            # 实现用户行为日志功能
            return "logs..."

        elif action == 'get_image':
            response = requests.get("https://api.apiopen.top/api/getImages")
            data = json.loads(response.text)
            print("data:", data)
            sentences = data["result"]
            return sentences

        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Invalid action'})
            }

    except TencentCloudSDKException as err:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f'TencentCloudSDKException: {err}'})
        }

    except Exception as err:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f'Unknown error: {err}'})
        }