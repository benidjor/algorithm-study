def solution(wallpaper):          
            
    answer = []

    lux = len(wallpaper)
    luy = len(wallpaper[0])
    rdx = 0
    rdy = 0

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                lux = min(i, lux)
                luy = min(j, luy)
                rdx = max(i, rdx) 
                rdy = max(j, rdy) 
    
    answer = [lux, luy, rdx+1, rdy+1]
    
    return answer