# Llama AI Model Deployment with AWS Lightsail and Lambda

## Project Overview

This project deploys the Llama AI Model using an AWS Lightsail instance to host a Dockerized Llama application. The Lightsail instance used in this project costs $40 USD per month and includes 8GB memory, 2 vCPUs, 160 GB SSD Disk, and 5 TB transfer. AWS Lightsail offers a cost-effective hosting solution with predictable pricing based on instance size, additional costs for data transfer and storage, scalability options, and reliable performance backed by AWS infrastructure.

## Steps for Creating an AWS Lightsail Instance

1. **Create an Instance:**
   - Platform: Linux/Unix
   - Blueprint: OS Only (Ubuntu)
   - Region: ap-southeast-1 (Asia Pacific (Singapore))
   - Networking: Dual-stack (IPv4/IPv6)
   - Add 160 GB SSD storage and 5 TB transfer
   - Enter a unique name for your instance

2. **Wait for the Instance to be Created:**
   - Once ready, it will appear on the Lightsail dashboard.

3. **Configure Firewall Rules:**
   - Click on the instance name > Networking tab
   - Create rules to open ports to the internet or specific IPv4 addresses/ranges

4. **Access Your Instance:**
   - Connect using SSH or manage via the Lightsail console

5. **Configure Your Instance:**

1. **Install Docker**:
   ```
   sudo apt update
   sudo apt upgrade -y
   sudo apt install docker.io -y
   ```

2. **Create a Docker Volume for Ollama**:
   ```
   sudo mkdir -p /home/ubuntu/ollama
   ```

3. **Run the Docker Container**:
   ```
   sudo docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
   ```

4. **Configure the Docker Container**:
   - Access the Docker container's terminal:
     ```
     sudo docker exec -it ollama /bin/bash
     ```
   - Pull the required Docker image:
     ```
     ollama pull llama2-uncensored
     ```
   - Run the desired command:
     ```
     ollama run wizardlm2
     ```

These steps will configure your AWS Lightsail instance to run the Docker container and execute the necessary commands to set up your application.

6. **Configure the Docker Container to Start on Boot:**
   - Create a systemd service file: `sudo vim /etc/systemd/system/my_docker_container.service`
   - Add the service file content (docker-on-boot.txt)
   - Reload systemd: `sudo systemctl daemon-reload`
   - Enable the service to start on boot: `sudo systemctl enable my_docker_container`
   - Start the service: `sudo systemctl start my_docker_container`

## AWS Lambda Function for Lightsail Instance Control

1. **Create the Lambda Function:**
   - Runtime: Python 3.9
   - Edit code inline and paste the lambda function code
   - (lambda-function.py)
   - Add an environment variable "instance_name" with the value set to your Lightsail instance name

2. **Create the Lambda Execution Role:**
   - Attach the AWSLambdaBasicExecutionRole and your custom policy for Lightsail access to the role

3. **Create a Custom Policy for Lightsail Access:**
   - Attach the policy allowing (lambda-policy.json)
4. **Attach the Policy to the Lambda Execution Role:**
   - Attach the policy to the role created for the Lambda function

## Invoking the Lambda Function

To start or stop your Lightsail instance using the Lambda function, you can invoke the function with an event JSON specifying the action to perform. Here's how you can structure the event JSON for the Lambda function:

### Start Instance Event JSON
```json
{
    "action": "start"
}
```

### Stop Instance Event JSON
```json
{
    "action": "stop"
}
```

When you invoke the Lambda function with one of these event JSON objects, the function will start or stop the specified Lightsail instance accordingly.
