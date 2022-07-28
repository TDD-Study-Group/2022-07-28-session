import reactivex as rx
from reactivex import operators as ops
from http.client import HTTPConnection
from requests import get

source = rx.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")

composed = source.pipe(
    ops.map(lambda s: len(s)),
    ops.filter(lambda i: i >= 5)
)

composed.subscribe(lambda value: print("Received {0}".format(value)))


# components.scheme = "https"
#     components.host = "api.chucknorris.io"
#     components.path = "/jokes/random"
#     components.setQueryItems(with: ["category": "dev"])
# https://api.chucknorris.io/jokes/random?category=dev

# con = HTTPConnection("api.chucknorris.io")
# con.request("GET", "/jokes/random?category=dev")
# httpResponse = con.getresponse()
# status = httpResponse.status
# print("state {0}".format(status))
# body = httpResponse.read()
# print("body {0}".format(body))

# response = get("https://api.chucknorris.io/jokes/random?category=dev")
# print(f"json: {response.json()['value']}")
# print(f"json: {response.json()}")

responseOriginal = get("https://api.chucknorris.io/jokes/random?category=dev")
if 200 <= responseOriginal.status_code < 300:
    raise Exception()
valueOriginal = responseOriginal.json()["value"]

responseSource = rx.of(get("https://api.chucknorris.io/jokes/random?category=dev"))

responseComposed = responseSource.pipe(
    ops.filter(lambda response: 200 <= response.status_code < 300),
    ops.map(lambda body: body.json()),
    ops.map(lambda json: json["value"])
)

responseComposed.subscribe(lambda value: print("Received {0}".format(value)))