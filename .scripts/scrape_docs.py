#!/usr/bin/env python3
"""
Openclaw Documentation Scraper
Crawls https://docs.openclaw.ai/ and converts all pages to clean Markdown files.

When run from the repository root (e.g., via GitHub Actions), output defaults to
the current working directory so files are written directly into the repo.
"""

import os
import re
import sys
import time
import json
import hashlib
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import html2text

BASE_URL = "https://docs.openclaw.ai"

# Output to current working directory by default (works for GitHub Actions)
OUTPUT_DIR = os.environ.get("DOCS_OUTPUT_DIR", os.getcwd())
VISITED_FILE = os.path.join(OUTPUT_DIR, ".scripts", "visited_urls.json")

# Configure html2text converter
converter = html2text.HTML2Text()
converter.ignore_links = False
converter.ignore_images = False
converter.body_width = 0
converter.protect_links = True
converter.unicode_snob = True
converter.mark_code = True

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; OpenclawDocScraper/1.0)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

def normalize_url(url):
    parsed = urlparse(url)
    path = parsed.path.rstrip('/')
    if not path:
        path = '/'
    return f"{parsed.scheme}://{parsed.netloc}{path}"

def url_to_filepath(url):
    parsed = urlparse(url)
    path = parsed.path.strip('/')
    if not path:
        path = 'index'
    return os.path.join(OUTPUT_DIR, path.replace('/', os.sep) + '.md')

def extract_content(soup, url):
    content = None
    selectors = ['article', 'main article', '[class*="content"]', '[class*="prose"]', 'main', '#content']
    for selector in selectors:
        content = soup.select_one(selector)
        if content:
            break
    if not content:
        content = soup.find('body')
    for tag in content.find_all(['nav', 'header', 'footer', 'aside']):
        tag.decompose()
    for tag in content.find_all(class_=re.compile(r'nav|sidebar|menu|breadcrumb|footer|header|toc|pagination', re.I)):
        tag.decompose()
    for tag in content.find_all(['script', 'style']):
        tag.decompose()
    for tag in content.find_all(string=re.compile(r'On this page', re.I)):
        parent = tag.parent
        if parent:
            parent.decompose()
    return str(content)

def html_to_markdown(html_content, page_url):
    md = converter.handle(html_content)
    md = re.sub(r'\n{4,}', '\n\n\n', md)
    lines = md.split('\n')
    cleaned = [l for l in lines if not re.match(r'^\s*(Skip to (main )?content|\[Skip to)', l, re.I)]
    md = '\n'.join(cleaned)
    return re.sub(r'\n{4,}', '\n\n\n', md).strip()

def get_page_links(soup, current_url):
    links = set()
    for a_tag in soup.find_all('a', href=True):
        full_url = urljoin(current_url, a_tag['href'])
        normalized = normalize_url(full_url)
        if normalized.startswith(BASE_URL):
            links.add(normalized)
    return links

def scrape_page(url, session):
    try:
        response = session.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find('h1')
        title = title_tag.get_text(strip=True) if title_tag else url.split('/')[-1].replace('-', ' ').title()
        links = get_page_links(soup, url)
        html_content = extract_content(soup, url)
        markdown = html_to_markdown(html_content, url)
        header = f"---\ntitle: {title}\nsource_url: {url}\nscraped_at: {time.strftime('%Y-%m-%d')}\n---\n\n"
        return header + markdown, links, title
    except Exception as e:
        print(f"  ERROR scraping {url}: {e}")
        return None, set(), None

