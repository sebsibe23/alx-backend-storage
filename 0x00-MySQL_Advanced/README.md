0x00. MySQL Advanced

Welcome to the 0x00. MySQL Advanced project!

Project Overview

This project delves into advanced MySQL concepts, equipping you with the skills to optimize database performance and create powerful database interactions.

Key Concepts

Advanced SQL queries
MySQL indexing for query optimization
Stored Procedures: Streamline complex operations
Functions: Reusable logic for database tasks
Triggers: Automated actions based on events
Views: Virtual tables offering simplified data access
Learning Objectives

By the end of this project, you'll be able to:

Design tables with constraints for robust data integrity.
Strategically implement indexes to dramatically improve query performance.
Create and utilize stored procedures and functions for efficient database interaction.
Leverage views to simplify complex data retrieval for users.
Develop triggers to automate database actions based on events.
Project Timeline

Start Date: May 8, 2024, 6:00 AM
Checker Release: May 8, 2024, 6:00 PM
Deadline: May 10, 2024, 6:00 AM (Auto-review)
Development Environment

Operating System: Ubuntu 18.04 LTS
MySQL Version: 5.7 (version 5.7.30)
Requirements

All SQL files must end with a newline character.
Each query should be preceded by a clear comment explaining its purpose.
Every file should begin with a comment outlining the task it accomplishes.
Use uppercase for SQL keywords (SELECT, WHERE, etc.).
A mandatory README.md file is required at the project's root directory.
File lengths will be assessed using wc.
Commenting Guidelines

Adopt a clear and informative commenting style, similar to the example below:

SQL
-- Retrieve the 3 most recently created students in Batch ID 3 (the best batch!).
SELECT id, name
FROM students
WHERE batch_id = 3
ORDER BY created_at DESC
LIMIT 3;
Use code with caution.
content_copy
MySQL Setup

Utilize "container-on-demand" to run MySQL.

Request a container with Ubuntu 18.04 and Python 3.7.

Connect through SSH or WebTerminal.

Within the container, initiate MySQL:

Bash
service mysql start
Use code with caution.
content_copy
Verify successful startup:

Bash
# Output should indicate MySQL Community Server 5.7.30 is started
Use code with caution.
content_copy
Import an SQL dump (optional):

Bash
# Create a database named hbtn_0d_tvshows
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p

# Download and import the hbtn_0d_tvshows.sql dump
curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows

# Verify the import
echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows

# Expected output:
# id | name
#---|---|
# 1  | Drama
# 2  | Mystery
# ... (other genres)
