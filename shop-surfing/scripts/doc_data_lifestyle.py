"""Per-product content: clothing, safety, wax and maintenance, travel, training. See doc_data_gear.py for the format."""

DATA = {}


def D(pid, **kw):
    DATA[pid] = kw


# ---------------------------------------------------------------- Clothing and sun protection
D("board-shorts",
  S=["Fabric: quick-dry stretch polyester blend", "Fit: relaxed, 18 inch outseam", "Closure: velcro fly with drawcord", "Zippered back pocket"],
  C=["Rinse with fresh water after use.", "Machine-wash cold on a gentle cycle.", "Hang to dry out of direct sun.", "Avoid fabric softener."])
D("surf-bikini",
  C=["Rinse with fresh water after each session.", "Hand-wash in cool water with mild soap.", "Lay flat to dry in the shade.", "Avoid wringing and tumble-drying."])
D("surf-swimsuit",
  C=["Rinse with fresh water after surfing.", "Hand-wash with mild soap.", "Lay flat to dry away from direct sun.", "Do not iron."])
D("long-sleeve-rash-guard",
  S=["Fabric: stretch nylon blend", "UV protection: UPF 50+", "Fit: close, with flat-lock seams", "Sizes: XS to XXL"],
  C=["Rinse with fresh water after each session.", "Machine-wash cold, inside out.", "Hang to dry; do not tumble dry.", "Keep away from sunscreen build-up by washing regularly."])
D("short-sleeve-rash-guard",
  S=["Fabric: stretch polyester blend", "UV protection: UPF 50+", "Fit: athletic with flat-lock seams", "Sizes: XS to XXL"],
  C=["Rinse with fresh water after use.", "Machine-wash cold.", "Hang to dry.", "Avoid bleach."])
D("uv-protection-surf-leggings",
  S=["Fabric: stretch nylon blend", "UV protection: UPF 50+", "Fit: close fit with a drawcord waist", "Sizes: XS to XXL"],
  C=["Rinse after each use.", "Machine-wash cold.", "Hang to dry.", "Avoid fabric softener."])
D("surf-poncho",
  M=["Pull the poncho over your head.", "Change under it for privacy and warmth.", "Hang it to dry after use.", "Machine-wash when needed."])
D("surf-hoodie",
  C=["Machine-wash cold with similar colours.", "Tumble dry low or hang to dry.", "Avoid bleach.", "Rinse salt water before washing."])
D("surf-cap",
  C=["Spot-clean with mild soap.", "Rinse salt water with fresh water.", "Air dry away from direct heat.", "Do not machine-wash."])
D("surf-sunglasses-with-retainer",
  M=["Attach the retainer strap to the frame.", "Place the glasses on before you head into the water.", "Rinse with fresh water after use.", "Wipe with a microfibre cloth."],
  C=["Rinse with fresh water after each use.", "Wipe lenses with a microfibre cloth.", "Check the retainer for wear.", "Store in a case."])

# ---------------------------------------------------------------- Safety and water accessories
D("surf-helmet",
  S=["Shell: impact-resistant ABS with a foam liner", "Chin strap and adjustment dial", "Ventilation and ear drains", "Sizes: S to L"],
  M=["Adjust the dial for a snug fit.", "Fasten the chin strap under your chin.", "Check the helmet does not shift when you shake your head.", "Replace the helmet after any significant impact."],
  C=["Rinse with fresh water after each use.", "Dry out of direct sun.", "Inspect the shell and liner for cracks.", "Replace after a hard impact."])
D("impact-vest",
  S=["Foam-panel construction", "Buoyancy: 50 N", "Adjustable side straps", "Sizes: S to XL"],
  M=["Fit the vest snugly with the straps adjusted.", "Check that it does not restrict movement.", "Wear it under or over a wetsuit.", "Inspect it for tears before each use."])
D("personal-flotation-vest",
  S=["Certified buoyancy: 50 N", "Foam-panel construction", "Adjustable side and chest straps", "Sizes: S to XL"],
  M=["Fit the vest so that it is snug but allows comfortable breathing.", "Fasten all straps and buckles.", "Pull the shoulder straps upward to test the fit.", "Replace the vest if foam or stitching is damaged."],
  C=["Rinse with fresh water after each use.", "Hang to dry out of direct sun.", "Inspect straps and buckles regularly.", "Do not store under heavy items."])
D("waterproof-phone-pouch",
  M=["Check the seal and zipper are clean.", "Insert your phone and close the seal.", "Test the pouch with a dry tissue before use.", "Rinse and dry after each use."],
  C=["Rinse with fresh water after use.", "Dry the seal fully.", "Check for scratches and tears.", "Store open to prevent odour."])
D("waterproof-waist-pack",
  M=["Open the pack and place your items inside.", "Roll the top or close the seal securely.", "Fasten the belt around your waist.", "Rinse after use."])
