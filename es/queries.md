## Queries.

Get products from "toys" category having 10 <= price <= 50:
```
GET /test-products/_search?
{
  "query" : {
    "bool": {
      "filter": [
        {
          "range": {
            "price": {
              "gte": 10,
              "lte": 50
            }
          }
        },
        {
          "match": {
            "category": "toys"
          }
        }
      ]
    }
  }
}
```


Search for all products where producing country is similar to "Kattar" with two mistakes allowed (including mistakes in first letter):
```
GET /test-products/_search?
{
  "query" : {
    "match": {
      "producer_country": {
        "query": "Kattar",
        "fuzziness": 2
      }
    }
  }
}
```


Get products from "books" category with those produced in Lithuania being on top.
```
GET /test-products/_search
{
  "query" : {
    "bool": {
      "must": {
        "match": {
          "category": "books"
        }
      },
      "should": {
        "match": {
          "producer_country": "Lithuania"
        }
      }
    }
  }
}
```
