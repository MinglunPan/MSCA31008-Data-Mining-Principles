#!/bin/bash


# Create and load table query
create_load_table_q="""

use dmp_yelp_rs;

drop table if exists ts_features;

create external table if not exists ts_features 
(
month_year string,
simplified_category string,
seasonal_review_counts float,
trend_review_counts float,
seasonal_avg_stars float,
trend_avg_stars float,
review_counts int,
avg_stars float,
is_pre_covid int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES ('separatorChar' = ',')  
STORED AS TEXTFILE
tblproperties ('skip.header.line.count'='1');

LOAD DATA LOCAL INPATH '/project2/msca/mtoolsidas/data_mining/yelp_dataset/time_series_features.csv' OVERWRITE INTO TABLE ts_features;
"""

# Run queries
hive -e "${create_load_table_q}"


#-----------------------------------------------------------