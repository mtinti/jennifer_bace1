# %%
import pandas as pd
import numpy as np
indf = pd.read_csv('../BACE1_pulldown/res_48.csv',index_col=[0])
indf.head()
indf.index.name = 'Gene_acc'
indf.rename({'desc':'Desc'},axis=1,inplace=True)
indf=indf[['Gene_id','srank','Intensity','FDR','Desc']]
indf=indf[indf['Intensity']>0]
indf['Intensity']=np.log10(indf['Intensity'])
indf.describe()
# %%
indf.to_csv('res_48.csv')

# %%
import os
cwd = os.getcwd()
cwd
# %%
