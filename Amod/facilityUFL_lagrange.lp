\ Model facility relax lagrangian cfl
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  8008 X[0] + 10182 X[1] + 7259 X[2] + 4563 X[3] + 9432 X[4] + 761 Y[0,0]
   + 766 Y[0,1] + 847 Y[0,2] + 642 Y[0,3] + 200 Y[1,0] + 409 Y[1,1]
   + 447 Y[1,2] + 340 Y[1,3] + 160 Y[2,0] + 665 Y[2,1] + 209 Y[2,2]
   + 735 Y[2,3] + 165 Y[3,0] + 463 Y[3,1] + 842 Y[3,2] + 982 Y[3,3]
   + 259 Y[4,0] + 522 Y[4,1] + 759 Y[4,2] + 810 Y[4,3]
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
