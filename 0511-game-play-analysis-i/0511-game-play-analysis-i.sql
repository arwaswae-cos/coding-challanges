# Write your MySQL query statement below
SELECT DISTINCT a.player_id, a.event_date as first_login
FROM Activity a
WHERE a.event_date = (SELECT min(ac.event_date)
FROM Activity ac
WHERE a.player_id = ac.player_id)