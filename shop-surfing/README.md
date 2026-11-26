# Surf shop catalog

`catalog.json` holds the surf shop's product catalog (118 products and 84 variants). It is indexed in a Coveo Catalog source in the `dev` environment. `catalog-overview.md` is a readable view of the same catalog.

| Setting      | Value                                                |
| ------------ | ---------------------------------------------------- |
| Environment  | `dev` (region `us`)                                  |
| Organization | `lbergeronsfdevt1z2624x`                             |
| Source ID    | `lbergeronsfdevt1z2624x-xxwzkybk6sclc5qkobvjseslnu`  |

## Push the catalog

You need the [Coveo CLI](https://docs.coveo.com/en/cli/) (tested with 3.3.1).

1. Log in to the `dev` organization:

   ```bash
   coveo auth:login -e dev -r us -o lbergeronsfdevt1z2624x
   ```

2. From the repository root, push the file:

   ```bash
   coveo source:catalog:add lbergeronsfdevt1z2624x-xxwzkybk6sclc5qkobvjseslnu \
     --files shop-surfing/catalog.json
   ```

   This adds new items and updates existing ones. Items that you removed from the file stay in the source.

3. To replace the whole catalog, add `--fullUpload`. This deletes every item in the source that isn't in the file.

Indexing runs in the background. Items can take a few minutes to appear in the source's Content Browser.

## File format

The CLI only accepts this format:

- A plain JSON array of documents. Don't wrap it in `{ "addOrUpdate": [...] }`, which is the Push API's batch format.
- Each document needs a `documentId` and a `title`. In this file, `title` repeats `ec_name`.
- `objecttype` is `Product` or `Variant`. Variants link to their product through `ec_product_id`.

## Catalog model

- A product is made of a single material, stored in the product's `material` field along with its `quality` tier. A model sold in several materials is one product per material: for example, `longboard-surfboard-pu-fiberglass`, `longboard-surfboard-eps-epoxy` and `longboard-surfboard-soft-top-foam`. These products share `ec_item_group_id` (`longboard-surfboard`). Their SKUs append a material code (`SRF-SB-001-PU`).
- Variants hold the attributes a shopper picks for a given product: `color` (colour scheme) for boards, fins and fin boxes, and `thickness` and `quality` for wetsuits. Wax and maintenance variants keep `material_compatibility`, which describes the boards they work on, not what they are made of.

After editing `catalog.json`, regenerate the overview and the documents:

```bash
python3 shop-surfing/scripts/render_overview.py
python3 shop-surfing/scripts/generate_documents.py
```

The flag is `--files` (plural). With `--file`, the CLI fails with `Unexpected arguments`.

## Product documents (push source)

`documents.json` holds 208 short documents (user manuals, specification sheets, installation guides and maintenance guides) that link to the products and variants in `catalog.json`. They are meant for a regular **Push** source, separate from the Catalog source.

| Setting | Value |
| ------- | ----- |
| Source ID | `lbergeronsfdevt1z2624x-vd5gscm5k7miel2xxs2pcrkkua` |

1. Log in to the `dev` organization (see above).

2. From the repository root, push the documents. `--createMissingFields` creates the custom fields (`doc_type`, `related_product_ids`, ...) in the organization:

   ```bash
   coveo source:push:add lbergeronsfdevt1z2624x-vd5gscm5k7miel2xxs2pcrkkua \
     --files shop-surfing/documents.json \
     --createMissingFields
   ```

   Make `related_product_ids`, `related_variant_ids` and `related_skus` **multi-value facet** fields (Administration > Fields) so each id is matched individually.

### Document fields

| Field | Description |
| ----- | ----------- |
| `documentId` | `doc://shop-surfing/<slug>` |
| `title`, `data` | Document title and body text |
| `doc_type` | `User manual`, `Specification sheet`, `Installation guide` or `Maintenance guide` |
| `doc_scope` | `product` (every product of an item group, such as all longboards, and their variants), `material` (all products made of `doc_material`, plus compatible repair and care products) or `variant` (specific variants) |
| `doc_material` | Material the document applies to (material documents only) |
| `doc_category` | Catalog category, or `Multiple` |
| `related_product_ids` | `ec_product_id` values the document applies to. A product is listed only when the document applies to **all** its variants. For example, the EPS epoxy repair guide lists only the EPS formula variant of the UV repair resin, not the resin product, because the product also has a PU formula |
| `related_variant_ids` | `ec_variant_id` values the document applies to. This is always the complete resolved list, including the variants of every linked product. Omitted when no linked product has variants |
| `related_skus` | Product and variant SKUs, for convenience |

A variant is linked to at most 10 documents (currently at most 6). To look up the documents of a variant, filter on `@related_variant_ids==<ec_variant_id>`.

### Regenerate

`documents.json` is generated. Product document content is keyed by `ec_item_group_id` in `scripts/doc_data_*.py`; material guides are in `scripts/generate_documents.py`. After editing, run:

```bash
python3 shop-surfing/scripts/generate_documents.py
```

The script fails if a variant would exceed 10 documents, if a product is linked without all its variants, if a material guide is linked to a product of another material or misses a product made of its material, if a link points to an unknown product or variant, or if a product has no document.
