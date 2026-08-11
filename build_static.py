"""Render the portfolio to static HTML for fast CDN hosting (Netlify/Cloudflare).

Usage: python build_static.py
Output: ./build/  (index.html + static assets)
"""
import os
import shutil

from jinja2 import Environment, FileSystemLoader, select_autoescape

from portfolio import views

DATA = views.home(None)
BUILD_DIR = "build"
SITE_URL = DATA["site_url"]

env = Environment(
    loader=FileSystemLoader("portfolio/templates"),
    autoescape=select_autoescape(["html", "jinja2"]),
)

if os.path.exists(BUILD_DIR):
    shutil.rmtree(BUILD_DIR)
os.makedirs(BUILD_DIR)

with open(os.path.join(BUILD_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(env.get_template("index.jinja2").render(**DATA))

shutil.copytree("portfolio/static", os.path.join(BUILD_DIR, "static"))

robots = f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n"
with open(os.path.join(BUILD_DIR, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots)

sitemap = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    f"  <url><loc>{SITE_URL}/</loc><changefreq>monthly</changefreq><priority>1.0</priority></url>\n"
    "</urlset>\n"
)
with open(os.path.join(BUILD_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap)

print(f"Build complete -> {BUILD_DIR}/")
