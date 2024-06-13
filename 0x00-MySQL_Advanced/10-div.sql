-- function that divides 2 int but if the dominator = 0 return 0
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	IF b = 0
	THEN
		RETURN (0)
	ELSE
		RETURN (a / b)
	END IF;
END $$
DELIMITER ;
