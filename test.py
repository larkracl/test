def solution(wallet, bill):
    answer = 0

    if max(bill[0],bill[1]) > max(wallet[0],wallet[1]) or min(bill[0],bill[1]) > min(wallet[0],wallet[1]):
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1
    return answer

print(solution([50, 50], [100, 241]))
print("Done!")
print("and git connected!")