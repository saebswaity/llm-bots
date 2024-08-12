
import boto3
import json
from abc import ABC, abstractmethod

class LLM(ABC):
    @abstractmethod
    def get_response(self, message):
        pass

class TitanLLM(LLM):
    def __init__(self, region_name='us-west-2'):
        self.bedrock = boto3.client(
            service_name='bedrock-runtime',
            region_name=region_name
        )
        self.model_id = "amazon.titan-text-express-v1"

    def get_response(self, message):
        body = json.dumps({
            "inputText": message,
            "textGenerationConfig": {
                "maxTokenCount": 8192,
                "stopSequences": [],
                "temperature": 0,
                "topP": 1
            }
        })

        response = self.bedrock.invoke_model(
            modelId=self.model_id,
            contentType="application/json",
            accept="application/json",
            body=body
        )

        response_body = json.loads(response['body'].read())
        return response_body['results'][0]['outputText']
    



# File: llm.py

import boto3
import json
from abc import ABC, abstractmethod

class LLM(ABC):
    @abstractmethod
    def get_response(self, message):
        pass

class TitanLLM(LLM):
    def __init__(self, region_name='us-west-2'):
        self.bedrock = boto3.client(
            service_name='bedrock-runtime',
            region_name=region_name
        )
        self.model_id = "amazon.titan-text-express-v1"

    def get_response(self, message):
        body = json.dumps({
            "inputText": message,
            "textGenerationConfig": {
                "maxTokenCount": 8192,
                "stopSequences": [],
                "temperature": 0,
                "topP": 1
            }
        })

        response = self.bedrock.invoke_model(
            modelId=self.model_id,
            contentType="application/json",
            accept="application/json",
            body=body
        )

        response_body = json.loads(response['body'].read())
        return response_body['results'][0]['outputText']

class CohereCommandLLM(LLM):
    def __init__(self, region_name='us-west-2'):
        self.bedrock = boto3.client(
            service_name='bedrock-runtime',
            region_name=region_name
        )
        self.model_id = "cohere.command-r-v1:0"

    def get_response(self, message, chat_history=None):
        if chat_history is None:
            chat_history = []

        body = {
            "chat_history": chat_history,
            "message": message,
            "temperature": 0.7,
            "p": 0.7,
            "k": 0,
            "max_tokens": 300,
            "stop_sequences": []
        }

        response = self.bedrock.invoke_model(
            modelId=self.model_id,
            contentType="application/json",
            accept="application/json",
            body=json.dumps(body)
        )

        response_body = json.loads(response['body'].read())
        print("Full response:", response_body)  # For debugging

        return response_body['text']