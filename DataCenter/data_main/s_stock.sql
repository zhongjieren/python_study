-- ----------------------------
--  Table structure for s_stock
-- ----------------------------
DROP TABLE IF EXISTS "public"."s_stock";
CREATE TABLE "public"."s_stock" (
	"id" serial NOT NULL,
	"stock_type_id" int4 NOT NULL DEFAULT 0 REFERENCES s_stock_type (id),
	"code" varchar(50) NOT NULL DEFAULT '',
	"name" varchar(200) NOT NULL DEFAULT '',
	"alias" varchar(200) NOT NULL DEFAULT '',
  	"initials" varchar(200) NOT NULL DEFAULT '',
	"status" int2 NOT NULL DEFAULT 1,
	"remove" bool NOT NULL DEFAULT false,
	"create_time" timestamp(6) NOT NULL DEFAULT now()
)
WITH (OIDS=FALSE)
TABLESPACE "data_main";
ALTER TABLE "public"."s_stock" OWNER TO "saligia";

COMMENT ON TABLE "public"."s_stock" IS '股票';

COMMENT ON COLUMN "public"."s_stock"."id" IS '股票主键';
COMMENT ON COLUMN "public"."s_stock"."stock_type_id" IS '股票类型编号';
COMMENT ON COLUMN "public"."s_stock"."code" IS '代码';
COMMENT ON COLUMN "public"."s_stock"."name" IS '股票名称';
COMMENT ON COLUMN "public"."s_stock"."alias" IS '股票别名如英文名';
COMMENT ON COLUMN "public"."s_stock"."initials" IS '首字母';
COMMENT ON COLUMN "public"."s_stock"."status" IS '状态 1:正常,2:第一天上市,3:退市';
COMMENT ON COLUMN "public"."s_stock"."remove" IS '是否删除数据';
COMMENT ON COLUMN "public"."s_stock"."create_time" IS '创建时间';

-- ----------------------------
--  Primary key structure for table s_stock
-- ----------------------------
ALTER TABLE "public"."s_stock" ADD PRIMARY KEY ("id") NOT DEFERRABLE INITIALLY IMMEDIATE;

-- ----------------------------
--  Indexes structure for table s_stock
-- ----------------------------
CREATE UNIQUE INDEX  "idx_s_stock_type_code" ON "public"."s_stock" USING btree(stock_type_id ASC NULLS LAST, code COLLATE "default" ASC NULLS LAST);

-- ----------------------------
--  Triggers structure for table s_stock
-- ----------------------------
CREATE TRIGGER "trigger_s_stock_log" AFTER DELETE OR UPDATE ON "public"."s_stock" FOR EACH ROW EXECUTE PROCEDURE "table_change_log"(s_stock);
COMMENT ON TRIGGER "trigger_s_stock_log" ON "public"."s_stock" IS '操作日志';








