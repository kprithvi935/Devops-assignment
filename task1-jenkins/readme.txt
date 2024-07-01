Part A: SETUP JENKINS WITH DOCKER

Step 1: Install Docker Desktop on Windows
Make sure Docker Desktop is installed and running on your Windows 11 machine.

Step 2: Create a Docker Network
This network allows containers to communicate with each other.
# docker network create jenkins

Step 3: Run Jenkins Master
Start the Jenkins master container on the Docker network.
# docker run --name jenkins-master --network jenkins -p 8080:8080 -p 50000:50000 -d jenkins/jenkins:lts
This will run Jenkins master in detached mode, and expose port 8080 for the Jenkins web UI and port 50000 for Jenkins agents to connect.

Step 4: Set Up Jenkins Slave Nodes
# docker run --name jenkins-slave1 --network jenkins -d jenkins/inbound-agent -url http://jenkins-master:8080 <secret> <agent-name>

Step 5: Configure Jenkins
Open Jenkins in your browser (http://localhost:8080) and follow the setup wizard to install.
Go to Manage Jenkins > Manage Nodes and Clouds > New Node to add each slave. Specify the launch method as "Launch agents via Java Web Start" (JNLP).

Step 6: Create a Dummy Task
Create a new job (freestyle project).
Under the build configuration, you can add a simple shell command like echo "Hello from Jenkins node".
Set the job to run on the specific slave by using the slave label.
Execute the job multiple times to demonstrate that tasks can run on any slave node.


PART B: SETUP AUTOSCALING WHERE JENKINS NODES/SLAVES ARE CREATED AND DESTROYED AFTER JOB HAS RUN ON IT

Step 1: Install Docker Plugin for Jenkins
Go to "Manage Jenkins" -> "Manage Plugins" -> "Available".
Search for "Docker" and install "Docker" and "Docker Pipeline" plugins.

Step 2: Configure Docker Cloud in Jenkins
Go to "Manage Jenkins" -> "Manage Nodes and Clouds" -> "Configure Clouds".
Click "Add a new cloud" and select "Docker".
Configure the Docker cloud with the following details:
Name: Docker
Docker Host URI: unix:///var/run/docker.sock(or your local dockerhost url:2375)
Enabled: Check the box
Docker Cloud Details:
Docker Host URI: unix:///var/run/docker.sock(or your local dockerhost url:2375)
Enabled: Check this box
Test Connection to ensure Jenkins can connect to Docker.

Step 3: Add Docker Agent Template
Under the Docker cloud configuration, add a Docker Agent Template:
Click "Add Docker Template".
Configure the Docker Agent Template:
Label: docker-agent
Name: jenkins-agent
Docker Image: jenkins/inbound-agent
Remote File System Root: /home/jenkins
Instance Capacity: 2
Connect Method: Connect with JNLP in my case
Click "Save" to save the configuration.

Step 4: Create a Jenkins Pipeline
Create a Jenkins pipeline to use the Docker agent.

Step 5: I have screenshots of succesfull job run and slaves creation will be attaching it to the email 

