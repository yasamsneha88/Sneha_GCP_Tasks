# GCP_PUB-SUB
Synopsys on Google Cloud Pub/Sub

Google Cloud Pub/Sub is a fully managed messaging service on GCP.
It allows applications to communicate using asynchronous messages.
Pub/Sub uses topics to which publishers send messages.
Subscribers receive messages from topics they subscribe to.
This model helps decouple systems and improves scalability.
Applications do not need to know about each other directly.
Pub/Sub supports real-time event streaming.
It is commonly used in data pipelines and microservices.
Messages are stored securely until delivered.
At-least-once delivery ensures reliability.
Message acknowledgement confirms successful processing.
Unacknowledged messages are redelivered automatically.
Pub/Sub supports push and pull subscriptions.

Pub/Sub is designed to handle high-throughput event ingestion with low latency. Messages published to a topic are stored durably until they are delivered and acknowledged by subscribers. The service guarantees at-least-once delivery, meaning messages can be delivered more than once, so applications must be able to handle duplicates. Pub/Sub also supports exactly-once delivery when using supported client libraries, which helps ensure data consistency in critical pipelines. Messages can include a data payload and attributes, and common formats such as JSON or Avro are widely used.

Push subscriptions send messages to HTTP endpoints.

Pull subscriptions allow clients to fetch messages manually.

Message ordering can be enabled using ordering keys.

Dead-letter topics help manage failed messages.

Pub/Sub integrates with Cloud Functions and BigQuery.

It scales automatically based on traffic.

IAM controls access and security.

Messages are encrypted at rest and in transit.

Monitoring is available through Cloud Monitoring.

Pub/Sub is ideal for event-driven architectures.

It supports streaming analytics workflows.

It reduces system dependency and improves fault tolerance.

Common GCP Pub/Sub Commands
1. Create a topic

gcloud pubsub topics create my-topic

2. List topics

gcloud pubsub topics list

3. Create a subscription

gcloud pubsub subscriptions create my-subscription --topic=my-topic

4. List subscriptions

gcloud pubsub subscriptions list

5. Publish a message

gcloud pubsub topics publish my-topic --message="Hello Pub/Sub"

6. Pull messages (manual)

gcloud pubsub subscriptions pull my-subscription --auto-ack

7. Delete a subscription

gcloud pubsub subscriptions delete my-subscription

8. Delete a topic

gcloud pubsub topics delete my-topic

