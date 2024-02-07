import json
import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from requests.auth import HTTPBasicAuth

from .credentials import MpesaAccessToken, LipanaMpesaPpassword



def home(request):
    return render(request, 'home.html', {'navbar': 'home'})

def token(request):
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    try:
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
        r.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        mpesa_access_token = json.loads(r.text)
        validated_mpesa_access_token = mpesa_access_token["access_token"]
        MpesaAccessToken.validated_mpesa_access_token = validated_mpesa_access_token
        return render(request, 'token.html', {"token": validated_mpesa_access_token})

    except requests.exceptions.RequestException as e:
        # Log the error or handle it as needed
        print(f"Error obtaining access token: {e}")
        return JsonResponse({"error": "Failed to obtain access token"}, status=500)
def pay(request):
    access_token_instance = MpesaAccessToken()
    lipa_password_instance = LipanaMpesaPpassword()

    if request.method == "POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = access_token_instance.get_access_token()
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request_data = {
            "BusinessShortCode": lipa_password_instance.Business_short_code,
            "Password": lipa_password_instance.decode_password,
            "Timestamp": lipa_password_instance.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": lipa_password_instance.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Sila",
            "TransactionDesc": "Web Development Charges"
        }

        response = requests.post(api_url, json=request_data, headers=headers)
        return HttpResponse("success")

def mpesaapp(request):
    return render(request, 'pay.html', {'navbar': 'mpesaapp'})

#
# import json
#
# import requests
# from django.http import HttpResponse
# from django.shortcuts import render
# from requests.auth import HTTPBasicAuth
#
# from .credentials import MpesaAccessToken, LipanaMpesaPpassword
#
#
# def home(request):
#     return render(request, 'home.html', {'navbar': 'home'})
#
#
# def token(request):
#     consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
#     consumer_secret = 'viM8ejHgtEmtPTHd'
#     api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
#
#     r = requests.get(api_URL, auth=HTTPBasicAuth(
#         consumer_key, consumer_secret))
#     mpesa_access_token = json.loads(r.text)
#     validated_mpesa_access_token = mpesa_access_token["access_token"]
#
#     return render(request, 'token.html', {"token": validated_mpesa_access_token})
#
#
# def pay(request):
#     global api_url, headers
#     if request.method == "POST":
#         phone = request.POST['phone']
#         amount = request.POST['amount']
#         access_token = MpesaAccessToken.validated_mpesa_access_token
#         api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
#         headers = {"Authorization": "Bearer %s" % access_token}
#         request = {
#             "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
#             "Password": LipanaMpesaPpassword.decode_password,
#             "Timestamp": LipanaMpesaPpassword.lipa_time,
#             "TransactionType": "CustomerPayBillOnline",
#             "Amount": amount,
#             "PartyA": phone,
#             "PartyB": LipanaMpesaPpassword.Business_short_code,
#             "PhoneNumber": phone,
#             "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
#             "AccountReference": "Sila",
#             "TransactionDesc": "Web Development Charges"
#         }
#
#     response = requests.post(api_url, json=request, headers=headers)
#     return HttpResponse("success")
#
#
# def mpesaapp(request):
#     return render(request, 'pay.html', {'navbar': 'mpesaapp'})