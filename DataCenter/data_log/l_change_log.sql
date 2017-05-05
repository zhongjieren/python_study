-- ----------------------------
--  Table structure for l_change_log
-- ----------------------------
DROP TABLE IF EXISTS "public"."l_change_log";
CREATE TABLE "public"."l_change_log" (
	"id" serial NOT NULL,
	"table" varchar(100) NOT NULL DEFAULT '',
	"action" varchar(50) NOT NULL DEFAULT '',
	"data" text NOT NULL DEFAULT '',
	"create_time" timestamp(6) NOT NULL DEFAULT now()
)
WITH (OIDS=FALSE)
TABLESPACE "data_log";
ALTER TABLE "public"."l_change_log" OWNER TO "saligia";

COMMENT ON TABLE "public"."l_change_log" IS '数据变更日志';

COMMENT ON COLUMN "public"."l_change_log"."id" IS '类型主键';
COMMENT ON COLUMN "public"."l_change_log"."table" IS '数据表';
COMMENT ON COLUMN "public"."l_change_log"."action" IS '操作';
COMMENT ON COLUMN "public"."l_change_log"."data" IS '数据';
COMMENT ON COLUMN "public"."l_change_log"."create_time" IS '创建时间';

-- ----------------------------
--  Primary key structure for table l_change_log
-- ----------------------------
ALTER TABLE "public"."l_change_log" ADD PRIMARY KEY ("id") NOT DEFERRABLE INITIALLY IMMEDIATE;

-- ----------------------------
--  Indexes structure for table l_change_log
-- ----------------------------
CREATE INDEX  "idx_l_change_log_create_time" ON "public"."l_change_log" USING btree(create_time ASC NULLS LAST);

