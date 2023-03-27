USE sampledb;

INSERT INTO
    Person (id, username, pwd, last_log_in)
VALUES
    (1, "employee1", "pwd1", "2022-11-11 12:33:45"),
    (2, "employee2", "pwd2", "2020-04-03 09:12:30"),
    (3, "employee3", "pwd3", "2020-11-02 06:41:01"),
    (4, "employee4", "pwd4", "2021-01-15 11:34:38"),
    (5, "employee5", "pwd5", "2022-07-17 19:51:02"),
    (6, "employee6", "pwd6", "2022-09-18 13:42:01"),
    (7, "employee7", "pwd7", "2020-09-02 10:16:50"),
    (8, "employee8", "pwd8", "2020-05-09 03:07:47"),
    (9, "employee9", "pwd9", "2021-05-25 00:12:56"),
    (10, "employee10", "pwd10", "2021-11-17 10:43:47"),
    (11, "employee11", "pwd11", "2020-04-10 12:18:06"),
    (12, "employee12", "pwd12", "2021-09-04 20:29:00"),
    (13, "employee13", "pwd13", "2022-03-16 16:06:40"),
    (14, "employee14", "pwd14", "2021-07-13 14:20:04"),
    (15, "employee15", "pwd15", "2020-10-03 20:41:34"),
    (16, "employee16", "pwd16", "2020-09-13 17:12:55"),
    (17, "employee17", "pwd17", "2021-01-06 22:00:44"),
    (18, "employee18", "pwd18", "2020-06-23 20:28:18"),
    (19, "employee19", "pwd19", "2020-01-07 00:32:53"),
    (20, "employee20", "pwd20", "2021-03-06 19:09:55"),
    (21, "user1", "pwd1", "2022-08-20 10:16:59"),
    (22, "user2", "pwd2", "2021-05-06 08:20:36"),
    (23, "user3", "pwd3", "2021-03-12 18:06:57"),
    (24, "user4", "pwd4", "2022-12-24 22:06:28"),
    (25, "user5", "pwd5", "2020-06-10 14:25:36"),
    (26, "user6", "pwd6", "2020-09-15 12:04:37"),
    (27, "user7", "pwd7", "2021-03-24 11:37:27"),
    (28, "user8", "pwd8", "2022-03-03 11:36:34"),
    (29, "user9", "pwd9", "2021-03-09 22:37:14"),
    (30, "user10", "pwd10", "2022-03-13 10:56:58"),
    (31, "user11", "pwd11", "2022-05-10 01:51:36"),
    (32, "user12", "pwd12", "2020-11-03 08:20:57"),
    (33, "user13", "pwd13", "2022-07-14 20:09:16"),
    (34, "user14", "pwd14", "2021-10-23 10:40:25"),
    (35, "user15", "pwd15", "2021-02-21 03:03:37"),
    (36, "user16", "pwd16", "2021-04-05 15:09:25"),
    (37, "user17", "pwd17", "2021-12-30 12:37:37"),
    (38, "user18", "pwd18", "2021-02-20 18:19:10"),
    (39, "user19", "pwd19", "2020-08-26 06:27:46"),
    (40, "user20", "pwd20", "2022-01-09 19:29:31");
    
INSERT INTO
    Permission (id, name)
VALUES
    (1, "permission1"),
    (2, "permission2"),
    (3, "permission3"),
    (4, "permission4"),
    (5, "permission5"),
    (6, "permission6"),
    (7, "permission7"),
    (8, "permission8"),
    (9, "permission9"),
    (10, "permission10");

INSERT INTO
    Employee (id, salary, working_hours)
VALUES
    (1, 3966.71, 38.6),
    (2, 4370.95, 37.1),
    (3, 4741.64, 37.9),
    (4, 3084.2, 37.9),
    (5, 3669.07, 36.0),
    (6, 3306.73, 36.5),
    (7, 4692.89, 36.9),
    (8, 3881.84, 37.5),
    (9, 3302.04, 39.0),
    (10, 3480.67, 37.8),
    (11, 3808.67, 35.1),
    (12, 4125.67, 39.0),
    (13, 3235.62, 37.9),
    (14, 4904.84, 39.7),
    (15, 3480.44, 38.7),
    (16, 4057.47, 36.1),
    (17, 4941.79, 38.7),
    (18, 4280.67, 37.1),
    (19, 4385.61, 39.7),
    (20, 4509.09, 37.1);

