exceptions = {}
catch_list = []

def search_ex(child):
    for next_child in exceptions[child]:
        if next_child in catch_list:
            return True
        if search_ex(next_child):
            return True
    return False


n = int(input())
for _ in range(n):
    arr = input().split(' : ')
    child = arr[0]
    if len(arr) > 1:
        parents = arr[1].split()
        exceptions[child] = parents
    else:
        exceptions[child] = []

m = int(input())
for _ in range(m):
    exception = input()
    if not search_ex(exception):
        catch_list.append(exception)
    else:
        print(exception)