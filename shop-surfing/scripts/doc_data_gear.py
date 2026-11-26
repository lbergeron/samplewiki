"""Per-product content: surfboards, fins/hardware, leashes/accessories, wetsuits, wetsuit care.

Each entry: product_id -> dict with optional keys
  S = specification bullets   (-> Specification sheet)
  M = usage steps             (-> User manual)
  I = installation steps      (-> Installation guide)
  C = maintenance steps       (-> Maintenance guide)
Documents are only generated for the keys that are present.
"""

DATA = {}


def D(pid, **kw):
    DATA[pid] = kw


# ---------------------------------------------------------------- Surfboards
D("longboard-surfboard",
  S=["Length range: 9'0\" to 9'6\"; volume 62 to 78 L depending on length", "Outline: rounded nose, wide mid-point, pulled-in tail", "Fin setup: single center fin box or 2+1 (center box plus two side bites)",
     "Rider weight guidance: 65 kg and up for the 9'0\" size", "Leash plug and deck pad zone pre-marked"],
  M=["On PU fiberglass and EPS epoxy models, wax the deck with basecoat, then a temperature-matched top coat. On the soft-top foam model, skip the wax: the foam deck provides grip.", "Carry the board under your arm with the fins facing away from your body.", "Paddle from the middle of the board and take a few strokes before the wave lifts the tail.",
     "Pop up smoothly and step forward gradually to trim along the face."],
  C=["Rinse with fresh water after every session, including the fin box.", "Store out of direct sun and never leave the board in a closed car.", "Check the rails, nose and tail for dings before each session.",
     "On waxed models, strip and re-wax the deck every few weeks, or when the wax turns gritty."])
D("funboard-surfboard",
  S=["Length range: 7'2\" to 8'0\"; volume 45 to 58 L", "Outline: full nose, moderate rocker, round tail", "Fin setup: thruster (three fins) or 2+1",
     "Suited to small to medium waves up to head high"],
  M=["Wax the deck (PU fiberglass and EPS epoxy models only) and fit the fins before heading to the water.", "Paddle near the centre of the board; the extra volume makes early entry easy.", "Pop up with your back foot over the fins and your front foot near the midpoint.",
     "Use the tail to pivot your turns, then trim to keep speed."],
  C=["Rinse with fresh water after each session.", "Keep the board in a padded bag when travelling.", "Inspect the fin boxes and leash plug for cracks.", "Repair dings promptly: exposed foam absorbs water."])
D("fish-surfboard",
  S=["Length range: 5'4\" to 6'2\"; volume 30 to 38 L", "Outline: wide nose, short and flat rocker, swallow tail", "Fin setup: twin, thruster or quad",
     "Best in weak to medium waves up to shoulder high"],
  M=["Wax the deck (PU fiberglass and EPS epoxy models only) and fit your chosen fin setup.", "Paddle from slightly further back than on a shortboard; the wide outline keeps the board stable.", "Drive off the bottom turn using the board's speed instead of forcing it.",
     "Use short, quick turns: a fish rewards flow over power."],
  C=["Rinse with fresh water and dry out of direct sunlight.", "Check the swallow tail edges for pressure dings.", "Store flat or on its rail on a padded rack.", "On waxed models, reapply wax when traction fades."])
D("shortboard-surfboard",
  S=["Length range: 5'8\" to 6'4\"; volume 26 to 34 L", "Outline: pointed nose, narrow tail, progressive rocker", "Fin setup: thruster (default) or quad",
     "Designed for waist-high to overhead waves with good shape"],
  M=["Wax the deck fully and add a traction pad if you want extra rear-foot grip.", "Paddle with a low profile; lying too far forward will bury the nose.", "Time the take-off carefully: shortboards need speed and angle to catch the wave.",
     "Commit to the bottom turn, then project along the line."],
  C=["Rinse with fresh water after each use.", "Inspect the rails and tail after hard turns or contact with the bottom.", "Wipe sand from the fin boxes.", "Keep the board shaded between sessions."])
