**Django RestFramework PaycomUz** 
![alt text](https://i.imgur.com/bmVCvl8.jpg)

````
pip install django
pip install djangorestframework
pip install PaycomUz 
````
**settings.py**

````
INSTALLED_APPS = [
    'rest_framework`,
    'PaycomUz`
]
````

**python manage.py migrate**

````
PAYCOM_SETTINGS = {
    "HOST":"https://checkout.test.paycom.uz/api",   #test host
    "ID":"qwertt12345",          #token
    "SECRET_KEY":"wertyu234567",  #password
    "PATH_CLASS":"apps.order.views" #Paycom class ,
    "ACCOUNTS":{
        "KEY1":"order_id",
        "KEY2":None #or "type"
    }
}

````


````
from PaycomUz.methods_subscribe_api import Subcribe

token = 'paycom token'
data = Subcribe(token=token,order_id=1,amount=5000.00,order_type='order').receipts_create()
print(data)

>>> {'transaction_id': '5c42fb5ae3331dc358f3afef', 'paid': True, 'status': 'success', 'error': None}
or
>>> {'transaction_id': 'error_response14', 'paid': False, 'status': 'failed', 'error': {'jsonrpc': '2.0', 'id': 123, 'error': {'code': -31700, 'id': 138, 'message': 'З
аказ не найден', 'origin': 'merchants.checkPerformTransaction'}}}

````

