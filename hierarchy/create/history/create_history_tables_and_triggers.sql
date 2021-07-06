do language plpgsql
$f$DECLARE
    origin_name text;
    history_name text;
	history_trigger_name text;
BEGIN
    FOR origin_name IN
        (select tablename from pg_tables
       		where schemaname='public' AND tablename NOT LIKE '%_history')
    LOOP
        history_name := format('%s_history', origin_name);
        raise notice 'Table: %', origin_name;
        
		-- Create history table
        EXECUTE format(
            $$CREATE TABLE IF NOT EXISTS %I (
                LIKE %I,
                -- delete, update, insert: every operation contains 6 charecters
                operation CHAR(6),
                changed_at timestamp
            )$$,
            history_name, origin_name);
        
        -- Create trigger
		history_trigger_name := format('trigger_update_%s', history_name);
        EXECUTE format(
            $$
			DROP TRIGGER IF EXISTS %I on "public".%I;
			CREATE TRIGGER %I
                BEFORE INSERT OR UPDATE OR DELETE ON %I
                FOR EACH ROW EXECUTE PROCEDURE history()$$,
            history_trigger_name, origin_name, history_trigger_name, origin_name);

    end loop;
end;$f$;