D("gun-surfboard",
  S=["Length range: 7'0\" to 9'0\"; volume 36 to 48 L", "Outline: narrow with a pulled-in pin tail and extra rocker", "Fin setup: thruster with larger side fins",
     "Intended for steep, powerful waves from overhead and up"],
  M=["Inspect the leash, leash plug and fins before every session.", "Paddle early: a gun needs long strokes to match the wave's speed.", "Take a steep, committed line down the face and rely on the narrow tail for hold.",
     "Surf within your experience; large waves carry real risk."],
  C=["Rinse with fresh water after every session.", "Check the rails and tail for pressure dings after large surf.", "Have any crack assessed by a repairer before the next big day.", "Store the board in a padded bag."])
D("mini-malibu-surfboard",
  S=["Length range: 7'0\" to 8'0\"; volume 42 to 54 L", "Outline: rounded nose and tail with a forgiving rocker", "Fin setup: thruster or 2+1", "Suited to small waves and progressing surfers"],
  M=["Wax the deck and fit the fins.", "Paddle at the centre of the board to keep the nose just above water.", "Pop up in one smooth motion and keep your knees bent.", "Practice small turns first, then add speed."],
  C=["Rinse with fresh water after every session.", "Store out of the sun.", "Inspect the nose for dings.", "Re-wax when traction drops."])
D("soft-top-beginner-surfboard",
  S=["Length range: 7'0\" to 9'0\"; volume 60 to 90 L", "Construction: soft-top foam deck over a foam core with a rigid stringer", "Fin setup: soft or molded fins (included hardware)",
     "Weight capacity up to 100 kg on the 8'0\" size"],
  M=["No wax is needed: the soft deck provides grip.", "Attach the leash to the ankle opposite your front foot.", "Practice your pop-up on the sand before entering the water.", "Stay in white water at first, and always keep the board between you and the shore."],
  C=["Rinse with fresh water and let dry in the shade.", "Do not leave the board in direct sun for long periods: heat can bubble the deck.", "Wipe the deck with a soft cloth and mild soap.", "Store flat or on a padded rack."])
D("midlength-surfboard",
  S=["Length range: 6'6\" to 7'6\"; volume 38 to 50 L", "Outline: full nose, smooth rocker, round pin tail", "Fin setup: thruster or twin plus trailer",
     "Suited to waves from knee high to overhead"],
  M=["Wax the deck (PU fiberglass and EPS epoxy models only) and fit the fins.", "Paddle from the middle of the board: the volume gives early entry.", "Use long, flowing turns to draw out the line.", "Shift weight to the back foot for tighter manoeuvres."],
  C=["Rinse with fresh water after every session.", "Check the fin boxes and rails.", "Keep the board in a day bag between sessions.", "On waxed models, re-wax as soon as traction fades."])
D("foamie-surfboard",
  S=["Length range: 6'0\" to 8'0\"; volume 40 to 70 L", "Construction: foam core with a slick HDPE bottom and soft deck", "Fin setup: soft molded or screw-in fins",
     "Rated for beginners and casual surf up to chest high"],
  M=["No wax is needed on the soft deck.", "Attach the leash and check the cuff fits snugly.", "Paddle with the nose just clear of the water.", "Stand up in the middle of the board with your feet shoulder-width apart."],
  C=["Rinse with fresh water after each session.", "Dry in the shade and avoid heat sources.", "Clean the HDPE bottom with mild soap if it is stained.", "Check the fins are secure before use."])
D("stand-up-paddle-surfboard",
  S=["Length range: 9'6\" to 11'6\"; volume 150 to 230 L", "Construction: sealed foam core with a textured full-length deck pad", "Fin setup: center fin plus two side bites",
     "Paddle not included"],
  M=["Fit the center fin and check the leash plug.", "Wear a leash at all times, attached to your ankle.", "Kneel to get balanced, then stand with feet shoulder-width apart, centred on the handle.", "Paddle with a straight shaft and alternate sides every few strokes."],
  C=["Rinse the deck, handle area and fin box with fresh water.", "Store indoors or under cover.", "Do not leave the board in a closed vehicle.", "Check the deck pad for lifting corners."])

