import json
import pytest
from fin_data import app

@pytest.fixture()
def ai_event():
    """ Generates AI Agent Event"""

    return {
        "messageVersion": "1.0",
        "agent": {
            "name": "string",
            "id": "string",
            "alias": "string",
            "version": "string"
        },
        "inputText": "string",
        "sessionId": "string",
        "actionGroup": "string",
        "function": "analyze_industry_performance",
        "parameters": [
            {
            "name": "industry",
            "type": "string",
            "value": "cafes"
            },
            {
            "name": "date_from",
            "type": "string",
            "value": "2024-01-01"
            },
            {
            "name": "date_to",
            "type": "string",
            "value": "2024-06-30"
            }
        ],
        "sessionAttributes": {
            "string": "string"
        },
        "promptSessionAttributes": {
            "string": "string"
        }
    }
    

def test_lambda_handler(ai_event):
    ret = app.lambda_handler(ai_event, "")
    print(ret)

    assert "response" in ret
