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

The client provides direct access to all the ESI domains (see the list of implemented domains at the end of this chapter).

In order to access a particular domain's calls, just get the relative client's attribute, for example:

```python
alliance_api = client.alliance
```

## Implemented calls

List of all the available ESI API calls.

The client's attribute is in the parenthesis.

The check marked ones are the implemented ones, the pointed ones are the tested ones against at the API version shown after the pointing hand.

- Alliances (`alliances`)
    - ☑ [get_alliances](https://esi.evetech.net/ui/#/Alliance/get_alliances) 👉 1.10.1
    - ☐ [get_alliances_alliance_id](https://esi.evetech.net/ui/#/Alliance/get_alliances_alliance_id)
    - ☐ [get_alliances_alliance_id_corporations](https://esi.evetech.net/ui/#/Alliance/get_alliances_alliance_id_corporations)
    - ☐ [get_alliances_alliance_id_icons](https://esi.evetech.net/ui/#/Alliance/get_alliances_alliance_id_icons)
- Assets
    - ☐ [get_characters_character_id_assets](https://esi.evetech.net/ui/#/Assets/get_characters_character_id_assets)
    - ☐ [post_characters_character_id_assets_locations](https://esi.evetech.net/ui/#/Assets/post_characters_character_id_assets_locations)
    - ☐ [post_characters_character_id_assets_names](https://esi.evetech.net/ui/#/Assets/post_characters_character_id_assets_names)
    - ☐ [get_corporations_corporation_id_assets](https://esi.evetech.net/ui/#/Assets/get_corporations_corporation_id_assets)
    - ☐ [post_corporations_corporation_id_assets_locations](https://esi.evetech.net/ui/#/Assets/post_corporations_corporation_id_assets_locations)
    - ☐ [post_corporations_corporation_id_assets_names](https://esi.evetech.net/ui/#/Assets/post_corporations_corporation_id_assets_names)
- Bookmarks
    - ☐ [get_characters_character_id_bookmarks](https://esi.evetech.net/ui/#/Bookmarks/get_characters_character_id_bookmarks)
    - ☐ [get_characters_character_id_bookmarks_folders](https://esi.evetech.net/ui/#/Bookmarks/get_characters_character_id_bookmarks_folders)
    - ☐ [get_corporations_corporation_id_bookmarks](https://esi.evetech.net/ui/#/Bookmarks/get_corporations_corporation_id_bookmarks)
    - ☐ [get_corporations_corporation_id_bookmarks_folders](https://esi.evetech.net/ui/#/Bookmarks/get_corporations_corporation_id_bookmarks_folders)
- Calendar
    - ☐ [get_characters_character_id_calendar](https://esi.evetech.net/ui/#/Calendar/get_characters_character_id_calendar)
    - ☐ [get_characters_character_id_calendar_event_id](https://esi.evetech.net/ui/#/Calendar/get_characters_character_id_calendar_event_id)
    - ☐ [put_characters_character_id_calendar_event_id](https://esi.evetech.net/ui/#/Calendar/put_characters_character_id_calendar_event_id)
    - ☐ [get_characters_character_id_calendar_event_id_attendees](https://esi.evetech.net/ui/#/Calendar/get_characters_character_id_calendar_event_id_attendees)
- Character
- Clones
- Contacts
- Contracts
- Corporation
- Dogma
- Faction Warfare
- Fittings
- Fleets
- Incursions
- Industry
- Insurance
- Killmails
- Location
- Loyalty
- Mail
- Market
- Opportunities
- Planetary Interaction
- Routes
- Search
- Skills
- Sovereignty
- Status
- Universe
- User Interface
- Wallet
- Wars