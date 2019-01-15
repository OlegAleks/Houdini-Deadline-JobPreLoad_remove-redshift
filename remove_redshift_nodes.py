def remove():
	import hou
	remove_types = []
	cat_list = [hou.nodeTypeCategories()['Vop'], hou.nodeTypeCategories()['Shop'], hou.nodeTypeCategories()['Object'], hou.nodeTypeCategories()['Driver'], hou.nodeTypeCategories()['VopNet']]
	for m in cat_list:
		for i, j in m.nodeTypes().items():
			if i.find('redshift')!=-1 or i.find('rs_')!=-1 or i.find('Redshift')!=-1 or i.find('rslight')!=-1 or i.find('PP18_RSLight')!=-1:
				remove_types.append(j)
	nodes = []
	for i in remove_types:
		for j in i.instances():
			nodes.append(j)
	if len(nodes)>0:
		print "nodes: ", len(nodes)
		new = []
		for i in nodes:
			par = i.parent()
			if not i.isInsideLockedHDA() and not par.isInsideLockedHDA() and par not in nodes:
				new.append(i)
		print "actual nodes: ", len(new)
		for i in new:
			i.destroy()
	else:
		print "No RS nodes found"