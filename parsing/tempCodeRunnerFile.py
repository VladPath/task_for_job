or i in range(len(file)):
        
        k,v = file[i].items()
        print(k,v)
    
json_string = '{"name": "John", "age": 30}'
data = json.loads(json_string)
print(data)