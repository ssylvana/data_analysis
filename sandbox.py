import json

def recurs_find_key(key, obj):
    if obj == None:
        return None
    else:
        if key in obj:
            return obj[key]
        if type(obj) == dict or type (obj) == list:
            for k, v in obj.items():
                if type(v) == dict:
                    result = recurs_find_key(key,v)
                    return result
                elif type(v) == list:
                    for el in range(len(v)):
                        result = recurs_find_key(key, v[el-1])
                        return result

with open('result.json', 'r') as f:
   
    json_data = json.loads(f.read())

    data = json_data['contracts']['data']


for contract in data:
    contract_url = recurs_find_key('contractUrl', contract)
    sign_data = recurs_find_key('signDate', contract)
    num_reg = recurs_find_key('regNum', contract)
    price = recurs_find_key('price', contract)
    region_code = recurs_find_key("regionCode", contract)

    customer = recurs_find_key('customer', contract)
    customer_inn = recurs_find_key('inn', customer)
    customer_name = recurs_find_key('fullName', customer)

    suppliers_dict = {}
    suppliers = recurs_find_key('suppliers', contract)

    for supplier in suppliers:
        supplier_inn = recurs_find_key("inn", supplier)
        supplier_name = recurs_find_key("organizationName", supplier)
        suppliers_dict[supplier_inn] = supplier_name


    products = recurs_find_key('products', contract)
    subjects = '; '.join([recurs_find_key('name', product) for product in products])
    
    print(price)
    