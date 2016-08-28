# https://www.youtube.com/watch?v=UPanUFVFfzY
# https://github.com/keeppythonweird/catinabox/blob/master/examples/complected/cats.py
# pip install pytest-flakes for syntax cheking

import random

def setup_cats(num_cats):

	cat_names = ["Fluffles", "Enzo", "Lisa", "Berto", "Jillian", "Amy",
                 "Bella", "Moe", "Tibby"]


	foods = ["vinegar", "vegemite", "vanilla", "acorn squash",
             "Canadian bacon", "alligator", "cayenne pepper", "adobo",
             "almond butter",
             "garlic"]
	cats = []

	for _ in range(num_cats):
		new_cat = {"name":random.choice(cat_names),"last_ate":None}
		cats.append(new_cat)




	for cat in cats:
		cat['last_ate'] = random.choice(foods)
	return cats

print(setup_cats(5))


def sumary(a,b):
	return a+b


def test_sumary():
	assert 5+3 == 8



