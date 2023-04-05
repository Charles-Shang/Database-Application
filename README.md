# Database-Application

This is the repository for team project of CS 348.

## Description

Our project, Film Searching Platform, enables users to perform searches based on various categories, and provides ratings for films within our database. The platform includes a wide range of search keywords, including film name, actor name, annual top list, most views, age group and production year (see some specific functionalities that are implemented below). If time permits, we plan to incorporate additional features such as user login, recent views, and support for various themes into our platform.

## Team members

Jiaqi Shang: j32shang@uwaterloo.ca

Keira Xing: y42xing@uwaterloo.ca

Vicky Yao: y264yao@uwaterloo.ca

Isaac Xie: ixie@uwaterloo.ca

Yuki Yu: y447yu@uwaterloo.ca

## Database

Our sample database has been generated thoughtfully and conatianing all corner cases
using `Database-Application/generate_sample_data.py`.

Our production database has been retrived and partially generated using iMDb and openAI. For more information, checkout our report. To load this database, set up a database connect using

```
host: cs348project.ceggb9lnr3wd.us-west-1.rds.amazonaws.com
user: root
password: cs348group11
database: sampledb
```

Note that the server is set up on AWS RDS, sometimes it is not as stable, if the database is down, contact j32shang@uwaterloo.ca for rebooting the server.

## SQL Query and output

All SQL outputs are displayed in the report using snapshots. All SQL related files are place in folder `assets`, specifically `assets/sql_sample` stores all sample sql code, `assets/sql_sample_out` stores all output from sample sql code, `assets/sql_template` stores all sql templates. Note that the production data is not stored in this repository as they can be large, but the snapshots of output using production data sets are included in the report.

## Environment setup (Based on Linux)
1. Install `Anaconda3-2022.10-Linux-x86_64.sh`[https://repo.anaconda.com/archive/Anaconda3-2023.03-Linux-x86_64.sh]
2. All pip required packages are listed in `requirement.txt`
3. The pre-define environment is shared in `environment.yml` (Python 3.8.16)

## Pre-setup Server
We set a server for remote implementation
```
HostName: ec2-52-53-128-223.us-west-1.compute.amazonaws.com
```
The identity file (public key) is in `uwcs348-2` file.
Note that the server is set up on AWS EC2, sometimes it is not as stable, if the server is down, contact j32shang@uwaterloo.ca for rebooting the server.

## Running Application
To run the application, go to `Database-Application/implementation/` and `python movieApplication.py`. To start with, type `menu` to get a series of commands. More details on the demonstration of the application is in our report.

## Current Supported Features
### Features from R6 to R16
1. Top n movies by ratings
2. Top n actors with their one best movies by ratings
3. Top n categories with m best movies in each category
4. Fuzzy search keyword on movie name, director and actors
5. Functional filtering on region, category, year, starting letter and sorting by ratings (both ascending and descending)
6. User Rating insertion, update and deletion
7. Graph Summary of three important statistics
8. Employment authentication system

### Additional features
1. Displaying menu
2. Going back to home page
3. Login Account
4. Logout Account
5. Register User
6. Register Employee
7. Modifying movie information (update and delete)
8. Modifying rating information (update and delete)
9. Navigate command to movie, celebrity, director, actor and rating
10. Displying profile of current user
11. List suboptions for `fsp` command
12. Error handling system and message system to help user navigate the application
