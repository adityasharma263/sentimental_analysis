from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from mychatbot.constant.response_obj import ReturnObj
from textblob import TextBlob



@api_view(['GET'])
def hello(request):
    return render(request, 'chat.html', {'form': "form"})


@api_view(['POST'])
@parser_classes((JSONParser,))
def ask(request):
    testimonial = TextBlob(request.data['messageText'])
    no = testimonial.sentiment.polarity
    if no >= 0:
        bot_response = "happy"
    elif no < 0:
        bot_response = "sad"
    return_obj = ReturnObj.ret(200)
    return_obj['content']['answer'] = bot_response
    return Response(data=return_obj['content'], status=return_obj['status'])

