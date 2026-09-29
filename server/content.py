"""All site copy lives here. Edit this file to change what the site says."""

PROFILE = {
    "name": "Lydia Cortez",
    "headline_lead": "Adaptive by nature.",
    "headline_emphasis": "Problem solver by instinct.",
    "summary": (
        "Over ten years working across eCommerce, fintech, SaaS, EHR, CRM, and compliance "
        "systems. I build for real users, spot the gaps between teams, processes, and "
        "systems, and close them at the root. I'm the one who finds the edge case before "
        "it finds you."
    ),
    "industries_line": (
        "Industries under my belt: apparel, distilled spirits, payment processing, "
        "subscription billing, and social and clinical services."
    ),
    "tags": [
        "Operations Leadership",
        "Process Improvement",
        "Business Acumen",
        "Cross-Functional Collaboration",
        "Systems & Data",
    ],
    "email": "cortez0715@gmail.com",
    "photo": {
        "src": "/static/img/lydia.jpg",
        "thumb": "/static/img/lydia-face.jpg",
        "alt": "Lydia Cortez smiling, wearing a red and purple patterned cardigan",
    },
    "links": [
        {"label": "LinkedIn", "url": "https://www.linkedin.com/in/lydia-cortez/", "kind": "linkedin"},
        {"label": "GitHub", "url": "https://github.com/lylyco", "kind": "github"},
    ],
}

ABOUT = {
    "title": "Operator. Strategist. Creative",
    "title_emphasis": "Leader.",
    # **double asterisks** mark bold phrases; the frontend renders them safely.
    "paragraphs": [
        "For more than ten years, I've worked where business operations meet the systems "
        "that run them, across apparel, distilled spirits, payment processing, subscription "
        "billing, and social and clinical services. I've been **promoted 5 times in 8 "
        "years**, each time into more scope and more at stake.",
        "I started on the business side of eCommerce, then moved into QA on ONEHOPE's "
        "commerce platform, where I learned how systems break and why. Most recently, as the "
        "first Data Operations Manager at the Alliance for Community Empowerment, I led three "
        "Data Support Specialists and two engineering contractors supporting an EHR platform "
        "used by **nine distinct social and clinical service programs**. I brought full "
        "visibility to the data team's work, introduced formal scoping and strategic planning, "
        "and closed gaps no one had owned before.",
        "My QA background is why I go deep. I learn systems inside and out, use data to see "
        "what's actually happening, and look at every decision through the eyes of the people "
        "doing the work. When I recommend a solution, I explain why, what it will affect, and "
        "what it costs. When a full fix has to wait, I put a temporary one in place and I'm "
        "clear about its tradeoffs. And I don't solve problems alone. I bring the right teams "
        "together to solve them.",
    ],

    "strengths": [
        {"icon": "target", "title": "Business acumen and foresight",
         "body": "I see where a decision leads before it's made, and I plan for the impact, not just the fix."},
        {"icon": "compass", "title": "Recommendations with reasoning",
         "body": "Every solution comes with the why, the tradeoffs, and a short-term plan when the long-term one needs time."},
        {"icon": "gear", "title": "Operational improvement",
         "body": "I spot friction in day-to-day workflows and redesign them so programs, and the people supporting them, work more efficiently."},
        {"icon": "users", "title": "Collaborative leadership",
         "body": "I lead teams and partner across departments, using sprint planning, backlog ownership, and mentorship to keep execution on track."},
    ],
}

# The systems map in the hero. connects_to draws the lines between platforms.
PLATFORMS = [
    {"id": "ecom", "name": "eCommerce", "blurb": "Storefronts, catalogs, and order flow from cart to fulfillment.",
     "connects_to": ["pay", "wms", "crm", "comp"]},
    {"id": "pay", "name": "Payments", "blurb": "Payment processing, subscription billing, and recurring revenue.",
     "connects_to": ["ecom", "comp"]},
    {"id": "wms", "name": "WMS", "blurb": "Warehouse management and inventory operations.",
     "connects_to": ["ecom"]},
    {"id": "ehr", "name": "EHR", "blurb": "Electronic health records with layered clinical and admin roles.",
     "connects_to": ["comp"]},
    {"id": "crm", "name": "CRM", "blurb": "Customer data, lifecycle workflows, and reporting.",
     "connects_to": ["ecom"]},
    {"id": "comp", "name": "Compliance", "blurb": "Audit trails, permissions, and regulatory controls, including compliance and distribution management software for distilled spirits.",
     "connects_to": ["ecom", "pay", "ehr"]},
]

EXPERTISE = [
    {"icon": "layers", "title": "Technical & Systems Operations",
     "body": "End-to-end ownership of complex platforms, from requirements through configuration to rollout. I catch failure points early and build systems that hold up as the business grows.",
     "platforms": ["ecom", "pay", "wms", "ehr", "comp"]},
    {"icon": "box", "title": "Product Ownership",
     "body": "Business requirements, stakeholder alignment, sprint planning, and delivery for a platform serving nine programs.",
     "platforms": ["ehr"]},
    {"icon": "compass", "title": "Business Strategy",
     "body": "I find operational inefficiencies, size the opportunity, and build the business case for change.",
     "platforms": ["ehr", "ecom"]},
    {"icon": "chart", "title": "Data & Reporting Infrastructure",
     "body": "Designing reporting pipelines, ensuring data integrity, and giving teams the visibility to make good decisions quickly.",
     "platforms": ["ehr", "ecom"]},
    {"icon": "eye", "title": "End-User Experience",
     "body": "Users aren't a footnote. I bring the user's perspective into every operational and product decision, especially in multi-role environments.",
     "platforms": ["ehr", "ecom"]},
    {"icon": "users", "title": "People Leadership",
     "body": "I listen first, collaborate openly, and build team morale that lasts. Strong teams keep delivering long after a single project ends.",
     "platforms": ["ecom", "pay", "wms", "ehr", "crm", "comp"]},
]

UNDER_THE_HOOD = {
    "title": "Under the Hood",
    "body": (
        "Every word here comes from a Python GraphQL API (FastAPI and Strawberry), "
        "coded by Claude to my spec. I set the structure, made the calls, and wrote "
        "the copy. The browser sends the query on the right and renders what comes "
        "back. The platform filter above runs its own query with an argument."
    ),
}

CONTACT = {
    "title": "Optimize what exists.",
    "title_emphasis": "Build what's next.",
    "body": "Open to operations leadership roles at the Manager, Associate Director, and Director level, and to select consulting engagements. Let's talk.",
}

FOOTER = "Business Operations · Technical Operations · Systems Strategy"