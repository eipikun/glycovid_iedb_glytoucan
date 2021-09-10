import pandas as pd
# Set display setting as full(limitation = None)
pd.set_option('display.max_rows', None)

# import csv files
mhc_df = pd.read_csv('./data/mhc_3d_assays.csv')
bcr_df = pd.read_csv('./data/bcr_3d_assays.csv')
tcr_df = pd.read_csv('./data/tcr_3d_assays.csv')

# import full epitope csv file
full_epitope_df = pd.read_csv('./data/epitope_full_v3.csv')

# import target csv file
target_df = pd.read_csv('./data/linkout_16_glytoucan_080121.csv')

# Modify target df
target_df['link_url_41'] = target_df['link_url_41'].str[42:]
df_epitope_glytoucan = target_df.dropna()[['Epitope IRI', 'link_url_41']]


# MHC
mhc_df['Epitope IRI'] = mhc_df['Epitope IRI'].str[28:]
mhc_df = mhc_df.astype({'Epitope IRI':'int64'})
new_mhc_df = pd.merge(mhc_df, df_epitope_glytoucan,how = 'inner', on = 'Epitope IRI')
new_mhc_df.to_csv('./export/mhc_matched.csv')

# BCR
bcr_df['Epitope IRI'] = bcr_df['Epitope IRI'].str[28:]
bcr_df = bcr_df.astype({'Epitope IRI':'int64'})
new_bcr_df = pd.merge(bcr_df, df_epitope_glytoucan,how = 'inner', on = 'Epitope IRI')
new_bcr_df.to_csv('./export/bcr_matched.csv')

# TCR
tcr_df['Epitope IRI'] = tcr_df['Epitope IRI'].str[28:]
tcr_df = tcr_df.astype({'Epitope IRI':'int64'})
new_tcr_df = pd.merge(tcr_df, df_epitope_glytoucan,how = 'inner', on = 'Epitope IRI')
new_tcr_df.to_csv('./export/tcr_matched.csv')

# Full epitope
full_epitope_df['Epitope IRI'] = full_epitope_df['Epitope IRI'].str[28:]
full_epitope_df = full_epitope_df.astype({'Epitope IRI':'int64'})
new_full_epitope_df = pd.merge(full_epitope_df, df_epitope_glytoucan,how = 'inner', on = 'Epitope IRI')
new_full_epitope_df.to_csv('./export/matched_epitope.csv')