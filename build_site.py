#!/usr/bin/env python3
"""Build the Jordan Lee / AI Acquisition swipe site.

Run: python3 build_site.py
"""
import sys, os, glob
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/JORDAN_LEE_Swipe")

tx = sorted(glob.glob(os.path.join(PKG, "Transcript/jordan_lee_*.md")))

CONFIG = {
    "SITE": "Jordan Lee — AI Acquisition Method",
    "CREATOR": "Jordan Lee",
    "ADS_KEY": "jordan_lee",
    "FUNNEL_IDS": ["F003", "F067"],
    "CAPTURED": "31 July 2026",
    "REPO": REPO,
    "PACKAGE": "~/Downloads/Swipes/JORDAN_LEE_Swipe",
    "BLURB": "An &ldquo;AI Middleman&rdquo; workshop funnel running a $27 VIP upsell straight "
             "off the opt-in. Sells the same &ldquo;AI arbitrage&rdquo; mechanism as Richard Yu, "
             "with a near-identical AI-job-loss news montage — strong evidence of a shared "
             "template moving through this space.",

    "PAGES": [
        ("index.html", "Overview"),
        ("analysis.html", "Analysis"),
        ("transcripts.html", "Transcripts"),
        ("videos.html", "Video library"),
    ],

    "STATS": [
        ("VIP upsell", "$27"),
        ("Claimed avg", "$18,105/mo"),
        ("Survey base", "~100 of 660"),
        ("Video captured", "13m 12s"),
        ("Event", "Zoom, live"),
        ("Guarantee", "10x or refund +$27"),
        ("Market claim", "$1.7 trillion"),
        ("Phone required", "No"),
    ],

    "OFFER": [
        ("Product", "AI Acquisition Method — the &ldquo;AI Middleman&rdquo; model"),
        ("Lead claim", "&ldquo;$0 to $5m/mo in 6 months while travelling the world&rdquo;"),
        ("Front-end", "Free live workshop, Zoom, evening ET"),
        ("Upsell", "<b>$27 VIP Fast-Track</b>, offered immediately after the opt-in"),
        ("VIP guarantee", "&ldquo;10 times the value or I refund every penny, plus an extra $27 "
                          "just for wasting your time&rdquo;"),
        ("Headline stat", "Average partner makes <b>$18,105/month</b>"),
        ("Stat's small print", "From a survey of 660 businesses with <b>~100 responding</b> — "
                               "buried in the footer disclaimer"),
        ("Other stats", "$308,960 average cash collected; $3,752 average monthly retainer"),
        ("Price", '<span class="tag warn">not observed</span> — the core offer sits behind the '
                  'live workshop'),
    ],

    "FINDINGS": [
        ("Shared template with Richard Yu",
         "Both sell a mechanism called &ldquo;AI arbitrage&rdquo;. Both open on a montage of "
         "broadcast news clips about AI replacing jobs before the founder appears. Jordan Lee's "
         "confirmation video opens on exactly that. Two operators, one script architecture — "
         "worth watching for whoever is selling the template."),
        ("The refund-plus-$27 guarantee",
         "&ldquo;If you don't feel you got at least 10 times the value, email us and I'll refund "
         "every penny, plus send you an extra $27 for wasting your time.&rdquo; Paying a penalty "
         "on top of the refund is a sharper risk-reversal than a plain money-back promise, and it "
         "costs almost nothing at a $27 price point."),
        ("The $18,105 stat is thinner than it reads",
         "The footer discloses it came from a survey of 660 businesses with roughly 100 "
         "responses — a ~15% response rate, self-reported, almost certainly skewed to winners. "
         "The number is quoted three times on the page as though it were a population average."),
        ("His no-show sequence is the best thing in this swipe file",
         "Within 7 hours of a missed workshop he sends: <b>&ldquo;Do you hate me William?&rdquo;</b> "
         "(subject line), then <b>&ldquo;I know why you didn't show up tonight&rdquo;</b>. The first "
         "takes the blame himself &mdash; <i>&ldquo;there's one last reason that could explain why "
         "you didn't show up. And that's because I let you down.&rdquo;</i> The second names the "
         "prospect's actual thought: <i>&ldquo;You thought: it is just another webinar. Another "
         "pitch. Another guy promising the world.&rdquo;</i> Then the reframe that sets up his "
         "guarantee: <b>&ldquo;If you want to expose a fake guru in ten seconds, ask them to take "
         "their payment from your results. They will give you 48 reasons why they can't.&rdquo;</b> "
         "<b>Show rate is our keystone metric and this is a working answer to it.</b>"),
        ("The real offer is a Done-For-You service, sold only by email",
         "The workshop is the front end. By email he pitches <b>DFY</b>: he builds the AI agency, "
         "finds the first paying client and nine more, and hands over a cash-flowing asset. "
         "Guarantee is <b>cash flow within 120 days or your money back</b>, framed against "
         "Buffett and Thiel &mdash; &ldquo;even they can't find business investments with that "
         "level of guarantee.&rdquo; A <b>$5,000 discount</b>, only 10 places, on a different "
         "domain (aiagentmethod.com) under a different entity (Growth Partner &amp; Consultancy "
         "Ltd, London). A $5k discount implies a mid-five-figure ticket."),
        ("Two domains, two form treatments",
         "aiacquisitionmethod.com takes name and email only. aiagentmethod.com runs the same "
         "workshop but <b>does</b> ask for a phone with SMS consent. Same offer, two domains, "
         "two friction levels &mdash; worth reading as a live test."),
        ("A 201-email machine already sitting in Will's inbox",
         "Two to three sends a day at 08:01 and 15:01 ET, the same subject resent to non-openers "
         "four hours later, first name in the subject line, and newsjacked AI headlines as hooks "
         "(&ldquo;The Chinese are coming for your AI&rdquo;, &ldquo;Musk is going to use Grok to "
         "remake The Odyssey&rdquo;). ActiveCampaign, with link tags like "
         "<code>el=MT-Promo-Wed-29-07-26-DFY1-MLL-E</code>. No waiting required to swipe it."),
        ("No phone field",
         "The only funnel of the seven that registers on name and email alone. Everything else in "
         "this set demands a mobile number with autodial consent."),
        ("Upsell before confirmation",
         "The opt-in does not land on a thank-you page. It lands on the $27 VIP pitch, with the "
         "confirmation details subordinated beneath it."),
    ],

    "FUNNEL": [
        ("Workshop opt-in", "aiacquisitionmethod.com/workshop",
         "Modal off &ldquo;YES! SAVE MY SEAT&rdquo;. Name + email + consent checkbox. <b>No phone.</b>"),
        ("VIP fast-track", "aiacquisitionmethod.com/workshop-fast-track",
         "$27 upsell with a 5m35s pitch video. Decline path available."),
        ("Confirmation", "aiacquisitionmethod.com/workshop-confirmation",
         "Two ConverteAI videos, both <code>main.m3u8</code> exposed in the markup."),
        ("Live workshop", "joinevent.link &rarr; us02web.zoom.us/w/…",
         '<span class="tag good">genuinely live</span> Zoom webinar'),
    ],

    "TRANSCRIPT_GROUPS": [("Captured video", tx)],
    "SLIDE_PAGES": [],

    "VIDEOS": [
        ("jordan_lee_vip_oto.mp4", 335, "39 MB", "The $27 VIP Fast-Track pitch."),
        ("jordan_lee_conf_1.mp4", 241, "31 MB", "Confirmation video — founder welcome, hospital-bed origin."),
        ("jordan_lee_conf_2.mp4", 197, "35 MB", "Confirmation video — the AI-job-loss news montage."),
    ],

    "ANALYSIS": """
<div class="note"><b>The finding that matters.</b> Jordan Lee and Richard Yu are running the same
architecture: the same mechanism name (&ldquo;AI arbitrage&rdquo;), the same cold open of
broadcast news clips about AI job losses, the same everyday-people-to-five-figures proof pattern.
Either they share an agency, a swipe, or a template vendor. When two unrelated funnels converge
this precisely, it usually means a third party is selling the blueprint.</div>

<h2 class="sec">Worth taking</h2>
<div class="grid g2">
<div class="card"><h3>Guarantee with a penalty attached</h3><p>Refund plus an extra $27 for
wasting the buyer's time. At a low ticket the downside is trivial and it converts the guarantee
from a defensive clause into an offensive claim. There is a version of this for our own
low-ticket entry point.</p></div>
<div class="card"><h3>Upsell in the confirmation slot</h3><p>The moment after opt-in is the
highest-intent moment in the funnel and every operator in this swipe file monetises it. Ours is
currently a plain thank-you page.</p></div>
<div class="card"><h3>Opt-in with no phone</h3><p>The only one of the seven that does not demand
a mobile number. Worth testing against our own form — the phone field is a measurable drop-off
and he is clearly willing to trade it away.</p></div>
</div>

<h2 class="sec">Read carefully</h2>
<p>The $18,105/month figure is presented as what &ldquo;our average client&rdquo; makes and
repeated three times. The footer says it came from 660 businesses surveyed with about 100
responding. That is a self-selected sixth of the base. If we ever quote a client average, the n
and the response rate belong next to the number, not in an eight-point footer.</p>
""",
}

if __name__ == "__main__":
    build(CONFIG)