INSERT INTO
    Permits (employee_id, permission_id)
VALUES
    (1, 8),
    (2, 6),
    (3, 6),
    (4, 8),
    (5, 5),
    (6, 10),
    (7, 3),
    (8, 3),
    (9, 4),
    (10, 10),
    (11, 4),
    (12, 7),
    (13, 1),
    (14, 10),
    (15, 10),
    (16, 2),
    (17, 9),
    (18, 3),
    (19, 3),
    (20, 8),
    (20, 5),
    (2, 9),
    (16, 7),
    (15, 2),
    (20, 2),
    (6, 9),
    (13, 10),
    (15, 7),
    (12, 4),
    (17, 5);

INSERT INTO
    User (id, activeness, level)
VALUES
    (21, 4, "level1"),
    (22, 2, "level2"),
    (23, 7, "level1"),
    (24, 4, "level5"),
    (25, 4, "level1"),
    (26, 2, "level4"),
    (27, 18, "level2"),
    (28, 1, "level5"),
    (29, 37, "level4"),
    (30, 30, "level5"),
    (31, 16, "level2"),
    (32, 17, "level2"),
    (33, 12, "level4"),
    (34, 27, "level2"),
    (35, 23, "level1"),
    (36, 15, "level3"),
    (37, 1, "level1"),
    (38, 12, "level1"),
    (39, 4, "level1"),
    (40, 39, "level1");

INSERT INTO
    Celebrity (id, name, nationality, birth, summary)
VALUES
    (1, "director1", "nationality3", NULL, NULL),
    (2, "director2", NULL, NULL, "summary2"),
    (3, "director3", "nationality2", NULL, NULL),
    (4, "director4", NULL, NULL, NULL),
    (5, "director5", "nationality2", NULL, "summary5"),
    (6, "director6", NULL, "1953-06-15", "summary6"),
    (7, "director7", NULL, "2008-02-03", NULL),
    (8, "director8", NULL, "1979-07-01", "summary8"),
    (9, "director9", NULL, "1995-12-13", NULL),
    (10, "director10", NULL, "1953-10-06", NULL),
    (
        11,
        "director11",
        NULL,
        "1986-06-08",
        "summary11"
    ),
    (
        12,
        "director12",
        "nationality4",
        NULL,
        "summary12"
    ),
    (
        13,
        "director13",
        NULL,
        "1971-04-20",
        "summary13"
    ),
    (14, "director14", NULL, "1988-04-15", NULL),
    (15, "director15", NULL, NULL, NULL),
    (16, "director16", NULL, "1959-01-28", NULL),
    (17, "director17", NULL, NULL, NULL),
    (18, "director18", NULL, NULL, NULL),
    (19, "director19", NULL, NULL, NULL),
    (
        20,
        "director20",
        NULL,
        "1989-11-28",
        "summary20"
    ),
    (21, "actor1", NULL, NULL, NULL),
    (22, "actor2", NULL, NULL, NULL),
    (23, "actor3", NULL, "1953-04-02", "summary23"),
    (24, "actor4", NULL, "2004-03-17", NULL),
    (25, "actor5", "nationality6", "1972-12-05", NULL),
    (26, "actor6", NULL, "1997-09-18", NULL),
    (27, "actor7", NULL, "1953-10-24", NULL),
    (28, "actor8", "nationality4", NULL, NULL),
    (29, "actor9", NULL, NULL, "summary29"),
    (30, "actor10", NULL, NULL, "summary30"),
    (31, "actor11", "nationality6", NULL, NULL),
    (32, "actor12", NULL, "1969-01-28", "summary32"),
    (
        33,
        "actor13",
        "nationality8",
        "2003-08-30",
        "summary33"
    ),
    (34, "actor14", NULL, NULL, "summary34"),
    (
        35,
        "actor15",
        "nationality6",
        "2020-11-03",
        NULL
    ),
    (36, "actor16", NULL, NULL, "summary36"),
    (37, "actor17", NULL, NULL, "summary37"),
    (38, "actor18", NULL, "1976-10-31", NULL),
    (39, "actor19", NULL, NULL, "summary39"),
    (40, "actor20", NULL, "1966-10-26", NULL),
    (41, "actor21", NULL, NULL, NULL),
    (42, "actor22", "nationality5", NULL, NULL),
    (43, "actor23", NULL, NULL, NULL),
    (
        44,
        "actor24",
        "nationality4",
        "1966-09-08",
        "summary44"
    ),
    (
        45,
        "actor25",
        "nationality10",
        "2016-01-31",
        NULL
    ),
    (46, "actor26", NULL, NULL, "summary46"),
    (47, "actor27", "nationality5", NULL, "summary47"),
    (48, "actor28", NULL, "2017-07-13", "summary48"),
    (
        49,
        "actor29",
        "nationality4",
        "2019-11-30",
        NULL
    ),
    (50, "actor30", NULL, "2002-04-22", NULL),
    (51, "actor31", NULL, NULL, "summary51"),
    (52, "actor32", NULL, "1984-02-27", "summary52"),
    (53, "actor33", NULL, "1996-06-27", NULL),
    (54, "actor34", "nationality2", NULL, "summary54"),
    (55, "actor35", NULL, NULL, "summary55"),
    (
        56,
        "actor36",
        "nationality4",
        "2006-02-17",
        NULL
    ),
    (57, "actor37", NULL, "2020-05-03", NULL),
    (58, "actor38", NULL, "1984-01-27", NULL),
    (
        59,
        "actor39",
        "nationality6",
        "1988-11-20",
        NULL
    ),
    (60, "actor40", NULL, NULL, "summary60");


