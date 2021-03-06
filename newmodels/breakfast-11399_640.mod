model([d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16],
      [f(1,n_butter_1,[d1]),
       f(1,n_cup_1,[d2,d3]),
       f(1,n_plate_1,[d4,d5]),
       f(1,n_pretzel_1,[d6,d7]),
       f(1,n_teapot_1,[d8]),
       f(1,n_banana_2,[d9]),
       f(1,n_knife_3,[d10,d11]),
       f(1,n_tea_2,[d12,d13,d14]),
       f(1,n_apple_1,[d15,d16]),
       f(1,a_red_1,[d15]),
       f(1,a_green_1,[d16]),
       f(1,a_yellow_1,[d9]),
       f(2,s_supports,[(d4,d6),(d5,d15)]),
       f(2,s_touches,[(d4,d6),(d5,d15),(d12,d8),(d13,d2),(d14,d3)]),
       f(2,s_part_of,[(d12,d8),(d13,d2),(d14,d3)]),
       f(2,s_occludes,[(d6,d4)])]).
