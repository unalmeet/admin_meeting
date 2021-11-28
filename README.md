# admin_meeting

This repository contains the necessary files to deploy the admin_meeting microservice.

Follow the instructions to deploy locally this microservice:

1. Clone the repository using  ``` git clone https://github.com/unalmeet/admin_meeting.git ```
2. Open the CMD and go to the path ``` admin_meeting/admin_meeting_db ``` which contains the DockerFile to create the PosgrestSQL image. 
3. Execute ``` docker build -t unmeet_adminmeeting_db . ``` in this path to create the database image
4. Execute docker run   -d -i  -p  5432:5432 --name unmeet_adminmeeting_db unmeet_adminmeeting_db to run the database image in the port 5432 
5. Return to the path where ``` admin_meeting ``` and execute ``` docker build -t unmeet_adminmeeting_ms . ```. This will create the Django API Rest image
6. To run the Django Api Rest image in the port 4000, specifying the connection with the PGSQL DB, execute ``` docker run --name unmeet_adminmeeting_ms -p 4000:4000 -e DB_HOST=host.docker.internal -e DB_PORT=5432 -e DB_USER=unmeet -e DB_PASSWORD=unmeet2021 -e DB_NAME=unmeet_adminmeeting_db -e URL=0.0.0.0:4000 unmeet_adminmeeting_ms ```

At this point, both containers (Django Api REST and PGSQL Database) will be running and you can consume the microservice at 
``` http://localhost:4000/ ```
