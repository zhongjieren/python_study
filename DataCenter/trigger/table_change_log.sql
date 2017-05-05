-- Function: table_change_log()

-- DROP FUNCTION table_change_log();

CREATE OR REPLACE FUNCTION table_change_log()
  RETURNS trigger AS
$BODY$
DECLARE
  VAR_TABLE VARCHAR(100);
  VAR_ACTION VARCHAR(50);
  VAR_DATA TEXT;
  VAR_CREATE_TIME TIMESTAMP;
  BEGIN
    IF( TG_OP='UPDATE' OR TG_OP='DELETE' ) THEN
      VAR_TABLE := TG_ARGV[0];
      VAR_ACTION :=TG_OP;
      VAR_DATA := OLD;
      VAR_CREATE_TIME := now();
            
      INSERT INTO l_change_log ("table","action","data","create_time") VALUES (VAR_TABLE,VAR_ACTION,VAR_DATA,VAR_CREATE_TIME);
    END IF;
    RETURN NULL;
  END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION table_change_log()
  OWNER TO saligia;
