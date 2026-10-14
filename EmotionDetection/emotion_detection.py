"""
This module takes text and returns what emotions the text conveys
as well as highlighting the most dominant one.
"""
import requests
import json


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input_obj, headers=headers)
    
    # If empty response
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            "dominant_emotion": None
        }

    # Parse response
    json_response = json.loads(response.text)

    # Get the emotion scores
    formatted_response = json_response['emotionPredictions'][0]['emotion']

    # find dominant emotion
    dominant_emotion = max(formatted_response, key=formatted_response.get)
    formatted_response['dominant_emotion'] = dominant_emotion
    return formatted_response