# ---------------------------------------------------------------- Fins and hardware
D("thruster-fin-set",
  S=["Set of three fins (two sides plus one center)", "Template: medium base with a moderate rake", "Fits dual-tab compatible fin boxes", "Size options matched to rider weight"],
  I=["Seat each fin base in its box with the front tab first.", "Insert the fin screw and turn clockwise until snug; do not overtighten.", "Check that all three fins sit flush with no gap at the base.", "Repeat the check after the first session."],
  M=["Fit the side fins slightly toed-in, and the center fin on the centreline.", "Start with the recommended size for your weight.", "Move to a larger size for more drive, smaller for a looser feel.", "Remove the fins before long storage or air travel."])
D("quad-fin-set",
  S=["Set of four fins (two front, two rear)", "Template: low-rake front fins with smaller rear fins", "Fits dual-tab compatible fin boxes", "Designed for speed and hold in small to medium waves"],
  I=["Place each fin in its box with the front tab first.", "Fit the screws and tighten until the fin is held firmly.", "Check that the front fins and rear fins match their positions.", "Re-check the screws after the first session."],
  M=["Use a quad setup in small to mid-size surf for extra speed.", "Move the rear fins forward in the box for a looser feel.", "Move them back for more hold.", "Rinse the fins after each surf."])
D("twin-fin-set",
  S=["Set of two fins", "Template: upright with a raked profile", "Fits dual-tab compatible fin boxes", "Designed for flow and release in small surf"],
  I=["Seat the front tab of each fin and press the rear tab down.", "Tighten the screws evenly.", "Confirm the fins have equal toe-in.", "Re-check the hardware after the first session."],
  M=["Twin fins reward a smooth, flowing style.", "Keep turns rounded rather than abrupt.", "Remove sand from the fin box before fitting.", "Use a fin key rather than your fingers to tighten screws."])
D("single-longboard-fin",
  S=["Single center fin", "Length options: 8\" to 10\"", "Fits single-fin (US box) systems", "Designed for stable trim and classic noserides"],
  I=["Slide the fin into the center box until the base is flush.", "Fit the plate and screw, and tighten with a fin key.", "Check there is no side play in the fin.", "Rinse the box after use to prevent seizing."],
  M=["Choose a longer fin for stability and a shorter fin for turning.", "Move the fin back in the box for more hold and forward for freer turns.", "Rinse after each session.", "Check the screw is tight before each paddle-out."])
D("fcs-compatible-fin-box",
  S=["Replacement fin box compatible with FinFoundry-style fin systems", "Sold individually", "Suitable for professional installation by a repairer", "Requires installation tools and resin"],
  I=["Mark the box position and cut a precise pocket with the correct router bit.", "Dry-fit the box to check alignment with the other fin boxes.", "Bond the box with resin that is compatible with your board's construction.", "Allow the resin to fully cure before fitting fins or surfing."])
D("futures-compatible-fin-box",
  S=["Replacement fin box compatible with HorizonTide-style fin systems", "Sold individually", "Suitable for professional installation by a repairer", "Requires installation tools and resin"],
  I=["Mark the box position and cut a precise pocket for a HorizonTide-style box.", "Dry-fit the box using a spare fin to confirm alignment.", "Bond the box using resin that is compatible with your board's construction.", "Allow full cure time before use."])
D("surfboard-fin-screws-and-plates",
  S=["Replacement screws and plates for compatible fins", "Material: stainless steel screws, composite plates", "Includes assorted lengths", "Fin key not included"],
  I=["Remove the old screw and plate from the fin box.", "Insert the new plate and thread the screw by hand.", "Tighten with a fin key until snug.", "Keep spares in your board bag."])
D("surfboard-leash-plug",
  S=["Replacement anchor plug for leash attachment", "Material: reinforced composite", "Includes a stainless steel leash bar", "Suitable for professional installation"],
  I=["Remove the damaged plug and any loose material.", "Cut a clean pocket in the tail of the board, avoiding the stringer.", "Bond the plug with compatible resin, ensuring it sits flush with the deck.", "Cure fully before attaching a leash."])
