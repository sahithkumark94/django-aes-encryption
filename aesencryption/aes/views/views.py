from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from aes.utils.encryption import *
from django.http import HttpResponse
from urllib.parse import quote, unquote

@csrf_exempt
@api_view(['POST'])
def encryt(request):
    try:
        error_msg = "Failed to encrypt the data"
        param = request.GET.get("param")
        cipher_text = Encrypt(param,'text').encrypt()
        convert_data = responseFormat(status.HTTP_200_OK, "Successfully Encrypted the details", "", cipher_text)
        return JsonResponse(convert_data, safe=False, status=200)
    except Exception as e:
        error = responseFormat(status.HTTP_500_INTERNAL_SERVER_ERROR, error_msg, str(e), "")
        return JsonResponse(error, safe=False, status=500)
    
@csrf_exempt
@api_view(['POST'])
def decrypt(request):
    try:
        error_msg = "Failed to decrypt the data"
        request_body = JSONParser().parse(request)
        plain_text = Decryption(request_body['request']).decrypt()
        convert_data = responseFormat(status.HTTP_200_OK, "Successfully Encrypted the details", "", convertToJson(plain_text))
        return JsonResponse(convert_data, safe=False, status=200)
    except Exception as e:
        error = responseFormat(status.HTTP_500_INTERNAL_SERVER_ERROR, error_msg, str(e), "")
        return JsonResponse(error, safe=False, status=500)

@csrf_exempt
@api_view(['GET'])
def encrytUrlParam(request):
    try:
        error_msg = "Failed to encrypt the data"
        param = request.GET.get("param")
        cipher_text = Encrypt(param,'text').encrypt()
        cipher = quote(cipher_text['response'])
        cipher_text['response'] = cipher
        convert_data = responseFormat(status.HTTP_200_OK, "Successfully Encrypted the url param", "", cipher_text)
        return JsonResponse(convert_data, safe=False, status=200)
    except Exception as e:
        error = responseFormat(status.HTTP_500_INTERNAL_SERVER_ERROR, error_msg, str(e), "")
        return JsonResponse(error, safe=False, status=500)

@csrf_exempt
@api_view(['GET'])
def decryptUrlParam(request):
    try:
        error_msg = "Failed to decrypt the data"
        param = request.GET.get("param")
        param = unquote(param)
        plain_text = Decryption(param).decrypt()
        convert_data = responseFormat(status.HTTP_200_OK, "Successfully Encrypted the url param", "", plain_text)
        return JsonResponse(convert_data, safe=False, status=200)
    except Exception as e:
        error = responseFormat(status.HTTP_500_INTERNAL_SERVER_ERROR, error_msg, str(e), "")
        return JsonResponse(error, safe=False, status=500)