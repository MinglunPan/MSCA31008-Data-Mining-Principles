#!/bin/bash


# Create and load table query
create_load_table_q="""

use dmp_yelp_rs;

drop table if exists ts_features_new;

create external table if not exists ts_features_new 
(
business_id string, 
pre_covid_avg_stars float, 
pre_covid_review_count int,
post_covid_avg_stars float, 
post_covid_review_count int, 
last_7_avg_stars float,
last_7_review_count int, 
last_30_avg_stars float, 
last_30_review_count int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES ('separatorChar' = ',')  
STORED AS TEXTFILE
tblproperties ('skip.header.line.count'='1');

LOAD DATA LOCAL INPATH '/project2/msca/mtoolsidas/data_mining/yelp_dataset/ts_adjusted.csv' OVERWRITE INTO TABLE ts_features_new;
"""

# Run queries
hive -e "${create_load_table_q}"


#-----------------------------------------------------------