D("surf-whistle",
  M=["Attach the whistle to your wetsuit or board bag.", "Blow three long blasts to signal for help.", "Check the whistle works before surfing.", "Rinse after use."])
D("marine-first-aid-kit",
  S=["Water-resistant case with a clip", "Contents: dressings, antiseptic wipes, tape, tweezers and gloves", "Suitable for common beach and surf injuries", "Not a substitute for medical care"],
  M=["Check the kit's contents before each trip.", "Replace any items that have been used or expired.", "Keep the kit dry and accessible.", "Seek medical help for serious injuries."])
D("reef-boots",
  S=["Neoprene upper, 3 mm", "Rubber sole with grip pattern", "Reinforced toe and heel", "Sizes: EU 36 to 46"],
  C=["Rinse with fresh water after each use.", "Dry in the shade.", "Check the sole for wear.", "Replace if the sole is damaged."])
D("earplugs-for-surfers",
  M=["Roll or push the plug gently into the ear canal.", "Make sure it is seated, but do not force it.", "Remove gently after surfing.", "Wash with warm water after each use."],
  C=["Wash with mild soap and warm water.", "Dry fully.", "Store in the case.", "Replace when worn or damaged."])
D("waterproof-action-camera-housing",
  S=["Depth rating: 40 m", "Compatible with most action cameras", "Includes a mount adapter", "Anti-fog inserts included"],
  I=["Clean and inspect the O-ring and seal.", "Place the camera inside and close the latches.", "Attach the mount adapter to the board or helmet.", "Test the housing in shallow water first."],
  M=["Insert an anti-fog insert before closing the housing.", "Check the seal for sand or hair.", "Test the controls before entering the water.", "Rinse with fresh water after each use."])

# ---------------------------------------------------------------- Wax and maintenance
D("tropical-surf-wax",
  S=["Water temperature range: above 22°C", "Hard formulation", "Scent: coconut", "Weight: 85 g"],
  M=["Apply over a basecoat on a clean deck.", "Rub the wax in circular motions.", "Build up small bumps for grip.", "Store out of sun."])
D("cold-water-surf-wax",
  S=["Water temperature range: below 14°C", "Soft formulation", "Weight: 85 g", "Fragrance-free"],
  M=["Apply over a basecoat on a clean deck.", "Rub in cross-hatched lines.", "Use a comb to refresh the texture.", "Store out of sun."])
D("basecoat-surf-wax",
  S=["Firm foundation wax", "Suitable for PU fiberglass and EPS epoxy boards", "Weight: 85 g", "Use under top coat wax"],
  M=["Clean the deck of old wax.", "Apply in diagonal lines across the deck.", "Rub the wax in until a bumpy base forms.", "Add top coat wax matched to water temperature."])
D("wax-comb",
  M=["Use the teeth side to texture wax.", "Use the scraper edge to lift old wax.", "Wipe the board with a cloth after use.", "Rinse the comb with fresh water."])
D("wax-removal-tool",
  M=["Soften old wax in the sun or with warm water.", "Use the tool at a shallow angle to lift the wax.", "Do not scrape bare fiberglass.", "Wipe with surfboard cleaner."])
D("surfboard-cleaner",
  M=["Apply a small amount to a clean cloth.", "Wipe the surface of the board.", "Remove the residue with a second cloth.", "Rinse with fresh water."])
D("fiberglass-repair-cloth",
  M=["Cut the cloth slightly larger than the damaged area.", "Mix and apply compatible resin.", "Lay the cloth over the repair and saturate it.", "Let cure, then sand smooth."])
D("epoxy-resin-repair-kit",
  M=["Sand away the damaged material.", "Mix the epoxy components as directed.", "Apply to the damaged area and smooth it.", "Let it cure fully before sanding."])
D("solarez-style-uv-repair-resin",
  M=["Dry and sand the damaged area.", "Apply resin to fill the ding.", "Cure under sunlight or UV for the stated time.", "Sand smooth when hard."])
D("surfboard-repair-sanding-kit",
  M=["Start with coarse sandpaper to shape the repair.", "Move to finer grit to smooth.", "Wipe away dust with a damp cloth.", "Finish with polishing compound if desired."])

# ---------------------------------------------------------------- Travel and transport
D("roof-rack-surfboard-pads",
  I=["Wrap each pad around the roof rack bar.", "Close the velcro strap.", "Check the pad sits flat and does not slide.", "Place boards on the pads."],
  M=["Place boards fin-side up on the pads.", "Strap the boards down over the pads.", "Check pad positions periodically.", "Remove pads when not in use."])
D("surfboard-tie-down-straps",
  M=["Loop the strap around the rack bar.", "Pass the strap over the boards and through the buckle.", "Tighten until snug but not crushing.", "Twist the strap to reduce hum at speed."])
