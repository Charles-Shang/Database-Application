CREATE TABLE USER (
  userID INTEGER,
  name VARCHAR(300) NOT NULL,
  PRIMARY KEY(userID)
);

CREATE TABLE MOVIE (
  movieID INTEGER,
  name VARCHAR(300) NOT NULL,
  region VARCHAR(30) NOT NULL,
  year INTEGER CHECK(
    year >= 1800
    and year <= 2023
  ),
  category VARCHAR(50) NOT NULL,
  rates DECIMAL(3, 1) NOT NULL default 0,
  summary TEXT,
  PRIMARY KEY(movieID)
);

CREATE TABLE RATES (
  rateID INTEGER,
  rate INTEGER NOT NULL CHECK(
    rate >= 1
    and rate <= 10
  ),
  movieID INTEGER NOT NULL,
  userID INTEGER NOT NULL,
  FOREIGN KEY (movieID) REFERENCES MOVIE(movieID),
  FOREIGN KEY (userID) REFERENCES USER(userID),
  PRIMARY KEY(rateID)
);

CREATE TABLE DIRECTOR (
  directorID INTEGER,
  name VARCHAR(300) NOT NULL,
  birthYear INTEGER,
  PRIMARY KEY(directorID)
);

CREATE TABLE DIRECTS (
  directorID INTEGER,
  movieID INTEGER NOT NULL,
  FOREIGN KEY (movieID) REFERENCES MOVIE (movieID),
  PRIMARY KEY (directorID, movieID)
);

CREATE TABLE ACTOR (
  actorID INTEGER,
  name VARCHAR(300) NOT NULL,
  birthYear INTEGER,
  PRIMARY KEY (actorID)
);

CREATE TABLE ACTS (
  actorID INTEGER,
  movieID INTEGER NOT NULL,
  FOREIGN KEY (actorID) REFERENCES ACTOR (actorID),
  FOREIGN KEY (movieID) REFERENCES MOVIE (movieID),
  PRIMARY KEY (actorID, movieID)
);