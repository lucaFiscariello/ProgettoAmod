\ Model facility
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  1.682052e+06 X[0] + 1.784637e+06 X[1] + 1.114672e+06 X[2] + 878194 X[3]
   + 1.08606e+06 X[4] + 973180 X[5] + 192683 y[0,0] + 478370 y[0,1]
   + 50397 y[0,2] + 250704 y[0,3] + 14627 y[0,4] + 362099 y[1,0]
   + 403043 y[1,1] + 349057 y[1,2] + 347524 y[1,3] + 430882 y[1,4]
   + 14457 y[2,0] + 337199 y[2,1] + 277737 y[2,2] + 314773 y[2,3]
   + 301189 y[2,4] + 130393 y[3,0] + 265148 y[3,1] + 61652 y[3,2]
   + 157119 y[3,3] + 441840 y[3,4] + 200929 y[4,0] + 376048 y[4,1]
   + 101453 y[4,2] + 334969 y[4,3] + 298780 y[4,4] + 102194 y[5,0]
   + 159670 y[5,1] + 36829 y[5,2] + 234732 y[5,3] + 435200 y[5,4]
Subject To
 Capacity[0]: - 148 X[0] + 20 y[0,0] + 46 y[0,1] + 16 y[0,2] + 46 y[0,3]
   + 39 y[0,4] <= 0
 Capacity[1]: - 20 X[1] + 20 y[1,0] + 46 y[1,1] + 16 y[1,2] + 46 y[1,3]
   + 39 y[1,4] <= 0
 Capacity[2]: - 62 X[2] + 20 y[2,0] + 46 y[2,1] + 16 y[2,2] + 46 y[2,3]
   + 39 y[2,4] <= 0
 Capacity[3]: - 107 X[3] + 20 y[3,0] + 46 y[3,1] + 16 y[3,2] + 46 y[3,3]
   + 39 y[3,4] <= 0
 Capacity[4]: - 113 X[4] + 20 y[4,0] + 46 y[4,1] + 16 y[4,2] + 46 y[4,3]
   + 39 y[4,4] <= 0
 Capacity[5]: - 61 X[5] + 20 y[5,0] + 46 y[5,1] + 16 y[5,2] + 46 y[5,3]
   + 39 y[5,4] <= 0
 Demand[0]: y[0,0] + y[1,0] + y[2,0] + y[3,0] + y[4,0] + y[5,0] = 1
 Demand[1]: y[0,1] + y[1,1] + y[2,1] + y[3,1] + y[4,1] + y[5,1] = 1
 Demand[2]: y[0,2] + y[1,2] + y[2,2] + y[3,2] + y[4,2] + y[5,2] = 1
 Demand[3]: y[0,3] + y[1,3] + y[2,3] + y[3,3] + y[4,3] + y[5,3] = 1
 Demand[4]: y[0,4] + y[1,4] + y[2,4] + y[3,4] + y[4,4] + y[5,4] = 1
Bounds
Binaries
 X[0] X[1] X[2] X[3] X[4] X[5] y[0,0] y[0,1] y[0,2] y[0,3] y[0,4] y[1,0]
 y[1,1] y[1,2] y[1,3] y[1,4] y[2,0] y[2,1] y[2,2] y[2,3] y[2,4] y[3,0]
 y[3,1] y[3,2] y[3,3] y[3,4] y[4,0] y[4,1] y[4,2] y[4,3] y[4,4] y[5,0]
 y[5,1] y[5,2] y[5,3] y[5,4]
End
