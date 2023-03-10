import os
import sys
import json
import base64
import etcd3
import logging
from logdna import LogDNAHandler

# Useful for debugging, prints all environment variables
# for name, value in os.environ.items():
#     print("{0}: {1}".format(name, value))

# Set up logging to LogDNA
loggingIngestionKey = os.environ.get('LOGDNA_INGESTION_KEY')
print(loggingIngestionKey)
# log = logging.getLogger('logdna')

# options = {
#   'app': 'python-etcd-private-test',
#   'env': 'code-engine',
#   'level': 'info'
# }

# loggingClient = LogDNAHandler(loggingIngestionKey, options)

# log.addHandler(loggingClient)

# log.warning("Warning message", extra={'app': 'bloop'})
# log.info("This is an Info message from private etce python app testing")
# Pull database connection details via Code Engine environment variable
# do some base64 decoding and type manipulation to get everything humming along
# etcdServiceVars = os.environ.get('DATABASES_FOR_ETCD_CONNECTION')
# connectionJson = json.loads(etcdServiceVars)
# connectionVars = list(connectionJson.values())[1]
# encodedCert = connectionVars['certificate']['certificate_base64']
# certName = connectionVars['certificate']['name']
# certFileName = certName + '.crt'
# ca_cert=base64.b64decode(encodedCert)
# decodedCert = ca_cert.decode('utf-8')

# etcdCert = '/usr/src/app/' + certFileName
# print(etcdCert)
# with open(etcdCert, 'w+') as output_file:
#     output_file.write(decodedCert)

# # Set up etcd service client
# etcdClient = etcd3.client(
#     host=connectionVars['hosts'][0]['hostname'], 
#     port=connectionVars['hosts'][0]['port'], 
#     ca_cert=certname, 
#     timeout=10, 
#     user=connectionVars['authentication']['username'], 
#     password=connectionVars['authentication']['password']
# )

# # Write instance IDs to etcd service
# def etcdWrite(etcdClient):
#     print("Connected to etcd service...")
#     print("Attempting to write albumns to etcd:")
#     etcdClient.put('/radiohead/albums/1', 'pablo-honey')
#     etcdClient.put('/radiohead/albums/2', 'the-bends')
#     etcdClient.put('/radiohead/albums/3', 'ok-computer')
#     etcdClient.put('/radiohead/albums/4', 'kid-a')
#     etcdClient.put('/radiohead/albums/5', 'amnesiac')
#     etcdClient.put('/radiohead/albums/6', 'hail-to-the-thief')
#     etcdClient.put('/radiohead/albums/7', 'in-rainbows')
#     etcdClient.put('/radiohead/albums/8', 'the-king-of-limbs')
#     etcdClient.put('/radiohead/albums/9', 'a-moon-shaped-pool')
#     print("Albums written to etcd")
# try:
#     etcdWrite(etcdClient)

# except KeyError():
#     print("KeyError: Unable to write to etcd service")
# # except ApiException as e:
# #     print("Etcd write failed " + str(e.code) + ": " + e.message)
