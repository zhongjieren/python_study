-- ----------------------------
--  Table structure for m_finance_type
-- ----------------------------
DROP TABLE IF EXISTS "public"."m_finance_type";
CREATE TABLE "public"."m_finance_type" (
	"id" serial NOT NULL,
	"name" varchar(50) NOT NULL DEFAULT '',
	"alias" varchar(50) NOT NULL DEFAULT '',
	"status" int2 NOT NULL DEFAULT 1,
	"remove" bool NOT NULL DEFAULT false,
	"create_time" timestamp(6) NOT NULL DEFAULT now()
)
WITH (OIDS=FALSE)
TABLESPACE "data_main";
ALTER TABLE "public"."m_finance_type" OWNER TO "saligia";

COMMENT ON TABLE "public"."m_finance_type" IS '金融类别';

COMMENT ON COLUMN "public"."m_finance_type"."id" IS '类型主键';
COMMENT ON COLUMN "public"."m_finance_type"."name" IS '名称';
COMMENT ON COLUMN "public"."m_finance_type"."alias" IS '别名';
COMMENT ON COLUMN "public"."m_finance_type"."status" IS '状态 1:正常';
COMMENT ON COLUMN "public"."m_finance_type"."remove" IS '是否删除数据';
COMMENT ON COLUMN "public"."m_finance_type"."create_time" IS '创建时间';

-- ----------------------------
--  Primary key structure for table m_finance_type
-- ----------------------------
ALTER TABLE "public"."m_finance_type" ADD PRIMARY KEY ("id") NOT DEFERRABLE INITIALLY IMMEDIATE;


-- ----------------------------
--  Triggers structure for table m_finance_type
-- ----------------------------
CREATE TRIGGER "trigger_m_finance_type_log" AFTER DELETE OR UPDATE ON "public"."m_finance_type" FOR EACH ROW EXECUTE PROCEDURE "table_change_log"(m_finance_type);
COMMENT ON TRIGGER "trigger_m_finance_type_log" ON "public"."m_finance_type" IS '操作日志';

INSERT INTO m_finance_type ("id","name","alias") VALUES(1,'大陆股票','沪深股市');
INSERT INTO m_finance_type ("id","name","alias") VALUES(2,'香港股市','港股');
INSERT INTO m_finance_type ("id","name","alias") VALUES(3,'美国股市','美股');
INSERT INTO m_finance_type ("id","name","alias") VALUES(4,'基金','基金');
INSERT INTO m_finance_type ("id","name","alias") VALUES(5,'期货','期货');
INSERT INTO m_finance_type ("id","name","alias") VALUES(6,'现货','现货');
INSERT INTO m_finance_type ("id","name","alias") VALUES(7,'外汇','外汇');
INSERT INTO m_finance_type ("id","name","alias") VALUES(8,'黄金','黄金');
INSERT INTO m_finance_type ("id","name","alias") VALUES(9,'债券','债券');
INSERT INTO m_finance_type ("id","name","alias") VALUES(10,'全球指数','全球指数');








