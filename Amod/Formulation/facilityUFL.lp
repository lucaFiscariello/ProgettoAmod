\ Model facility
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  1.682052e+06 X[0] + 1.784637e+06 X[1] + 1.114672e+06 X[2] + 878194 X[3]
   + 1.08606e+06 X[4] + 973180 X[5] + 192683 Y[0,0] + 478370 Y[0,1]
   + 50397 Y[0,2] + 250704 Y[0,3] + 14627 Y[0,4] + 362099 Y[1,0]
   + 403043 Y[1,1] + 349057 Y[1,2] + 347524 Y[1,3] + 430882 Y[1,4]
   + 14457 Y[2,0] + 337199 Y[2,1] + 277737 Y[2,2] + 314773 Y[2,3]
   + 301189 Y[2,4] + 130393 Y[3,0] + 265148 Y[3,1] + 61652 Y[3,2]
   + 157119 Y[3,3] + 441840 Y[3,4] + 200929 Y[4,0] + 376048 Y[4,1]
   + 101453 Y[4,2] + 334969 Y[4,3] + 298780 Y[4,4] + 102194 Y[5,0]
   + 159670 Y[5,1] + 36829 Y[5,2] + 234732 Y[5,3] + 435200 Y[5,4]
Subject To
 Demand[0]: Y[0,0] + Y[1,0] + Y[2,0] + Y[3,0] + Y[4,0] + Y[5,0] = 1
 Demand[1]: Y[0,1] + Y[1,1] + Y[2,1] + Y[3,1] + Y[4,1] + Y[5,1] = 1
 Demand[2]: Y[0,2] + Y[1,2] + Y[2,2] + Y[3,2] + Y[4,2] + Y[5,2] = 1
 Demand[3]: Y[0,3] + Y[1,3] + Y[2,3] + Y[3,3] + Y[4,3] + Y[5,3] = 1
 Demand[4]: Y[0,4] + Y[1,4] + Y[2,4] + Y[3,4] + Y[4,4] + Y[5,4] = 1
 Continuity[0,0]: X[0] - Y[0,0] >= 0
 Continuity[0,1]: X[0] - Y[0,1] >= 0
 Continuity[0,2]: X[0] - Y[0,2] >= 0
 Continuity[0,3]: X[0] - Y[0,3] >= 0
 Continuity[0,4]: X[0] - Y[0,4] >= 0
 Continuity[1,0]: X[1] - Y[1,0] >= 0
 Continuity[1,1]: X[1] - Y[1,1] >= 0
 Continuity[1,2]: X[1] - Y[1,2] >= 0
 Continuity[1,3]: X[1] - Y[1,3] >= 0
 Continuity[1,4]: X[1] - Y[1,4] >= 0
 Continuity[2,0]: X[2] - Y[2,0] >= 0
 Continuity[2,1]: X[2] - Y[2,1] >= 0
 Continuity[2,2]: X[2] - Y[2,2] >= 0
 Continuity[2,3]: X[2] - Y[2,3] >= 0
 Continuity[2,4]: X[2] - Y[2,4] >= 0
 Continuity[3,0]: X[3] - Y[3,0] >= 0
 Continuity[3,1]: X[3] - Y[3,1] >= 0
 Continuity[3,2]: X[3] - Y[3,2] >= 0
 Continuity[3,3]: X[3] - Y[3,3] >= 0
 Continuity[3,4]: X[3] - Y[3,4] >= 0
 Continuity[4,0]: X[4] - Y[4,0] >= 0
 Continuity[4,1]: X[4] - Y[4,1] >= 0
 Continuity[4,2]: X[4] - Y[4,2] >= 0
 Continuity[4,3]: X[4] - Y[4,3] >= 0
 Continuity[4,4]: X[4] - Y[4,4] >= 0
 Continuity[5,0]: X[5] - Y[5,0] >= 0
 Continuity[5,1]: X[5] - Y[5,1] >= 0
 Continuity[5,2]: X[5] - Y[5,2] >= 0
 Continuity[5,3]: X[5] - Y[5,3] >= 0
 Continuity[5,4]: X[5] - Y[5,4] >= 0
Bounds
Binaries
 X[0] X[1] X[2] X[3] X[4] X[5] Y[0,0] Y[0,1] Y[0,2] Y[0,3] Y[0,4] Y[1,0]
 Y[1,1] Y[1,2] Y[1,3] Y[1,4] Y[2,0] Y[2,1] Y[2,2] Y[2,3] Y[2,4] Y[3,0]
 Y[3,1] Y[3,2] Y[3,3] Y[3,4] Y[4,0] Y[4,1] Y[4,2] Y[4,3] Y[4,4] Y[5,0]
 Y[5,1] Y[5,2] Y[5,3] Y[5,4]
End
