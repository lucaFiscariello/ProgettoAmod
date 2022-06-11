\ Model facility relax lagrangian cfl
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  8008 X[0] + 10182 X[1] + 7259 X[2] + 4563 X[3] + 9432 X[4] + 3566 Y[0,0]
   + 3584 Y[0,1] + 4001 Y[0,2] + 2984 Y[0,3] + 776 Y[1,0] + 1955 Y[1,1]
   + 2143 Y[1,2] + 1612 Y[1,3] + 721 Y[2,0] + 3250 Y[2,1] + 402 Y[2,2]
   + 3029 Y[2,3] + 186 Y[3,0] + 1687 Y[3,1] + 3585 Y[3,2] + 4256 Y[3,3]
   + 637 Y[4,0] + 1958 Y[4,1] + 3151 Y[4,2] + 3410 Y[4,3]
Subject To
 Demand[0]: Y[0,0] + Y[1,0] + Y[2,0] + Y[3,0] + Y[4,0] = 1
 Demand[1]: Y[0,1] + Y[1,1] + Y[2,1] + Y[3,1] + Y[4,1] = 1
 Demand[2]: Y[0,2] + Y[1,2] + Y[2,2] + Y[3,2] + Y[4,2] = 1
 Demand[3]: Y[0,3] + Y[1,3] + Y[2,3] + Y[3,3] + Y[4,3] = 1
Bounds
Binaries
 X[0] X[1] X[2] X[3] X[4] Y[0,0] Y[0,1] Y[0,2] Y[0,3] Y[1,0] Y[1,1] Y[1,2]
 Y[1,3] Y[2,0] Y[2,1] Y[2,2] Y[2,3] Y[3,0] Y[3,1] Y[3,2] Y[3,3] Y[4,0]
 Y[4,1] Y[4,2] Y[4,3]
End
