# iedb_glytoucan
This repository is a part of Glycovid project.
The purpose of the program in this repository is for filtering IEDB related data by 'Epitope ID' which is associated with GlyToucan.

## Environment
You are required to execute 'filtering.py'
- numpy==1.21.2
- pandas==1.3.2
- python-dateutil==2.8.2
- pytz==2021.1
- six==1.16.0


## Procedures
### Step 0
- Get an IEDB registered Epitope file from this [link](https://www.iedb.org/database_export_v3.php).
- Click 'epitope_full_v3.zip' in 'CSV Metric Exports' folder.
  
### Step 0-1(optional)
This optional procedure is for those who want to execute in virtual environment.
```
$python3 -m venv venv
$pip install -r requirements.txt
```
### Step 1
Please make sure that there is downloaded Epitope csv file as '/data/epitope_full_v3.csv'

### Step 2
```
$python3 filtering.py
```

### Step 3
confirm there are four csv files in '/export/'.
> export/bcr_matched.csv
> > This csv is a filtered list of B cell assays
>
> export/tcr_matched.csv
> > This csv is a filtered list of T cell assays
> 
> export/mhc_matched.csv
> > This csv is a filtered list of MHC assays
> 
> export/matched_epitope.csv
> > This csv is a filtered list of epitope from all registered epitope in IEDB

※ Originally, there are four csv files in export which were generated on the same day as commit.

## Note
'data/link_out_16_glytoucan....csv' would be updated as further epitope associated with GlyToucan.
'data/~~assays.csv' also may be updated. Please check the same IEDB data store [link](https://www.iedb.org/database_export_v3.php), referring 'CSV Metric Exports/iedv_3d_full.zip'