d = {'Name':'Zara','Age': 7}
d2 = {'Sex':'female','Age': 77}
#d.update(d2)
for key in d2.keys():
	d[key] = d2[key]
print d
