# iss.security-audit-backend

## Requirements
- Docker
- Docker-compose
- Port 80 and Port 27017

## Project setup
```RUN bash Start.sh```
-  To fill in dummy data RUN "python test_data.py"

## Foundation for following projects:
- iss.security-audit-frontend
- iss.security-audit-client

## Information
- MongoDB Admin (Can be changed in .env)
  - username: root 
  - password: example 
- Frontend Login
  - username: ISS_ADMIN
  - password: 7|/S!~t8Z"E3&>Nm
- Each collection has it own user. In the .env file are the accounts for the python script defined. If you want to change these values, please also change these values in connect-and-insert.js, which is the startup script for the mongo database
- When changing the frontend login, the password needs to have the according hash. The standard user is created at the end of connect-and-insert, where the plain text password is written in the comment above
- To provide an easier configuration, the account modification via .env will be added in the future
