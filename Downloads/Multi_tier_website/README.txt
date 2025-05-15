AWS Project Modules - Overview and Instructions

1. Lambda + SQS:
   - lambda_function.py is the AWS Lambda function triggered by SQS.
   - Deploy it on AWS Lambda and connect with SQS as event source.

2. Elastic Beanstalk PHP App:
   - index.php is a simple PHP file.
   - Use Elastic Beanstalk CLI or Console to create a PHP environment and deploy this file.

3. AWS OpsWorks:
   - Steps to create a stack, layer, instances, and deploy app from Git repo:

   a) Create Stack:
      aws opsworks create-stack --name "MyOpsWorksStack" --region YOUR_REGION \
      --default-instance-profile-arn YOUR_INSTANCE_PROFILE_ARN \
      --service-role-arn YOUR_SERVICE_ROLE_ARN \
      --default-os AMAZON_LINUX_2

   b) Create Layer:
      aws opsworks create-layer --stack-id STACK_ID --name "PHP App Layer" \
      --shortname "php-app-layer" --enable-auto-healing --auto-assign-public-ips

   c) Add Instances:
      aws opsworks create-instance --stack-id STACK_ID --layer-ids LAYER_ID \
      --instance-type t2.medium --os AMAZON_LINUX_2 --ssh-key-name YOUR_KEY_PAIR

   d) Start Instances:
      aws opsworks start-instance --instance-id INSTANCE_ID

   e) Create App:
      aws opsworks create-app --stack-id STACK_ID --name "MyApp" \
      --type "php" --app-source Type=git,Url=GIT_REPO_URL

   f) Deploy App:
      aws opsworks create-deployment --stack-id STACK_ID --app-id APP_ID --command Name=deploy

   - After updating your Git repo, trigger deploy again to reflect changes on all instances.

Please replace placeholders like YOUR_REGION, ROLE_ARNS, STACK_ID, LAYER_ID, etc., with your actual values.

