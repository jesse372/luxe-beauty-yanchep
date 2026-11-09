#!/usr/bin/env bash
# Rebuild every generated page, in the one order that works, then check the result.
# Usage: marketing/seo/build_all.sh
set -euo pipefail
cd "$(dirname "$0")/../.."
python3 marketing/seo/build_seo.py      >/dev/null   # suburb pages + areas hub (+ shared nav/footer/head)
python3 marketing/seo/build_guides.py   >/dev/null   # guides + guides hub
python3 marketing/seo/build_yanchep.py  >/dev/null   # lash prices page
python3 marketing/seo/build_brows.py    >/dev/null   # eyebrows page
python3 marketing/seo/build_infills.py  >/dev/null   # lash infills page
python3 marketing/seo/build_schema.py                # homepage graph + FAQ, static page schema, llms.txt, robots.txt
python3 marketing/seo/finalize.py                    # images, fonts, links, sitemap (must run last)
python3 marketing/seo/check.py                       # fails loudly if anything is broken
