def rec(item,z):
	sd = len(str(item))-4
	print str(item)[sd:]

	if str(item)[sd:] in z:
		print 'is in'
		newitem = item[sd:] + 1
		rec(newitem,z)
	else:
		print ' {} is not in'.format(str(item)[sd:])
		return item


x = [1000,2000,3000,4000,6000,7000,8000]

print rec(3000, x)
