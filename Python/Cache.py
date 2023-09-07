# https://school.programmers.co.kr/learn/courses/30/lessons/17680#
def solution(cacheSize, cities):
    answer = 0
    if(cacheSize == 0): 
        return len(cities)*5
    else:
        cache = {}
        for i in range( len(cities) ):
            city = cities[i].lower()
            if(city in cache.keys()):
                del(cache[city])
                cache[city] = i
                answer += 1
                continue
            if( len( cache.keys() ) < cacheSize ):
                cache[city] = i
                answer += 5
            else: 
                key = list(cache.keys())[0]
                del(cache[key])
                cache[city] = i
                answer += 5
        return answer
