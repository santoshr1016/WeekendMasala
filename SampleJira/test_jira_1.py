import botocore
import boto3


APP_ENV = "dev"
NAMER_HOST = 'dev.namer.cis.acquia.com'


def get_parameters(*names, output='tuple'):
    """ Get decrypted parameters from arguments. """
    client = boto3.client('ssm')
    response = client.get_parameters(
        Names=names,
        WithDecryption=True
    )

    results = {}

    for name in names:
        for params in response['Parameters']:
            if params['Name'] == name:
                results[name] = params['Value']
    return results if output == 'dict' else tuple(results.values())


try:
    NAMER_USER, NAMER_PASS = get_parameters(
        'namer.user.' + APP_ENV, 'namer.pass.' + APP_ENV)
except (ssm.InvalidParameter, botocore.exceptions.NoRegionError):
    NAMER_USER = None
    NAMER_PASS = None

print(NAMER_USER)
print(NAMER_PASS)
