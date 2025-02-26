## Try it

[https://my-json-server.typicode.com/devmanorg/congrats-mentor](https://my-json-server.typicode.com/devmanorg/congrats-mentor)

## Use your own data

Fork it and change `db.json` values or create a repo with a `db.json` file.

ULRs:
- [https://my-json-server.typicode.com/devmanorg/congrats-mentor/mentors](https://my-json-server.typicode.com/devmanorg/congrats-mentor/mentors) - mentors.json
- [https://my-json-server.typicode.com/devmanorg/congrats-mentor/holidays](https://my-json-server.typicode.com/devmanorg/congrats-mentor/holidays) - holidays.json
- [https://my-json-server.typicode.com/devmanorg/congrats-mentor/postcards](https://my-json-server.typicode.com/devmanorg/congrats-mentor/postcards) - postcards.json

## Using
You can send GET request to one of the link above. You can also filter objects in response by url-params.  
Examples that return the same result:
- [/postcards?date=03.08](https://my-json-server.typicode.com/devmanorg/congrats-mentor/postcards?date=03.08) -- using the `date` param of the `postcards` object
- [/holidays/03.08/postcards](https://my-json-server.typicode.com/devmanorg/congrats-mentor/holidays/03.08/postcards) -- using the `holidayId` param of the `postcards` object, that links it with the `holisays` object.

