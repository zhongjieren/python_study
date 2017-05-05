createlang plpgsql DataCenter


--创建表空间

--日志
CREATE TABLESPACE data_log
  OWNER saligia
  LOCATION '/Users/saligia/postgresql_data/data/log';

--日报数据
CREATE TABLESPACE data_daily
  OWNER saligia
  LOCATION '/Users/saligia/postgresql_data/data/daily';

--分笔数据
CREATE TABLESPACE data_tick
  OWNER saligia
  LOCATION '/Users/saligia/postgresql_data/data/tick';

--财务数据
CREATE TABLESPACE data_financial
  OWNER saligia
  LOCATION '/Users/saligia/postgresql_data/data/financial';

--主体数据
CREATE TABLESPACE data_main
  OWNER saligia
  LOCATION '/Users/saligia/postgresql_data/data/main';

--新闻数据
CREATE TABLESPACE data_news
  OWNER saligia
  LOCATION '/Users/saligia/postgresql_data/data/news';

--报表数据
CREATE TABLESPACE data_report
  OWNER saligia
  LOCATION '/Users/saligia/postgresql_data/data/report';


--日报数据索引表空间
CREATE TABLESPACE index_daily
  OWNER saligia
  LOCATION '/Users/saligia/postgresql_data/index/daily';

--分笔数据索引表空间
CREATE TABLESPACE index_tick
  OWNER saligia
  LOCATION '/Users/saligia/postgresql_data/index/tick';

