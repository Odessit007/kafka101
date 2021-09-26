CREATE STREAM camp_users_input (
    email VARCHAR,
    first_name VARCHAR,
    last_name VARCHAR,
    age INT,
    address VARCHAR,
    gender VARCHAR,
    job VARCHAR,
    has_children_under_sixteen BOOLEAN
  ) WITH (
    KAFKA_TOPIC = 'test-users',
    VALUE_FORMAT = 'AVRO'
  );

CREATE STREAM adult_users AS
    SELECT
        email,
        first_name,
        last_name,
        age,
        address,
        gender,
        job,
        has_children_under_sixteen
FROM camp_users_input
WHERE age >= 18
EMIT CHANGES;
