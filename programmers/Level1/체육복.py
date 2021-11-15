def solution(n, lost, reserve):
    
    reserves = set(reserve)-set(lost) 
    losts = set(lost)-set(reserve)
    
    for i in reserves:
        if i-1 in losts:
            losts.remove(i-1)

        elif i+1 in losts:
            losts.remove(i+1)

    return n-len(losts)