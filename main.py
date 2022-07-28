import reactivex as rx
from reactivex import operators as ops

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