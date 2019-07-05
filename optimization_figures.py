#PLOT
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("optimization_detailed_results.csv",delimiter=";")
parameters = ["LENGTH","FUSE_MAX_CSA","B","CR","TR","SWEEP","AREA","AR","WEIGHT","USABLE_FUEL","ITR","MMACH","SEP","ACC","TAKEOFF","LANDING"]
for parm in parameters:
	x = df["SUPM"]
	y = df["SUSG"]
	c = df[parm]
	plt.figure(dpi=360)
	plt.scatter(x,y,c=c)
	plt.colorbar(label=parm)
	plt.clim(min(c),max(c))
	plt.grid()
	plt.savefig(parm+".png")
	plt.clf()

