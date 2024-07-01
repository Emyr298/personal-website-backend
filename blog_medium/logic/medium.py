import requests
import defusedxml.ElementTree as DET
from datetime import datetime
from xml.etree.ElementTree import Element
from html_sanitizer import Sanitizer

def parse_post_xml(xml_post: Element):
    sanitizer = Sanitizer({
        'tags': {
            'img', 'h1', 'h2', 'h3', 'h4', 'p', 'b', 'i', 'u', 'a', 'ul', 'ol', 'li', 'br', 'strong', 'em', 'pre', 'figure', 'figcaption'
        },
        'attributes': {
            'img': ('src', 'alt'),
            'a': ('href',),
        },
        'empty': {'img', 'br'},
        'separate': set(),
        'whitespace': set(),
        'keep_typographic_whitespace': True,
        'is_mergeable': lambda e1, e2: False,
    })
    
    guid = xml_post.find('guid')
    title = xml_post.find('title')
    content = xml_post.find('{http://purl.org/rss/1.0/modules/content/}encoded')
    created_at = xml_post.find('pubDate')
    updated_at = xml_post.find('{http://www.w3.org/2005/Atom}updated')
    link = xml_post.find('link')
    
    if None in [guid, title, content, created_at, updated_at, link]:
        return None
    
    return {
        'id': guid.text.split("/")[-1],
        'name': title.text,
        'content': sanitizer.sanitize(content.text),
        'created_at': datetime.strptime(created_at.text, "%a, %d %b %Y %H:%M:%S %Z"),
        'updated_at': datetime.fromisoformat(updated_at.text),
        'url': link.text,
    }

def get_medium_posts():
    response = requests.get("https://medium.com/feed/@emi.ru298", headers={
        "User-Agent": "python-requests"
    })
    xml_root = DET.fromstring(response.text)
    xml_channel = xml_root.find("channel")
    xml_posts = xml_channel.findall("item")
    posts = {}
    for xml_post in xml_posts:
        parsed_post = parse_post_xml(xml_post)
        if not parsed_post:
            continue
        posts[parsed_post['id']] = parsed_post
    return posts
