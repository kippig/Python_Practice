SELECT
    tenantID,
    COUNT(DISTINCT apartmentID) as apartments
FROM
    table1
GROUP BY 1
HAVING
    apartments > 1
