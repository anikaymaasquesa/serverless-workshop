import boto3


TABLE_NAME = 'CounterAPI-group#'
COUNTER_KEY = {'CounterId': '1'}


def lambda_handler(event, context):
    # Get current value from the proper table and item
    table = boto3.resource('dynamodb').Table(TABLE_NAME)
    item = table.get_item(Key=COUNTER_KEY).get('Item')
    value = item.get('value')

    ## Increase the value and save it in the table
    value += 1
    table.update_item(
        Key=COUNTER_KEY,
        AttributeUpdates={'value': {'Value': value, 'Action': 'PUT'}})

    return {'message': 'Counter has been increased'}
