#!/bin/bash

set -e

HTML_DIR=docs
BASE_URL=https://linuxcmd.wiki

{ cat <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>$BASE_URL</loc>
      <lastmod>$(date -d @$(stat -c %Y "$HTML_DIR"/index.html) +%Y-%m-%d)</lastmod>
      <changefreq>always</changefreq>
      <priority>0.3</priority>
   </url>
EOF

  IFS=$'\n'

  for html in $(find "$HTML_DIR" -type f -name '*.html' -printf '%P\n'); do
    if [[ $html =~ index.html|search.html|genindex.html ]]; then
      continue
    fi

    cat <<EOF
   <url>
      <loc>$BASE_URL/$html</loc>
      <lastmod>$(date -d @$(stat -c %Y "$HTML_DIR"/$html) +%Y-%m-%d)</lastmod>
      <changefreq>always</changefreq>
      <priority>0.5</priority>
   </url>
EOF
  done

  cat <<EOF
</urlset> 
EOF

} > "$HTML_DIR/sitemap.xml"

echo -e "'$HTML_DIR/sitemap.xml' is generated."
