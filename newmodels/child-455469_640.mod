model([d1,d2,d3,d4,d5],
	[f(1,n_boy_1,[d1]),
	 f(1,n_alsatian_2,[d2]),
	 f(1,n_dog_1,[d3]),
	 f(1,n_hat_1,[d4]),
	 f(1,n_meadow_1,[d5]),
	 f(1,a_gray_1,[d4]),
	 f(2,s_supports,[(d5,d1),(d5,d2),(d5,d3)]),
	 f(2,s_touches,[(d5,d1),(d1,d5),(d5,d2),(d2,d5),(d5,d3),(d3,d5),(d1,d4),(d4,d1)]),
	 f(2,s_near,[(d1,d2),(d2,d1),(d1,d3),(d3,d1)])]).
