import json
import logging
import os

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# SNS topics should be a comma seperated list sns-a,sns-b,sns-c e
topic_arns = os.environ['topic_arns'].split(',')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    logger.info('Got event {}'.format(event))
    logger.info('Got context {}'.format(context))

    # Create an SNS client
    sns = boto3.client('sns')

    # Publish a simple message to the specified SNS topics
    for topic in topic_arns:
        response = sns.publish(
            TopicArn=topic,
            Message=json.dumps(event),
        )
    logger.info('Publish response {}'.format(response))
