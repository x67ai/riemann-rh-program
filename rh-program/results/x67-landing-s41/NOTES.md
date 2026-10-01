# x67.ai landing page: notes for review

Files here: `index.html` (5,852 bytes, self-contained, inline CSS, no JavaScript),
`_redirects.proposed`, and six screenshots: `desktop-light.png` and `desktop-dark.png`
(1280×900), `mobile-light.png` and `mobile-dark.png` (390×844), and full-length
`desktop-light-full.png` (1280×1114) and `mobile-light-full.png` (390×1236), which show
the whole page down to the footer.

## Palette (from the brand-guidelines skill)

| Role | Light theme | Dark theme |
|---|---|---|
| Background | `#faf9f5` Light | `#141413` Dark |
| Text | `#141413` Dark | `#faf9f5` Light |
| Secondary text (labels, year/pages, footer) | `#5a5955` derived* | `#b0aea5` Mid Gray |
| Links and focus ring | `#af4928` derived** | `#d97757` Orange |
| Section rules | `#b0aea5` Mid Gray | `#4b4a46` derived (Dark + 35% Mid Gray) |
| Separators between papers | `#e8e6dc` Light Gray | `#2b2b29` derived (Dark + 15% Mid Gray) |
| Mark and favicon | `#d97757` square, `#faf9f5` x | same |

\* Mid Gray mixed 55% toward Dark: raw Mid Gray on Light is only 2.11:1.
\** Orange at the same hue and saturation, HSL lightness 0.596 → 0.42: raw Orange on
Light is only 2.96:1, which fails AA for text. The dark theme uses the raw palette.
Blue `#6a9bcc` and Green `#788c5d` are not used (one accent, for restraint).

## Type

The skill sets headings in Poppins (Arial fallback) and body text in Lora (Georgia
fallback), with Poppins for headings 24 pt and larger. The stacks are
`Poppins, Arial, sans-serif` (wordmark, section labels, year/page lines, repository
link, footer) and `Lora, Georgia, serif` (lead sentence, paper titles, body sentence).
The 20 px paper titles fall under that 24 pt line, so they use the serif. No font files
are loaded: visitors who have Poppins and Lora installed see them, everyone else sees
Arial and Georgia. Neither font is installed on this Mac, so the screenshots show the
fallbacks, which is what most visitors will see.

## Contrast (WCAG 2.x relative luminance)

| Pair | Ratio | Need |
|---|---|---|
| Light: text `#141413` on `#faf9f5` | 17.50:1 | 4.5 |
| Light: secondary `#5a5955` on `#faf9f5` | 6.66:1 | 4.5 |
| Light: link and focus `#af4928` on `#faf9f5` | 5.24:1 | 4.5 (focus 3) |
| Dark: text `#faf9f5` on `#141413` | 17.50:1 | 4.5 |
| Dark: secondary `#b0aea5` on `#141413` | 8.29:1 | 4.5 |
| Dark: link and focus `#d97757` on `#141413` | 5.90:1 | 4.5 (focus 3) |

Rules (2.11, 1.19, 2.08 and 1.30:1) are decorative separators, which have no
requirement. Links are underlined, so they do not rely on color alone. The mark's x
(`#faf9f5` on `#d97757`, 2.96:1) is a decorative logo graphic marked `aria-hidden`.

## Check list

- **Size:** 5,852 bytes, under the 20 kB limit.
- **`grep -c "http" index.html` prints 5:**
  - line 11: `xmlns='http://www.w3.org/2000/svg'` inside the favicon's `data:` URI.
    This is the SVG namespace name, an identifier that is never fetched; the icon is
    inline.
  - lines 145, 151, 157: the three DOI hyperlinks (`<a href>`), followed only on click.
  - line 166: the GitHub hyperlink (`<a href>`), followed only on click.
- The file contains no `src=`, `url(`, `@import`, `<script`, `<img`, stylesheet link or
  `@font-face`. Its only `<link>` is the icon, as a `data:` URI.
- **Measured:** Chrome's network log (`--log-net-log`) while loading the page, compared
  with the same capture on an empty page. Both runs contacted the same hosts, all of
  them Chrome's own background services (update, time, accounts, google.com). Nothing
  went to doi.org, github.com or any font host.
- **`grep -i -c "anthropic\|claude" index.html` prints 0.** The page has no email
  address and no British spellings.
- **W3C Nu HTML checker** (validator.w3.org/nu, 2026-10-01): no errors. Its one
  info-level message is "The list role is unnecessary for element ol". I kept the role
  on purpose: Safari with VoiceOver stops announcing a list styled `list-style: none`
  unless it carries `role="list"`. Delete it if a message-free validation matters more.
- **PDF page counts** in `public/*.pdf` (15, 41, 19) match the brief.
- **Focus:** tested with a throwaway copy whose first PDF link had `autofocus`. The 2 px
  outline in the link color (offset 3 px) is clearly visible in both themes.
- **Widths:** checked at 360, 390 and 1280 px. There is no horizontal scroll at any of
  them.

How the screenshots were made, with headless Chrome 154: (1) Headless Chrome follows the
Mac's dark appearance, so the color scheme was forced with
`--blink-settings=preferredColorScheme=1` (light) or `=0` (dark), without editing the
CSS. (2) Its viewport is never narrower than 500 px, so a plain `--window-size=390,844`
lays the page out at 500 px and then crops it. The mobile shots therefore load the page
in a 390 px iframe and crop to that iframe, which gives a true 390 px layout. (3) It
needs `--use-mock-keychain`, or it waits on the macOS keychain and never exits.

## Choices made, and things I was unsure about

1. **Apostrophe:** "Haglund’s" uses a curly apostrophe (the brief has a straight one),
   because the typeset paper uses ’. Changing it back is a one-character edit.
2. **No-wrap span:** "Rudnick–Sarnak-range" sits in a no-wrap span so the name pair
   never splits across lines. At 360 px this leaves "robust under" as a short line.
3. **Screen readers:** each PDF and DOI link has `aria-describedby` pointing at its
   paper's title, so it is announced with the title rather than as a bare "PDF". The
   titles are `h3` elements whose ids equal the PDF names, so links such as
   `x67.ai/#haglund-counterexample` work. The titles themselves are not links.
4. **Footer license:** "CC BY 4.0" is plain text, as given. It could link to the
   license deed.
5. **Extra head tags:** `color-scheme` and `theme-color` meta tags are present; they
   make no requests.
6. **Deploy:** copy `index.html` into `public/` and replace `public/_redirects` with
   `_redirects.proposed`. The current `/` rule must be removed. The comments in
   `public/README.md` and `wrangler.toml` still say `/` redirects to GitHub.
7. **Validation upload:** validating meant posting the page source to
   validator.w3.org. The page contains only public facts.
