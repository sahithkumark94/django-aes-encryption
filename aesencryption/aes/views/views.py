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

@csrf_exempt
@api_view(['POST'])
def encryt(request):
    try:
        error_msg = "Failed to fetch details"
        request_body = JSONParser().parse(request)
        cipher_text = Decryption(request_body).decrypt()
        convert_data = responseFormat(status.HTTP_200_OK, "Successful Encrypted the details", "", cipher_text)
        masked = Encrypt(convert_data).encrypt()
        return JsonResponse(masked, safe=False, status=200)
    except Exception as e:
        error = responseFormat(status.HTTP_500_INTERNAL_SERVER_ERROR, error_msg, str(e), "")
        masked = Encrypt(error).encrypt()
        return JsonResponse(masked, safe=False, status=500)
    
@csrf_exempt
@api_view(['POST'])
def decrypt(request):
    try:
        error_msg = "Failed to fetch details"
        request_body = JSONParser().parse(request)
        plain_text = Decryption(request_body['request']).decrypt()
        convert_data = responseFormat(status.HTTP_200_OK, "Successful Encrypted the details", "", plain_text)
        masked = Encrypt(convert_data).encrypt()
        return JsonResponse(masked, safe=False, status=200)
    except Exception as e:
        error = responseFormat(status.HTTP_500_INTERNAL_SERVER_ERROR, error_msg, str(e), "")
        masked = Encrypt(error).encrypt()
        return JsonResponse(masked, safe=False, status=500)