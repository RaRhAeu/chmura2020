# chmura2020

## Running api:

`$ docker-compose up`

`$ ./scripts/migrate`

then visit:

`http://localhost:8080/api/products`

# product json schema:
```json
{
  "name": "string",
  "price": "decimal",
  "created": "datetime (added automatically)"
}
```

## Important files:
 - docker-compose.yml
 - service/Dockerfile
 - db_setup.env
