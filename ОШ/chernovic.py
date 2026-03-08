def solution(lst, target):
    print(lst, target)
    for i in range(len(lst) - 1):
        for k in range(i + 1, len(lst)):
            if lst[i] + lst[k] == target:
                return [i, k]


lst = list(map(int, input()))
target = int(input())
print(solution(lst, target))



    
    



