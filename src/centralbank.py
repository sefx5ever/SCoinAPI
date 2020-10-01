from bank import Bank, 

class Central_Bank(Bank):
    @print_msg
    def remove_layer1(self,name:str,password:str,l:str=None):
        """
        說明:刪除 did 帳號第一層權限

        變數:
            password : str       : 設定帳號密碼
            name     : str       : 設定帳號 did
            l        : str(None) : 設定 IOTA API 鏈接，若需切換其它鏈接，可只針對function進行輸入
        """
        l = self.l if l == None else l
        data = super().return_json(username=name)
        headers = {
            'Content-Type' : 'application/json', 
            'X-API-key' : password 
        }

        try:
            res = requests.delete(l + 'remove_layer1',header=headers,data=data)
            if res.status_code == 200:
                return super().return_dict(status=True,msg=res.text)
            elif res.status_code == 404: msg = 'User does not exist!'
        except Exception as e: msg = e
        return super().return_dict(status=False,msg=msg)

    @print_msg
    def get_transactions_by_timestamp(self,start_time:int=0,
                        end_time:int=2000000000,l:str=None):
        """
        說明:以 timestamp 查詢時間區間內之交易紀錄。

        變數:
            start_time : int(0)            : 查詢起始時間
            end_time   : int(2000000000)   : 查詢結束時間
        """
        l = self.l if l == None else l
        payload = {
            'start'  :  start_time,
            'end'    :  end_time
        }

        try:
            res = requests.get(l + 'get_transactions_by_timestamp',params=payload)
            if res.status_code == 200:
                return super().return_dict(
                    status = True,
                    res_data = super().return_dict(
                        status = True,
                        data = res.text
                    ),
                    msg='Get transaction successfully!'
                )
            elif res.status_code == 404: msg = 'Page not found!'
        except Exception as e: msg = e
        return super().return_dict(status=False,msg=msg)

    @print_msg
    def get_user_by_timestamp(self,start_time:int=0,
                        end_time:int=2000000000,l:str=None):
        """
        說明:以 timestamp 查詢時間區間內之用戶註冊紀錄。

        變數:
            start_time : int(0)            : 查詢起始時間
            end_time   : int(2000000000)   : 查詢結束時間
        """
        l = self.l if l == None else l
        payload = {
            'start'  :  start_time,
            'end'    :  end_time
        }

        try:
            res = requests.get(l + 'get_user_by_timestamp',params=payload)
            if res.status_code == 200:
                return super().return_dict(
                    status = True,
                    res_data = super().return_dict(
                        status = True,
                        data = res.text
                    ),
                    msg='Get transaction successfully!'
                )
            elif res.status_code == 404: msg = 'Page not found!'
        except Exception as e: msg = e
        return super().return_dict(status=False,msg=msg)

    @print_msg
    def get_info(self,l:str=None):
        """
        說明:獲取目前總註冊人數
        """
        l = self.l if l == None else 

        try:
            res = requests.get(l + 'info')
            if res.status_code == 200:
                return super().return_dict(
                    status = True,
                    res_data = super().return_dict(
                        status = True,
                        total_user = res.text['totalUser']
                    ),
                    msg = 'Get info successfully!'
                )
            elif res.status_code == 404: msg = 'Page not found!'
        except Exception as e: msg = e
        return super().return_dict(status=False,msg=msg)

    @print_msg
    def set_central_bank(self,name:str,password:str,l:str=None):
        """
        説明: 設定 did 帳號為央行權限

        變數:
            password  : str         : 設定帳號密碼
            name      : str         : 設定帳號 did
            l         : str(None) : 設定 IOTA API 鏈接，若需切換其它鏈接，可只針對function進行輸入
        """
        l = self.l if l == None else l
        headers = { 'X-API-key' : password }
        payload = super().return_dict(username = name)
        
        try:
            res = requests.get(l + 'set_layer1',headers=headers,params=payload)
            
            if res.status_code == 200:
                return super().return_dict(status=True,msg='Set central bank successfully!')
            elif res.status_code == 400: msg = 'No such account or account already exist!'
            elif res.status_code == 403: msg = 'Authentication fail!'
            else: msg = 'Function error!'
        except Exception as e: msg = e
        return super().return_dict(status=False,msg=msg)