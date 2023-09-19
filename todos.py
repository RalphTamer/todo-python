import requests


def post(url, json):
    x = requests.post(url, json=json)
    return x.json()


def get(url):
    x = requests.get(url)
    return x.json()


base_url = "http://127.0.0.1:5000"
todos = get(base_url)

for todo in todos:
    print(f'{todo["id"]} || {todo["content"]}')

while True:
    inp = input(
        """ 
type 1 to add a todo,
type 2 to delete a todo by id,
type 3 to clear todos
type quit to quit
"""
    )

    if inp == "1":
        try:
            todo = input("enter a todo: ")

            x = post(base_url, json={"content": todo})
        except:
            print("unexpected equation")
    elif inp == "2":
        id = input("please enter id: ")
        res = requests.delete(url=base_url + f"/delete/{int(id)}")
    elif inp == "3":
        requests.delete(f"{base_url}/clear")
    elif inp == "quit":
        break
    else:
        print("wrong input")
    todos = get(base_url)
    for todo in todos:
        print(f'{todo["id"]} || {todo["content"]}')
