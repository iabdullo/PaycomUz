![alt text](https://i.imgur.com/bmVCvl8.jpg)

# ✈️ Ishni boshlash

````
pip install django
pip install djangorestframework
pip install PaycomUz 
pip install requests
````

**settings.py**

````
INSTALLED_APPS = [
    'rest_framework`,
    'PaycomUz`
]
````

**python manage.py migrate**

# ⚙️ To'lovlarni sozlash
Tolovlarni amalga oshirish uchun sizda **Paycom** classi bolishi kerak u qanday yoziladi va nega kerak!
**Paycom** classi buyurtma bor yoki yoligi yoki narxini tekwirib javob qaytarish uchun kerak!
mana pasda qanday yozilishi xudi wunday yozilishi kerak **Paycom** classni ichida check_order funksiyasi bolishi kerak u buyurtma bor yoki yoligini tekshirb beradi va return qilb javob yuboradi.


````
from PaycomUz.status import ORDER_FOUND,ORDER_NOT_FOUND,INVALID_AMOUNT

class Paycom:
    def __init__(self,order_id=None,order_type=None,amount=None):
        self.order_id = None  #buyurtmaning raqami
        self.order_type = None  #buyurtmaning turi yozilmasayam boladi
        self.amount = None      #buyurtmaning narxi
    
    def check_order(self):
        if self.order == True: #bazada xudi wunday buyurtma bor narxi xam tori keladi
            return ORDER_FOUND 
        else:  #agar bunday buyurtma bolmasa
            return ORDER_NOT_FOUND #yoki INVALID_AMOUNT #narxi tori kelmadi
````
**settings.py**
````
PAYCOM_SETTINGS = {
    "HOST":"https://checkout.test.paycom.uz/api",   #test host
    "ID":"qwertt12345",          #token
    "SECRET_KEY":"wertyu234567",  #password
    "PATH_CLASS":"apps.order.views", #Paycom classini qayerga yozgan bolsangiz owa joyni korsating
    "ACCOUNTS":{
        "KEY1":"order_id",
        "KEY2":None #or "type"
    }
}

````

**urls.py**
````
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/payment/', include('PaycomUz.urls'))

]

````
# 💲 To'lovlarni amalga oshirish
````
from PaycomUz.methods_subscribe_api import Subcribe

token = 'token'
data = Subcribe(token=token,order_id=1,amount=5000.00,order_type='order').receipts_create()
print(data)

>>> {'_id': '5c42fb5ae3331dc358f3afef', 'paid': True, 'status': 'success', 'error': None}
or
>>> {'_id': 'error_response14', 'paid': False, 'status': 'failed', 'error': {'jsonrpc': '2.0', 'id': 123, 'error': {'code': -31700, 'id': 138, 'message': 'З
аказ не найден', 'origin': 'merchants.checkPerformTransaction'}}}

````
![alt text](https://i.imgur.com/TFjxbkL.png)
#
![alt text](https://i.imgur.com/JlpsLiz.png)




# YouTube : https://youtu.be/pyj3WSLDe9g
