# DEPLOY notes

## GitHub Actions CI workflow

The CI workflow file lives in `DEPLOY/github-workflows/ci.yml` instead of
`.github/workflows/ci.yml` because the access token used for the initial
upload didn't have the `workflow` scope (GitHub blocks workflow file
creation without it).

To enable CI:

1. Open <https://github.com/settings/tokens> and create a new classic PAT
   with both `repo` **and** `workflow` scopes (or edit the existing one).
2. In your local clone, move the file:

   ```bash
   git clone https://github.com/amanraj1240/AradhyeMusic.git
   cd AradhyeMusic
   mkdir -p .github/workflows
   git mv DEPLOY/github-workflows/ci.yml .github/workflows/ci.yml
   git commit -m "ci: enable GitHub Actions"
   git push
   ```

   …or use the GitHub web UI: open `DEPLOY/github-workflows/ci.yml`,
   click "Edit" → "Save in a new file" → set path to
   `.github/workflows/ci.yml`, then delete the file under `DEPLOY/`.

That's the only manual step. Everything else (Dockerfile, docker-compose,
deploy manifests, code) is already wired up.