INSERT INTO
    Director (id, graduation)
VALUES
    (1, "school10"),
    (2, "school1"),
    (3, NULL),
    (4, NULL),
    (5, NULL),
    (6, "school4"),
    (7, "school4"),
    (8, "school2"),
    (9, "school1"),
    (10, "school4"),
    (11, NULL),
    (12, NULL),
    (13, "school2"),
    (14, NULL),
    (15, "school1"),
    (16, "school6"),
    (17, "school3"),
    (18, NULL),
    (19, "school3"),
    (20, NULL);
 
INSERT INTO
    Movie (id, name, region, YEAR, introduction, avg_rate, director_id)
VALUES
    (1, "movie1", "region26", 1879, "introduction1", 0.0, 1),
    (2, "movie2", "region2", 2003, "introduction2", 0.0, 2),
    (3, "movie3", "region19", 1833, "introduction3", 0.0, 3),
    (4, "movie4", "region8", 1899, "introduction4", 0.0, 4),
    (5, "movie5", "region23", 1964, "introduction5", 0.0, 5),
    (6, "movie6", "region11", 1909, "introduction6", 0.0, 6),
    (7, "movie7", "region8", 1861, "introduction7", 0.0, 7),
    (8, "movie8", "region35", 1943, "introduction8", 0.0, 8),
    (9, "movie9", "region20", 1998, "introduction9", 0.0, 9),
    (10, "movie10", "region26", 1817, "introduction10", 0.0, 10),
    (11, "movie11", "region31", 1980, "introduction11", 0.0, 11),
    (12, "movie12", "region14", 1814, "introduction12", 0.0, 12),
    (13, "movie13", "region39", 1930, "introduction13", 0.0, 13),
    (14, "movie14", "region34", 1969, "introduction14", 0.0, 14),
    (15, "movie15", "region12", 2003, "introduction15", 0.0, 15),
    (16, "movie16", "region16", 1979, "introduction16", 0.0, 16),
    (17, "movie17", "region17", 1933, "introduction17", 0.0, 17),
    (18, "movie18", "region29", 2006, "introduction18", 0.0, 18),
    (19, "movie19", "region35", 1963, "introduction19", 0.0, 19),
    (20, "movie20", "region7", 1837, "introduction20", 0.0, 20),
    (21, "movie21", "region27", 1813, "introduction21", 0.0, 13),
    (22, "movie22", "region24", 2000, "introduction22", 0.0, 2),
    (23, "movie23", "region25", 1865, "introduction23", 0.0, 19),
    (24, "movie24", "region31", 1810, "introduction24", 0.0, 4),
    (25, "movie25", "region28", 1889, "introduction25", 0.0, 20),
    (26, "movie26", "region39", 1857, "introduction26", 0.0, 4),
    (27, "movie27", "region30", 1910, "introduction27", 0.0, 12),
    (28, "movie28", "region25", 1972, "introduction28", 0.0, 7),
    (29, "movie29", "region30", 1862, "introduction29", 0.0, 6),
    (30, "movie30", "region14", 1823, "introduction30", 0.0, 7),
    (31, "movie31", "region9", 1974, "introduction31", 0.0, 14),
    (32, "movie32", "region18", 1971, "introduction32", 0.0, 5),
    (33, "movie33", "region39", 1951, "introduction33", 0.0, 7),
    (34, "movie34", "region3", 1900, "introduction34", 0.0, 3),
    (35, "movie35", "region17", 1859, "introduction35", 0.0, 19),
    (36, "movie36", "region7", 1810, "introduction36", 0.0, 7),
    (37, "movie37", "region13", 1884, "introduction37", 0.0, 3),
    (38, "movie38", "region13", 1888, "introduction38", 0.0, 7),
    (39, "movie39", "region13", 1812, "introduction39", 0.0, 8),
    (40, "movie40", "region37", 1815, "introduction40", 0.0, 8);

