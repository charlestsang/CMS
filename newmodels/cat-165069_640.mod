model([d1,d2,d3,d4],
      [f(1,n_cat_1,[d1]),
       f(1,a_grey_1,[d1]),
       f(1,n_eye_1,[d2,d3]),
       f(1,a_green_1,[d2,d3]),
       f(1,n_chair_1,[d4]),
       f(1,a_black_1,[d4]),
       f(2,s_supports,[(d4,d1)]),
       f(2,s_touches,[(d1,d4)]),
       f(2,s_part_of,[(d2,d1)]),
       f(2,s_occludes,[(d1,d4)])]).
