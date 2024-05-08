-- Creates an index idx_name_first on a
-- table names and the first letter of name.
-- @author sebsibe solomon https://github.com/sebsibe23
CREATE INDEX idx_name_first ON names(name(1));
