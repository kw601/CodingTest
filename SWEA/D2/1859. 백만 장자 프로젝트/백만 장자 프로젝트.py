#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    prices = list(map(int, input().split()))
    max_price = 0
    benefit = 0
    
    for i in range( n-1, -1, -1):
        if max_price <= prices[i]:
            max_price = prices[i]
        else:
            benefit += max_price - prices[i]
    print(f"#{test_case} {benefit}")
        