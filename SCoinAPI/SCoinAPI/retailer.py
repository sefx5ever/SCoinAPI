import requests, json

def print_msg(method):
    def wrapper(this,*args):
        action_result = method(this,*args)
        print(f'【{method.__name__}】: {action_result["msg"]}')
        return action_result
    return wrapper

class Retailer:
    def __init__(self,l='http://52.44.57.177:8888/'):
        """
        説明：初始化物件。

        變數：
            l : str（http://52.44.57.177:8888/） : 設定 IOTA API 鏈接
        """
        self.l = l

    @print_msg
    def connection_test(self,l:str=None):
        """
        説明:測試 IOTA API 連綫。

        變數:
            l : str(None) : 設定 IOTA API 鏈接，若需切換其它鏈接，可只針對function進行輸入
        """
        l = self.l if l == None else l
        res = requests.get(l)
        if res.status_code == 200:
            return self.return_dict(status=True,msg='Connection successfully!')
        else:
            return self.return_dict(status=False,msg="Connection failed!")

    @print_msg
    def send_tokens(self,password:str,sen:str,rev:str,
                    num:int,method:str='2',description:str='',
                    l:str=None):
        """
        説明:透過 token 之 Hash 值進行一般轉賬

        變數:
            password    : str         : 設定帳號密碼
            sen         : str         : 設定發送人
            rev         : str         : 設定收款人 
            num         : int         : 需要轉賬數量
            method      : str(2)      : 設定交易類別
            description : str('')     : 設定交易説明
            l           : str(None)   : 設定 IOTA API 鏈接，若需切換其它鏈接，可只針對function進行輸入
        """
        l = self.l if l == None else l

        headers = {
            'Content-Type' : 'application/json', 
            'X-API-key' : password 
        }

        sen_data = self.get_balance(sen)
        if sen_data['status'] == True:
            token_list = sen_data['res_data']['token']
            if (token_list[0] == '') | (sen_data['res_data']['count'] < num):
                return self.return_dict(status=False)

        try:
            data = self.return_json(
                sen = sen,
                rev = rev,
                method = method,
                description = description,
                txn = token_list[:num] 
            )
            res = requests.post(l + 'send_tokens',headers = headers,data = data)
            print(res.text)
            if res.status_code == 200:
                return self.return_dict(status=True,res_data=res.text.split('\n'),msg='Transaction complete!')
            elif res.status_code == 404: msg = 'Sendor and Receiver does not exist!'
            elif res.status_code == 403: msg = 'Permission deny!'
            else: msg = 'Function error!'
        except Exception as e: msg = e  
        return self.return_dict(status=False,msg=msg)

    @print_msg
    def get_balance(self,name:str,l:str=None):
        """
        説明:透過帳號 did 獲取帳號 token 内容

        變數:
            name : str       : 設定帳號 did
            l    : str(None) : 設定 IOTA API 鏈接，若需切換其它鏈接，可只針對function進行輸入
        """
        l = self.l if l == None else l
        payload = self.return_dict(user=name)
        
        try:
            res = requests.get(l + 'get_balance',params=payload)
            if res.status_code == 200:
                token = res.text.split()
                return self.return_dict(
                    status=True,
                    res_data=self.return_dict(
                        status = True,
                        name = name,
                        token = token,
                        count = len(token)
                    ),
                    msg='Get balance successfully!'
                )
            else: msg = 'Page not found!'
        except Exception as e: msg = e
        return self.return_dict(status=False,msg=msg)

# ========== Tool Method ===============
    def return_dict(self,**kwargs):
        return kwargs

    def return_json(self,**kwargs):
        return json.dumps(kwargs)
# ========== Tool Method ===============
