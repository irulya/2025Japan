import os

# Create day4 folder if it doesn't exist
os.makedirs('day4', exist_ok=True)

# HTML template
template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day 4 - {title}</title>
    <style>
        li strong.top-level {{ font-size: 1.2em; }}
    </style>
</head>
<body>
    <h1>{header}</h1>
    {content}
    <p><a href="../japan_main.html">Back to Main Itinerary</a></p>
</body>
</html>'''

# Main day4.html content
main_content = '''<ul>
    <li><strong class="top-level">Route Overview:</strong> From Ōkubo to Ryuguden via Tokyo Station and Odawara [<a href="route_overview.html">Details</a>]</li>
    <li><strong class="top-level">Is It Worth It?:</strong> Morning exploration options near Ryuguden before the 1:00 PM shuttle [<a href="worth_it.html">Details</a>]</li>
    <li><strong class="top-level">Hakone Ropeway:</strong> Feasibility and details for a morning visit [<a href="hakone_ropeway.html">Details</a>]</li>
</ul>'''

with open('day4/day4.html', 'w', encoding='utf-8') as f:
    f.write(template.format(
        title="Day 4 Overview",
        header="Day 4 (04/03/25): Travel to Ryuguden, Hakone",
        content=main_content
    ))

# Route Overview content
route_content = '''<p>
Starting Point: 1-chōme-16-15 Ōkubo, near Shin-Ōkubo Station.<br>
Destination: Ryuguden, 139 Motohakone, Hakone (via Odawara Station).<br>
Route: Taxi/subway to Tokyo Station → Shinkansen to Odawara → Free shuttle to Ryuguden.<br>
Total Time: ~2.5-3.5 hours, depending on connections.<br>
Total Cost: ~¥22,500-¥24,000 for six (details below).
</p>
<h2>Step-by-Step Route</h2>
<h3>Step 1: From Ōkubo to Tokyo Station</h3>
<p>
Distance: ~5.5 km from Ōkubo to Tokyo Station (Shin-Ōkubo is closer to Shinjuku, but Shinkansen departs from Tokyo Station).<br>
Options:<br>
<strong>Taxi:</strong><br>
Hail a taxi or book via app (e.g., JapanTaxi) to Tokyo Station’s Yaesu Exit (Shinkansen gates).<br>
Time: 15-25 minutes, depending on traffic (Sakura season may add delays).<br>
Cost: ¥2,000-¥3,000 total (base fare ¥730 + ~¥410/km for 5.5 km + traffic).<br>
Notes: Best for six people with luggage—direct and hassle-free.<br>
<strong>Yamanote Line + Walk:</strong><br>
Walk 300m to Shin-Ōkubo Station (5 minutes).<br>
Take Yamanote Line (inner loop) to Tokyo Station (~15 minutes, 7 stops).<br>
Time: 25-35 minutes total, including transfers.<br>
Cost: ¥200 per person × 6 = ¥1,200 (IC card like Suica/Pasmo).<br>
Notes: Cheaper but crowded; managing suitcases on the train and through Tokyo Station’s busy corridors is tricky.<br>
Recommendation: Taxi to Tokyo Station (~¥3,000 total) for convenience with luggage and group size.
</p>
<h3>Step 2: Shinkansen from Tokyo Station to Odawara</h3>
<p>
Location: Tokyo Station, Tokaido Shinkansen platforms (Yaesu side, gates 14-19).<br>
Booking: Reserve seats via “smartEX” (global.jr-central.co.jp) now (March 25) for April 3. Select “Tokyo” to “Odawara,” Hikari or Kodama train (Nozomi skips Odawara), and six seats with oversized luggage space (required for bags over 160 cm combined dimensions).<br>
Details:<br>
Train: Hikari (faster, ~35 minutes) or Kodama (all stops, ~40-45 minutes).<br>
Frequency: Every 15-30 minutes (e.g., Hikari at 9:03 AM, Kodama at 9:16 AM).<br>
Cost: ¥3,500 per person (unreserved ¥3,260, but reserved recommended) × 6 = ¥21,000.<br>
Duration: 35-45 minutes.<br>
Luggage: Overhead racks for standard suitcases; oversized bag goes in reserved space behind last row (book early—limited spots during Sakura season). Arrive 15-20 minutes early to board.<br>
Experience: Smooth, fast ride with urban-to-rural views; wider aisles than Romancecar.<br>
Arrival: Odawara Station (Shinkansen gates).
</p>
<h3>Step 3: Free Shuttle from Odawara to Ryuguden</h3>
<p>
Location: Odawara Station West Exit (exit Shinkansen gates, follow signs to West Exit bus area).<br>
Booking: Reserve via Ryuguden (+81-460-83-1121) or princehotels.com (shuttle page) for April 3. Times: 11:45 AM, 2:00 PM, 4:10 PM (plus 2:30 PM/4:40 PM on Saturdays). Match with your Shinkansen arrival (e.g., 9:03 AM Hikari arrives ~9:38 AM—wait for 11:45 AM shuttle).<br>
Details:<br>
Duration: 50-60 minutes (traffic near Lake Ashi may add 5-10 minutes).<br>
Cost: Free for Ryuguden guests.<br>
Luggage: Shuttle is a van or small bus—six suitcases (one oversized) should fit, but confirm capacity when booking. Owners must accompany bags.<br>
Arrival: Ryuguden’s entrance (139 Motohakone).
</p>
<h2>Total Cost Breakdown</h2>
<p>
Taxi to Tokyo Station: ¥3,000 (group total).<br>
Shinkansen: ¥21,000 (¥3,500 × 6).<br>
Shuttle: ¥0.<br>
Grand Total: ¥24,000 (~¥4,000 per person).
</p>
<h2>Timing Example (Morning Departure)</h2>
<p>
8:30 AM: Taxi from Ōkubo to Tokyo Station (~20 minutes).<br>
9:03 AM: Hikari departs Tokyo (arrive by 8:45 AM to board).<br>
9:38 AM: Arrive Odawara.<br>
9:38-11:45 AM: Wait at Odawara (grab coffee or explore station shops).<br>
11:45 AM: Shuttle departs Odawara.<br>
12:45 PM: Arrive Ryuguden.<br>
Total Travel Time: ~4 hours 15 minutes, including wait (faster Shinkansen options like 10:03 AM reduce it to ~3 hours 15 minutes).
</p>'''

with open('day4/route_overview.html', 'w', encoding='utf-8') as f:
    f.write(template.format(
        title="Day 4 Route Overview",
        header="Route Overview: Ōkubo to Ryuguden",
        content=route_content
    ))

# Worth It content
worth_it_content = '''<p>
Yes, it’s absolutely worth staying until the 1:00 PM shuttle if you’re up for a short morning outing. The area around Ryuguden is rich with iconic Hakone attractions, all within walking distance or a quick bus ride, making it easy to enjoy a few highlights without rushing. With six people and no luggage to haul (since you can leave it at Ryuguden), you’ll have flexibility to explore, especially during peak Sakura season when the scenery is stunning. The alternative—taking the 10:30 AM shuttle—means missing out on these nearby gems and spending extra time waiting in Odawara, which offers less in terms of morning appeal unless you’re keen on Odawara Castle (20-30 minutes from the station).
</p>
<h2>Must-See Attractions Near Ryuguden (Morning Before 1:00 PM)</h2>
<p>Here are the top options within reach from Ryuguden, all doable in your timeframe:</p>
<h3>1. Hakone Shrine (Hakone-jinja)</h3>
<p>
Distance: 1.2 km north along Lake Ashi (15-20 minute walk from Ryuguden).<br>
Time Needed: 30-60 minutes (including walking back).<br>
Why It’s a Must-See: One of Hakone’s most famous landmarks, known for its striking red “Heiwa no Torii” (Gate of Peace) rising from Lake Ashi—perfect for photos, especially with cherry blossoms framing it in early April. The shrine, founded in 757 AD, sits atop a stone stairway (about 90 steps, manageable for most), offering a serene atmosphere and lake views. It’s a cultural highlight and a short, scenic stroll from Ryuguden.<br>
Morning Appeal: Quiet and mystical in the early hours; crowds build later. Open 24/7, free entry.<br>
Plan: Leave Ryuguden at 10:00 AM, arrive by 10:20 AM, spend 20-30 minutes, return by 11:00-11:15 AM. Total: ~1-1.25 hours.
</p>
<h3>2. Onshi Hakone Park (Onshi-Hakone-Koen)</h3>
<p>
Distance: 800m (10-15 minute walk from Ryuguden, south along the lake).<br>
Time Needed: 30-45 minutes.<br>
Why It’s a Must-See: A former imperial summer retreat, this lakeside park offers panoramic views of Lake Ashi and Mount Fuji (weather permitting—April mornings can be clear). The cherry blossoms should be in bloom, adding to the charm. The observation tower (a short climb) enhances the vista, and the gardens are peaceful for a family stroll.<br>
Morning Appeal: Calm and uncrowded early; ideal for a relaxed visit. Open 9:00 AM-5:00 PM, free entry.<br>
Plan: Depart 10:00 AM, arrive 10:15 AM, explore until 10:45-11:00 AM, back by 11:15 AM. Total: ~1-1.25 hours.
</p>
<h3>3. Lake Ashi (Ashinoko) Shoreline Walk + Cedar Avenue</h3>
<p>
Distance: Starts right at Ryuguden; Cedar Avenue is 1 km south (15-minute walk).<br>
Time Needed: 45-90 minutes (depending on how far you go).<br>
Why It’s a Must-See: Lake Ashi is Hakone’s scenic centerpiece, with potential Mount Fuji views and pirate ships gliding across. The nearby Ancient Cedar Avenue, a 500m stretch of 400-year-old trees along the old Tokaido road, feels like stepping into history—especially atmospheric with spring blossoms. It’s flat and family-friendly.<br>
Morning Appeal: Fresh air and light crowds early; the lake sparkles in morning light. Free, open anytime.<br>
Plan: Walk from 10:00 AM, head south to the cedars (~15 minutes), spend 15-30 minutes, return by 11:15-11:30 AM. Total: ~1-1.5 hours.
</p>
<h3>4. Narukawa Art Museum</h3>
<p>
Distance: 300m (5-minute walk from Ryuguden, just north).<br>
Time Needed: 45-60 minutes.<br>
Why It’s a Must-See: A small, modern museum with Japanese paintings (nihonga) and a panoramic window overlooking Lake Ashi and Mount Fuji. The tea lounge adds a cozy touch—perfect for a quick matcha break. It’s the closest attraction, minimizing travel time.<br>
Morning Appeal: Opens at 9:00 AM, quiet early; great for art lovers or a relaxed stop. Entry: ¥1,300/adult, ¥900/child (discounts with Hakone Freepass).<br>
Plan: Leave 10:00 AM, arrive 10:05 AM, spend 45 minutes, back by 11:00 AM. Total: ~1 hour.
</p>
<h2>Does It Make Sense?</h2>
<p>
Yes, If: You want to maximize your Hakone experience, enjoy nature/culture, and don’t mind a short outing. The proximity of these attractions (all within 1.2 km) means you can pick 1-2 without overextending—ideal for a morning before the 1:00 PM shuttle. The shuttle ride to Odawara (~50-60 minutes) gets you there by 2:00 PM, still early for onward plans.<br>
No, If: You’re exhausted from travel, prefer a slow morning at Ryuguden’s onsen (available until check-out), or want to head to Odawara sooner for shopping/lunch (e.g., at Milord mall near the station).
</p>
<h2>Suggested Morning Plan</h2>
<p>
For a balanced, must-see experience:<br>
10:00 AM: Check out, leave luggage at Ryuguden’s front desk (confirm with staff—they typically hold bags for shuttle guests).<br>
10:00-10:20 AM: Walk to Hakone Shrine (20 minutes).<br>
10:20-10:50 AM: Explore the shrine and torii gate (30 minutes—snap photos, enjoy the vibe).<br>
10:50-11:10 AM: Walk back to Ryuguden via the lakefront (20 minutes, enjoy blossoms).<br>
11:10-12:00 PM: Visit Narukawa Art Museum (5-minute walk, 45 minutes inside—art + tea).<br>
12:00-12:30 PM: Relax at Ryuguden (grab a snack from their shop if needed).<br>
1:00 PM: Board shuttle to Odawara.<br>
Total Time: ~2.5-3 hours, back with time to spare. Covers Hakone’s top shrine and a cultural stop, both steps away.
</p>
<h2>Final Take</h2>
<p>
It’s definitely worth it—Hakone Shrine alone justifies the morning, paired with a lake walk or Narukawa for variety. You’re already at Lake Ashi’s heart; skipping these would miss Hakone’s essence. Take the 1:00 PM shuttle and savor a compact, memorable morning over rushing off at 10:30 AM. Enjoy the blossoms and Fuji views if the weather cooperates!
</p>'''

with open('day4/worth_it.html', 'w', encoding='utf-8') as f:
    f.write(template.format(
        title="Day 4 - Is It Worth It?",
        header="Is It Worth It? Morning Near Ryuguden",
        content=worth_it_content
    ))

# Hakone Ropeway content
ropeway_content = '''<p>
Overview: The Hakone Ropeway is an aerial cable car system connecting Sounzan Station to Togendai Station via Owakudani, offering stunning views of Mount Fuji (weather permitting), Lake Ashi, and the volcanic landscape of Owakudani. It’s one of Hakone’s most famous attractions, part of the “Hakone Round Course” tourist loop.<br>
Distance from Ryuguden: Ryuguden is near Togendai Station (~1.5 km, 20-25 minute walk or 5-10 minute bus/taxi), the ropeway’s lakeside endpoint.<br>
Operation:<br>
Route: Sounzan → Owakudani → Togendai (or reverse).<br>
Duration: Full ride (one-way) is ~25-30 minutes; round-trip from Togendai to Owakudani and back is ~50-60 minutes.<br>
Hours: 9:00 AM-5:00 PM (last ascent ~4:15 PM), runs every 1-2 minutes.<br>
Cost: ¥1,600 one-way (Togendai to Owakudani), ¥2,900 round-trip (2023 rates—slight increases possible by 2025). Covered by Hakone Freepass (~¥6,100 from Shinjuku, ¥5,000 from Odawara).
</p>
<h2>Can You Fit It In?</h2>
<p>
Timeframe: Check-out at 10:00 AM, shuttle at 1:00 PM—leaves ~2.5-3 hours (aim to be back by 12:30 PM for buffer).<br>
Travel to Togendai:<br>
Walk: 1.5 km (~20-25 minutes)—doable without luggage but tightens your schedule.<br>
Bus: Hakone Tozan Bus from “Motohakone” stop (near Ryuguden, 700m walk) to “Togendai” (5-10 minutes, ¥360/person, every 15-30 minutes).<br>
Taxi: ¥1,000-¥1,500 (5 minutes)—fastest option.<br>
Ropeway Time:<br>
Togendai to Owakudani (one-way): 15-20 minutes.<br>
Explore Owakudani (volcanic area, black eggs): 20-30 minutes.<br>
Return to Togendai: 15-20 minutes.<br>
Total: ~50-70 minutes (round-trip).<br>
Return to Ryuguden: 5-25 minutes (taxi vs. walk).<br>
Sample Timeline:<br>
10:00 AM: Check out, store luggage.<br>
10:00-10:10 AM: Taxi to Togendai (¥1,500 total).<br>
10:15-10:35 AM: Ropeway to Owakudani.<br>
10:35-11:00 AM: Explore Owakudani (quick photos, black egg if lines are short).<br>
11:00-11:20 AM: Ropeway back to Togendai.<br>
11:25-11:35 AM: Taxi to Ryuguden (¥1,500).<br>
11:35 AM-12:30 PM: Buffer/relax at Ryuguden.<br>
1:00 PM: Shuttle departs.<br>
Total Time: ~1.5-2 hours (tight but feasible with taxis), ~2.5-3 hours with bus/walking.
</p>
<h2>Is It a Must-See That Morning?</h2>
<p>
Pros:<br>
Iconic Views: Mount Fuji and Lake Ashi from above are breathtaking, especially if clear (April mornings often are). Sakura season enhances the scenery.<br>
Unique Experience: Owakudani’s volcanic steam vents and black eggs (boiled in sulfur springs, ¥500/5 eggs) are quirky and memorable—great for your group.<br>
Close Proximity: Togendai’s nearness to Ryuguden makes it more accessible than, say, the Open-Air Museum (farther west).<br>
Cons:<br>
Time Crunch: Fitting it in leaves little room for error—delays (e.g., long lines at Owakudani, bus wait) could stress your 1:00 PM shuttle.<br>
Crowds: Sakura season packs the ropeway; expect queues (5-15 minutes) and full cabins (8-10 people), though it runs frequently.<br>
Cost: ¥2,900/person round-trip × 6 = ¥17,400 (or ¥9,600 one-way), plus transport (~¥3,000 taxis) = ~¥12,600-¥20,400. Pricey for a quick visit unless you have a Freepass.<br>
Weather Risk: Clouds or fog (possible in April) could obscure Fuji, reducing the payoff.<br>
Compared to Alternatives:<br>
Hakone Shrine: Closer (15-20 minute walk), free, cultural, 1-1.5 hours—less rushed, more serene.<br>
Onshi Park: 10-15 minute walk, free, scenic, 1 hour—easiest fit.<br>
Narukawa Museum: 5-minute walk, ¥1,300/person, 1 hour—low effort, high reward.
</p>
<h2>Does It Make Sense?</h2>
<p>
Yes, If: You prioritize the ropeway’s aerial views and volcanic experience over quieter cultural spots, don’t mind a brisk pace, and can splurge on taxis (~¥3,000 round-trip) to save time. It’s a bucket-list item for many in Hakone.<br>
No, If: You prefer a relaxed morning, want to avoid crowds/costs, or value shrine/park vibes more. Missing the 1:00 PM shuttle for a tight ropeway trip isn’t worth the stress when alternatives fit better.
</p>
<h2>Recommendation</h2>
<p>
The Hakone Ropeway is a “must-see” in Hakone generally, but for your tight morning window, it’s not the best fit. Instead:<br>
Go for Hakone Shrine + Narukawa: 2 hours total (10:00-11:00 AM shrine, 11:10-12:00 PM museum), low-cost (¥7,800 for six at Narukawa), and steps from Ryuguden—perfectly paced for the 1:00 PM shuttle.<br>
Ropeway Alternative: If you’re set on it, take taxis (10:00 AM to Togendai, back by 11:35 AM), budget ¥12,600-¥20,400, and keep it brisk—skip Owakudani lingering. But it’s riskier and pricier than the shrine/park combo.
</p>'''

with open('day4/hakone_ropeway.html', 'w', encoding='utf-8') as f:
    f.write(template.format(
        title="Day 4 - Hakone Ropeway",
        header="Hakone Ropeway: Morning Feasibility",
        content=ropeway_content
    ))