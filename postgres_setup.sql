CREATE USER voteapp WITH PASSWORD 'VotePassword';

CREATE DATABASE vote;

GRANT ALL PRIVILEGES ON DATABASE vote to voteapp;
