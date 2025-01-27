import json
import time

def count_items_and_sum(path_file):
    count_items = {}
    count_sum = {}
    pass_id = set()
    try:
        with open(path_file, "r") as f:
            data = json.load(f)
            
            for i in data:
                if i['id'] not in pass_id:
                    count_items[i['category']] = count_items.get(i['category'],0) +1
                    count_sum[i['category']] = count_sum.get(i['category'],0) + i['price']
                    pass_id.add(i['id'])
                else:
                    print('Такой уже есть')

        return f'items {count_items}\nsum {count_sum}'
    
    except json.JSONDecodeError as err:
        print(f"Ошибка декодирования JSON: {err}")
    


start = time.time()
print(count_items_and_sum("parsing/f.json"))
print(time.time()-start)