D("surfboard-traction-pad",
  S=["Multi-piece textured deck pad", "Peel-and-stick adhesive backing", "Arch and kick tail design", "Surface prep: clean and dry the deck first"],
  I=["Remove all wax from the area and wipe with surfboard cleaner.", "Position the pad dry to confirm placement.", "Peel the backing, press the pad in place and smooth it from the centre outward.", "Allow the adhesive to cure for 24 hours before use."])
D("longboard-nose-rider-pad",
  S=["Extended front deck pad", "Peel-and-stick adhesive backing", "Fits the nose area of most longboards", "Textured surface for added grip"],
  I=["Remove wax and clean the area with surfboard cleaner.", "Place the pad dry to confirm alignment with the nose.", "Peel the backing and press down firmly from the centre outward.", "Leave for 24 hours before surfing."])

# ---------------------------------------------------------------- Leashes and accessories
D("shortboard-surf-leash",
  S=["Length: 6'", "Cord thickness: 7 mm", "Rail saver included", "Rated for waves up to head high"],
  M=["Attach the leash to the board's leash plug with the rail saver in place.", "Fasten the cuff around the ankle opposite your front foot.", "Check the Velcro closes securely.", "Check the swivels move freely before each session."],
  C=["Rinse the leash with fresh water after each session.", "Inspect the cord for cuts and the swivels for corrosion.", "Replace the leash if the urethane shows cracks.", "Store out of direct sunlight."])
D("longboard-surf-leash",
  S=["Length: 9'", "Cord thickness: 7 mm", "Padded cuff for comfort", "Rated for waves up to head high"],
  M=["Attach the leash to the leash plug and use a rail saver.", "Secure the padded cuff on your back ankle.", "Check the Velcro closure.", "Check the cord for cuts before use."],
  C=["Rinse the leash with fresh water after each use.", "Check the cuff for wear.", "Replace the leash if the cord is damaged.", "Store coiled loosely."])
D("big-wave-surf-leash",
  S=["Length: 8'", "Cord thickness: 10 mm", "Double-swivel construction", "Rated for overhead waves"],
  M=["Attach the leash to the plug using a rail saver.", "Fit the cuff snugly above the ankle.", "Check the swivels, cord and cuff before each session.", "Use the leash as part of a safety plan for big surf."],
  C=["Rinse with fresh water.", "Inspect cord and swivels after each large session.", "Replace the leash at any sign of wear.", "Store away from sunlight."])
D("coiled-surf-leash",
  S=["Length: 6' extended", "Coiled cord that reduces drag", "Rail saver included", "Rated for small waves and flat water"],
  M=["Attach the leash to the leash plug with the rail saver.", "Secure the cuff and check the coils are free of tangles.", "Keep the coil clear of your feet when standing up.", "Check the cuff closure before each session."],
  C=["Rinse with fresh water after use.", "Check the coil for stretching.", "Replace if the cord frays.", "Hang to dry out of direct sunlight."])
D("leash-rail-saver",
  S=["Strap wraps around the rail", "Material: abrasion-resistant webbing", "Fits boards up to 3 inches thick", "Sold individually"],
  I=["Thread the strap through the leash plug.", "Wrap the strap around the rail and feed the leash through the loop.", "Pull the strap tight.", "Check the strap sits against the rail without twisting."],
  M=["Use a rail saver on every session.", "Replace it when the webbing frays.", "Check it after each surf.", "Rinse it with fresh water."])
D("surfboard-deck-grip-tape",
  S=["Self-adhesive grip sheet", "Cuttable to any shape", "Abrasive textured surface", "Surface prep: clean and dry the deck"],
  I=["Clean the deck area and remove all wax.", "Cut the grip tape to your chosen shape.", "Peel the backing and smooth the tape from the centre outward.", "Leave for 24 hours before surfing."])
D("surfboard-tail-block",
  S=["Replacement tail block for traction pad installation", "Compatible with most arch-style tail pads", "Includes adhesive", "Sold individually"],
  I=["Remove the damaged tail block with a plastic scraper.", "Clean the area with surfboard cleaner.", "Apply adhesive to the new tail block and press in place.", "Let cure for 24 hours before surfing."])
