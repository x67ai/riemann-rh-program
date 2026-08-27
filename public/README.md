# What this folder is

The two papers, served at https://x67.ai by Cloudflare Pages.

## Cloudflare Pages settings

    Production branch   main
    Framework preset    None
    Build command       (leave empty)
    Output directory    public
    Root directory      (leave empty)

Nothing is built. The files here are served as-is, so a push to `main` on GitHub
redeploys within a minute or two.

## URLs — permanent once posted, do not rename

    https://x67.ai/cubic-augmentation-no-go.pdf
    https://x67.ai/tate-products-no-go.pdf

`/` itself 302s to the GitHub repository (see `_redirects`), so the root does not
return 404 for anyone who trims the URL out of curiosity. To put a real page
there later, drop an `index.html` into this folder and delete that line.

## Keeping the PDFs current

These are copies. The papers live at
`rh-program/results/arxiv/{a4-no-go,seed-no-go}/main.pdf`. After rebuilding
either one:

    bash public/sync.sh && git add -A public && git commit -m "sync served PDFs"

## How it is actually deployed (done 2026-08-28)

Not Cloudflare Pages. The dashboard now routes git-connected projects through
Workers, so this is an assets-only Worker configured by `wrangler.toml` at the
repository root: `[assets] directory = "./public"`, no `main`, no script. The
build runs `npx wrangler deploy` in Cloudflare's container, so nothing needs
installing locally.

    Worker            riemann-rh-program
    workers.dev       riemann-rh-program.jay7yagi.workers.dev
    Custom domain     x67.ai  (root, Production)
    Build command     None
    Deploy command    npx wrangler deploy
    Root directory    /

`.assetsignore` keeps this README and `sync.sh` from being served.

## The apex redirect, and why it mattered

The zone had three redirect rules. `Redirect from root to WWW [Template]`
matched `https://x67.ai/*` and fired *before* the Worker, so every paper URL
301'd to www even though the Worker was correctly bound. It is now **Disabled**
rather than deleted, so it is one toggle to restore under
Rules -> Overview -> Redirect Rules.

The other two rules, both `Redirect from HTTP to HTTPS`, are still Active and
should stay: `http://x67.ai/` still upgrades to HTTPS correctly.

## Still outstanding

`www.x67.ai` continues to point at the Notion host and will break when that
lapses. To keep it working, add `www.x67.ai` as a second custom domain on the
same Worker.
