"""GraphQL schema. Every piece of site content is served through this API."""
from typing import List
import strawberry
from . import content as c


@strawberry.type
class Link:
    label: str
    url: str
    kind: str


@strawberry.type
class Photo:
    src: str
    thumb: str
    alt: str


@strawberry.type
class Profile:
    name: str
    headline_lead: str
    headline_emphasis: str
    summary: str
    industries_line: str
    tags: List[str]
    email: str
    photo: Photo
    links: List[Link]


@strawberry.type
class Strength:
    icon: str
    title: str
    body: str


@strawberry.type
class About:
    title: str
    title_emphasis: str
    paragraphs: List[str]
    strengths: List[Strength]


@strawberry.type
class Platform:
    id: strawberry.ID
    name: str
    blurb: str
    connects_to: List[str]


@strawberry.type
class Expertise:
    title: str
    body: str


@strawberry.type
class Contact:
    title: str
    title_emphasis: str
    body: str


@strawberry.type
class Recommendation:
    name: str
    photo: str
    title: str
    relationship: str
    date: str
    quote: str
    paragraphs: List[str]


@strawberry.type
class Recommendations:
    title: str
    title_emphasis: str
    source: str
    source_label: str
    source_url: str
    items: List[Recommendation]


@strawberry.type
class UnderTheHood:
    title: str
    title_emphasis: str
    body: str


@strawberry.type
class Query:
    @strawberry.field
    def profile(self) -> Profile:
        p = dict(c.PROFILE)
        p["links"] = [Link(**l) for l in p["links"]]
        p["photo"] = Photo(**p["photo"])
        return Profile(**p)

    @strawberry.field
    def about(self) -> About:
        a = dict(c.ABOUT)
        a["strengths"] = [Strength(**s) for s in a["strengths"]]
        return About(**a)

    @strawberry.field
    def platforms(self) -> List[Platform]:
        return [Platform(**p) for p in c.PLATFORMS]

    @strawberry.field
    def expertise(self) -> List[Expertise]:
        return [Expertise(**e) for e in c.EXPERTISE]

    @strawberry.field
    def recommendations(self) -> Recommendations:
        r = dict(c.RECOMMENDATIONS)
        r["items"] = [Recommendation(**i) for i in r["items"]]
        return Recommendations(**r)

    @strawberry.field
    def contact(self) -> Contact:
        return Contact(**c.CONTACT)

    @strawberry.field
    def under_the_hood(self) -> UnderTheHood:
        return UnderTheHood(**c.UNDER_THE_HOOD)

    @strawberry.field
    def footer(self) -> str:
        return c.FOOTER


schema = strawberry.Schema(query=Query)

# The single query the page runs. Shared by the live server and the static build.
PAGE_QUERY = """query Portfolio {
  profile { name headlineLead headlineEmphasis summary industriesLine tags email photo { src thumb alt } links { label url kind } }
  about { title titleEmphasis paragraphs strengths { icon title body } }
  platforms { id name blurb connectsTo }
  expertise { title body }
  recommendations { title titleEmphasis source sourceLabel sourceUrl items { name photo title relationship date quote paragraphs } }
  underTheHood { title titleEmphasis body }
  contact { title titleEmphasis body }
  footer
}"""
