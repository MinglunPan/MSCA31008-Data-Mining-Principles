#!/bin/bash


# Create and load table query
create_load_table_q="""

use dmp_yelp_rs;

drop table if exists business_hairspecializesin;

create external table if not exists business_hairspecializesin 
(
business_id string,
africanamerican boolean,
asian boolean,
coloring boolean,
curly boolean,
extensions boolean,
kids boolean,
perms boolean,
straightperms boolean
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES ('separatorChar' = ',')  
STORED AS TEXTFILE
tblproperties ('skip.header.line.count'='1');

LOAD DATA LOCAL INPATH '/project2/msca/mtoolsidas/data_mining/yelp_dataset/df_business_hairspecializesin.csv' OVERWRITE INTO TABLE business_hairspecializesin;
"""

# Run queries
hive -e "${create_load_table_q}"


#-----------------------------------------------------------


# Create and load table query
create_load_table_q="""

use dmp_yelp_rs;

drop table if exists business_attributes;

create external table if not exists business_attributes 
(
business_id string,
RestaurantsTableService boolean,
WiFi string,
BikeParking boolean,
BusinessAcceptsCreditCards boolean,
RestaurantsReservations boolean,
WheelchairAccessible boolean,
Caters boolean,
OutdoorSeating boolean,
RestaurantsGoodForGroups boolean,
HappyHour boolean,
BusinessAcceptsBitcoin boolean,
RestaurantsPriceRange2 string,
HasTV boolean,
Alcohol string,
DogsAllowed boolean,
RestaurantsTakeOut boolean,
NoiseLevel string,
RestaurantsAttire string,
RestaurantsDelivery boolean,
GoodForKids boolean,
ByAppointmentOnly boolean,
AcceptsInsurance boolean,
GoodForDancing boolean,
BYOB boolean,
CoatCheck boolean,
Smoking string,
DriveThru boolean,
BYOBCorkage string,
Corkage boolean,
RestaurantsCounterService boolean,
AgesAllowed string,
Open24Hours boolean
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES ('separatorChar' = ',')  
STORED AS TEXTFILE
tblproperties ('skip.header.line.count'='1');

LOAD DATA LOCAL INPATH '/project2/msca/mtoolsidas/data_mining/yelp_dataset/df_business_attributes.csv' OVERWRITE INTO TABLE business_attributes;
"""

# Run queries
hive -e "${create_load_table_q}"


#-----------------------------------------------------------


# Create and load table query
create_load_table_q="""

use dmp_yelp_rs;

drop table if exists business_dietaryrestrictions;

create external table if not exists business_dietaryrestrictions 
(
business_id string,
dairy_free boolean,
gluten_free boolean,
vegan boolean,
vegetarian boolean
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES ('separatorChar' = ',')  
STORED AS TEXTFILE
tblproperties ('skip.header.line.count'='1');

LOAD DATA LOCAL INPATH '/project2/msca/mtoolsidas/data_mining/yelp_dataset/df_business_dietaryrestrictions.csv' OVERWRITE INTO TABLE business_dietaryrestrictions;
"""

# Run queries
hive -e "${create_load_table_q}"


#-----------------------------------------------------------


# Create and load table query
create_load_table_q="""

use dmp_yelp_rs;

drop table if exists business_bestnights;

create external table if not exists business_bestnights 
(
business_id string,
friday boolean,
monday boolean,
saturday boolean,
sunday boolean,
thursday boolean,
tuesday boolean,
wednesday boolean
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES ('separatorChar' = ',')  
STORED AS TEXTFILE
tblproperties ('skip.header.line.count'='1');

LOAD DATA LOCAL INPATH '/project2/msca/mtoolsidas/data_mining/yelp_dataset/df_business_bestnights.csv' OVERWRITE INTO TABLE business_bestnights;
"""

# Run queries
hive -e "${create_load_table_q}"


#-----------------------------------------------------------

# Create and load table query
create_load_table_q="""

use dmp_yelp_rs;

drop table if exists business_goodformeal;

create external table if not exists business_goodformeal 
(
business_id string,
breakfast boolean,
brunch boolean,
dessert boolean,
dinner boolean,
latenight boolean,
lunch boolean
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES ('separatorChar' = ',')  
STORED AS TEXTFILE
tblproperties ('skip.header.line.count'='1');

LOAD DATA LOCAL INPATH '/project2/msca/mtoolsidas/data_mining/yelp_dataset/df_business_goodformeal.csv' OVERWRITE INTO TABLE business_goodformeal;
"""

