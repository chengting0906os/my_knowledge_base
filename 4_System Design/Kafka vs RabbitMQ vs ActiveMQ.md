Kafka 
零拷貝/順序寫入，批次寫入

**RabbitMQ** 在單一訊息的延遲上更低：
訊息被消費並確認後就會刪除
設計用於工作分配——每個訊息只給一個消費者



https://most.tw/posts/systemarchitect/comparsionmessagequeue/
https://www.geeksforgeeks.org/advance-java/apache-activemq-vs-kafka/
https://medium.com/@reshmakoshy01/kafka-vs-rabbitmq-why-kafka-handles-100-more-messages-4aad20f1d429

Kafka - Pull-based
SQS is a fully managed MQ service that enables you to decouple and scale micorservices, distrubuted systems, and serverless applications. 

Use Kafka When you need 
- **Event streaming and log aggregation**
- **Message replay and historical data**
- **Multiple consumers need same data**
- **High throughput (millions of messages/sec)**


RabbitMQ - Push-based
Use RabbitMQ when you need
 **Task distribution (job queues)**
