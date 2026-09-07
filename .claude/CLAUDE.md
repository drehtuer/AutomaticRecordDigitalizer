# AutomaticRecordDigitalizer

A DIY record changer that digitises a vinyl collection unattended. The repository holds the
design documents, an interactive concept model, and a parametric CadQuery model with a motion
planner and a collision checker. Nothing has been built yet.

## How changes reach main

**Never commit to `main`.** Every change — code, documents, configuration — goes through a pull
request on its own branch:

1. `git switch -c <topic-branch>` from an up-to-date `main`.
2. Commit the change there.
3. `git push -u origin <topic-branch>` and open the pull request (`gh pr create`).
4. **Switch back to `main` afterwards** (`git switch main`), so the working tree is never left
   sitting on a pushed topic branch.

Wait for CI to pass on the pull request before asking for a merge.

## Checks

All three run in CI on every pull request, and all three must be clean before pushing:

```sh
ruff check .                         # Python, configured in ruff.toml
npx --yes markdownlint-cli2@0.23.2   # Markdown, configured in .markdownlint-cli2.yaml
python -m cad.check_collisions       # the full cycle, exit 1 on any intersection
```

Dependabot (`.github/dependabot.yml`) keeps the actions, `cad/requirements.txt` and the
devcontainer image current; its pull requests run the same three checks.

Formatting is governed by `.editorconfig`: UTF-8, LF, a final newline, spaces not tabs, two-space
indentation everywhere except Python, which stays at the four spaces PEP 8 and ruff assume.

## Layout

- `README.md` — entry point; every design document is linked from it, and a new one has to be
  added to its table.
- `docs/01…07-*.md` — the design: specification, operating cycle, electronics and software,
  bill of materials, design decisions, open questions, status.
- `cad/` — the CadQuery model, `kinematics.py` (poses and planner) and `check_collisions.py`;
  `cad/params.py` holds every dimension in millimetres and everything downstream follows it.
  See `cad/README.md`.
- `cad/export/` — generated STEP and STL files, committed at reviewed states. Regenerate them
  after changing `cad/params.py`.
- `cad-model.html` — WebGL viewer of the machine, fed by `cad/export/web/machine.glb`. Regenerate
  the glb with `python -m cad.export_web` after changing `cad/params.py`, in the same breath as
  the STEP and STL exports.
- `concept-model.html` — standalone interactive 3D model of the full cycle. Its geometry is its
  own and predates the CAD corrections, so it is right about the sequence and wrong about
  dimensions.

## Working on the model

`cad/params.py` is the single source of dimensions; change numbers there rather than in the part
files. After any change to geometry or to the planner, run the collision checker and say what it
reported; CI runs it too, so a change that makes the machine hit itself cannot be merged. The
sweep takes about a minute and a half and currently reports 831 samples with 0 collisions.

The devcontainer (`.devcontainer/`) has CadQuery, ruff and markdownlint-cli2 installed.

## Documentation site

`.github/workflows/documentation.yml` builds `_config.yml` with GitHub Pages Jekyll and publishes
it to <https://drehtuer.github.io/AutomaticRecordDigitalizer/> when a `v*` release tag is pushed.

Publishing depends on one setting that is not in the repository: the `github-pages` environment
must have a deployment rule for the tag pattern `v*`. It allows the default branch only until
someone adds it, and then the build succeeds while the deploy is rejected with `Tag "v0.1.0" is
not allowed to deploy to github-pages due to environment protection rules`. The rule is in place
on this repository; a fork or a rebuilt repository needs it added again. The comment at the top
of the workflow has the `gh` command. There is no Gemfile and none is needed:
`actions/jekyll-build-pages` brings its own `github-pages` gem set. To preview the site locally,
build it in a throwaway container rather than adding gems to the repository:

```sh
docker run --rm -v "$PWD":/srv -w /srv ruby:3.2-slim bash -c \
  'apt-get update -qq && apt-get install -y -qq build-essential git >/dev/null &&
   git config --global --add safe.directory /srv &&
   gem install bundler github-pages --no-document -q &&
   jekyll build --destination /srv/_site'
```
