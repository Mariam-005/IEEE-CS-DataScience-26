def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >=k+maxPts: 
            return 1.0
        
        chance = [0]* (n + 1)
        chance[0] = 1.0
        st = 1.0
        w_chance = 0.0

        for i in range(1, n + 1):
            chance[i] = st / maxPts
            if i < k:
                st += chance[i]
            else:
                w_chance += chance[i]
                
            if i - maxPts >= 0:
                st -= chance[i - maxPts]

        return round(w_chance, 5) 