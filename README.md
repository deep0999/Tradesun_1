# Tradesun_1

Implementation of cognito UI with Dynamo DB logging with Lambda Trigger


# steps to be followed:

Firstly run the html files  in the local port by running: 
python -m http server

now lets go the AWS environment and as we have attached our Cognito UI to HTML, the signed in users will be collected in User pools in cognito, Now attach a lamda trigger to cognito.

we must attach roles with permission to read and write to dynamo DB, after giving permissions add the postAuth.py code to lambda trigger and run it after creating a Dynamo DB table with approproiate items.





