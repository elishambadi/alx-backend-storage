-- Average score
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
  DECLARE total_score INT;
  DECLARE total_corrections INT;
  
  SELECT SUM(score), COUNT(*) INTO total_score, total_corrections
  FROM corrections
  WHERE user_id = user_id;
  
  IF total_corrections > 0 THEN
    UPDATE users
    SET average_score = total_score / total_corrections
    WHERE id = user_id;
  END IF;
END;
//
DELIMITER ;
