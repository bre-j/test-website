#!/usr/bin/env bash
#
# Remove the GitHub Actions workflows that only make sense for the upstream
# al-folio project, not for a site built from it.
#
# Each one below either needs a secret this repository does not have, publishes
# artefacts belonging to the upstream project, or benchmarks the upstream demo
# site. They burn Actions minutes and show up as red X's on every commit.
#
# Run once, from the repository root, then review with `git status`:
#
#   bash bin/trim-ci-workflows.sh
#
set -euo pipefail

cd "$(dirname "$0")/.."

if [ ! -d .github/workflows ]; then
  echo "error: run this from the repository root" >&2
  exit 1
fi

remove() {
  local path=".github/workflows/$1"
  local why="$2"
  if [ -e "$path" ]; then
    if git ls-files --error-unmatch "$path" >/dev/null 2>&1; then
      git rm -q "$path"
    else
      rm -f "$path"
    fi
    printf '  removed %-28s %s\n' "$1" "$why"
  fi
}

echo "Removing upstream-only workflows:"
remove lighthouse-badger.yml "page_build trigger, needs LIGHTHOUSE_BADGER_TOKEN"
remove update-citations.yml "scheduled 3x/week, needs secrets.PAT"
remove deploy-image.yml "pushes a Docker image, needs DOCKER_USERNAME/PASSWORD"
remove deploy-docker-tag.yml "pushes a Docker image, needs DOCKER_USERNAME/PASSWORD"
remove docker-slim.yml "pushes a Docker image, needs DOCKER_USERNAME/PASSWORD"
remove star-history.yml "regenerates upstream star-history SVGs, commits to main"
remove release.yml "cuts al-folio releases"
remove update-screenshots.yml "regenerates the upstream README screenshots"
remove visual-regression.yml "diffs against an upstream v0.16.3 baseline"
remove prettier-comment-on-pr.yml "driven by upstream repository_dispatch"
remove prettier-html.yml "maintainer-only formatting helper"

cat <<'NOTE'

Kept, because they are useful on your own site:

  deploy.yml           builds the site and pushes it to gh-pages  <- the important one
  prettier.yml         formatting check on push and PR
  unit-tests.yml       style contract + the seven integration tests
  upgrade-check.yml    al-folio upgrade audit
  codeql.yml           security scanning
  broken-links.yml     link check on push (can be noisy about external links)
  broken-links-site.yml link check against the deployed site
  axe.yml              accessibility check, manual trigger only
  update-tocs.yml      regenerates TOCs in root/docs markdown
  render-cv.yml        only fires if _data/cv.yml changes; the CV page is off

If deploy.yml is the only one you care about, delete the rest too — nothing in
the site depends on them.

NOTE
