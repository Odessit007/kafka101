CREATE STREAM products_input (
    barcode VARCHAR,
    category VARCHAR,
    name VARCHAR,
    price DOUBLE,
    color VARCHAR,
    producer_country VARCHAR
  ) WITH (
    KAFKA_TOPIC = 'test-products',
    VALUE_FORMAT = 'AVRO'
);

CREATE STREAM book_products AS
    SELECT
        barcode,
        category,
        name,
        price,
        color,
        producer_country
FROM products_input
WHERE category = 'books'
EMIT CHANGES;
