import requests
from flask import Flask, request, jsonify, Response
import json

app = Flask(__name__)

@app.route('/<text>', methods=['GET']) 
def send_to_myself(text):

    if text:
        # Kakao API에 요청할 URL
        url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'
        
        # 요청할 Params 설정
        params = {
            'text': text
        }
        
        # Headers 설정 
        headers = {
            'Authorization': 'Bearer 5f3165fa1a23c7da99531fb38a69ce15' 
        }
        
        # API 요청 보내기
        response = requests.post(url, headers=headers, params=params)
        # 응답 처리
        if response.status_code == 200:
            return jsonify({"success": "send message to me"})
        else:
            return response.content
        #jsonify({"error": f"Failed to fetch data from Kakao API, {response.status_code}"})
    else:
        return jsonify({"error": "address_name not provided"}), 400


if __name__ == '__main__':
    app.run(port = 3001, debug=True)
