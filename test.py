from src import centralbank

bk = centralbank.Central_Bank()
# res = bk.send_token('nUjymFTzrJcuqizbswdKACJtpRwMZtEkwXzQDxBk','cb','sefx2ever',2)
res = bk.get_balance('sefx2ever')
print(res)