INSERT INTO
    Movie_category (movie_id, category)
VALUES
    (1, "category10"),
    (2, "category3"),
    (3, "category5"),
    (4, "category4"),
    (5, "category5"),
    (6, "category6"),
    (7, "category7"),
    (8, "category2"),
    (9, "category5"),
    (10, "category7"),
    (11, "category4"),
    (12, "category2"),
    (13, "category3"),
    (14, "category7"),
    (15, "category9"),
    (16, "category6"),
    (17, "category7"),
    (18, "category9"),
    (19, "category8"),
    (20, "category9"),
    (21, "category4"),
    (22, "category10"),
    (23, "category2"),
    (24, "category1"),
    (25, "category6"),
    (26, "category8"),
    (27, "category1"),
    (28, "category8"),
    (29, "category2"),
    (30, "category9"),
    (31, "category2"),
    (32, "category2"),
    (33, "category7"),
    (34, "category5"),
    (35, "category4"),
    (36, "category6"),
    (37, "category4"),
    (38, "category4"),
    (39, "category4"),
    (40, "category4"),
    (20, "category10"),
    (23, "category5"),
    (40, "category7"),
    (26, "category6"),
    (2, "category2"),
    (18, "category8"),
    (40, "category10"),
    (16, "category7"),
    (33, "category8"),
    (20, "category6"),
    (39, "category10"),
    (14, "category8"),
    (11, "category5"),
    (10, "category6"),
    (15, "category1"),
    (5, "category2"),
    (2, "category6"),
    (17, "category6"),
    (23, "category10"),
    (14, "category2");
    
INSERT INTO
    Actor (id, organization)
VALUES
    (21, "organization8"),
    (22, NULL),
    (23, NULL),
    (24, NULL),
    (25, NULL),
    (26, "organization1"),
    (27, "organization8"),
    (28, NULL),
    (29, NULL),
    (30, NULL),
    (31, NULL),
    (32, "organization3"),
    (33, "organization12"),
    (34, NULL),
    (35, NULL),
    (36, NULL),
    (37, "organization2"),
    (38, NULL),
    (39, "organization15"),
    (40, "organization20"),
    (41, NULL),
    (42, NULL),
    (43, NULL),
    (44, "organization6"),
    (45, NULL),
    (46, "organization14"),
    (47, NULL),
    (48, "organization6"),
    (49, "organization16"),
    (50, "organization4"),
    (51, NULL),
    (52, "organization15"),
    (53, NULL),
    (54, NULL),
    (55, "organization7"),
    (56, NULL),
    (57, "organization20"),
    (58, "organization1"),
    (59, "organization3"),
    (60, NULL);
 
INSERT INTO
    Acts (actor_id, movie_id)
