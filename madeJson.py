import pandas as pd
import json
import os

# 读取 Excel 文件
excel_file = r'C:\Users\salom\Documents\ExcelFile\order.xlsx'  # 替换为实际的文件名
sheet_name = 'Sheet1'  # 如果有多个工作表，指定工作表名称

# 使用 pandas 读取 Excel 文件
df = pd.read_excel(excel_file, sheet_name=sheet_name).fillna("")

# 初始化一个列表来存储多个 JSON 数据
json_data_list = []

# 遍历每一行，构建对应的 JSON 格式数据
for index, row in df.iterrows():
    # 构建每一条订单的 JSON 数据
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

# 保存 JSON 文件到指定路径
json_output_file = r'C:\Users\salom\Documents\ExcelFile\orders.json'

# 确保文件夹路径存在
os.makedirs(os.path.dirname(json_output_file), exist_ok=True)

# 将 JSON 列表保存为文件
with open(json_output_file, 'w') as json_file:
    json.dump(json_data_list, json_file, indent=4)

# 输出生成的 JSON 数据，便于查看
print(f"JSON 文件已保存到: {json_output_file}")