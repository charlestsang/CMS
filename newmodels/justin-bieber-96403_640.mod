model([d1,d2,d3,d4,d5,d6,d7,d8],
      [f(1,n_boy_1,[d1]),
       f(1,n_piano_1,[d2]),
       f(1,n_smoke_1,[d3]),
       f(1,n_microphone_1,[d4]),
       f(1,n_cap_1,[d5]),
	   f(1,a_white_1,[d2]),
	   f(1,a_red_1,[d5]),
	   f(2,s_near,[(d1,d4),(d4,d1),(d2,d4),(d4,d2)]),
	   f(2,s_supports,[(d1,d5)]),
	   f(2,s_touches,[(d3,d1),(d1,d3),(d2,d3),(d3,d2),(d4,d3),(d3,d4),(d5,d1),(d1,d5),(d1,d2),(d2,d1)])]).
