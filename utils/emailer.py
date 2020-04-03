import boto3


def send_email(sender_email, sender_name, message, phone):
    client = boto3.client('ses', region_name='us-west-2')

    response = client.send_email(
        Source='szablya@gmail.com',
        Destination={
            'ToAddresses': ['szablya@gmail.com'],
            'CcAddresses': [],
            'BccAddresses': []
        },
        Message={
            'Subject': {
                'Data': 'New Consultant Client Inquiry: {}'.format(sender_name),
                'Charset': 'utf-8'
            },
            'Body': {
                'Text': {
                    'Data': '{}  please call at {}'.format(message, phone),
                    'Charset': 'utf-8'
                },
                'Html': {
                    'Data': '<p>{}</p><br/><br/><br/><p> please call at {}</p>'.format(message, phone),
                    'Charset': 'utf-8'
                }
            }
        },
        ReplyToAddresses=[sender_email],
    )
    return response