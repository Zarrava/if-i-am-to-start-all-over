import webbrowser
import msal
from msal import PublicClientApplication
APPLICATION_ID = 'ebabf750-2860-4b34-b77a-748f7c890f0d'
CLIENT_SECRET = 'tnk8Q~2MHXXfFaDskfUWrVdsPvw4iNTy~IENbcm3'
authority_url = 'https://login.microsoftonline.com/consumers/'
base_url = 'https://graph.microsoft.com/v1.0/me'

endpoint = base_url + 'me'
SCOPES = ['User.Read', 'User.Export.All']

client_instance = msal.ConfidentialClientApplication(
    client_id=APPLICATION_ID,
    client_credential=CLIENT_SECRET,
    authority=authority_url
)   
