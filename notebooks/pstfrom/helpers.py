

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

	ucn = [f for f in os.listdir(".") if f.lower().endswith(".ucn")][0]
	ucn = flopy.utils.HeadFile(ucn,precision="double",text="concentration")
	d = ucn.get_data()
	for k,dlay in enumerate(d):
		np.savetxt("sgn_50.lay{0}_ucn.dat".format(k+1),d[k,:,:],fmt="%15.6E")
	hds = [f for f in os.listdir(".") if f.lower().endswith(".hds")][0]
	hds = flopy.utils.HeadFile(hds)
	d = hds.get_data()
	for k,dlay in enumerate(d):
		np.savetxt("sgn_50.lay{0}_hds.dat".format(k+1),d[k,:,:],fmt="%15.6E")

	lst = [f for f in os.listdir(".") if f.lower().endswith(".list")][0]
	lst = flopy.utils.Mf6ListBudget(lst)
	cum,inc = lst.get_dataframes(diff=True,start_datetime=None)
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
	cum,inc = lst.get_dataframes(diff=True,start_datetime=None)
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
	
