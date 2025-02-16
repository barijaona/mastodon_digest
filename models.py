from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from scorers import Scorer


class ScoredPost:
    def __init__(self, info: dict):
        self.info = info

    @property
    def url(self) -> str:
        return self.info["url"]

    def get_home_url(self, mastodon_base_url: str) -> str:
        return f"{mastodon_base_url}/authorize_interaction?uri={self.info['url']}"

    def get_score(self, scorer: Scorer) -> float:
        return scorer.score(self)

    @property
    def account(self) -> dict:
        return self.info.account

    @property
    def content(self) -> str:
        return self.info.content

    @property
    def media(self) -> str:
        medias = []
        for media in self.info.media_attachments:
            if media.type == 'image':
                medias.append(f'<img src="{media.url}">')
            elif media.type == 'gifv':
                medias.append(f'<video src="{media.url}" autoplay="true" loop="true"></video>')
            elif media.type == 'video':
                medias.append(f'<video src="{media.url}" controls></video>')
            elif media.type == 'audio':
                medias.append(f'<audio src="{media.url}" controls></audio>')
        return '\n'.join(medias)
