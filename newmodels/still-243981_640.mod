model([d1,d2,d3,d4,d5,d6],
      [f(1,n_straight_chair_1,[d1]),
       f(1,n_gueridon_1,[d2]),
       f(1,n_orange_1,[d3,d4]),
       f(1,n_wall_1,[d5]),
       f(1,n_pot_1,[d6]),
       f(1,a_orange_1,[d3,d4]),
       f(1,a_brown_1,[d1]),
       f(1,a_ocher_1,[d6]),
       f(2,s_touches,[(d2,d3),(d2,d4),(d6,d5)]),
       f(2,s_near,[(d1,d2),(d5,d1),(d5,d2)]),
       f(2,s_supports,[(d2,d3),(d2,d4)])]).
