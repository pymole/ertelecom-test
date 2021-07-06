WITH address_life_span AS (
    SELECT address_insertion.id, address_insertion.inserted, address_deletion.deleted FROM (
        SELECT id, changed_at as inserted
        FROM address_history
        WHERE operation='INSERT'
    ) address_insertion LEFT JOIN (
        SELECT id, changed_at as deleted
        FROM address_history
        WHERE operation='DELETE'
    ) address_deletion
    ON address_insertion.id = address_deletion.id
), monthes as (
	SELECT date_trunc('month', monthes_from_now)::date as month
	FROM generate_series(
		now() - INTERVAL '2 YEARS',
		now(),
		INTERVAL '1 month'
	) monthes_from_now
)

SELECT monthes.month, CASE WHEN addresses_count IS NULL THEN 0 ELSE addresses_count END
FROM monthes
LEFT JOIN (
	SELECT month, count(*) as addresses_count
	FROM monthes
	INNER JOIN address_life_span
	ON address_life_span.inserted < monthes.month + INTERVAL '1 month'
		AND (address_life_span.deleted IS NULL OR address_life_span.deleted > monthes.month + INTERVAL '1 month')
	GROUP BY month
	ORDER BY month
) monthes_addresses_count ON monthes.month = monthes_addresses_count.month