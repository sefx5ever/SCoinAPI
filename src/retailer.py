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
    def send_token(self,password:str,sen:str,rev:str,
                    num:int,layer:str,method:str='1',
                    description="",l:str=None):
        """
        説明:透過 token 之 Hash 值進行轉賬

        變數:
            layer       : str         : 設定 SCoin 體系之層級
            password    : str         : 設定帳號密碼
            sen         : str         : 設定發送人
            rev         : str         : 設定收款人 
            num         : int         : 需要轉賬數量
            method      : str(1)      : 設定交易類別
            description : any         : 設定交易説明
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
                return self.return_dict(status=False,msg='Account sender not enough amount!')

        try:
            result = list()
            for txn in token_list[:num]:                
                data = self.return_json(
                    sen = sen,
                    rev = rev,
                    method = layer,
                    description = description,
                    txn = '' if layer == '1' else txn
                )
            
                res = requests.post(l + 'send_token',headers = headers,data = data)
                if res.status_code == 200:
                    progress_rate = (len(result)/num)*100
                    bar_count = progress_rate//10
                    print(f'Transfering({progress_rate}%) : {bar_count*"="}{(10-bar_count)*"*"}')
                    result.append(self.return_dict(
                        sen = sen,
                        rev = rev,
                        new_txn_hash = res.text
                    ))
                    continue
                elif res.status_code == 404: msg = 'Sendor and Receiver does not exist!'
                elif res.status_code == 403: msg = 'Permission deny!'
                else: msg = 'Function error!'
                return self.return_dict(status=False,res_data=result,msg=msg)
            return self.return_dict(status=True,res_data=result,msg='Transaction complete!')
        except Exception as e:     
            return self.return_dict(status=False,msg=e)

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
            token = res.text
            print(token)
            if res.status_code == 200:
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
        return self.return_dict(status=False,msg=e)

# ========== Tool Method ===============
    def return_dict(self,**kwargs):
        return kwargs

    def return_json(self,**kwargs):
        return json.dumps(kwargs)
# ========== Tool Method ===============
