import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64

class MpesaC2BCredential:
    consumer_key = '39agA5hvaAnQz2FKSY16Gi8XoFkyApaT'
    consumer_secret = '8TQzhIKAWtQshAoc'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    def __init__(self):
        self.access_token = None

    def get_access_token(self):
        # Return the stored access token
        return self.access_token

    def set_access_token(self, access_token):
        # Set the access token
        self.access_token = access_token
def token(request):
        try:
            r = requests.get(MpesaC2BCredential.api_URL,
                             auth=HTTPBasicAuth(MpesaC2BCredential.consumer_key, MpesaC2BCredential.consumer_secret))
            r.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
            response_data = json.loads(r.text)
            # access_token_instance.set_access_token(validated_mpesa_access_token)
            #
            # return render(request, 'token.html', {"token": validated_mpesa_access_token})
            self.access_token = response_data.get("access_token")
        except requests.exceptions.RequestException as e:
            print(f"Error obtaining access token: {e}")

class LipanaMpesaPpassword:
    Business_short_code = "174379"
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    def __init__(self):
        self.generate_online_password()

    def generate_online_password(self):
        lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
        business_short_code = "174379"
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

        data_to_encode = business_short_code + passkey + lipa_time

        online_password = base64.b64encode(data_to_encode.encode())
        self.decode_password = online_password.decode('utf-8')

# import requests
# import json
# from requests.auth import HTTPBasicAuth
# from datetime import datetime
# import base64
#
#
# class MpesaC2bCredential:
#     consumer_key = '39agA5hvaAnQz2FKSY16Gi8XoFkyApaT'
#     consumer_secret = '8TQzhIKAWtQshAoc'
#     api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
#
#
# class MpesaAccessToken:
#     def __init__(self):
#         self.get_access_token()
#
#     def get_access_token(self):
#         try:
#             r = requests.get(MpesaC2bCredential.api_URL,
#                              auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
#             r.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
#             MpesaAccessToken = json.loads(r.text)
#             self.validated_mpesa_access_token = MpesaAccessToken["access_token"]
#         except requests.exceptions.RequestException as e:
#             print(f"Error obtaining access token: {e}")
#
#
# class LipanaMpesaPpassword:
#     def __init__(self):
#         self.generate_online_password()
#
#     def generate_online_password(self):
#         lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
#         Business_short_code = "174379"
#         OffSetValue = '0'
#         passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
#
#         data_to_encode = Business_short_code + passkey + lipa_time
#
#         online_password = base64.b64encode(data_to_encode.encode())
#         self.decode_password = online_password.decode('utf-8')
