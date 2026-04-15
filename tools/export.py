#!/usr/bin/env python3
"""
Architecture Diagram Exporter
Converts HTML architecture diagrams to PNG, PDF, and SVG formats.

Usage:
    python export.py diagram.html --format png
    python export.py diagram.html --format pdf
    python export.py diagram.html --format svg
    python export.py diagram.html --format all
    python export.py diagram.html --format png --width 2400 --output my-diagram.png

Requirements:
    pip install playwright beautifulsoup4
    playwright install chromium
"""

import argparse
import sys
import os
import re
from pathlib import Path


def extract_svg(html_path: str, output_path: str) -> str:
    """Extract inline SVG from HTML file."""
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        print("Error: beautifulsoup4 is required for SVG extraction.")
        print("Install with: pip install beautifulsoup4")
        sys.exit(1)

    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")
    svg_tag = soup.find("svg")

    if not svg_tag:
        print("Error: No <svg> element found in the HTML file.")
        sys.exit(1)

    # Add standalone SVG header
    svg_content = str(svg_tag)

    # Get viewBox for dimensions
    viewBox = svg_tag.get("viewBox", "0 0 1000 600")
    parts = viewBox.split()

    # Ensure xmlns is present
    if 'xmlns="http://www.w3.org/2000/svg"' not in svg_content:
        svg_content = svg_content.replace("<svg", '<svg xmlns="http://www.w3.org/2000/svg"', 1)

    # Add dark background
    if '<rect width="100%"' not in svg_content and '<rect width="' in svg_content:
        # Background already exists in the inline SVG
        pass

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    return output_path


def html_to_image(html_path: str, output_path: str, fmt: str = "png",
                  width: int = 1920, scale: int = 2) -> str:
    """Convert HTML to PNG or PDF using Playwright."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Error: playwright is required for PNG/PDF export.")
        print("Install with:")
        print("  pip install playwright")
        print("  playwright install chromium")
        sys.exit(1)

    abs_path = os.path.abspath(html_path)
    file_url = f"file://{abs_path}"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(
            viewport={"width": width, "height": 800},
            device_scale_factor=scale,
        )
        page.goto(file_url, wait_until="networkidle")

        # Wait for fonts to load
        page.wait_for_timeout(2000)

        if fmt == "png":
            # Full page screenshot
            page.screenshot(path=output_path, full_page=True, type="png")
        elif fmt == "pdf":
            # PDF export
            page.pdf(
                path=output_path,
                format="A3",
                landscape=True,
                print_background=True,
                margin={"top": "0.5in", "right": "0.5in", "bottom": "0.5in", "left": "0.5in"},
            )
        else:
            print(f"Error: Unknown format '{fmt}'")
            sys.exit(1)

        browser.close()

    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Export architecture diagrams to PNG, PDF, or SVG.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python export.py diagram.html --format png
  python export.py diagram.html --format pdf
  python export.py diagram.html --format svg
  python export.py diagram.html --format all
  python export.py diagram.html --format png --width 2400 --scale 3
        """,
    )

    parser.add_argument("input", help="Input HTML file path")
    parser.add_argument(
        "--format", "-f",
        choices=["png", "pdf", "svg", "all"],
        default="png",
        help="Output format (default: png)",
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path (auto-generated if not specified)",
    )
    parser.add_argument(
        "--width", "-w",
        type=int,
        default=1920,
        help="Viewport width in pixels for PNG/PDF (default: 1920)",
    )
    parser.add_argument(
        "--scale", "-s",
        type=int,
        default=2,
        help="Device scale factor for PNG (default: 2, use 3 for high-res)",
    )

    args = parser.parse_args()

    # Validate input
    if not os.path.exists(args.input):
        print(f"Error: File not found: {args.input}")
        sys.exit(1)

    input_path = Path(args.input)
    stem = input_path.stem
    parent = input_path.parent

    formats = ["png", "pdf", "svg"] if args.format == "all" else [args.format]

    for fmt in formats:
        if args.output and len(formats) == 1:
            output = args.output
        else:
            output = str(parent / f"{stem}.{fmt}")

        print(f"Exporting {fmt.upper()} → {output}")

        if fmt == "svg":
            extract_svg(args.input, output)
        elif fmt in ("png", "pdf"):
            html_to_image(args.input, output, fmt=fmt, width=args.width, scale=args.scale)
        else:
            print(f"Unknown format: {fmt}")
            continue

        size_kb = os.path.getsize(output) / 1024
        print(f"  ✓ {size_kb:.0f} KB")

    print("\nDone!")


if __name__ == "__main__":
    main()
