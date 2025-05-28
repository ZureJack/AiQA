import requests
import log
# # 发送请求
# x = requests.get('https://www.runoob.com/')

# # 返回 http 的状态码
# print(x.status_code)

# # 响应状态的描述
# print(x.reason)

# # 返回编码
# print(x.apparent_encoding)



class ZAi:
    def __init__(self, api_url:str, api_key:str, model:str, logfilename='./txt.log'):
        self.api_url = api_url
        self.api_key = api_key
        self.model = model
        self.log = log.Log(logfilename, 'zAi')

    def post(self, content:str, max_tokens: int = 1000):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": f"{self.model}",
            "messages": [
                {"role": "user", "content": f"{content}"}
            ],
            "max_tokens": max_tokens
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=data)

            self.log.debug(f"http response: {response.content}")
            if response.ok:
                self.log.info("http request success.")
                return response.json()["choices"][0]["message"]["content"]
            else:
                self.log.warning(f"http request failed! state: {response.status_code}")
        except Exception as e:
            self.log.error(f"http request exception! {e}")
            