def save_markdown(filepath, content):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def load_visited():
    if os.path.exists(VISITED_FILE):
        with open(VISITED_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_visited(visited):
    os.makedirs(os.path.dirname(VISITED_FILE), exist_ok=True)
    with open(VISITED_FILE, 'w') as f:
        json.dump(visited, f, indent=2)

def generate_index(page_index):
    lines = [
        "# Openclaw Documentation",
        "",
        "> This repository contains a local Markdown mirror of the official [Openclaw documentation](https://docs.openclaw.ai/).",
        "> It is automatically updated every Monday to reflect any changes in the upstream documentation.",
        "",
        f"**Last updated:** {time.strftime('%Y-%m-%d')}",
        "",
        "## Documentation Index",
        "",
    ]
    sections = {}
    for url, title in sorted(page_index.items()):
        parsed = urlparse(url)
        path_parts = parsed.path.strip('/').split('/')
        section = path_parts[0] if path_parts else 'root'
        if section not in sections:
            sections[section] = []
        rel_path = parsed.path.strip('/') + '.md'
        if not rel_path or rel_path == '.md':
            rel_path = 'index.md'
        sections[section].append((title or url, rel_path, url))

    section_order = ['', 'start', 'install', 'channels', 'concepts', 'tools', 'providers',
                     'platforms', 'gateway', 'cli', 'help', 'vps', 'automation', 'debug',
                     'diagnostics', 'nodes', 'plugins', 'reference', 'security', 'web']
    for section in section_order:
        if section in sections:
            section_title = section.replace('-', ' ').title() if section else 'Overview'
            lines.append(f"### {section_title}")
            lines.append("")
            for title, rel_path, url in sorted(sections[section]):
                lines.append(f"- [{title}]({rel_path}) — [source]({url})")
            lines.append("")
    for section, pages in sorted(sections.items()):
        if section not in section_order:
            section_title = section.replace('-', ' ').title()
            lines.append(f"### {section_title}")
            lines.append("")
            for title, rel_path, url in sorted(pages):
                lines.append(f"- [{title}]({rel_path}) — [source]({url})")
            lines.append("")

    lines.extend([
        "---",
        "",
        "## About This Repository",
        "",
        "This documentation mirror is maintained automatically via a GitHub Actions workflow",
        "that runs every Monday at 06:00 UTC. The workflow scrapes the official Openclaw",
        "documentation site, detects changed pages using content hashing, and commits only",
        "the modified files.",
        "",
        "**Source:** https://docs.openclaw.ai/",
        "**Openclaw GitHub:** https://github.com/openclaw/openclaw",
        "",
        "## Usage with AI Tools",
        "",
        "This repository is designed to serve as a reference for AI tools managing Openclaw",
        "installations. Each documentation page is stored as a clean Markdown file, organized",
        "by section, making it easy for AI assistants to locate and reference specific",
        "configuration, installation, or troubleshooting information.",
        "",
        "### Sections at a Glance",
        "",
        "| Section | Description |",
        "|---------|-------------|",
        "| `start/` | Getting started, onboarding, and setup guides |",
        "| `install/` | Installation methods: Docker, Nix, cloud providers, and more |",
        "| `channels/` | Channel setup: WhatsApp, Telegram, Discord, iMessage, etc. |",
        "| `gateway/` | Gateway configuration, security, routing, and API reference |",
        "| `tools/` | Tools and plugins: browser, search, exec, and more |",
        "| `providers/` | AI model provider configuration (Anthropic, OpenAI, Google, etc.) |",
        "| `platforms/` | Platform-specific guides (Windows, macOS, Linux) |",
        "| `concepts/` | Architecture overview and feature reference |",
        "| `cli/` | Full CLI command reference |",
        "| `help/` | Troubleshooting and diagnostics |",
        "| `nodes/` | iOS and Android node setup |",
        "| `security/` | Security, tokens, and access controls |",
    ])

    readme_path = os.path.join(OUTPUT_DIR, 'README.md')
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print(f"  -> README index saved to: {readme_path}")

def main():
    print("=" * 60)
    print("Openclaw Documentation Scraper")
    print(f"Output directory: {OUTPUT_DIR}")
    print("=" * 60)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    visited = load_visited()

    seed_urls = [
        "https://docs.openclaw.ai",
        "https://docs.openclaw.ai/install",
        "https://docs.openclaw.ai/channels",
        "https://docs.openclaw.ai/concepts/architecture",
        "https://docs.openclaw.ai/tools",
        "https://docs.openclaw.ai/providers",
        "https://docs.openclaw.ai/platforms",
        "https://docs.openclaw.ai/gateway",
        "https://docs.openclaw.ai/cli",
        "https://docs.openclaw.ai/help",
        "https://docs.openclaw.ai/start/getting-started",
        "https://docs.openclaw.ai/start/onboarding-overview",
        "https://docs.openclaw.ai/start/wizard",
        "https://docs.openclaw.ai/start/onboarding",
        "https://docs.openclaw.ai/start/openclaw",
        "https://docs.openclaw.ai/start/wizard-cli-reference",
        "https://docs.openclaw.ai/start/wizard-cli-automation",
        "https://docs.openclaw.ai/start/showcase",
        "https://docs.openclaw.ai/concepts/features",
        "https://docs.openclaw.ai/start/setup",
        "https://docs.openclaw.ai/vps",
    ]

    queue = list(dict.fromkeys([normalize_url(u) for u in seed_urls]))
    session = requests.Session()
    scraped_count = 0
    updated_count = 0
    page_index = {}

    while queue:
        url = queue.pop(0)
        if url in visited and visited[url].get("error"):
            continue

        print(f"\n[{scraped_count + 1}] Scraping: {url}")
        markdown, new_links, title = scrape_page(url, session)

        if markdown:
            filepath = url_to_filepath(url)
            content_hash = hashlib.md5(markdown.encode()).hexdigest()
            prev_hash = visited.get(url, {}).get("hash")

            if prev_hash != content_hash:
                save_markdown(filepath, markdown)
                print(f"  -> {'Updated' if prev_hash else 'Saved'}: {filepath}")
                updated_count += 1
            else:
                print(f"  -> Unchanged: {filepath}")

            visited[url] = {
                "title": title,
                "filepath": filepath,
                "hash": content_hash,
                "last_scraped": time.strftime('%Y-%m-%d %H:%M:%S')
            }
            page_index[url] = title
            scraped_count += 1

            for link in new_links:
                if link not in visited and link not in queue:
                    queue.append(link)
        else:
            visited[url] = {"title": None, "error": True, "last_scraped": time.strftime('%Y-%m-%d %H:%M:%S')}

        if scraped_count % 10 == 0:
            save_visited(visited)

        time.sleep(0.5)

    save_visited(visited)
    print(f"\n{'=' * 60}")
    print(f"Done! {scraped_count} pages checked, {updated_count} updated.")
    generate_index(page_index)

if __name__ == "__main__":
    main()
