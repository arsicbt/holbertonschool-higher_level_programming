-- Selectionner les infos nécessaires
SELECT id, name FROM cities WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
