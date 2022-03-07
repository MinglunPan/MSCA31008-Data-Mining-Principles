#!/bin/bash


# Create and load table query
create_load_table_q="""

use dmp_yelp_rs;

drop table if exists geo_features;

create external table if not exists geo_features 
(
business_id string,
HHI float,
total_review int,
avg_stars float,
most_category string,
within__2_km int,
within__5_km int,
within__10_km int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES ('separatorChar' = ',')  
STORED AS TEXTFILE
tblproperties ('skip.header.line.count'='1');

LOAD DATA LOCAL INPATH '/project2/msca/mtoolsidas/data_mining/yelp_dataset/df_geo_agg.csv' OVERWRITE INTO TABLE geo_features;
"""

# Run queries
hive -e "${create_load_table_q}"


#-----------------------------------------------------------