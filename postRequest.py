import requests
from requests.auth import HTTPBasicAuth

# API 终端地址
url = "https://uat-cps-api.eminxing.com/open-api/v2/order/create"

# 多条 JSON 数据
payloads = [
    {
        "cOrderNo": "CIFR4589222452317",
        "productType": "EXP",
        "shippingType": "",
        "pickUpCode": "",
        "declaredValue": "100",
        "orderGoods": {
            "weight": 2,
            "length": 10,
            "width": 11,
            "height": 12
        },
        "orderShipper": {
            "shipperName": "YYY",
            "shipperPhone": "13678987875",
            "shipperCountry": "china",
            "shipperState": "hunan",
            "shipperCity": "xiangtan",
            "shipperArea": "xiangxiangshi",
            "shipperStreet": "juntang",
            "shipperCode": "20000"
        },
        "orderConsignee": {
            "consigneeName": "CCC",
            "consigneePhone": "+33 565676778",
            "consigneeCountry": "France",
            "consigneeState": "Seine-Saint-Denis",
            "consigneeCity": "Noisy-le-Sec",
            "consigneeArea": "",
            "consigneeStreet": "11 Rue des Carrouges",
            "consigneeCode": "93130",
            "consigneeNumIn": "103",
            "consigneeNumExt": "2022",
            "remarks": "women's dress",
            "consigneeEmail": ""
        },
        "orderItemList": [
            {
                "itemNameEn": "women's dress",
                "itemNameZh": "women",
                "itemQty": "3"
            },
            {
                "itemNameEn": "women's dress2",
                "itemNameZh": "",
                "itemQty": 2
            }
        ],
        "orderInsurance": {
            "insuredAmount": "55"
        },
        "orderCod": {
            "codAmount": "2",
            "currency": "USD"
        }
    },
    # 第二条 JSON 数据
    {
        "cOrderNo": "CIFR4589222452318",
        "productType": "EXP",
        "shippingType": "",
        "pickUpCode": "",
        "declaredValue": "150",
        "orderGoods": {
            "weight": 1.5,
            "length": 15,
            "width": 10,
            "height": 8
        },
        "orderShipper": {
            "shipperName": "ZZZ",
            "shipperPhone": "13765432111",
            "shipperCountry": "china",
            "shipperState": "guangdong",
            "shipperCity": "shenzhen",
            "shipperArea": "nanshan",
            "shipperStreet": "dongmen",
            "shipperCode": "51000"
        },
        "orderConsignee": {
            "consigneeName": "DDD",
            "consigneePhone": "+44 123456789",
            "consigneeCountry": "France",
            "consigneeState": "Seine-Saint-Denis",
            "consigneeCity": "Noisy-le-Sec",
            "consigneeArea": "",
            "consigneeStreet": "11 Rue des Carrouges",
            "consigneeCode": "93130",
            "consigneeNumIn": "A1",
            "consigneeNumExt": "2023",
            "remarks": "men's suit",
            "consigneeEmail": ""
        },
        "orderItemList": [
            {
                "itemNameEn": "men's suit",
                "itemNameZh": "suit",
                "itemQty": "1"
            }
        ],
        "orderInsurance": {
            "insuredAmount": "100"
        },
        "orderCod": {
            "codAmount": "5",
            "currency": "GBP"
        }
    }
]

# 请求头
headers = {
    "Content-Type": "application/json"
}

# 用户名和密码
username = "YT_temu"
password = "YT_temu@123"

# 循环遍历 JSON 数据列表并发送请求
for payload in payloads:
    response = requests.post(
        url,
        json=payload,
        headers=headers,
        auth=HTTPBasicAuth(username, password)
    )

    # 打印每次请求的返回结果
    print(f"Order No: {payload['cOrderNo']}")
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
    print("-" * 40)  # 分隔符
