import pandas as pd
import json
import os

#read excel
excel_file = r'C:\Users\salom\Documents\ExcelFile\order.xlsx'  # Should replace by real name
sheet_name = 'Sheet1'  # cif exsit multipe sheet

# read excel
df = pd.read_excel(excel_file, sheet_name=sheet_name).fillna("")

# initil a new json
json_data_list = []


for index, row in df.iterrows():
    # consture data
    order_json = {
        "cOrderNo": row["cOrderNo"],
        "productType": row["productType"],
        "shippingType": row["shippingType"],
        "pickUpCode": row["pickUpCode"],
        "declaredValue": str(row["declaredValue"]),
        "orderGoods": {
            "weight": row["weight"],
            "length": row["length"],
            "width": row["width"],
            "height": row["height"]
        },
        "orderShipper": {
            "shipperName": row["shipperName"],
            "shipperPhone": row["shipperPhone"],
            "shipperCountry": row["shipperCountry"],
            "shipperState": row["shipperState"],
            "shipperCity": row["shipperCity"],
            "shipperArea": row["shipperArea"],
            "shipperStreet": row["shipperStreet"],
            "shipperCode": row["shipperCode"]
        },
        "orderConsignee": {
            "consigneeName": row["consigneeName"],
            "consigneePhone": row["consigneePhone"],
            "consigneeCountry": row["consigneeCountry"],
            "consigneeState": row["consigneeState"],
            "consigneeCity": row["consigneeCity"],
            "consigneeArea": row["consigneeArea"],
            "consigneeStreet": row["consigneeStreet"],
            "consigneeCode": row["consigneeCode"],
            "consigneeNumIn": str(row["consigneeNumIn"]),
            "consigneeNumExt": str(row["consigneeNumExt"]),
            "remarks": row["remarks"],
            "consigneeEmail": row["consigneeEmail"]
        },
        "orderItemList": [
            {
                "itemNameEn": row["itemNameEn1"],
                "itemNameZh": row["itemNameZh1"],
                "itemQty": str(row["itemQty1"])
            },
            {
                "itemNameEn": row["itemNameEn2"],
                "itemNameZh": row["itemNameZh2"],
                "itemQty": str(row["itemQty2"])
            }
        ],
        "orderInsurance": {
            "insuredAmount": str(row["insuredAmount"])
        },
        "orderCod": {
            "codAmount": str(row["codAmount"]),
            "currency": row["currency"]
        }
    }

    json_data_list.append(order_json)

# save to path, need to change to real path
json_output_file = r'C:\Users\salom\Documents\ExcelFile\orders.json'

# insure the path exsit
os.makedirs(os.path.dirname(json_output_file), exist_ok=True)

# save a real doc
with open(json_output_file, 'w') as json_file:
    json.dump(json_data_list, json_file, indent=4)

# printout
print(f"JSON 文件已保存到: {json_output_file}")