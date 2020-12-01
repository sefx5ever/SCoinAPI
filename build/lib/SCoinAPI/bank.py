from .retailer import *

class Bank(Retailer):
    @print_msg
    def create_did(self,name:str,password:str,
                    method:str='light',l:str=None,
                    description='',
                    pub_key:str=''):
        """
        説明:注冊 did 帳號

        變數:
            name        : str        : 設定 did / 登錄使用
            l           : str(None)  : 設定 IOTA API 鏈接，若需切換其它鏈接，可只針對function進行輸入
            password    : str        : 設定帳號密碼
            method      : str(light) : 固定變數
            description : any        : 設定更多相關説明
            pub_key     : str('')    : 若有自訂 RSA hash 可進行設定
        """
        l = self.l if l == None else l
            
        headers = { 
            "Content-Type" : "application/json" , 
            "X-API-key" : password
        }

        data = super().return_json(
            method = method,
            name = name, 
            description = description, 
            pub_key = pub_key
        )
        
        try:
            res = requests.post(l + 'new_did',headers=headers,data=data)
            if res.status_code == 200:
                return super().return_dict(status=True,res_data=res.text,msg='Sign up successfully!')
            elif res.status_code == 409: msg = 'Did was existed!'
            elif res.status_code == 400: msg = 'Invalid format!'
            else: msg = res.text
        except Exception as e: msg = e
        return super().return_dict(status=False,msg=msg)

    @print_msg
    def get_did(self,hash_:str,l:str=None):
        """
        説明:透過帳號 Hash 值獲取帳號内容

        變數:
            hash_ : str       : 設定帳號 Hash 值
            l     : str(None) : 設定 IOTA API 鏈接，若需切換其它鏈接，可只針對function進行輸入
        """
        l = self.l if l == None else l
            
        payload = {
            'hash' : hash_
        }
        
        try:
            res = requests.get(l + 'did',params=payload)
            if res.text != '':
                return super().return_dict(status=True,
                    res_data=json.loads(res.text),msg='Get hash data successfully!')
            else: msg = 'Did not found!'
        except Exception as e: msg = e
        return super().return_dict(status=False,msg=e)

    @print_msg
    def verify_token(self,name:str,password:str,
                    token:str,l:str=None):
        """
        説明:驗證 token 是否為自身 token

        變數:
            password : str         : 設定帳號密碼
            name     : str         : 設定帳號 did
            token    : str         : 需被驗證的 token 之 Hash 值            
            l        : str(None)   : 設定 IOTA API 鏈接，若需切換其它鏈接，可只針對function進行輸入
        """
        l = self.l if l == None else l
            
        headers = { 
            'Content-Type' : 'application/json', 
            'X-API-key' : password 
        }
        
        data = super().return_json(
            user = name,
            token = token
        )
        
        try:
            res = requests.post(l + 'verify_token',headers=headers,data=data)
            if res.status_code == 200:
                return super().return_dict(status=True,msg='Token valid!')
            elif res.status_code == 403: msg = 'Permission deny!'
            elif res.status_code == 400: msg = 'Token invalid!'
            else: msg = 'Function error!'
        except: msg = 'Requests error!'
        return super().return_dict(status=False,msg=msg)
