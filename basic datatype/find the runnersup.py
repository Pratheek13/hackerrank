if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_score = max(arr)
    scores = [x for x in arr if x != max_score]
    runner_up = max(scores)
    
    print(runner_up)