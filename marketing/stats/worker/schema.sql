CREATE TABLE IF NOT EXISTS hits (
  day      TEXT NOT NULL,          -- Perth date, YYYY-MM-DD
  event    TEXT NOT NULL,          -- view | book | call | email | instagram | review | maps
  path     TEXT NOT NULL,          -- page the event happened on, without .html
  ref      TEXT NOT NULL,          -- where the visit came from: google, instagram, direct, a hostname...
  dev      TEXT NOT NULL,          -- phone | desktop
  n        INTEGER NOT NULL DEFAULT 0,   -- how many times
  sessions INTEGER NOT NULL DEFAULT 0,   -- how many of those were the first page of a visit
  PRIMARY KEY (day, event, path, ref, dev)
);
