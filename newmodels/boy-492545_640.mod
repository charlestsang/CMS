model([d1,d2,d3,d4,d5],
      [f(1,n_boy_3,[d1]),
       f(1,n_fishnet_1,[d2]),
       f(1,n_fish_1,[d3]),
       f(1,n_pants_1,[d4]),
       f(1,n_beach_1,[d5]),
       f(1,a_brown_1,[d4]),
       f(2,s_touches,[(d1,d2),(d1,d3),(d1,d5),(d1,d4)]),
       f(2,s_supports,[(d5,d1)]),
       f(2,s_occludes,[(d1,d2),(d1,d3)]),
       f(2,s_part_of,[(d4,d1)])]).
      