\ Model facility relax lagrangian
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  8496 X[0] + 10483 X[1] + 8471 X[2] + 4559 X[3] + 9984 X[4] + 3560 Y[0,0]
   + 3578 Y[0,1] + 3995 Y[0,2] + 2978 Y[0,3] + 770 Y[1,0] + 1946 Y[1,1]
   + 2136 Y[1,2] + 1608 Y[1,3] + 719 Y[2,0] + 3246 Y[2,1] + 384 Y[2,2]
   + 3012 Y[2,3] + 172 Y[3,0] + 1667 Y[3,1] + 3566 Y[3,2] + 4237 Y[3,3]
   + 620 Y[4,0] + 1936 Y[4,1] + 3132 Y[4,2] + 3398 Y[4,3]
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
