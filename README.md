## Quick Deploy

1. Open the AWS Lambda console and select Create a Lambda function. When prompted to select a blueprint, choose Blank Function.

2. Choose Configure triggers if it is not already selected, and then choose Next. You will configure a Lambda trigger later.
3. Enter the following information to configure your Lambda function:
- For Name, enter "StopEC2Instances"
- For Description, add “stops EC2 instances every day at night”
- For Runtime, select Python 2.7.

4. Select 'Edit Code Inline' and copy the stop.py script over to the console.
5. Expand the Role drop-down menu and choose Create a custom role. Enter the following information to create a role for Lambda to use:
- Under IAM Role, choose Create a new IAM Role.
- For Role Name, enter “lambda_start_stop_ec2”

7. Choose View Policy Document, Edit, and then copy over the policy found in lambda_start_stop.json.
8. Choose Allow, Next, Create Function

Repeat the above steps for the start.py script.

### References
- https://aws.amazon.com/premiumsupport/knowledge-center/start-stop-lambda-cloudwatch/

### Notes
- A more complex system for scheduling EC2 instances can be created using the CloudFormation template found: http://docs.aws.amazon.com/solutions/latest/ec2-scheduler/template.html