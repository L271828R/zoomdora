DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS user_type;
DROP TABLE IF EXISTS user_profile_ref;
DROP TABLE IF EXISTS profile;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS country_code;
DROP TABLE IF EXISTS payment_method;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  payment_method INTEGER,   
  user_type INTEGER,
  user_profile_ref INTEGER
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);


CREATE TABLE user_type(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(30)
);

INSERT INTO user_type (name) VALUES ("buyer"); 
INSERT INTO user_type (name) VALUES ("seller"); 


CREATE TABLE user_profile_ref( 
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  profile_id INTEGER
);

CREATE TABLE profile (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  description TEXT NOT NULL
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30)
);

INSERT INTO categories (name) VALUES ("music");
INSERT INTO categories (name) VALUES ("IT");
INSERT INTO categories (name) VALUES ("teaching");

CREATE TABLE country_code(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30)
);

INSERT INTO country_code(name) VALUES ("US");

CREATE TABLE payment_methods(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30)
);

INSERT INTO payment_methods(name) VALUES ("paypal");


