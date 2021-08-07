from jinja2 import Template
from pathlib import Path

def get_latest_post(rss_feed):
    f = feedparser.parse(rss_feed)
    latest_post = sorted(f['entries'], key=lambda x:x['published_parsed'])[-1]
    return {
            'title': latest_post['title'],
            'link': latest_post['link'],
            }

template = Template(Path('./README_TEMPLATE.md').read_text())
Path('./Readme.md').write_text(
        template.render(
            latest_post=get_latest_post(rss_feed),
            latest_podcast_post=get_latest_post(podcast_url),
            )
        )