-- Creates an index idx_name_first_score on a table names and
-- the first letter of name and a score.
-- @author sebsibe solomon https://github.com/sebsibe23
CREATE INDEX idx_name_first_score ON names(name(1), score);
