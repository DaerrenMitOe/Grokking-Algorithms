from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


graph = {}

graph["you"] = ["alice", "bob", "claire"]

graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["jonny", "thom"]

graph["anuj"] = []
graph["jonny"] = []
graph["peggy"] = []
graph["thom"] = []


if __name__ == "__main__":
    print(search("you"))
