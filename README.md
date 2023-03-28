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

## SQL Query and output

All SQL outputs are displayed in the report using snapshots. All SQL related files are place in folder `assets`, specifically `assets/sql_sample` stores all sample sql code, `assets/sql_sample_out` stores all output from sample sql code, `assets/sql_template` stores all sql templates. Note that the production data is not stored in this repository as they can be large, but the snapshots of output using production data sets are included in the report.

## Running Application

To run the application, go to `Database-Application/implementation/` and `python movieApplication.py`. At milestone 1, all functionalities are tested using command line arguments. To start with, type `menu` to get a series of commands.

## Current Supported Features

1. Top n movies by ratings
2. Top n actors with their one best movies by ratings
3. Top n categories with m best movies in each category
4. Fuzzy search keyword on movie name, director and actors
5. Functional filtering on region, category, year, starting letter and sorting by ratings (both ascending and descending)
