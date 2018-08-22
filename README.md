# HTTP - protocols

Building a basic HTTP server using the Python standard library.


**Author**: Liz Mahoney
**Author**: Max McFarland

**Version**: 1.0.0

## Overview


## API
Using python scripting language

## Changelog

2018-08-21
=====

- [] GET / - returns a valid HTML formatted response with a project description and an anchor tag which references a new request to GET /cow.
- [] GET /cow?msg=text - returns a cowpy response which correctly displays a default cow object including the text from your query string.
- [] POST /cow msg=text - returns a cowpy response with a JSON body {"content": "<cowsay cow>"}
- [] Both GET and POST should handle any paths that are not defined by you, and return with the appropriate 404 Not Found response and headers.
- [] Ensure that each of your valid routes are also able to handle a malformed request, which should return a 400 Bad Request response and headers. For example, a request to GET /cow which does not include a query string message is not properly formatted for your API, and should respond properly.
- [] Clients should be able to send messages to all other clients by sending it to the server without a special command
- [] Create a module scoped fixture which will run your server on a background thred while the test suite is executing.
- [] Write test for the following functionality of your application, including separate assertions for each status code AND each response body (if a body exists)
    - [] GET /: 200 OK <HTML Response>
    - [] !GET /: 400 Bad Request
    - [] GET /cow?msg=text: 200 OK <Text Response>- [] Connected clients should be maintained as an in memory collection on the server instance called the client_pool
    - [] GET /cow: 400 Bad Request
    - [] GET /cow?who=dat&wat=do: 400 Bad Request
    - [] !GET /cow?msg=text: 405 Invalid Method
    - [] POST /cow msg=text: 201 Created <JSON Response>
    - [] POST /cow: 400 Bad Request
    - [] POST /cow who=this how=why: 400 Bad Request
    - [] !POST /cow msg=text: 405 Invalid Method
- [] ANY /does_not_exist: 404 Not Found