VALUES
    (21, 40),
    (22, 39),
    (23, 38),
    (24, 37),
    (25, 36),
    (26, 35),
    (27, 34),
    (28, 33),
    (29, 32),
    (30, 31),
    (31, 30),
    (32, 29),
    (33, 28),
    (34, 27),
    (35, 26),
    (36, 25),
    (37, 24),
    (38, 23),
    (39, 22),
    (40, 21),
    (41, 20),
    (42, 19),
    (43, 18),
    (44, 17),
    (45, 16),
    (46, 15),
    (47, 14),
    (48, 13),
    (49, 12),
    (50, 11),
    (51, 10),
    (52, 9),
    (53, 8),
    (54, 7),
    (55, 6),
    (56, 5),
    (57, 4),
    (58, 3),
    (59, 2),
    (25, 20),
    (42, 33),
    (47, 38),
    (54, 33),
    (42, 9),
    (60, 15),
    (41, 21),
    (50, 36),
    (36, 3),
    (56, 28),
    (54, 28),
    (21, 39),
    (58, 22),
    (25, 34),
    (52, 1),
    (33, 26),
    (44, 16),
    (52, 10),
    (43, 7),
    (52, 23),
    (45, 2),
    (58, 11),
    (36, 37),
    (36, 15),
    (26, 29),
    (32, 20),
    (38, 24),
    (23, 22),
    (46, 28),
    (28, 12),
    (34, 13),
    (31, 17),
    (32, 21),
    (40, 11),
    (33, 37),
    (31, 34),
    (45, 28),
    (60, 26),
    (32, 25),
    (37, 4);

INSERT INTO
    RateBy (movie_id, user_id)
VALUES
    (38, 22),
    (34, 38),
    (17, 29),
    (23, 36),
    (26, 31),
    (32, 35),
    (31, 35),
    (23, 21),
    (25, 26),
    (6, 39),
    (20, 24),
    (33, 33),
    (37, 32),
    (15, 21),
    (7, 34),
    (5, 21),
    (26, 25),
    (9, 24),
    (40, 25),
    (35, 38),
    (28, 34),
    (35, 33),
    (30, 27),
    (2, 28),
    (3, 27),
    (20, 39),
    (10, 25),
    (29, 39),
    (9, 37),
    (7, 39),
    (34, 30),
    (21, 29),
    (8, 34),
    (10, 34),
    (35, 26),
    (18, 31),
    (33, 25),
    (32, 36),
    (21, 35),
    (10, 39);

   INSERT INTO
    Rating (id, time, value, comment, movie_id, user_id)
VALUES
    (1, "2023-02-05 14:12:55", 9, "comment1", 38, 22),
    (2, "2023-02-13 06:23:00", 3, "comment2", 34, 38),
    (3, "2023-01-09 04:44:47", 1, "comment3", 17, 29),
    (4, "2023-02-05 09:23:02", 5, NULL, 23, 36),
    (5, "2023-02-21 19:29:26", 3, "comment5", 26, 31),
    (6, "2023-02-08 11:34:29", 9, "comment6", 32, 35),
    (7, "2023-02-05 14:34:12", 5, "comment7", 31, 35),
    (8, "2023-02-16 09:16:12", 1, "comment8", 23, 21),
    (9, "2023-01-23 18:17:28", 5, NULL, 25, 26),
    (10, "2023-01-04 12:08:58", 6, "comment10", 6, 39),
    (
        11,
        "2023-02-24 23:18:22",
        9,
        "comment11",
        20,
        24
    ),
    (
        12,
        "2023-01-06 12:02:24",
        10,
        "comment12",
        33,
        33
    ),
    (
        13,
        "2023-01-19 02:59:52",
        9,
        "comment13",
        37,
        32
    ),
    (
        14,
        "2023-01-26 08:02:24",
        8,
        "comment14",
        15,
        21
    ),
    (15, "2023-02-14 03:26:43", 6, NULL, 7, 34),
    (16, "2023-01-23 08:31:19", 9, NULL, 5, 21),
    (
        17,
        "2023-01-02 19:58:18",
        1,
        "comment17",
        26,
        25
    ),
    (18, "2023-02-17 04:43:44", 5, "comment18", 9, 24),
    (
        19,
        "2023-01-21 20:12:59",
        7,
        "comment19",
        40,
        25
    ),
    (20, "2023-01-06 18:27:39", 10, NULL, 35, 38),
    (
        21,
        "2023-02-01 00:33:49",
        10,
        "comment21",
        28,
        34
    ),
    (
        22,
        "2023-02-19 18:56:26",
        5,
        "comment22",
        35,
        33
    ),
    (
        23,
        "2023-01-05 09:26:27",
        10,
        "comment23",
        30,
        27
    ),
    (24, "2023-02-21 20:11:03", 1, NULL, 2, 28),
    (25, "2023-01-03 10:37:02", 9, "comment25", 3, 27),
    (
        26,
        "2023-02-20 11:17:50",
        9,
        "comment26",
        20,
        39
    ),
    (
        27,
        "2023-02-28 19:56:23",
        2,
        "comment27",
        10,
        25
    ),
    (
        28,
        "2023-01-21 14:53:37",
        10,
        "comment28",
        29,
        39
    ),
    (29, "2023-01-30 11:19:15", 2, "comment29", 9, 37),
    (30, "2023-02-20 15:49:19", 6, NULL, 7, 39),
    (31, "2023-01-17 15:44:49", 10, NULL, 34, 30),
    (
        32,
        "2023-02-23 05:01:59",
        2,
        "comment32",
        21,
        29
    ),
    (33, "2023-01-27 23:14:54", 5, "comment33", 8, 34),
    (
        34,
        "2023-02-09 22:16:20",
        2,
        "comment34",
        10,
        34
    ),
    (
        35,
        "2023-01-23 00:50:40",
        5,
        "comment35",
        35,
        26
    ),
    (36, "2023-02-19 00:08:17", 2, NULL, 18, 31),
    (
        37,
        "2023-02-16 04:05:54",
        9,
        "comment37",
        33,
        25
    ),
    (
        38,
        "2023-02-08 08:32:06",
        4,
        "comment38",
        32,
        36
    ),
    (
        39,
        "2023-01-20 06:50:52",
        1,
        "comment39",
        21,
        35
    ),
    (
        40,
        "2023-02-25 12:04:10",
        5,
        "comment40",
        10,
        39
    );
   
