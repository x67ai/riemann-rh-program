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

## Taking over the apex — two things that will bite

1. There is an existing redirect sending `x67.ai` to `www.x67.ai`. A Cloudflare
   Redirect Rule or Page Rule fires *before* Pages, so until it is deleted the
   PDF URLs will keep bouncing to www. Delete it.
2. The apex currently has DNS records pointing at the old Notion host. Adding
   `x67.ai` as a Pages custom domain will ask to replace them; let it.

`www.x67.ai` can be added to the same Pages project as a second custom domain if
you want both to work.