D("soft-roof-rack-system",
  I=["Place the rack pads on the roof.", "Run the straps through the vehicle doors.", "Tighten the straps until the rack is secure.", "Check that the doors close and that the rack does not move."],
  M=["Load the boards onto the pads.", "Secure them with tie-down straps.", "Check the rack at every stop.", "Remove the rack when not in use."])
D("surfboard-travel-straps",
  M=["Place the equipment on a flat surface.", "Wrap the strap around the bundle.", "Cinch the buckle until snug.", "Check the load before moving."])
D("board-bag-shoulder-strap",
  I=["Clip the strap onto the D-rings on the bag.", "Adjust the length.", "Check the clips are locked.", "Test with the board inside."])
D("surfboard-airline-protection-kit",
  M=["Wrap the rails in foam protection.", "Cover the nose and tail with guards.", "Place the board in a padded bag.", "Add extra padding around the fin boxes."])
D("waterproof-dry-bag",
  M=["Place items in the bag.", "Roll the top at least three times.", "Clip the buckle closed.", "Check for trapped air before sealing."],
  C=["Rinse with fresh water after use.", "Dry thoroughly.", "Store open to prevent odour.", "Inspect the seams for cracks."])
D("sand-free-beach-blanket",
  M=["Spread the blanket on the sand.", "Anchor the corners.", "Shake out sand at the end of the day.", "Fold and store."],
  C=["Shake out the sand after each use.", "Machine-wash cold when needed.", "Air dry.", "Store folded."])
D("beach-cart-for-surf-gear",
  S=["Wheeled cart with balloon tires", "Load capacity: 50 kg", "Folds flat for transport", "Fits boards up to 9'6\""],
  M=["Unfold the cart and lock the frame.", "Load boards on the rack and secure them.", "Pull the cart with the handle over sand.", "Fold the cart flat for storage."])
D("surfboard-rack-wall-mount",
  S=["Wall-mounted rack for up to 3 boards", "Padded arms", "Load capacity: 20 kg", "Mounting hardware included"],
  I=["Locate wall studs and mark the positions.", "Drill pilot holes and fix the rack with the supplied screws.", "Check the rack is level.", "Place boards on the padded arms."])

# ---------------------------------------------------------------- Training and lifestyle
D("balance-board",
  S=["Deck: wooden, 80 cm", "Roller: 15 cm diameter", "Non-slip surface", "Max user weight: 120 kg"],
  M=["Place the board on a flat, non-slip surface.", "Stand with feet shoulder-width apart.", "Keep your knees bent and core engaged.", "Practice for short sessions."])
D("surf-training-resistance-bands",
  S=["Set of three resistance levels", "Door anchor included", "Material: natural latex", "Carry pouch included"],
  M=["Select a band that matches your strength.", "Anchor the band securely.", "Perform controlled repetitions.", "Rest between sets."])
D("pop-up-training-mat",
  M=["Unroll the mat and place it on a flat surface.", "Lie on the mat and practice a smooth pop-up.", "Use the foot markings as a guide.", "Repeat for sets of 10."])
D("surf-fitness-handbook",
  S=["Paperback, approx. 120 pages", "Covers mobility, strength and conditioning", "Includes weekly training plans", "Illustrated exercises"])
D("wave-forecasting-watch",
  S=["Water resistance: 100 m", "Displays tide and swell forecasts via a paired app", "Session tracking", "Battery life: up to 14 days"],
  M=["Charge the watch fully before first use.", "Pair it with the companion app.", "Select your local surf spot.", "Start session tracking before paddling out."])
D("waterproof-sports-watch",
  S=["Water resistance: 50 m", "Activity timer and stopwatch", "Battery life: up to 30 days", "Adjustable strap"],
  M=["Set the time and date.", "Start the timer before your session.", "Rinse the watch with fresh water afterwards.", "Replace the battery when needed."])
D("surf-photography-water-housing",
  I=["Inspect the O-ring and seal.", "Place the camera inside the housing.", "Close and lock the latches.", "Test the housing in shallow water."],
  M=["Secure the housing with a wrist strap.", "Check the port for water droplets.", "Frame your shot and start shooting.", "Rinse the housing with fresh water afterwards."])
D("surf-spot-guidebook",
  S=["Paperback, approx. 200 pages", "Covers surf spots, seasons and hazards", "Includes maps", "Updated annually"])
D("reusable-insulated-water-bottle",
  M=["Fill the bottle with water.", "Close the lid securely.", "Carry in a bag or on a belt.", "Wash after use."],
  C=["Wash with warm soapy water after use.", "Dry thoroughly.", "Store with the lid off.", "Check the seal for wear."])
D("surfboard-cleaning-brush",
  M=["Brush sand from the board.", "Use gentle strokes.", "Rinse the brush.", "Hang to dry."])
