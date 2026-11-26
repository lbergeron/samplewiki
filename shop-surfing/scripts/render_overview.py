#!/usr/bin/env python3
"""Regenerate shop-surfing/catalog-overview.md from shop-surfing/catalog.json.

Usage (from the repository root):
    python3 shop-surfing/scripts/render_overview.py
"""
import json
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
catalog = json.load(open(ROOT / "catalog.json"))
products = [c for c in catalog if c["objecttype"] == "Product"]
variants = [c for c in catalog if c["objecttype"] == "Variant"]
pmap = {p["ec_product_id"]: p for p in products}

ATTR_LABELS = OrderedDict([("material", "Material"), ("quality", "Quality"), ("color", "Colour"),
                           ("thickness", "Thickness"), ("material_compatibility", "Material compatibility")])
TABLE_TITLES = {"Surfboards": "Surfboard variants", "Fins and Board Hardware": "Fin variants",
                "Wetsuits": "Wetsuit variants", "Wax and Maintenance Supplies": "Wax and maintenance variants"}


def price(v):
    return f"${v:,.0f} CAD"


def num(v):
    return f"{v:.2f}"


def table(headers, rows, right=()):
    widths = [max(len(h), *(len(r[i]) for r in rows)) for i, h in enumerate(headers)]

    def line(cells):
        return "| " + " | ".join(c.rjust(w) if i in right else c.ljust(w)
                                 for i, (c, w) in enumerate(zip(cells, widths))) + " |"
    sep = "| " + " | ".join(("-" * (w - 1) + ":") if i in right else "-" * w for i, w in enumerate(widths)) + " |"
    return "\n".join([line(headers), sep] + [line(r) for r in rows])


def attr(rec, key):
    """Attribute of a variant, falling back to its parent product (material and quality live on products)."""
    return rec.get(key) or pmap[rec["ec_product_id"]].get(key) or ""


out = ["# Surfing Product Catalog", "",
       "A curated starting catalog for a surf shop. All prices are in Canadian dollars (CAD). Variant counts are intentionally kept below 50 in every section.",
       "",
       "A product is made of a single material. Models offered in several materials (for example, the longboard in PU fiberglass, EPS epoxy and soft-top foam) are separate products that share the same `ec_item_group_id`. Variants of those products are colour schemes.",
       ""]

categories = list(OrderedDict.fromkeys(p["ec_category"] for p in products))
n = 0
for cat in categories:
    cprods = [p for p in products if p["ec_category"] == cat]
    cvars = [v for v in variants if pmap[v["ec_product_id"]]["ec_category"] == cat]
    out.append(f"## {cat}" + (f" — {len(cvars)} variants" if cvars else ""))
    out.append("")
    for p in cprods:
        n += 1
        out.append(f"{n}. {p['ec_name']} — **{price(p['ec_price'])}**")
    out.append("")
    if cvars:
        keys = [k for k in ATTR_LABELS if any(attr(v, k) for v in cvars)]
        headers = ["Product", "SKU"] + [ATTR_LABELS[k] for k in keys] + ["Price"]
        rows = [[pmap[v["ec_product_id"]]["ec_name"], v["sku"]] + [attr(v, k) for k in keys] + [price(v["ec_price"])]
                for v in cvars]
        out += [f"### {TABLE_TITLES.get(cat, cat + ' variants')}", "", table(headers, rows, right={len(headers) - 1}), ""]

out += ["## Coveo catalog metadata", "",
        "The tables below enrich the human-readable catalog with the fields required to build a Coveo Commerce catalog payload. The `documentId` values are stable identifiers, prices are decimal CAD amounts without currency symbols, and `objecttype` identifies the catalog object. The catalog currently models products and variants; availability objects are not included because store inventory data is not available.",
        "", "### ID and field conventions", "",
        "- Product `documentId`: `product://<ec_product_id>`.",
        "- Variant `documentId`: `variant://<ec_variant_id>`.",
        "- `sku`: unique per record. Products use `SRF-<category code>-<NNN>`, numbered within each category (SB Surfboards, FN Fins and Board Hardware, LA Leashes and Surf Accessories, WS Wetsuits, WC Wetsuit Care and Changing Gear, CL Clothing and Sun Protection, SF Safety and Water Accessories, WX Wax and Maintenance Supplies, TR Travel and Transport, TL Training and Lifestyle). Models offered in several materials append a material code to the model number: PU (PU fiberglass), EP (EPS epoxy), ST (soft-top foam), CS (carbon sandwich), FG (fiberglass), CC (carbon composite), HC (honeycomb composite), NY (nylon composite), RP (reinforced polymer). Variants append `-V<NN>` to their parent product's SKU.",
        "- `ec_item_group_id` groups the products of the same model built from different materials (for example, all longboard surfboards). Other products use their own product ID.",
        "- `material` and `quality` are product attributes. Variant attributes are `color` (colour scheme), `thickness` and `quality` (wetsuits) and `material_compatibility` (wax and maintenance supplies).",
        "- `ec_category` uses a stable category path.",
        "- `ec_brand` uses a representative fictional brand assortment, including AquaArc, TideNest, WaveWoven, Breakwater Atelier, Saltglass, FoamHarbor, FinFoundry, HorizonTide, Northstar Surfworks, SwellCove, DriftKite, WaxWisp, and Seastone Works; replace these with the actual brands carried.",
        "- Product records include Coveo-required fields: `documentId`, `ec_name`, `ec_product_id`, `ec_description`, `ec_category`, `ec_price`, `ec_item_group_id`, and `objecttype`.",
        "- Variant records include Coveo-required fields: `documentId`, `ec_name`, `ec_product_id`, `ec_variant_id`, and `objecttype`, plus their variant attributes and price.",
        "", "### Product records", ""]
ph = ["documentId", "ec_name", "ec_product_id", "sku", "ec_description", "ec_category", "ec_price", "ec_item_group_id", "ec_brand", "material", "quality", "objecttype"]
out += [table(ph, [[p.get(k) and (num(p[k]) if k == "ec_price" else str(p[k])) or "—" for k in ph] for p in products], right={6}), ""]
out += ["### Variant records", "",
        "Each row has a unique `ec_variant_id` and a parent `ec_product_id`.", ""]
vh = ["documentId", "ec_name", "ec_product_id", "ec_variant_id", "sku", "quality", "color", "thickness", "material_compatibility", "ec_price", "objecttype"]
out += [table(vh, [[v.get(k) and (num(v[k]) if k == "ec_price" else str(v[k])) or "—" for k in vh] for v in variants], right={9}), ""]

(ROOT / "catalog-overview.md").write_text("\n".join(out))
print(f"Wrote {ROOT / 'catalog-overview.md'}: {len(products)} products, {len(variants)} variants")
