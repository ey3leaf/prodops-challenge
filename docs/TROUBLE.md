Prologue:
While using AWS credentials in default location everything was fine.
The troubles beginned when I was trying to set ENV from the app itself:

 - 'boto3' module doesn't have an option to specify external credentials file. Only 'AWS_SHARED_CREDENTIALS' ENV VARIABLE. 
	I wrote some code to read environments file and using os.environ[ENV]=VAL set it. Locally works fine.

 - When starting docker container with application, setting ENV variables fails and I still don't know why. 
	That piece of code just don't work. I used '@app.before_first_request' decorator and locally it worked fine, but not in container.

 - Fallback to simple '.env' in docker-compose. 
