-- Add bonuse
DELIMITER //
CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score INT)
BEGIN
  INSERT INTO projects (name)
  VALUES (project_name)
  ON DUPLICATE KEY UPDATE name = name;
  
  INSERT INTO corrections (user_id, project_id, score)
  VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END;
//
DELIMITER ;
