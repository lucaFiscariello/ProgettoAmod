\ Model facility
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  8600 X[0] + 10587 X[1] + 8575 X[2] + 4663 X[3] + 10088 X[4] + 3552 Y[0,0]
   + 3569 Y[0,1] + 3988 Y[0,2] + 2973 Y[0,3] + 766 Y[1,0] + 1945 Y[1,1]
   + 2132 Y[1,2] + 1603 Y[1,3] + 714 Y[2,0] + 3244 Y[2,1] + 378 Y[2,2]
   + 3004 Y[2,3] + 163 Y[3,0] + 1666 Y[3,1] + 3565 Y[3,2] + 4231 Y[3,3]
   + 611 Y[4,0] + 1934 Y[4,1] + 3129 Y[4,2] + 3389 Y[4,3]
Subject To
 Demand[0]: Y[0,0] + Y[1,0] + Y[2,0] + Y[3,0] + Y[4,0] = 1
 Demand[1]: Y[0,1] + Y[1,1] + Y[2,1] + Y[3,1] + Y[4,1] = 1
 Demand[2]: Y[0,2] + Y[1,2] + Y[2,2] + Y[3,2] + Y[4,2] = 1
 Demand[3]: Y[0,3] + Y[1,3] + Y[2,3] + Y[3,3] + Y[4,3] = 1
 Continuity[0,0]: X[0] - Y[0,0] >= 0
 Continuity[0,1]: X[0] - Y[0,1] >= 0
 Continuity[0,2]: X[0] - Y[0,2] >= 0
 Continuity[0,3]: X[0] - Y[0,3] >= 0
 Continuity[1,0]: X[1] - Y[1,0] >= 0
 Continuity[1,1]: X[1] - Y[1,1] >= 0
 Continuity[1,2]: X[1] - Y[1,2] >= 0
 Continuity[1,3]: X[1] - Y[1,3] >= 0
 Continuity[2,0]: X[2] - Y[2,0] >= 0
 Continuity[2,1]: X[2] - Y[2,1] >= 0
 Continuity[2,2]: X[2] - Y[2,2] >= 0
 Continuity[2,3]: X[2] - Y[2,3] >= 0
 Continuity[3,0]: X[3] - Y[3,0] >= 0
 Continuity[3,1]: X[3] - Y[3,1] >= 0
 Continuity[3,2]: X[3] - Y[3,2] >= 0
 Continuity[3,3]: X[3] - Y[3,3] >= 0
 Continuity[4,0]: X[4] - Y[4,0] >= 0
 Continuity[4,1]: X[4] - Y[4,1] >= 0
 Continuity[4,2]: X[4] - Y[4,2] >= 0
 Continuity[4,3]: X[4] - Y[4,3] >= 0
Bounds
Binaries
 X[0] X[1] X[2] X[3] X[4] Y[0,0] Y[0,1] Y[0,2] Y[0,3] Y[1,0] Y[1,1] Y[1,2]
 Y[1,3] Y[2,0] Y[2,1] Y[2,2] Y[2,3] Y[3,0] Y[3,1] Y[3,2] Y[3,3] Y[4,0]
 Y[4,1] Y[4,2] Y[4,3]
End
