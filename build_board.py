#!/usr/bin/env python3
"""Jordan Lee / AI Acquisition — the whole business, wired.

Run: python3 build_board.py  ->  board.html
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from boardbuild import build, X

REPO = os.path.dirname(os.path.abspath(__file__))
S = os.path.expanduser("~/UNDERGROUND_FUNNELS_SSOT/01_RAW_FUNNELS")
W = f"{S}/Jordan_Lee - AI_Acquisition_Method_workshop - 2026-07-31/02_Pages"
V = f"{S}/Jordan_Lee - AI_Acquisition_VSL_funnel - 2026-07-30/02_Pages"

CONFIG = {
    "OUT": os.path.join(REPO, "board.html"),
    "KICK": "Competitor swipe · captured 31 July 2026",
    "TITLE": "Jordan Lee — the whole business, wired",
    "BLURB": "An &ldquo;AI Middleman&rdquo; workshop with a $27 VIP upsell sitting where the "
             "thank-you page should be. Sells the same <b>AI arbitrage</b> mechanism as Richard "
             "Yu and opens on the same AI-job-loss news montage &mdash; strong evidence that a "
             "third party is selling this blueprint.",

    "SHOTS": {
        "optin": {
            "col": 1, "y": 120, "lane": "event", "step": "Entry",
            "title": "Workshop registration",
            "url": "aiacquisitionmethod.com/workshop",
            "img": f"{W}/01_Webinar_registration/20260731T120358Z__screenshot_fullpage.png",
            "max_h": 1000,
            "note": "&ldquo;$0 to $5m/mo in 6 months while travelling the world.&rdquo; Modal "
                    "off <i>YES! SAVE MY SEAT</i>. Name + email + consent. <b>No phone</b> "
                    "&mdash; the only one of the seven that does not demand a number.",
        },
        "vip": {
            "col": 2, "y": 120, "lane": "back", "step": "Upsell",
            "title": "$27 VIP Fast-Track",
            "url": "aiacquisitionmethod.com/workshop-fast-track",
            "img": f"{W}/P2_optin_P2_20260731T115714Z/20260731T115726Z__s1_after__screenshot_fullpage.png",
            "max_h": 1000,
            "note": "Lands here instead of a thank-you page. 5m35s pitch video, and the "
                    "confirmation details are subordinated beneath the offer.",
        },
        "conf": {
            "col": 3, "y": 120, "lane": "event", "step": "Confirmation",
            "title": "Workshop confirmation",
            "url": "aiacquisitionmethod.com/workshop-confirmation",
            "img": f"{W}/02_Webinar_confirmation/20260731T120405Z__screenshot_fullpage.png",
            "max_h": 1000,
            "note": "Two ConverteAI videos, both with <code>main.m3u8</code> sitting in the "
                    "rendered markup. One is the founder welcome, one is the news montage.",
        },
        "vslapp": {
            "col": 1, "y": 1300, "lane": "paid", "step": "Second route",
            "title": "VSL / apply",
            "url": "go.aiacquisition.com/apply",
            "img": f"{V}/01_VSL_apply/20260730T105613Z__screenshot_fullpage.png",
            "max_h": 900,
            "note": "A parallel direct-application route running alongside the workshop.",
        },
        "vslty": {
            "col": 2, "y": 1300, "lane": "paid", "step": "Booked",
            "title": "Thank-you",
            "url": "aiacquisitionmethod.com/thank-you",
            "img": f"{V}/02_Thank-you/20260730T105624Z__screenshot_fullpage.png",
            "max_h": 900,
            "note": "Post-application confirmation on the direct route.",
        },
    },

    "DATA": {
        "dfy": {
            "col": 6, "y": 120, "lane": "back", "step": "BACK END",
            "title": "Done-For-You — the real offer",
            "kv": [("He builds", "your AI agency"),
                   ("He finds", "client 1, then 9 more"),
                   ("Handover", "already cash-flowing"),
                   ("Guarantee", "cash flow in 120 days"),
                   ("Discount", "<b>$5,000 off</b>"),
                   ("Places", "limited to 10"),
                   ("Domain", "aiagentmethod.com"),
                   ("Entity", "Growth Partner Ltd, UK")],
            "note": "A separate, far higher-ticket offer promoted only by email. A $5k discount "
                    "implies a mid-five-figure ticket.",
        },
        "email": {
            "col": 7, "y": 120, "lane": "ever", "step": "The machine",
            "title": "The email engine",
            "kv": [("Volume", "201 emails on file"),
                   ("Cadence", "2&ndash;3&times; daily"),
                   ("Send times", "08:01 &amp; 15:01 ET"),
                   ("Resend", "same subject +4h"),
                   ("ESP", "ActiveCampaign"),
                   ("Tag format", "el=MT-Promo-Wed-29-07-26-DFY1-MLL-E")],
            "note": "Newsjacked AI headlines as subject lines, first name in the subject, and a "
                    "resend to non-openers four hours later.",
        },
        "claims": {
            "col": 4, "y": 120, "lane": "event", "step": "Proof claims",
            "title": "The numbers on the page",
            "kv": [("Avg monthly revenue", "$18,105"),
                   ("Avg cash collected", "$308,960"),
                   ("Avg retainer", "$3,752"),
                   ("Market", "$1.7 trillion"),
                   ("Attended", "50,000+"),
                   ("Survey base", "~100 of 660")],
            "note": "The $18,105 figure is quoted three times as an average. The footer says it "
                    "came from 660 surveyed with about 100 responding.",
        },
        "event": {
            "col": 5, "y": 120, "lane": "event", "step": "The pitch",
            "title": "Live workshop — genuinely live",
            "kv": [("When", "Sat 1 Aug, 8:00 PM ET"),
                   ("Platform", "Zoom (us02web)"),
                   ("Via", "joinevent.link"),
                   ("Registered", "yes"),
                   ("Price", "not yet observed")],
            "note": "Unlike Richard Yu and Karla Marie, this one is a real Zoom webinar on a "
                    "real date. It has to be attended.",
        },
    },

    "EDGES": [
        ("optin", "vip"), ("vip", "conf"), ("conf", "claims"), ("claims", "event"), ("event", "dfy"), ("dfy", "email"),
        ("vslapp", "vslty"), ("vslty", "claims"),
    ],

    "LABELS": [
        {"x": X[1], "y": 60, "t": "Workshop route"},
        {"x": X[1], "y": 1240, "t": "Direct application route"},
        {"x": X[1], "y": 2500, "t": "Routing logic"},
    ],

    "BRANCH": [
        {"id": "b_template", "x": X[1] + 10, "y": 2560, "state": "dq",
         "cond": "Same template as Richard Yu",
         "body": "Both sell a mechanism named <b>&ldquo;AI arbitrage&rdquo;</b>. Both open cold "
                 "on a montage of broadcast news clips about AI replacing jobs before the founder "
                 "appears &mdash; Jordan Lee's second confirmation video is exactly that. Two "
                 "unrelated operators do not converge this precisely by accident. Worth finding "
                 "out who is selling the blueprint.",
         "ev": "VERIFIED · both funnels captured and transcribed 31 Jul"},
        {"id": "b_guarantee", "x": X[3] + 10, "y": 2560, "state": "yes",
         "cond": "Buys VIP → refund plus $27 if unhappy",
         "body": "&ldquo;If you don't feel you got at least 10 times the value, email support and "
                 "I will refund every single penny with no questions asked. Plus I'll send you an "
                 "extra $27 on top just for wasting your time.&rdquo; Paying a penalty on top of "
                 "the refund is a sharper risk reversal than money-back, and at $27 it costs "
                 "almost nothing.",
         "ev": "VERIFIED · captured on the fast-track page 31 Jul"},
        {"id": "b_stat", "x": X[5] + 10, "y": 2560, "state": "unver",
         "cond": "The $18,105 average is thin",
         "body": "Presented three times as what &ldquo;our average client&rdquo; makes. The "
                 "footer discloses a survey of 660 businesses with roughly <b>100 responding</b> "
                 "&mdash; a self-selected sixth of the base, self-reported, almost certainly "
                 "skewed to winners. If we ever quote a client average, the n belongs beside the "
                 "number, not in an eight-point footer.",
         "ev": "VERIFIED as disclosed · underlying data not auditable"},
        {"id": "b_dfy", "x": X[9] + 10, "y": 2560, "state": "yes",
         "cond": "Stays on the list → pitched a Done-For-You service",
         "body": "The real money is not the workshop. By email he sells a <b>DFY</b> service "
                 "where he builds the agency, finds the first paying client and nine more, and "
                 "hands over a cash-flowing asset. Guarantee: <b>cash flow within 120 days or "
                 "your money back</b>. Framed with an investor lens — Buffett and Thiel "
                 "cannot get that guarantee. A <b>$5,000 discount</b> and only 10 places. "
                 "Different domain (aiagentmethod.com) and a different legal entity "
                 "(Growth Partner &amp; Consultancy Ltd, London) from the front end.",
         "ev": "VERIFIED · full email pulled from Will's inbox, 29 Jul"},
        {"id": "b_nophone", "x": X[11] + 10, "y": 2560, "state": "yes",
         "cond": "Registers on name and email only",
         "body": "The only funnel of the seven with no phone field. Every other one demands a "
                 "mobile number under autodial consent. Worth testing against our own opt-in "
                 "&mdash; he is clearly willing to trade the number for the conversion.",
         "ev": "VERIFIED · registered successfully with no phone, 31 Jul"},
    ],

    "LEGEND": [("event", "Workshop route"), ("paid", "Direct application"),
               ("back", "$27 upsell + DFY back end")],
}

if __name__ == "__main__":
    build(CONFIG)
