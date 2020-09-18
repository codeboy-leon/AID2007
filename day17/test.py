with open('./static/index.html','rb') as file:
    data = file.read()

print(data.decode())