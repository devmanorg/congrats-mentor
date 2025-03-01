## Try it

[https://my-json-server.typicode.com/devmanorg/congrats-mentor](https://my-json-server.typicode.com/devmanorg/congrats-mentor)

## Use your own data

Fork it and change `db.json` values or create a repo with a `db.json` file.

## Endpoints
- [/mentors](https://my-json-server.typicode.com/devmanorg/congrats-mentor/mentors)
- [/holidays](https://my-json-server.typicode.com/devmanorg/congrats-mentor/holidays)
- [/postcards](https://my-json-server.typicode.com/devmanorg/congrats-mentor/postcards)

## Using
You can send GET request to one of the link above. You can also filter objects in response by url-params.  
Examples that return the same result:
- [/postcards?date=03.08](https://my-json-server.typicode.com/devmanorg/congrats-mentor/postcards?date=03.08) -- using the `date` param of the `postcards` object
- [/holidays/03.08/postcards](https://my-json-server.typicode.com/devmanorg/congrats-mentor/holidays/03.08/postcards) -- using the `holidayId` param of the `postcards` object, that links it with the `holisays` object.

## Deprication
- The `date` param of `postcards` may be deleted in the future, because `holidayId` is more versatile.

## Links
- [OpenAPI Generator installer](https://openapi-generator.tech/docs/installation#pypi) for Python 3.10+