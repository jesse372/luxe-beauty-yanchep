#!/usr/bin/env bash
# Inject a Google Search Console verification meta tag into index.html, deploy, confirm.
# Usage:  ./marketing/seo/verify-gsc.sh <token>
#   <token> = the content="..." value from GSC's "HTML tag" method (NOT the whole tag)
set -euo pipefail
cd "$(dirname "$0")/../.."

TOKEN="${1:-}"
[ -n "$TOKEN" ] || { echo "usage: verify-gsc.sh <token>"; exit 1; }
# accept a full tag paste too, and pull the token out of it
if [[ "$TOKEN" == *"google-site-verification"* ]]; then
  TOKEN=$(printf '%s' "$TOKEN" | sed -n 's/.*content="\([^"]*\)".*/\1/p')
fi
[[ "$TOKEN" =~ ^[A-Za-z0-9_-]{20,}$ ]] || { echo "token looks wrong: '$TOKEN'"; exit 1; }

TAG="<meta name=\"google-site-verification\" content=\"$TOKEN\">"

python3 - "$TOKEN" <<'PY'
import sys,re
tok=sys.argv[1]; tag='<meta name="google-site-verification" content="%s">'%tok
s=open("index.html",encoding="utf-8").read()
s=re.sub(r'\n?<meta name="google-site-verification"[^>]*>','',s)   # idempotent
s=s.replace('<meta charset="utf-8">','<meta charset="utf-8">\n'+tag,1)
open("index.html","w",encoding="utf-8").write(s)
assert tag in open("index.html",encoding="utf-8").read(), "injection failed"
print("  injected into index.html")
PY

git add index.html
git commit -q -m "Add Google Search Console verification tag

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
git push -q origin main
echo "  pushed - waiting for GitHub Pages..."
for i in $(seq 1 20); do
  sleep 10
  if curl -s "https://luxebeautyyanchep.com/" | grep -q "$TOKEN"; then
    echo "  LIVE: verification tag is serving. Click Verify in Search Console now."; exit 0
  fi
done
echo "  not live after 200s - check https://github.com/jesse372/luxe-beauty-yanchep/actions"; exit 1
