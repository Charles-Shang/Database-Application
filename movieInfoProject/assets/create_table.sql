USE sampledb;

CREATE TABLE Person (
	id INTEGER NOT NULL,
	username VARCHAR(25) NOT NULL,
	pwd VARCHAR(25) NOT NULL,
	last_log_in TIMESTAMP NOT NULL,
	PRIMARY KEY(id)
);

CREATE TABLE Employee (
	id INTEGER NOT NULL,
	salary NUMERIC(8,2) NOT NULL,
	working_hours NUMERIC(3,1) NOT NULL,
	FOREIGN KEY (id) REFERENCES Person(id),
	PRIMARY KEY (id)
);

CREATE TABLE Permission (
	id INTEGER NOT NULL,
	name VARCHAR(50) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE Permits (
	employee_id INTEGER NOT NULL,
	permission_id INTEGER NOT NULL,
	FOREIGN KEY (employee_id) REFERENCES Employee(id),
	FOREIGN KEY (permission_id) REFERENCES Permission(id),
	PRIMARY KEY (employee_id, permission_id)
);


CREATE TABLE User (
	id INTEGER NOT NULL,
	activeness INTEGER NOT NULL,
	level VARCHAR(25) NOT NULL,
	FOREIGN KEY (id) REFERENCES Person(id),
	PRIMARY KEY (id)
);

CREATE TABLE Celebrity (
	id INTEGER NOT NULL,
	name VARCHAR(150) NOT NULL,
	nationality VARCHAR(150),
	birth DATE,
	summary TEXT,
  	PRIMARY KEY (id)
);

CREATE TABLE Director (
	id INTEGER NOT NULL,
	graduation VARCHAR(100),
	FOREIGN KEY (id) REFERENCES Celebrity(id),
	PRIMARY KEY (id)
);

CREATE TABLE Actor (
	id INTEGER NOT NULL,
	organization VARCHAR(100),
	FOREIGN KEY (id) REFERENCES Celebrity(id),
	PRIMARY KEY (id)
);


CREATE TABLE Movie (
	id INTEGER NOT NULL,
	name VARCHAR(150) NOT NULL,
	region VARCHAR(100),
	year INTEGER CHECK(
		year >= 1800
		AND year <= 2023
	),
	introduction TEXT,
	avg_rate NUMERIC(3,1) DEFAULT 0,
	director_id INTEGER NOT NULL,
	FOREIGN KEY (director_id) REFERENCES Director(id),
	PRIMARY KEY (id)
);

CREATE TABLE Acts(
	actor_id INTEGER NOT NULL,
	movie_id INTEGER NOT NULL,
	FOREIGN KEY (actor_id) REFERENCES Actor(id),
	FOREIGN KEY (movie_id) REFERENCES Movie(id),
	PRIMARY KEY (actor_id, movie_id)
);

CREATE TABLE RateBy(
	movie_id INTEGER NOT NULL,
	user_id INTEGER NOT NULL,
	FOREIGN KEY (movie_id) REFERENCES Movie(id),
	FOREIGN KEY (user_id) REFERENCES User(id),
	PRIMARY KEY (movie_id, user_id)
);


CREATE TABLE Rating (
	id INTEGER NOT NULL,
	time TIMESTAMP NOT NULL,
	value INTEGER NOT NULL CHECK(
		value >= 0
		AND value <= 10
	),
	comment TEXT,
	movie_id INTEGER NOT NULL,
	user_id INTEGER NOT NULL,
	FOREIGN KEY (movie_id, user_id) REFERENCES RateBy(movie_id, user_id),
	PRIMARY KEY (id)
);

CREATE TABLE Movie_category(
	movie_id INTEGER NOT NULL,
	category VARCHAR(50) NOT NULL,
	FOREIGN KEY (movie_id) REFERENCES Movie(id),
	PRIMARY KEY (movie_id, category)
);

CREATE TABLE Director_famousMovie(
	director_id INTEGER NOT NULL,
	movie_id INTEGER NOT NULL,
	FOREIGN KEY (director_id) REFERENCES Director(id),
	FOREIGN KEY (movie_id) REFERENCES Movie(id),
	PRIMARY KEY (director_id, movie_id)
);