Update Movie SET avg_rate=0.0 WHERE id=1;
Update Movie SET avg_rate=1.0 WHERE id=2;
Update Movie SET avg_rate=9.0 WHERE id=3;
Update Movie SET avg_rate=0.0 WHERE id=4;
Update Movie SET avg_rate=9.0 WHERE id=5;
Update Movie SET avg_rate=6.0 WHERE id=6;
Update Movie SET avg_rate=6.0 WHERE id=7;
Update Movie SET avg_rate=5.0 WHERE id=8;
Update Movie SET avg_rate=3.5 WHERE id=9;
Update Movie SET avg_rate=3.0 WHERE id=10;
Update Movie SET avg_rate=0.0 WHERE id=11;
Update Movie SET avg_rate=0.0 WHERE id=12;
Update Movie SET avg_rate=0.0 WHERE id=13;
Update Movie SET avg_rate=0.0 WHERE id=14;
Update Movie SET avg_rate=8.0 WHERE id=15;
Update Movie SET avg_rate=0.0 WHERE id=16;
Update Movie SET avg_rate=1.0 WHERE id=17;
Update Movie SET avg_rate=2.0 WHERE id=18;
Update Movie SET avg_rate=0.0 WHERE id=19;
Update Movie SET avg_rate=9.0 WHERE id=20;
Update Movie SET avg_rate=1.5 WHERE id=21;
Update Movie SET avg_rate=0.0 WHERE id=22;
Update Movie SET avg_rate=3.0 WHERE id=23;
Update Movie SET avg_rate=0.0 WHERE id=24;
Update Movie SET avg_rate=5.0 WHERE id=25;
Update Movie SET avg_rate=2.0 WHERE id=26;
Update Movie SET avg_rate=0.0 WHERE id=27;
Update Movie SET avg_rate=10.0 WHERE id=28;
Update Movie SET avg_rate=10.0 WHERE id=29;
Update Movie SET avg_rate=10.0 WHERE id=30;
Update Movie SET avg_rate=5.0 WHERE id=31;
Update Movie SET avg_rate=6.5 WHERE id=32;
Update Movie SET avg_rate=9.5 WHERE id=33;
Update Movie SET avg_rate=6.5 WHERE id=34;
Update Movie SET avg_rate=6.7 WHERE id=35;
Update Movie SET avg_rate=0.0 WHERE id=36;
Update Movie SET avg_rate=9.0 WHERE id=37;
Update Movie SET avg_rate=9.0 WHERE id=38;
Update Movie SET avg_rate=0.0 WHERE id=39;
Update Movie SET avg_rate=7.0 WHERE id=40;

