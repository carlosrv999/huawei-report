import os
from dotenv import load_dotenv
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkvpc.v2 import *
from vpc.vpc import list_vpc

load_dotenv()

access_key = os.getenv("access_key")
secret_key = os.getenv("secret_key")
sts_token = os.getenv("sts_token")
project_id = os.getenv("project_id")


if __name__ == "__main__":
    ak = access_key
    sk = secret_key
    endpoint = "https://vpc.la-south-2.myhuaweicloud.com"
    project_id = project_id

    config = HttpConfig.get_default_config()
    credentials = BasicCredentials(ak, sk, project_id).with_security_token(sts_token)

    vpc_client = (
        VpcClient.new_builder()
        .with_http_config(config)
        .with_credentials(credentials)
        .with_endpoint(endpoint)
        .build()
    )

    list_vpc(vpc_client)
