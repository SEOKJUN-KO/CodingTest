def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(0, len(phone_book)-1):
        a = phone_book[i]
        b = phone_book[i+1]
        if (a == b[0: len(a)]): return False
    return True