D("surfboard-ding-repair-kit",
  S=["Portable repair kit for small dings", "Includes epoxy resin, hardener, cloth and sandpaper; epoxy is safe on both PU fiberglass and EPS epoxy boards", "Suited to small surface dings", "Cure time approx. 30 minutes in warm weather"],
  M=["Dry the ding fully and sand away loose material.", "Mix the resin and hardener as directed.", "Apply the mixture over the ding, then add cloth if needed.", "Let it cure, then sand smooth."])
D("surfboard-travel-bag",
  S=["Padded bag for travel", "Sizes: 6'6\" to 9'6\"", "Compartments for fins and accessories", "Heavy-duty zippers and reinforced carry handles"],
  M=["Wrap the board in a towel before inserting it.", "Place the fins in the interior pocket.", "Zip the bag fully and check the handles.", "Add extra padding at the nose and tail."],
  C=["Empty the bag after each trip.", "Wipe clean with a damp cloth.", "Dry fully before storing.", "Check the zippers and stitching."])
D("surfboard-day-bag",
  S=["Lightweight padded day bag", "Sizes: 5'8\" to 9'6\"", "Reflective lining", "Shoulder strap included"],
  M=["Zip the board into the bag with the fins up.", "Use the shoulder strap for carrying.", "Keep the bag out of direct sunlight.", "Remove the board for storage."])

# ---------------------------------------------------------------- Wetsuits
D("full-length-wetsuit",
  S=["Style: full-length suit with a back zip", "Neoprene thickness options: 2/2 mm, 4/3 mm, 5/4/3 mm", "Flat-lock or glued-and-blind-stitched seams depending on tier", "Sizes: XS to XXL"],
  M=["Wet the suit and your limbs to make donning easier.", "Pull the legs up first, then the arms and shoulders.", "Zip the back zip fully with the cord.", "Rinse thoroughly after each use."],
  C=["Rinse the inside and outside with fresh water.", "Hang on a wide hanger in the shade.", "Do not wring, tumble or dry-clean the suit.", "Wash periodically with a neoprene-safe shampoo."])
D("spring-suit",
  S=["Style: short-leg, short-sleeve suit", "Neoprene thickness options: 1.5/1 mm, 2/2 mm", "Seam type: flat-lock stitched", "Sizes: XS to XXL"],
  M=["Wet the suit and your skin before pulling it on.", "Pull up the legs, then the arms.", "Close the zip and tuck in the cord.", "Rinse with fresh water after surfing."],
  C=["Rinse with fresh water after use.", "Dry inside out first, then right-side out.", "Use a wide hanger.", "Avoid direct sunlight."])
D("wetsuit-jacket",
  S=["Style: long-sleeve neoprene jacket", "Neoprene thickness options: 1.5 mm, 2/2 mm", "Front-zip or pullover construction", "Sizes: XS to XXL"],
  M=["Wet the jacket before putting it on.", "Pull it over your head and straighten the sleeves.", "Close any front zip fully.", "Rinse after each use."])
D("wetsuit-vest",
  S=["Style: sleeveless neoprene vest", "Neoprene thickness: 2 mm", "Flat-lock seams", "Sizes: XS to XXL"],
  M=["Wet the vest and pull it on over your head.", "Pull the vest down to sit flat against your torso.", "Layer under or over a rash guard.", "Rinse with fresh water."])
D("wetsuit-top",
  S=["Style: long-sleeve neoprene top", "Neoprene thickness options: 1 mm, 2 mm", "Flat-lock seams", "Sizes: XS to XXL"],
  M=["Wet the top before putting it on.", "Pull it over your head and arrange the sleeves.", "Layer over a rash guard on cold days.", "Rinse after surfing."])
D("wetsuit-pants",
  S=["Style: long neoprene pants", "Neoprene thickness options: 1.5 mm, 2 mm", "Elastic waist with drawcord", "Sizes: XS to XXL"],
  M=["Wet the pants before putting them on.", "Pull the legs up and adjust the waist drawcord.", "Wear with a wetsuit top or jacket.", "Rinse after use."])
