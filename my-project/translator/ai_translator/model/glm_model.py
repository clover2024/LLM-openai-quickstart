import requests
import simplejson

from model import Model
from zhipuai import ZhipuAI

class GLMModel(Model):
    def __init__(self, model: str, key: str):
        self.model = model
        self.client = ZhipuAI(api_key=key)

    def make_request(self, prompt):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            translation = response.choices[0].message.content.strip()
            return translation, True
        except Exception as e:
            raise Exception(f"发生了未知错误：{e}")
        return "", False
