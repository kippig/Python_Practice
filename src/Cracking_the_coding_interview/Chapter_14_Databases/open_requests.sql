SELECT
    BuildingID,
    COUNT(DISTINCT requestID) as open_requests
FROM
    Buildings
WHERE
    request_status = 'open'