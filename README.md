# ESIlib

Library to interact with the EVE Online's ESI API interface, focused on the server to server approach.

## Setup

In order to use the library, you need an [ESI application](https://developers.eveonline.com/applications).

The library uses TCP port `55533` only during the login process.

## Usage

### Client object and login

The library is designed to be used within a single entrypoint: `ESIClient`.

Example usage:

```python
from esilib import ESIClient

client = ESIClient(
    client_id='CLIENT_ID_HERE',
    permissions=['publicData', 'esi-characterstats.read.v1', '...'],
)

client.login()
```

`client.login()` will open a browser window to let the user authenticate via the OAuth 2.0 protocol.

**This is a blocking action (resolved once the login process is succesfull), so if you're running a UI, be sure it is being executed in a dedicated thread.**

You can personalize the callback page adding the `auth_callback_html` parameter in the client's initialization.

This change is purely cosmetic, as the authorization code will automatically be managed by the library.

It can either be a simple string, or a `urllib.Path` instance:

```python
from esilib import ESIClient
from urllib import Path

client = ESIClient(
    client_id='CLIENT_ID_HERE',
    permissions=['publicData', 'esi-characterstats.read.v1', '...'],
    auth_callback_html=Path(__file__).parent.joinpath('custom_callback_page.html')
)
```

See the `esilib.client.ESIClient` constructor for a full list of options.

### Accessing the various domains:

The client provides access to all the [ESI API domains](https://esi.evetech.net/ui/).

In order to access a particular domain's calls, just get the relative client's attribute, for example:

```python
alliance_api = client.alliance
```

The attribute naming convention is the following: lower case, spaces replaced by underscores.

A few examples:

- Alliance -> `alliance`
- Faction Warfare -> `faction_warfare`
- Planetary Interaction -> `planetary_interaction`

## Implemented calls

Client's domains and relative functions are being generated automatically from the [Swagger interface](https://esi.evetech.net/latest/swagger.json).

A list of HTTP verbs follow:

- **GET**: implemented
- **POST**: not implemented yet
- **PUT**: not implemented yet
- **DELETE**: not implemented yet