D("hooded-wetsuit",
  S=["Style: full-length suit with an attached hood", "Neoprene thickness: 5/4/3 mm", "Glued and blind-stitched seams with taped interiors", "Sizes: S to XXL"],
  M=["Wet the suit and your limbs before dressing.", "Pull up the legs first, then arms, then close the back zip.", "Draw the hood over your head and seal the neck.", "Rinse thoroughly after use."],
  C=["Rinse inside and out with fresh water.", "Hang on a wide hanger in the shade.", "Let the hood dry fully.", "Use neoprene-safe shampoo periodically."])
D("wetsuit-boots",
  S=["Neoprene surf boots, 3 mm to 5 mm", "Round or split toe options", "Rubber sole with grip pattern", "Sizes: EU 36 to 46"],
  M=["Wet your foot and pull the boot on.", "Close the zip or velcro tab.", "Walk carefully on rocks; boots reduce but do not remove all risk.", "Rinse and dry after use."])
D("wetsuit-gloves",
  S=["Neoprene gloves, 3 mm", "Pre-curved fingers", "Glued and blind-stitched seams", "Sizes: S to XL"],
  M=["Wet your hands and pull the gloves on.", "Adjust the wrist closure for a snug fit.", "Pull the glove cuff under your wetsuit sleeve.", "Rinse and dry after use."])
D("wetsuit-hood",
  S=["Neoprene hood, 3 mm", "Seam type: glued and blind-stitched", "Ear drains and a chin strap", "Sizes: S to XL"],
  M=["Pull the hood over your head.", "Adjust it so it covers your ears.", "Fasten the chin strap.", "Rinse and dry after use."])

# ---------------------------------------------------------------- Wetsuit care & changing gear
D("wetsuit-changing-mat",
  M=["Unroll the mat on flat ground.", "Stand on it while changing so your wetsuit and feet stay clean.", "Fold the mat to contain sand and water.", "Rinse and dry it after use."])
D("wetsuit-changing-robe",
  M=["Pull the robe over your head or zip it up.", "Change under it for privacy and warmth.", "Hang it to dry after use.", "Machine-wash on a gentle cycle when needed."])
D("wetsuit-hanger",
  S=["Wide-shoulder hanger", "Material: durable plastic with a non-slip surface", "Supports a full-length wetsuit", "Maximum load: 4 kg"],
  M=["Hang the wetsuit by the waist or folded over the bar.", "Use the wide shoulder to avoid stress on the neoprene.", "Keep the suit out of direct sunlight.", "Turn the suit inside out to dry the interior."])
D("wetsuit-shampoo",
  M=["Fill a tub with cool fresh water.", "Add the recommended amount of shampoo.", "Soak the wetsuit for 10 to 15 minutes.", "Rinse thoroughly and hang to dry in the shade."])
D("wetsuit-repair-glue",
  M=["Clean and dry the damaged area.", "Apply a thin layer to both edges of the tear.", "Press the edges together and hold for one minute.", "Let cure for 24 hours before use."])
D("wetsuit-storage-bag",
  M=["Let the wetsuit dry before storing it in the bag.", "Fold or roll the suit loosely.", "Close the ventilated bag and store it in a cool place.", "Wash the bag when needed."])
D("wetsuit-drying-rack",
  I=["Unfold the rack on a flat surface.", "Lock the support arms into place.", "Hang the wetsuit over the rack, using the width to spread the weight.", "Place the rack in a ventilated area away from direct sun."],
  M=["Rinse the wetsuit first.", "Place the wetsuit on the rack inside out.", "Let it dry, then flip it right-side out.", "Fold the rack flat for storage."])
D("wetsuit-zipper-and-seal-lubricant",
  M=["Clean the zipper of salt and sand.", "Apply a small amount of lubricant to the teeth.", "Work the zipper up and down to distribute it.", "Wipe off any excess."])
D("wetsuit-rinse-bottle",
  M=["Fill the bottle with fresh water.", "Squeeze or pump to rinse salt and sand from gear.", "Rinse the zippers and seams carefully.", "Empty and dry the bottle after use."])
D("waterproof-changing-poncho",
  M=["Pull the poncho over your head.", "Change under it for privacy.", "Hang it to dry after use.", "Wipe or rinse the exterior."])
