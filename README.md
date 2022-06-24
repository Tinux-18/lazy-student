# the Lazy Student

## Overview

The Lazy Student (LS) aims to determine whether a student used an online course for the required time to graduate.

This is useful for the course manager/buyer at the point of issuing a receipt and certificate. It prevents a student receiving a certificate without completing the course and an institution paying for a course which was not completed.

## Assumptions

This service lives downstream from a web application for e-learning. 

I assume the web application behaves in the following way:
- user has to login in order to use the application
- after n minutes the user is logged out
- upon logout the client makes a call to the backend sending login timestamp (stored in some kind of session storage) and logout timestamp
- in the backend the log is stored in Mongo DB

## Notes

-   this is just an experiment / personal project currently under development
<!--
## Tried it yourself locally

**Requirements**: git, node, npm, postgreSQL, redis

1. Clone the repo
2. Set-up your secrets.json file based on the
   [provided example](https://github.com/Tinux-18/GnD/blob/main/secrets_example.json)
3. Set-up your database with `createdb <database_name>`
4. Create the tables from
   [setup.sql](https://github.com/Tinux-18/GnD/blob/main/server/sql/setup.sql)
5. Install npm packages with `npm i`
6. Start the client with `npm run dev:client`
7. Start Redis with `redis-server --daemonize yes`
8. Start the server with `npm start`

-->
## Techstack

### Front-end

![](https://img.shields.io/badge/-Angular-DD0031?logo=react&logoColor=white)&nbsp;![](https://img.shields.io/badge/-ReactiveX-B7178C?logo=redux&logoColor=white)

### Back-end

![](https://img.shields.io/badge/-Python-3776AB?logo=Node.js&logoColor=white)

![](https://img.shields.io/badge/-MongoDB-7A248?logo=PostgreSQL&logoColor=white) 

<!--
## Features

**User registration**

-   forms for login, registration and password reset
-   client side form validation
-   password reset using AWS SES
-   separate user profiles for shoppers and NGO admins
-->