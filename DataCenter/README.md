# DataCenter
数据结构


##主键
必须命名id 类型必须为 serial

ALTER TABLE "public"."table_name" ADD PRIMARY KEY ("column_name") NOT DEFERRABLE INITIALLY IMMEDIATE;

##自增长类型
serial 例如： id serial NOT NULL,