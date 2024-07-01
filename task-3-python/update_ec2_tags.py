import boto3
import csv

def update_ec2_tags(csv_file):
    ec2 = boto3.client('ec2')

    # Read the CSV file
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            hostname = row['Hostname']
            new_department = row['New Department']

            # Describe instances to get the instance IDs
            response = ec2.describe_instances(
                Filters=[
                    {
                        'Name': 'tag:Hostname',
                        'Values': [hostname]
                    }
                ]
            )

            instances = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]

            # Update the tags
            if instances:
                ec2.create_tags(
                    Resources=instances,
                    Tags=[
                        {
                            'Key': 'Department',
                            'Value': new_department
                        }
                    ]
                )
                print(f"Updated Department tag for {hostname} to {new_department}")
            else:
                print(f"No instances found with Hostname: {hostname}")

if __name__ == "__main__":
    update_ec2_tags('tag_updates.csv')
