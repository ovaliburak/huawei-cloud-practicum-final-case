import requests
from .apig_sdk import signer


def modelart(image_path): 
    
    url = "https://f7bcf3d99ed24c4cbb2b30f352011bc6.apig.ap-southeast-3.huaweicloudapis.com/v1/infers/bfcd1827-fe76-4b97-8bbc-3e7a2351d559"
    ak = "YDX1Q5UVCGBAT569F9BW"
    sk = "FjWHYbtVuieQRxu6rpu2cISNyyw3ZKuQx2QrAUpA"
    
    method = 'POST'
    headers = {"x-sdk-content-sha256": "UNSIGNED-PAYLOAD"}
    request = signer.HttpRequest(method, url, headers)
    
    sig = signer.Signer()
    sig.Key = ak
    sig.Secret = sk
    sig.Sign(request)
    files = {'images': image_path}
    resp = requests.request(request.method, request.scheme + "://" + request.host + request.uri, headers=request.headers, files=files)
    
    
    return resp.text
    
