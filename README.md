# pushkit-python-sample

![Sample](push_kit_server_sample.gif)




## Table of Contents

 * [Introduction](#introduction)
 * [Installation](#installation)
 * [Configuration ](#configuration )
 * [Supported Environments](#supported-environments)
 * [Sample Code](#sample-code)
 * [License](#license)


## Introduction

Python sample code encapsulates APIs of the HUAWEI Push Kit server. It provides many sample programs about quick access to HUAWEI Push Kit for your reference or usage.

The following table describes packages of Python sample code.

| Package    | Description                                                  |
| ---------- | ------------------------------------------------------------ |
| examples   | Sample code packages. Each package can run independently.    |
| hms        | Package where APIs of the HUAWEI Push Kit server are encapsulated. |

## Installation

To install pushkit-python-sample, you should extract the compressed ZIP file, execute the following command in the unzipped directory:
```
python setup.py install
```

## Supported Environments
For pushkit-python-sample, We currently support Python 3.8 and JetBrains PyCharm are recommended.

Add src file into source file your project:

File -> Settings -> Project:... -> Project Structure -> [click src file] -> Mark as **Sources**


## Configuration 
The following table describes parameters of the initialize_app method.

| Parameter      |    Description |
| -------------  |   ------------------------------------------------------------------------- |
| appid          |    App ID, which is obtained from app information. |
| appsecret      |    Secret access key of an app, which is obtained from app information. |
| token_server   |    URL for the Huawei OAuth 2.0 service to obtain a token, please refer to [Generating an App-Level Access Token](https://developer.huawei.com/consumer/en/doc/development/parts-Guides/generating_app_level_access_token). |
| push_open_url  |    URL for accessing HUAWEI Push Kit, please refer to [Sending Messages](https://developer.huawei.com/consumer/en/doc/development/HMS-References/push-sendapi).|
| test_device_token | Add test device token, please refer to [Receive Token Application](https://github.com/Huawei/Consumer/tree/master/Codelabs/PushKit) |


## Sample Code
Download Python sample code in Downloading Server Sample Code.


Python sample code uses the Messaging structure in the push_admin package as the entry. Each method in the Messaging 
structure calls an API of the HUAWEI Push Kit server.

The following table describes methods in the Messaging structure.

| Method              |     Description
| -----------------   |     --------------------------------------------------- |
| send_message        |     Sends a message to a device. |
| subscribe_topic     |     Subscribes to a topic. |
| unsubscribe_topic   |     Unsubscribes from a topic. |
| list_topics         |     Queries the list of topics subscribed by a device. |
| initialize_app      |     Initializes the configuration parameters. |

1) Send an Android data message.
Code location: examples/send_data_message.py

2) Send an Android notification message.
Code location: examples/send_notify_message.py

3) Send a message by topic.
Code location: examples/send_topic_message.py

4) Send a message by conditions.
Code location: examples/send_condition_message.py

5) Send a message to a Huawei quick app.
Code location: examples/send_instance_app_message.py

6) Send a message through the WebPush agent.
Code location: examples/send_webpush_message.py

7) Send a message through the APNs agent.
Code location: examples/send_apns_message.py

8) Send a test message.
Code location: examples/send_test_message.py

## License

pushkit Python sample is licensed under the [Apache License, version 2.0](http://www.apache.org/licenses/LICENSE-2.0).

> This project based on official [HMS Push Kit python integration](https://github.com/HMS-Core/hms-push-serverdemo-python) documentation.
