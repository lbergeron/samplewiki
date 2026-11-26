#!/usr/bin/env python3
"""Generate shop-surfing/documents.json: product documents for a Coveo Push source.

Usage (from the repository root):
    python3 shop-surfing/scripts/generate_documents.py

Reads  shop-surfing/catalog.json
Writes shop-surfing/documents.json   (a plain JSON array, the format `coveo source:push:add` expects)

Link model (all values refer to ids in catalog.json):
  related_product_ids  ec_product_id of every product the document applies to
  related_variant_ids  ec_variant_id of every variant the document applies to (always the complete list)
  related_skus         product and variant SKUs, for convenience
  doc_scope            product  -> applies to every variant of the listed product(s)
                       material -> applies to every product/variant made of `material`
                       variant  -> applies to specific variants only
A variant is linked to at most MAX_DOCS_PER_VARIANT documents; the script fails if this is exceeded.
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from doc_data_gear import DATA as GEAR  # noqa: E402
from doc_data_lifestyle import DATA as LIFESTYLE  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
MAX_DOCS_PER_VARIANT = 10
DATE = "2026-11-26T00:00:00.000Z"
SOURCE_PREFIX = "doc://shop-surfing/"

DATA = {**GEAR, **LIFESTYLE}
catalog = json.load(open(ROOT / "catalog.json"))
products = {c["ec_product_id"]: c for c in catalog if c["objecttype"] == "Product"}
variants = [c for c in catalog if c["objecttype"] == "Variant"]
variants_by_product = defaultdict(list)
for v in variants:
    variants_by_product[v["ec_product_id"]].append(v)
# Models made in several materials are separate products sharing ec_item_group_id.
groups = defaultdict(list)
for p in products.values():
    groups[p["ec_item_group_id"]].append(p["ec_product_id"])


def group_products(gid):
    if gid not in groups:
        sys.exit(f"Unknown item group {gid}")
    return list(groups[gid])

TYPES = {
    "S": "Specification sheet",
    "M": "User manual",
    "I": "Installation guide",
    "C": "Maintenance guide",
}
SLUG = {"S": "specification-sheet", "M": "user-manual", "I": "installation-guide", "C": "maintenance-guide"}

SAFETY = {
    "Surfboards": "Always surf with a leash, stay aware of other surfers and keep a safe distance from rocks and the shore break. Check the board for dings and the fins for tightness before every session.",
    "Fins and Board Hardware": "Fins are sharp. Handle them with care, fit and remove them with a fin key, and never surf with a loose or damaged fin.",
    "Leashes and Surf Accessories": "No leash or accessory removes the risk of surfing. Inspect all gear before each session and replace anything that shows wear.",
    "Wetsuits": "A wetsuit provides thermal protection but not buoyancy. Choose the thickness that matches the water temperature and limit your time in cold water.",
    "Wetsuit Care and Changing Gear": "Keep care products out of reach of children and follow the label directions. Test any product on a small, hidden area first.",
    "Clothing and Sun Protection": "Clothing reduces but does not eliminate sun exposure. Reapply reef-safe sunscreen to exposed skin and take regular breaks in the shade.",
    "Safety and Water Accessories": "Safety gear reduces risk but does not remove it. Know your limits, surf with others and do not rely on a single piece of equipment.",
    "Wax and Maintenance Supplies": "Work in a ventilated area and wear gloves and eye protection when handling resins, solvents or sanding dust. Follow the label directions.",
    "Travel and Transport": "Check that loads are secure before moving and re-check at every stop. Do not exceed the rated load for any rack, strap or cart.",
    "Training and Lifestyle": "Warm up before exercising and stop if you feel pain. Consult a health professional before starting any new training programme.",
}

CLOSING = {
    "S": "Specifications are nominal and may vary slightly between production runs. Keep this sheet with your purchase records for compatibility and warranty checks.",
    "M": "Keep this manual for future reference. If you are unsure about any step, ask your surf shop before using the product.",
    "I": "If something does not seat or align properly, stop and check the steps again rather than forcing it. When in doubt, have a qualified surf shop technician carry out the installation.",
    "C": "Stop using the product and replace or repair it if you notice cracks, tears or other structural damage.",
}

EST_TIME = {
    "fcs-compatible-fin-box": "2 to 3 hours, plus resin cure time",
    "futures-compatible-fin-box": "2 to 3 hours, plus resin cure time",
    "surfboard-leash-plug": "1 to 2 hours, plus resin cure time",
    "surfboard-traction-pad": "20 minutes, plus 24 hours adhesive cure",
    "longboard-nose-rider-pad": "20 minutes, plus 24 hours adhesive cure",
    "surfboard-deck-grip-tape": "15 minutes, plus 24 hours adhesive cure",
    "surfboard-tail-block": "15 minutes, plus 24 hours adhesive cure",
    "surfboard-rack-wall-mount": "30 minutes",
    "soft-roof-rack-system": "10 minutes",
}


def numbered(steps):
    return "\n".join(f"{i}. {s}" for i, s in enumerate(steps, 1))


def bullets(items):
    return "\n".join(f"- {s}" for s in items)


def variant_label(v):
    return " / ".join(v[k] for k in ("thickness", "material_compatibility", "quality", "color") if v.get(k))


def coverage_table(pids):
    """Models (one per material) and their variants covered by a specification sheet."""
    lines = []
    if len(pids) > 1:
        lines.append("Models covered by this sheet:")
        for pid in pids:
            p = products[pid]
            colours = ", ".join(f"{v['color']} ({v['sku']})" for v in variants_by_product.get(pid, []))
            lines.append(f"- {p['sku']}: {p['material']}, {p['quality']} (${p['ec_price']:,.0f} CAD)"
                         + (f". Colour schemes: {colours}" if colours else ""))
    else:
        vs = variants_by_product.get(pids[0], [])
        if vs:
            lines.append("Variants covered by this sheet:")
            lines += [f"- {v['sku']}: {variant_label(v)} (${v['ec_price']:,.0f} CAD)" for v in vs]
    return "\n".join(lines)


def make_doc(slug, title, doc_type, body, scope, product_ids, variant_ids, category, material=None, extra=None):
    # A product is linked only when the document applies to ALL of its variants. Material and
    # variant documents usually cover some variants of a product (e.g. only the EPS epoxy
    # longboard), so the parent product must not be linked or every variant would inherit it.
    vset = set(variant_ids)
    product_ids = [p for p in product_ids
                   if all(v["ec_variant_id"] in vset for v in variants_by_product.get(p, []))]
    prods = [products[p] for p in product_ids]
    skus = [p["sku"] for p in prods]
    vmap = {v["ec_variant_id"]: v for v in variants}
    skus += [vmap[v]["sku"] for v in variant_ids]
    doc = {
        "documentId": SOURCE_PREFIX + slug,
        "title": title,
        "data": body,
        "objecttype": "Document",
        "doc_type": doc_type,
        "doc_scope": scope,
        "doc_category": category,
        "related_product_ids": list(product_ids),
        "related_variant_ids": list(variant_ids),
        "related_skus": skus,
        "language": "en",
        "date": DATE,
        "author": "Seastone Works Product Documentation",
    }
    # Empty arrays make the CLI infer the wrong field type, so omit empty link fields.
    for k in ("related_product_ids", "related_variant_ids", "related_skus"):
        if not doc[k]:
            del doc[k]
    if material:
        doc["doc_material"] = material
    if extra:
        doc.update(extra)
    return doc


docs = []


def product_vids(pid):
    return [v["ec_variant_id"] for v in variants_by_product.get(pid, [])]


def all_vids(pids):
    return [vid for pid in pids for vid in product_vids(pid)]


# ----------------------------------------------------------------------------
# 1. Product documents. Content is keyed by ec_item_group_id, so a document applies to
#    every product of the group (e.g. the longboard in all its materials) and all their variants.
# ----------------------------------------------------------------------------
for gid in DATA:
    if gid not in groups:
        sys.exit(f"Document data for unknown item group {gid}")
for gid, pids in groups.items():
    entry = DATA.get(gid)
    if entry is None:
        sys.exit(f"No document data for item group {gid}")
    first = products[pids[0]]
    multi = len(pids) > 1
    name = first["ec_name"].split(" - ")[0] if multi else first["ec_name"]
    desc = first["ec_description"].split(". ")[0].rstrip(".") + "."
    cat, brand = first["ec_category"], first["ec_brand"]
    lower = name[0].lower() + name[1:] if not name.split()[0].isupper() else name

    for key in "SMIC":
        items = entry.get(key)
        if not items:
            continue
        if key == "S":
            if multi:
                mats = ", ".join(products[p]["material"] for p in pids)
                intro = (f"This specification sheet describes the {name} range from {brand}. {desc} "
                         f"The {lower} is available in {len(pids)} constructions ({mats}); this sheet applies to all of them.")
            else:
                intro = (f"This specification sheet describes the {name} ({first['sku']}) from {brand}. {desc} It applies to "
                         + ("all variants of this product." if variants_by_product.get(pids[0]) else "all units of this product."))
            parts = [intro, "Key specifications\n" + bullets(items)]
            ct = coverage_table(pids)
            if ct:
                parts.append(ct)
        elif key == "M":
            parts = [f"This manual explains how to use your {lower}. {desc}",
                     "Getting started\n" + numbered(items),
                     "Safety and good practice\n" + SAFETY[cat]]
        elif key == "I":
            t = EST_TIME.get(gid)
            intro = f"This guide explains how to install the {lower}. " + (f"Allow about {t}. " if t else "") + "Read all steps before you begin."
            parts = [intro, "Installation steps\n" + numbered(items)]
            if cat in ("Fins and Board Hardware", "Leashes and Surf Accessories"):
                parts.append("Safety and good practice\n" + SAFETY[cat])
        else:
            parts = [f"Regular care keeps your {lower} performing well and extends its life. Follow these steps after every session or as indicated.",
                     "Care steps\n" + numbered(items)]
        parts.append(CLOSING[key])
        docs.append(make_doc(f"{gid}-{SLUG[key]}", f"{name} – {TYPES[key]}", TYPES[key], "\n\n".join(parts),
                             "product", pids, all_vids(pids), cat))

# ----------------------------------------------------------------------------
# 2. Material documents (apply to every product/variant made of the same material)
# ----------------------------------------------------------------------------
def products_made_of(material):
    return [pid for pid, p in products.items() if p.get("material") == material]


def compatible_variants(material, product_ids):
    """Variants of repair/care products whose material_compatibility includes `material`."""
    return [v for v in variants if v["ec_product_id"] in product_ids
            and material in (v.get("material_compatibility") or "")]


def material_doc(slug, title, doc_type, material, intro, steps, notes, tool_variants=(), tool_products=(), category="Multiple"):
    """Link every product made of `material`, plus compatible repair/care products (tools).
    Tool products whose variants are only partly compatible are linked through those variants only."""
    pids = products_made_of(material) + list(tool_products)
    vids = all_vids(pids)
    for v in tool_variants:
        if v["ec_variant_id"] not in vids:
            vids.append(v["ec_variant_id"])
        if v["ec_product_id"] not in pids:
            pids.append(v["ec_product_id"])  # dropped by make_doc unless all its variants are linked
    body = "\n\n".join([intro, "Steps\n" + numbered(steps), notes, CLOSING["C"] if doc_type == "Maintenance guide" else CLOSING["I"]])
    docs.append(make_doc(slug, title, doc_type, body, "material", pids, vids, category, material))


repair_extras = ["surfboard-ding-repair-kit"]

# --- Repair guide: EPS epoxy boards
material_doc(
    "material-eps-epoxy-board-repair-guide", "Repair guide for EPS epoxy surfboards", "Maintenance guide", "EPS epoxy",
    "EPS epoxy boards have a closed-cell foam core wrapped in epoxy resin, which makes them light and durable but sensitive to the wrong repair materials. "
    "Polyester resin can dissolve EPS foam, so use only epoxy-compatible or UV-cure repair products. This guide applies to every EPS epoxy board in the catalog.",
    ["Dry the board fully. Wet foam will trap water and stain, so leave the damaged area to dry for at least 24 hours in a warm, shaded place.",
     "Sand the damaged area back to sound material with 80-grit paper, extending 2 cm beyond the ding. Wipe clean with a dry cloth.",
     "Fill small dings with epoxy-compatible resin or UV-cure resin. For larger holes, mix the epoxy repair kit and apply it with a spreader.",
     "For cracks and delaminations, cut fiberglass cloth slightly larger than the repair and saturate it with epoxy.",
     "Cure fully (epoxy: 12 to 24 hours; UV resin: a few minutes in direct sun). Sand with 120-grit, then 220-grit paper until the repair is flush with the surface."],
    "Never use polyester resin or solvent-based fillers on EPS foam. If the core is exposed over a large area or the board is waterlogged, take it to a qualified repairer.",
    tool_variants=compatible_variants("EPS epoxy", ("epoxy-resin-repair-kit", "solarez-style-uv-repair-resin", "surfboard-repair-sanding-kit")),
    tool_products=repair_extras)

# --- Repair guide: PU fiberglass boards
material_doc(
    "material-pu-fiberglass-board-repair-guide", "Repair guide for PU fiberglass surfboards", "Maintenance guide", "PU fiberglass",
    "PU fiberglass boards have a polyurethane foam core and a polyester resin shell. They are traditional, responsive and easy to repair at home with fiberglass cloth and compatible resin. "
    "This guide applies to every PU fiberglass board in the catalog.",
    ["Dry the damaged area. Water absorbed by PU foam turns it yellow and weakens the board, so let it dry for at least 24 hours before repairing.",
     "Sand around the ding with 80-grit paper to remove loose glass and expose clean fiberglass.",
     "Cut fiberglass cloth slightly larger than the damaged area. Mix polyester resin with catalyst and saturate the cloth on the board.",
     "Squeegee out the excess resin and let it cure in a ventilated, shaded place. UV-cure resin is a quicker option for small dings.",
     "Sand the cured repair with 120-grit then 220-grit paper to blend it into the board. Apply wax or a traction pad when finished."],
    "Polyester resin is flammable and gives off fumes: work outdoors or in a well-ventilated area and wear gloves and eye protection. Large cracks, stringer damage and broken tails should be assessed by a qualified repairer.",
    tool_variants=compatible_variants("PU fiberglass", ("fiberglass-repair-cloth", "solarez-style-uv-repair-resin", "surfboard-repair-sanding-kit")),
    tool_products=repair_extras)

# --- Care guide: soft-top foam boards
material_doc(
    "material-soft-top-foam-board-care-guide", "Care guide for soft-top foam surfboards", "Maintenance guide", "Soft-top foam",
    "Soft-top boards have a foam deck over a lightweight core, so they are forgiving and durable but sensitive to heat and solvents. "
    "This guide applies to every soft-top foam board in the catalog, including the soft-top beginner and foamie boards.",
    ["Rinse with fresh water after every session and let the board dry in the shade.",
     "Clean the deck with mild soap and a soft brush. Do not use solvents, abrasive pads or wax removers.",
     "Never leave a soft-top board in a closed car or in direct summer sun: heat can bubble the deck or warp the bottom.",
     "Do not apply surf wax to the deck; the foam provides its own grip.",
     "Store the board flat or on a padded rack. Do not stack heavy items on top."],
    "Small compressions and surface scratches are normal and do not affect performance. If the deck delaminates or the bottom skin tears, stop using the board and contact the shop.",
    tool_variants=compatible_variants("Soft-top foam", ("surfboard-cleaner",)), category="Surfboards")

# --- Care guide: carbon sandwich boards
material_doc(
    "material-carbon-sandwich-board-care-guide", "Care guide for carbon sandwich surfboards", "Maintenance guide", "Carbon sandwich",
    "Carbon sandwich boards use a carbon-fibre layer over a lightweight core to create a stiff, high-performance board. They resist deformation but can crack under point impacts. "
    "This guide applies to every carbon sandwich board in the catalog.",
    ["Rinse with fresh water after each session and wipe the board dry.",
     "Inspect rails, nose and tail after each session. Carbon cracks look like hairline lines, often with a lighter patch beneath.",
     "Keep the board shaded and never leave it in a closed vehicle.",
     "Use a padded board bag and avoid hard contact with rocks, racks and other boards.",
     "Have any crack assessed by a qualified repairer. Do not apply regular resin to carbon yourself."],
    "Carbon dust is an irritant: wear a mask and gloves if you sand any part of the board.",
    category="Surfboards")

# --- Care guides: fin materials
for mat, slug, title, blurb, extra in [
    ("Fiberglass", "material-fiberglass-fin-care-guide", "Care guide for fiberglass fins",
     "Fiberglass fins are durable, flexible and affordable. They flex under load, which gives a forgiving feel but means the tips can chip or delaminate with hard impacts.", "Inspect the trailing edge for cracks and the base for loose tabs."),
    ("Carbon composite", "material-carbon-composite-fin-care-guide", "Care guide for carbon composite fins",
     "Carbon composite fins are lightweight and stiff and keep their shape under heavy loads. They are more brittle than fiberglass, so impacts can cause hairline cracks.", "Hairline cracks near the base mean the fin should be replaced."),
]:
    material_doc(
        slug, title, "Maintenance guide", mat,
        f"{blurb} This guide applies to every {mat.lower()} fin in the catalog.",
        ["Remove the fins from the board after each session and rinse with fresh water.",
         "Dry the fins and the fin boxes. Sand left in a box will stop the fins from seating properly.",
         "Inspect the leading edge, tip and base. " + extra,
         "Store the fins in a case or the board bag, not loose.",
         "Replace the screws and plates if they show corrosion."],
        "Fins are sharp. Handle them with care and keep them away from skin and board surfaces.",
        category="Fins and Board Hardware")

# --- Installation guides: fin box materials
for mat, slug, title, blurb in [
    ("Nylon composite", "material-nylon-composite-fin-box-installation-guide", "Installation guide for nylon composite fin boxes",
     "Nylon composite fin boxes are the standard-tier option. They bond well to PU and epoxy boards and flex slightly, which helps absorb shocks."),
    ("Reinforced polymer", "material-reinforced-polymer-fin-box-installation-guide", "Installation guide for reinforced polymer fin boxes",
     "Reinforced polymer fin boxes are the premium option. They are stiffer than nylon composite and resist deformation under high fin loads."),
]:
    material_doc(
        slug, title, "Installation guide", mat,
        f"{blurb} This guide applies to every {mat.lower()} fin box in the catalog. Installation requires basic repair skills; consider asking a surf shop repairer to do it.",
        ["Remove the old fin box by routing around it, taking care not to damage the stringer.",
         "Clean the pocket and sand the surface to remove loose fibres. Dry-fit the new box with a fin to check alignment.",
         "Mix resin that is compatible with the board's construction (epoxy resin for EPS epoxy boards, polyester or epoxy for PU boards).",
         "Press the box into the pocket and wipe away the excess resin. Hold it in place with tape until it sets.",
         "Allow the resin to cure completely before fitting fins or surfing. Sand the surrounding area flush."],
        "A box that is not aligned with the other boxes will cause the board to track badly. Dry-fit with fins before applying resin.",
        category="Fins and Board Hardware")

# --- Care guide: neoprene (all products made of neoprene)
material_doc(
    "material-neoprene-care-guide", "Care guide for neoprene wetsuits and accessories", "Maintenance guide", "Neoprene",
    "Neoprene is a closed-cell rubber foam that keeps you warm by trapping a thin layer of water against your skin. It is sensitive to heat, sunlight and chemicals. "
    "This guide applies to every neoprene product in the catalog: wetsuits, jackets, vests, tops, pants, boots, gloves and hoods.",
    ["Rinse the inside and outside with fresh, cool water after every session.",
     "Hang the suit on a wide-shoulder hanger or drying rack, inside out first, then flip it to dry the outside. Keep it out of direct sun.",
     "Never use a washing machine, dryer, hot water, bleach or dry-cleaning solvent. Wash occasionally by hand with a neoprene-safe shampoo.",
     "Lubricate zips and seals with a neoprene-safe lubricant, and repair small tears early with flexible wetsuit glue.",
     "Store the suit hung or loosely folded in a cool, dry place. Avoid creasing, and do not hang by the shoulders for long periods."],
    "Use only products labelled neoprene-safe: the catalog's wetsuit shampoo, repair glue and zipper lubricant are suitable. Cleaners and glues not made for neoprene can damage it.",
    tool_products=["wetsuit-shampoo", "wetsuit-repair-glue", "wetsuit-zipper-and-seal-lubricant"], category="Wetsuits")

# ----------------------------------------------------------------------------
# 3. Cross-product / variant-specific documents
# ----------------------------------------------------------------------------
def cross_doc(slug, title, doc_type, scope, gids, intro, steps, closing_key, extra_vids=None, category="Multiple", extra=None):
    pids = [pid for gid in gids for pid in group_products(gid)]
    vids = all_vids(pids)
    if extra_vids is not None:
        vids = extra_vids
    body = "\n\n".join([intro, "Steps\n" + numbered(steps), CLOSING[closing_key]])
    docs.append(make_doc(slug, title, doc_type, body, scope, pids, vids, category, extra=extra))


# Fin compatibility
# Item group ids (each expands to every product of the group).
fin_products = ["thruster-fin-set", "quad-fin-set", "twin-fin-set", "single-longboard-fin", "fcs-compatible-fin-box",
                "futures-compatible-fin-box", "surfboard-fin-screws-and-plates"]
board_products = ["longboard-surfboard", "funboard-surfboard", "fish-surfboard", "shortboard-surfboard", "gun-surfboard",
                  "mini-malibu-surfboard", "soft-top-beginner-surfboard", "midlength-surfboard", "foamie-surfboard", "stand-up-paddle-surfboard"]
cross_doc(
    "fin-setup-and-compatibility-guide", "Choosing fins and fin boxes: setup and compatibility guide", "User manual", "product",
    fin_products + board_products,
    "Your board's fin boxes decide which fins you can use. This guide explains how to match fin sets, fin boxes and hardware to your surfboard. It applies to all surfboards, fin sets, fin boxes and fin hardware in the catalog.",
    ["Look at the fin boxes on your board: single-box (center only), dual-tab (FinFoundry-style or HorizonTide-style) or a 2+1 layout.",
     "Choose a fin set that matches the box type. Thruster, quad and twin sets fit dual-tab boxes. The single longboard fin fits a single center box.",
     "Choose a setup for the waves: thruster for all-round control, quad for speed in small waves, twin for flow, single for trim.",
     "Replace worn screws and plates with the surfboard fin screws and plates set, and replace damaged boxes with a compatible replacement fin box.",
     "Test the fins in the water and adjust their position in the box if your board feels too stiff or too loose."],
    "M", category="Fins and Board Hardware")

# Transport and storage
transport_products = board_products + ["roof-rack-surfboard-pads", "surfboard-tie-down-straps", "soft-roof-rack-system",
                                       "surfboard-travel-straps", "surfboard-airline-protection-kit", "surfboard-travel-bag", "surfboard-day-bag"]
cross_doc(
    "surfboard-transport-and-storage-guide", "Transporting and storing your surfboard", "User manual", "product",
    transport_products,
    "Most surfboard damage happens out of the water. This guide explains how to carry, drive with, fly with and store your surfboard safely. It applies to all surfboards and the transport and storage products in the catalog.",
    ["Carry the board with the fins facing your body and the deck against your hip. Use a day bag for short trips.",
     "On a car, place the board fin-side up on padded roof rack bars (or a soft roof rack). Use two straps over each board, tight but not crushing, and twist the straps to reduce hum.",
     "For flights, remove the fins, wrap the rails and tail, and use the airline protection kit in a padded travel bag.",
     "At home, store the board indoors on a wall mount or padded rack, away from sun and heat.",
     "Never leave boards in a closed car and check straps at every stop."],
    "M", category="Travel and Transport")

# Cold-water wetsuit guide (variant-specific, thickness-based)
cold_vids = ["full-length-wetsuit-v03", "hooded-wetsuit-v01"]
cross_doc(
    "cold-water-wetsuit-5-4-3-guide", "Cold-water use guide for 5/4/3 mm wetsuits", "User manual", "variant",
    ["full-length-wetsuit", "hooded-wetsuit"],
    "The 5/4/3 mm wetsuits are built for cold water, usually below 10°C. This guide covers the Elite full-length wetsuit (SRF-WS-001-V03) and the hooded wetsuit (SRF-WS-007-V01).",
    ["Fit matters more than thickness: the suit should be snug at the neck, wrists and ankles, with no large gaps at the back or chest.",
     "Wet the suit and your skin with warm water to ease dressing. Take your time getting arms and shoulders in.",
     "Add boots, gloves and a hood when water is below 10°C. Cover as much skin as possible.",
     "Limit your session length and exit the water if you start to shiver. Have a warm drink and a changing robe ready.",
     "After surfing, rinse, hang to dry inside out and keep the suit away from heat."],
    "M", extra_vids=cold_vids, category="Wetsuits")

# ----------------------------------------------------------------------------
# Validation
# ----------------------------------------------------------------------------
ids = [d["documentId"] for d in docs]
assert len(ids) == len(set(ids)), "duplicate documentId"
variant_ids = {v["ec_variant_id"] for v in variants}
counts = defaultdict(int)
pcounts = defaultdict(int)
for d in docs:
    for pid in d.get("related_product_ids", []):
        assert pid in products, f"unknown product {pid} in {d['documentId']}"
        assert set(product_vids(pid)) <= set(d.get("related_variant_ids", [])), \
            f"{d['documentId']} links {pid} but not all of its variants"
        pcounts[pid] += 1
    if d["doc_scope"] == "material":
        m = d["doc_material"]
        for vid in d.get("related_variant_ids", []):
            v = next(x for x in variants if x["ec_variant_id"] == vid)
            pm = products[v["ec_product_id"]].get("material")
            assert pm in (None, m), f"{d['documentId']} ({m}) linked to {vid} made of {pm}"
            assert pm == m or not v.get("material_compatibility") or m in v["material_compatibility"], \
                f"{d['documentId']} ({m}) linked to {vid}, compatible with {v['material_compatibility']}"
        for pid in d.get("related_product_ids", []):
            assert products[pid].get("material") in (None, m), f"{d['documentId']} ({m}) linked to {pid}"
        missing_m = set(products_made_of(m)) - set(d.get("related_product_ids", []))
        assert not missing_m, f"{d['documentId']} misses products made of {m}: {missing_m}"
    for vid in d.get("related_variant_ids", []):
        assert vid in variant_ids, f"unknown variant {vid} in {d['documentId']}"
        counts[vid] += 1
    assert len(d.get("related_variant_ids", [])) == len(set(d.get("related_variant_ids", [])))
    assert len(d.get("related_product_ids", [])) == len(set(d.get("related_product_ids", [])))
over = {k: c for k, c in counts.items() if c > MAX_DOCS_PER_VARIANT}
over.update({k: c for k, c in pcounts.items() if c > MAX_DOCS_PER_VARIANT})
if over:
    sys.exit(f"Exceeds {MAX_DOCS_PER_VARIANT} documents: {over}")
missing = [p for p in products if pcounts[p] == 0]
if missing:
    sys.exit(f"Products without documents: {missing}")

out = ROOT / "documents.json"
with open(out, "w") as f:
    json.dump(docs, f, indent=2, ensure_ascii=False)
    f.write("\n")

by_type = defaultdict(int)
for d in docs:
    by_type[d["doc_type"]] += 1
print(f"Wrote {len(docs)} documents to {out}")
print(dict(by_type))
print("max docs per variant:", max(counts.values()), "| max docs per product:", max(pcounts.values()))
