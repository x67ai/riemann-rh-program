#!/usr/bin/env bash
# Refresh the served PDFs from the built papers. Run from the repository root.
set -euo pipefail
cd "$(dirname "$0")/.."
cp rh-program/results/arxiv/a4-no-go/main.pdf   public/cubic-augmentation-no-go.pdf
cp rh-program/results/arxiv/seed-no-go/main.pdf public/tate-products-no-go.pdf
echo "synced:"
ls -lh public/*.pdf | awk '{printf "  %-8s %s\n", $5, $9}'
