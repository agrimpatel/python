import os
print("Current working directory:", os.getcwd())  # Debugging line

if os.path.exists(""):
    with open("demo.txt","r") as f:
        content = f.read()
        print(content)
        print(type(content))
        f.close()
else:
    print("File not found.")