# Run queries
hive -e "${create_load_table_q}"


#-----------------------------------------------------------

# Create and load table query
create_load_table_q="""

use dmp_yelp_rs;

drop table if exists business_ambience;

create external table if not exists business_ambience 
(
business_id string,
casual boolean,
classy boolean,
divey boolean,
hipster boolean,
intimate boolean,
romantic boolean,
touristy boolean,
trendy boolean,
upscale boolean
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES ('separatorChar' = ',')  
STORED AS TEXTFILE
tblproperties ('skip.header.line.count'='1');

LOAD DATA LOCAL INPATH '/project2/msca/mtoolsidas/data_mining/yelp_dataset/df_business_ambience.csv' OVERWRITE INTO TABLE business_ambience;
"""

# Run queries
hive -e "${create_load_table_q}"


#-----------------------------------------------------------

# Create and load table query
create_load_table_q="""

use dmp_yelp_rs;

drop table if exists business_basicdata;

create external table if not exists business_basicdata 
(
business_id string,
name string,
address string,
city string,
state string,
postal_code string,
latitude float,
longitude float,
stars float,
review_count int,
is_open int,
categories string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES ('separatorChar' = ',')  
STORED AS TEXTFILE
tblproperties ('skip.header.line.count'='1');

LOAD DATA LOCAL INPATH '/project2/msca/mtoolsidas/data_mining/yelp_dataset/df_business_basicdata.csv' OVERWRITE INTO TABLE business_basicdata;
"""

# Run queries
hive -e "${create_load_table_q}"


#-----------------------------------------------------------

# Create and load table query
create_load_table_q="""

use dmp_yelp_rs;

drop table if exists business_businessparking;

create external table if not exists business_businessparking 
(
business_id string,
garage boolean,
lot boolean,
street boolean,
valet boolean,
validated boolean
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES ('separatorChar' = ',')  
STORED AS TEXTFILE
tblproperties ('skip.header.line.count'='1');

LOAD DATA LOCAL INPATH '/project2/msca/mtoolsidas/data_mining/yelp_dataset/df_business_businessparking.csv' OVERWRITE INTO TABLE business_businessparking;
"""

# Run queries
hive -e "${create_load_table_q}"


#-----------------------------------------------------------

# Create and load table query
create_load_table_q="""

use dmp_yelp_rs;

drop table if exists business_music;

create external table if not exists business_music 
(
business_id string,
background_music boolean,
dj boolean,
jukebox boolean,
karaoke boolean,
live boolean,
video boolean
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES ('separatorChar' = ',')  
STORED AS TEXTFILE
tblproperties ('skip.header.line.count'='1');

LOAD DATA LOCAL INPATH '/project2/msca/mtoolsidas/data_mining/yelp_dataset/df_business_music.csv' OVERWRITE INTO TABLE business_music;
"""

# Run queries
hive -e "${create_load_table_q}"


#-----------------------------------------------------------

# Create and load table query
create_load_table_q="""

use dmp_yelp_rs;

drop table if exists tip;

create external table if not exists tip 
(
user_id string,
business_id string,
text string,
tip_date string,
compliment_count int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES ('separatorChar' = ',')  
STORED AS TEXTFILE
tblproperties ('skip.header.line.count'='1');

LOAD DATA LOCAL INPATH '/project2/msca/mtoolsidas/data_mining/yelp_dataset/df_tip.csv' OVERWRITE INTO TABLE tip;
"""

# Run queries
hive -e "${create_load_table_q}"


#-----------------------------------------------------------

# Create and load table query
create_load_table_q="""

use dmp_yelp_rs;

drop table if exists checkin;

create external table if not exists checkin 
(
business_id string,
checkin_date string,
checkin_count int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES ('separatorChar' = ',')  
STORED AS TEXTFILE
tblproperties ('skip.header.line.count'='1');

LOAD DATA LOCAL INPATH '/project2/msca/mtoolsidas/data_mining/yelp_dataset/df_checkin.csv' OVERWRITE INTO TABLE checkin;
"""

# Run queries
hive -e "${create_load_table_q}"


#-----------------------------------------------------------




# Remove local/Linux files
# rm /project2/msca/mtoolsidas/data_mining/yelp_dataset/*


