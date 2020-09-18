import os
data = os.listdir("../test")
print(data)
for item in data:
    if os.path.getsize("../test/"+item) < 1024:
        os.remove("../test/"+item)
