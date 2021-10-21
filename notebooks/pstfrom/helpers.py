

def postproc():
	import os
	import flopy
	from flopy.utils.mflistfile import ListBudget
	import numpy as np

	class GwtListBudget(ListBudget):
		""" """

		def set_budget_key(self):
			self.budgetkey = "MASS BUDGET FOR ENTIRE MODEL"
			return


	# scrub the conc obs for missing "e"
	lines = open("conc_obs.csv",'r').readlines()
	with open("conc_obs.csv",'w') as f:
		for line in lines:
			line = line.lower()
			raw = line.strip().split(",")
			for i,r in enumerate(raw):
				if "-" in r[1:] and "e-" not in r:
					raw[i] = r[0] + r[1:].replace("-","e-")
					try:
						_ = float(raw[i])
					except:
						raise Exception("error casting repaired value: "+raw[i])
			line = ",".join(raw)
			f.write(line+"\n")


	ucn = [f for f in os.listdir(".") if f.lower().endswith(".ucn")][0]
	ucn = flopy.utils.HeadFile(ucn,precision="double",text="concentration")
	for it,t in enumerate(ucn.get_times()):
		d = ucn.get_data(totim=t)
		for k,dlay in enumerate(d):
			np.savetxt("sgn_50.lay{0}_t{1}_ucn.dat".format(k+1,it+1),d[k,:,:],fmt="%15.6E")
	hds = [f for f in os.listdir(".") if f.lower().endswith(".hds")][0]
	hds = flopy.utils.HeadFile(hds)
	for it,t in enumerate(hds.get_times()):
		d = hds.get_data(totim=t)
		for k,dlay in enumerate(d):
			np.savetxt("sgn_50.lay{0}__t{1}_hds.dat".format(k+1,it+1),d[k,:,:],fmt="%15.6E")

	lst = [f for f in os.listdir(".") if f.lower().endswith(".list")][0]
	lst = flopy.utils.Mf6ListBudget(lst)
	inc,cum = lst.get_dataframes(diff=True,start_datetime=None)
	cum.columns = cum.columns.map(lambda x: x.lower().replace(" ","-"))
	inc.columns = inc.columns.map(lambda x: x.lower().replace(" ", "-"))
	cum.index = cum.index.map(lambda x: np.round(x,1))
	inc.index = inc.index.map(lambda x: np.round(x,1))
	cum.index.name = "time"
	cum.to_csv("cum.csv")
	inc.index.name = "time"
	inc.to_csv("inc.csv")

	lst = [f for f in os.listdir(".") if f.lower().endswith(".lst")][0]
	lst = GwtListBudget(lst)
	inc,cum = lst.get_dataframes(diff=True,start_datetime=None)
	cum.columns = cum.columns.map(lambda x: x.lower().replace(" ","-"))
	inc.columns = inc.columns.map(lambda x: x.lower().replace(" ", "-"))
	cum.index = cum.index.map(lambda x: np.round(x,1))
	inc.index = inc.index.map(lambda x: np.round(x,1))
	cum.index.name = "time"
	cum.to_csv("tcum.csv")
	inc.index.name = "time"
	inc.to_csv("tinc.csv")


if __name__ == "__main__":
	postproc()
	
