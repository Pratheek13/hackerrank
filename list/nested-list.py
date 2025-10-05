if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    # Extract all scores
    scores = [score for name, score in records]
    
    # Find second lowest score
    lowest = min(scores)
    second_lowest = min(s for s in scores if s != lowest)
    
    # Get all names with second lowest score
    result = [name for name, score in records if score == second_lowest]
    
    # Print names in alphabetical order
    for name in sorted(result):
        print(name)
