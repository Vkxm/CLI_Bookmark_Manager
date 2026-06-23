import json

def view():
    with open('schema.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    for i in data:
        print(i["URL"])

def Add(name,url):
    new_book= {name,url}
    with open('schema.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    data.append(new_book)
    with open('schema.json',  'r', encoding='utf-8') as wfile:
        data = json.load(file)
 
def remove():
    print("This bookmark deleted")

def edit():
    print("this bookmark edited")