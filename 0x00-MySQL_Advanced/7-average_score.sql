-- calculating average score for students and save it
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avrg FLOAT;
	SET avrg = (SELECT AVG(score) FROM corrections AS C WHERE C.user_id=user_id);
	UPDATE users SET average_score = avrg WHERE id=user_id;
END $$
DELIMITER ;
