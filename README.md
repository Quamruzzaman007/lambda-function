# lambda-function
## create role
#### 1. open aws website 
#### 2. search for Identity and Access Management (IAM) 
#### 3. click on Roles > Create role > Lambda > next
#### 4. search and check AmazonEC2FullAccess, AmazonSNSFullAcess and CloudWatchFullAccess > next
#### 5. enter role name > Create role

## launch Instances
#### 1. search EC2 > Launch Instance
#### 2. Enter the name of server
#### 3. select Ubantu from Amazon MAchine Image
#### 3. Key pair select (Proceed Without Key pair(not recommended)) from dropdown > Launch Instance

## Amazon SNS
#### 1. Search sns and click on Simple Notification service > Create Topic
#### 2. select (Standard) enter the name of the topic > Create Topic
#### 3. ->Create Subscription, select protocol(Email), Enter the email id where you want to send the mail > Create Subscription
#### 4. check the mail and enable the subscription

## lambda function
#### 1. search lambda > Create Function
#### 2. Enter function name 
#### 3. Choose language (python 3.8)
#### 4. click on (Change default execution role) click (use an existing role) select the role from dropdown you created in first step > Create Function
#### 5. copy the code from https://github.com/Quamruzzaman007/lambda-function/blob/main/aws_instance.py and paste it into lambda function and deploy

## Amazon Event Bridge
## create two rule to schedule the task one for every hour second for every 6hour
#### 1. search Amazon Event Bridge
#### 2. click on Create Rule Enter rule name select Schedule > Next
#### 3. From Schedule Pattern select (A schedule that runs at a regular rate, such as every 10 minutes.) enter the rate value(1 or 6, hours) > Next
#### 4. Under select target pick Lambda Function -> select lambda function you've already created > Next > Next > Create Rule 

## Arn you need to copy and paste into your code
### 1. goto the Amazon Event Bridge, click on the rules, click on the rule you created for every hour copy the Rule ARN and paste it to line no. 19 of the lambda function.
### 2. goto the Amazon Event Bridge, click on the rules, click on the rule you created for every 6hour copy the Rule ARN and paste it to line no. 29 of the lambda function 
### 3. search sns, click on simple notification service, click on Topic, click the topic you created, copy ARN and paste it to line no. 4 of lambda function


### Enable all rules and code wil run according to the rules
