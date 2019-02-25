import random	

d = {8:37,38:9,11:2,13:34,40:68,65:46,52:81}

p = random.choice([2,8,9,13,40,65,52])


print("you got",p)

if p in d:
	if p > d[p]:
		print("oops!! A snake just swallowed you..")

	else:
		print("cheers!1 climb up..")
	print("you can go to ",d[p])
