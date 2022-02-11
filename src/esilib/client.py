from pathlib import Path
from typing import List, Union
from esilib.security import ESISecurity
from esilib.domain.gen_alliance import Alliance
from esilib.domain.gen_contacts import Contacts
from esilib.domain.gen_character import Character
from esilib.domain.gen_assets import Assets
from esilib.domain.gen_skills import Skills
from esilib.domain.gen_bookmarks import Bookmarks
from esilib.domain.gen_calendar import Calendar
from esilib.domain.gen_clones import Clones
from esilib.domain.gen_contracts import Contracts
from esilib.domain.gen_fittings import Fittings
from esilib.domain.gen_fleets import Fleets
from esilib.domain.gen_faction_warfare import FactionWarfare
from esilib.domain.gen_industry import Industry
from esilib.domain.gen_killmails import Killmails
from esilib.domain.gen_location import Location
from esilib.domain.gen_loyalty import Loyalty
from esilib.domain.gen_mail import Mail
from esilib.domain.gen_opportunities import Opportunities
from esilib.domain.gen_market import Market
from esilib.domain.gen_planetary_interaction import PlanetaryInteraction
from esilib.domain.gen_search import Search
from esilib.domain.gen_wallet import Wallet
from esilib.domain.gen_corporation import Corporation
from esilib.domain.gen_dogma import Dogma
from esilib.domain.gen_incursions import Incursions
from esilib.domain.gen_insurance import Insurance
from esilib.domain.gen_routes import Routes
from esilib.domain.gen_sovereignty import Sovereignty
from esilib.domain.gen_status import Status
from esilib.domain.gen_user_interface import UserInterface
from esilib.domain.gen_universe import Universe
from esilib.domain.gen_wars import Wars


class ESIClient:
    security: ESISecurity
    endpoint_url: str

    def __init__(
        self,
        client_id: str,
        permissions: List[str],
        auth_url: str = None,
        token_url: str = None,
        endpoint_url: str = None,
        auth_callback_html: Union[str, Path] = None,
    ) -> None:
        kwargs = {
            'client_id': client_id,
            'permissions': permissions,
        }

        if auth_url:
            kwargs['auth_url'] = auth_url
        if token_url:
            kwargs['token_url'] = token_url
        if auth_callback_html:
            kwargs['auth_callback_html'] = auth_callback_html

        self.security = ESISecurity(
            client_id=client_id,
            permissions=permissions,
            auth_url=auth_url,
            token_url=token_url,
            auth_callback_html=auth_callback_html,
        )

        self.endpoint_url = endpoint_url

    def login(self) -> None:
        self.security.login()

    def _get_domain(self, name: str, cls: type):
        attr = f'_{name}'
        if not hasattr(self, attr):
            setattr(self, attr, cls(self.security))

        return getattr(self, attr)

    @property
    def alliance(self) -> Alliance:
        return self._get_domain('alliance', Alliance)

    @property
    def contacts(self) -> Contacts:
        return self._get_domain('contacts', Contacts)

    @property
    def character(self) -> Character:
        return self._get_domain('character', Character)

    @property
    def assets(self) -> Assets:
        return self._get_domain('assets', Assets)

    @property
    def skills(self) -> Skills:
        return self._get_domain('skills', Skills)

    @property
    def bookmarks(self) -> Bookmarks:
        return self._get_domain('bookmarks', Bookmarks)

    @property
    def calendar(self) -> Calendar:
        return self._get_domain('calendar', Calendar)

    @property
    def clones(self) -> Clones:
        return self._get_domain('clones', Clones)

    @property
    def contracts(self) -> Contracts:
        return self._get_domain('contracts', Contracts)

    @property
    def fittings(self) -> Fittings:
        return self._get_domain('fittings', Fittings)

    @property
    def fleets(self) -> Fleets:
        return self._get_domain('fleets', Fleets)

    @property
    def faction_warfare(self) -> FactionWarfare:
        return self._get_domain('faction_warfare', FactionWarfare)

    @property
    def industry(self) -> Industry:
        return self._get_domain('industry', Industry)

    @property
    def killmails(self) -> Killmails:
        return self._get_domain('killmails', Killmails)

    @property
    def location(self) -> Location:
        return self._get_domain('location', Location)

    @property
    def loyalty(self) -> Loyalty:
        return self._get_domain('loyalty', Loyalty)

    @property
    def mail(self) -> Mail:
        return self._get_domain('mail', Mail)

    @property
    def opportunities(self) -> Opportunities:
        return self._get_domain('opportunities', Opportunities)

    @property
    def market(self) -> Market:
        return self._get_domain('market', Market)

    @property
    def planetary_interaction(self) -> PlanetaryInteraction:
        return self._get_domain('planetary_interaction', PlanetaryInteraction)

    @property
    def search(self) -> Search:
        return self._get_domain('search', Search)

    @property
    def wallet(self) -> Wallet:
        return self._get_domain('wallet', Wallet)

    @property
    def corporation(self) -> Corporation:
        return self._get_domain('corporation', Corporation)

    @property
    def dogma(self) -> Dogma:
        return self._get_domain('dogma', Dogma)

    @property
    def incursions(self) -> Incursions:
        return self._get_domain('incursions', Incursions)

    @property
    def insurance(self) -> Insurance:
        return self._get_domain('insurance', Insurance)

    @property
    def routes(self) -> Routes:
        return self._get_domain('routes', Routes)

    @property
    def sovereignty(self) -> Sovereignty:
        return self._get_domain('sovereignty', Sovereignty)

    @property
    def status(self) -> Status:
        return self._get_domain('status', Status)

    @property
    def user_interface(self) -> UserInterface:
        return self._get_domain('user_interface', UserInterface)

    @property
    def universe(self) -> Universe:
        return self._get_domain('universe', Universe)

    @property
    def wars(self) -> Wars:
        return self._get_domain('wars', Wars)
