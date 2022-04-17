import json
import boto3
# Topic ARN of created topic to send the email
SNS_ARN = "arn:aws:sns:us-east-1:303840799246:Tag-not-found-in-the-nstances"
sns = boto3.client("sns")
    
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    instance_tags_not_found= []
    for instance in ec2.instances.all():
        if instance.tags == None:
            instance_tags_not_found.append(instance.id)
        else:
            for item in instance.tags:
                if item['Key'] != 'Name' and item['Key'] != 'Environment' and item['Key'] != 'created_by':
                    instance_tags_not_found.append(instance.id)
    # ARN of the rule created for every hour
    if 'arn:aws:events:us-east-1:303840799246:rule/every_hour' in event["resources"]:
        if instance_tags_not_found is not None:
            message_contains = "Name or Environment or created_by tag are not in the" + ' , '.join(map(str, instance_tags_not_found))
            snsresponse=sns.publish(TopicArn=SNS_ARN,
                                    Message=message_contains,
                                    Subject="EC2 Violated Company Policy")
            print(snsresponse)
        else:
            return True
    # ARN of the rule created for every 6hour
    elif 'arn:aws:events:us-east-1:303840799246:rule/every_6hour' in event["resources"]:
        if instance_tags_not_found is not None:
            message_contains = "Name or Environment or created_by tag are not in the instances so i terminated it"
            snsresponse=sns.publish(TopicArn=SNS_ARN,
                                    Message=message_contains,
                                    Subject="EC2 Violated Company Policy")
            for i in instance_tags_not_found:                        
                instance = ec2.Instance(i)
                instance.terminate()
        else:
            return True
    else: True
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }