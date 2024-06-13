-- claculate the average weight score for stds that don't take any input
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users
        (SELECT users.id, SUM(score * weight) / SUM(weight) AS w_avg
        FROM users
        JOIN corrections as C ON users.id=C.user_id
        JOIN projects AS P ON C.project_id=P.id
        GROUP BY users.id)
    AS WA
    SET users.average_score = WA.w_avg
    WHERE users.id=WA.id;
END $$
DELIMITER ;
