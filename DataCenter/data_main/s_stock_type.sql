-- ----------------------------
--  Table structure for s_stock_type
-- ----------------------------
DROP TABLE IF EXISTS "public"."s_stock_type";
CREATE TABLE "public"."s_stock_type" (
	"id" serial NOT NULL,
	"finance_type_id" int4 NOT NULL DEFAULT 1 REFERENCES m_finance_type (id),
	"code" varchar(50) NOT NULL DEFAULT '',
	"name" varchar(50) NOT NULL DEFAULT '',
	"alias" varchar(50) NOT NULL DEFAULT '',
	"status" int2 NOT NULL DEFAULT 1,
	"remove" bool NOT NULL DEFAULT false,
	"create_time" timestamp(6) NOT NULL DEFAULT now()
)
WITH (OIDS=FALSE)
TABLESPACE "data_main";
ALTER TABLE "public"."s_stock_type" OWNER TO "saligia";

COMMENT ON TABLE "public"."s_stock_type" IS '股票类型';

COMMENT ON COLUMN "public"."s_stock_type"."id" IS '类型主键';
COMMENT ON COLUMN "public"."s_stock_type"."finance_type_id" IS '金融类别编号';
COMMENT ON COLUMN "public"."s_stock_type"."code" IS '代码';
COMMENT ON COLUMN "public"."s_stock_type"."name" IS '名称';
COMMENT ON COLUMN "public"."s_stock_type"."alias" IS '别名';
COMMENT ON COLUMN "public"."s_stock_type"."status" IS '状态 1:正常';
COMMENT ON COLUMN "public"."s_stock_type"."remove" IS '是否删除数据';
COMMENT ON COLUMN "public"."s_stock_type"."create_time" IS '创建时间';

-- ----------------------------
--  Primary key structure for table s_stock_type
-- ----------------------------
ALTER TABLE "public"."s_stock_type" ADD PRIMARY KEY ("id") NOT DEFERRABLE INITIALLY IMMEDIATE;

-- ----------------------------
--  Triggers structure for table s_stock_type
-- ----------------------------
CREATE TRIGGER "trigger_s_stock_type_log" AFTER DELETE OR UPDATE ON "public"."s_stock_type" FOR EACH ROW EXECUTE PROCEDURE "table_change_log"(s_stock_type);
COMMENT ON TRIGGER "trigger_s_stock_type_log" ON "public"."s_stock_type" IS '操作日志';


INSERT INTO s_stock_type ("id","finance_type_id","code","name","alias") VALUES(1,1,'sh','上证A股','沪市A股');
INSERT INTO s_stock_type ("id","finance_type_id","code","name","alias") VALUES(2,1,'sh','上证B股','沪市B股');
INSERT INTO s_stock_type ("id","finance_type_id","code","name","alias") VALUES(3,1,'sz','深证A股','深市A股');
INSERT INTO s_stock_type ("id","finance_type_id","code","name","alias") VALUES(4,1,'sz','深证B股','深市B股');
INSERT INTO s_stock_type ("id","finance_type_id","code","name","alias") VALUES(5,2,'hk','港股','港股');
INSERT INTO s_stock_type ("id","finance_type_id","code","name","alias") VALUES(6,3,'us','纽约交易所','纽交所');
INSERT INTO s_stock_type ("id","finance_type_id","code","name","alias") VALUES(7,3,'us','纳斯达克交易所','纳斯达克');
INSERT INTO s_stock_type ("id","finance_type_id","code","name","alias") VALUES(8,3,'us','美国交易所','美交所');










