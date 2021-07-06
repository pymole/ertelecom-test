CREATE OR REPLACE FUNCTION history()
	RETURNS TRIGGER
	LANGUAGE plpgsql
as $function$
	BEGIN
        IF (TG_OP = 'DELETE') THEN
            EXECUTE format($$INSERT INTO %I VALUES($1.*, 'DELETE', now())$$, concat(TG_TABLE_NAME, '_history')) USING OLD;
            RETURN OLD;
	    ELSE
            EXECUTE format($$INSERT INTO %I VALUES($1.*, %L, now())$$, concat(TG_TABLE_NAME, '_history'), TG_OP) USING NEW;
            RETURN NEW;
        END IF;
	END;
$function$
