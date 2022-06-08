'''
2048
'''
map = [
    [2,0,2,2],
    [4,4,2,2],
    [2,4,0,4],
    [0,0,2,2],
    ]

def merge(list_merge):
    #print(list_merge)
    for i in range(-1,-len(list_merge)-1,-1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)
    #return list_merge

def move_left(list_merge):
    for i in range(len(list_merge)-1):
        if list_merge[i] == list_merge[i+1]:
            list_merge[i] += list_merge[i+1]
            del list_merge[i+1]
            list_merge.append(0)
def move_right():
    for line in map:
        global list_merge1
        list_merge1 = line[::-1]
        merge()
        line[::-1] = list_merge1
list_merge1=[2,2,0,0]
move_left(list_merge1)
print(list_merge1)