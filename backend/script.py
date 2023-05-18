import oci
from oci.config import validate_config
from base64 import b64encode

ociMessageEndpoint = "https://cell-1.streaming.us-ashburn-1.oci.oraclecloud.com"
ociStreamOcid = (
    "ocid1.stream.oc1.iad.amaaaaaai5rgbiaa5dddgkvrolivhokfhflyhpnvxjm3afhx2n3dorwhlmea"
)


def produce_messages(client, stream_id):
    # Build up a PutMessagesDetails and publish some messages to the stream
    message_list = []
    for i in range(100):
        key = "messageKey" + str(i)
        value = "messageValue " + str(i)
        encoded_key = b64encode(key.encode()).decode()
        encoded_value = b64encode(value.encode()).decode()
        message_list.append(
            oci.streaming.models.PutMessagesDetailsEntry(
                key=encoded_key, value=encoded_value
            )
        )

    print(
        "Publishing {} messages to the stream {} ".format(len(message_list), stream_id)
    )
    messages = oci.streaming.models.PutMessagesDetails(messages=message_list)
    put_message_result = client.put_messages(stream_id, messages)

    # The put_message_result can contain some useful metadata for handling failures
    for entry in put_message_result.data.entries:
        if entry.error:
            print("Error ({}) : {}".format(entry.error, entry.error_message))
        else:
            print(
                "Published message to partition {} , offset {}".format(
                    entry.partition, entry.offset
                )
            )


config = {
    "user": "ocid1.user.oc1..aaaaaaaazymtziu7dmr2dm2ksuut7ykn6mta3uneggjmrf6lsej7zbvkzg7q",
    "key_file": "hackaton011team2@gmail.com_2023-05-18T02_59_27.712Z.pem",
    "fingerprint": "90:70:5c:9a:24:bf:72:8d:bb:9c:30:a3:c3:a8:77:10",
    "tenancy": "ocid1.tenancy.oc1..aaaaaaaafzpynbqwrzcyt7xzwdzusk6gjeagpl6f6lo5jmb5fnsn6s24oo3q",
    "region": "us-ashburn-1",
}

validate_config(config)

stream_client = oci.streaming.StreamClient(config, service_endpoint=ociMessageEndpoint)

# Publish some messages to the stream
produce_messages(stream_client, ociStreamOcid)
