# 주식가격
def solution(prices):
    price_sz = len(prices)
    price_dict = {i: 0 for i in range(price_sz)}
    for i in range(price_sz):
        for j in range(i+1, price_sz):
            price_dict[i] += 1
            if prices[i] > prices[j]:
                break
    return list(price_dict.values())