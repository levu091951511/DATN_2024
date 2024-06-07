import requests
from kafka import KafkaProducer
import json
from datetime import datetime

# Kafka producer với thông tin xác thực
producer = KafkaProducer(
    bootstrap_servers='10.165.24.28:32482,10.165.24.31:30924,10.165.24.33:30102',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    sasl_mechanism='PLAIN',
    security_protocol='SASL_PLAINTEXT',
    sasl_plain_username='admin',
    sasl_plain_password='adminKafka2021'
)

record = {
    'ngay': f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
    'thang': '6',
    'nam': 'Hai Khong Hai Tu'
}

producer.send('ban_ghi', value=record)
