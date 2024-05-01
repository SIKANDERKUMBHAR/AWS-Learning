import boto3
import time

def start_lightsail_instance(instance_name):
    lightsail_client = boto3.client('lightsail')
    lightsail_client.start_instance(instanceName=instance_name)
    return f"Started Lightsail instance with name '{instance_name}'"

def stop_lightsail_instance(instance_name):
    lightsail_client = boto3.client('lightsail')
    lightsail_client.stop_instance(instanceName=instance_name)
    return f"Stopped Lightsail instance with name '{instance_name}'"

def wait(seconds):
    time.sleep(seconds)

def stop_start_lightsail_instance(instance_name, action):
    if action not in ['start', 'stop']:
        return f"Invalid action '{action}'. Valid actions are 'start' or 'stop'."

    try:
        if action == 'stop':
            # Stop the Lightsail instance
            return stop_lightsail_instance(instance_name)
        elif action == 'start':
            # Start the Lightsail instance
            return start_lightsail_instance(instance_name)
    except Exception as e:
        return f"Error performing action on Lightsail instance: {e}"

def lambda_handler(event, context):
    # Get the action from the event
    action = event.get('action')
    if not action:
        return {
            'statusCode': 400,
            'body': "Action parameter not provided. Please provide 'action' parameter with value 'start' or 'stop'."
        }

    instance_name = 'instance name'  # Specify the name of the Lightsail instance to check

    response_message = stop_start_lightsail_instance(instance_name, action)

    return {
        'statusCode': 200,
        'body': response_message
    }
