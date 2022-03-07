#!/bin/bash


# Create and load table query
create_load_table_q="""

use dmp_yelp_rs;

drop table if exists users;

create external table if not exists users 
(
user_id string,
name string,
review_count int,
yelping_since string,
useful int,
funny int,
cool int,
elite string,
friends string,
fans int,
average_stars float,
compliment_hot int,
compliment_more int,
compliment_profile int,
compliment_cute int,
compliment_list int,
compliment_note int,
compliment_plain int,
compliment_cool int,
compliment_funny int,
compliment_writer int,
compliment_photos int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES ('separatorChar' = ',')  
STORED AS TEXTFILE
tblproperties ('skip.header.line.count'='1');

LOAD DATA LOCAL INPATH '/project2/msca/mtoolsidas/data_mining/yelp_dataset/yelp_user.csv' OVERWRITE INTO TABLE users;
"""

# Run queries
hive -e "${create_load_table_q}"


#-----------------------------------------------------------