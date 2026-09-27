"""All site copy lives here. Edit this file to change what the site says."""

PROFILE = {
    "name": "Lydia Cortez",
    "headline_lead": "Clarity",
    "headline_emphasis": "from Complexity",
    "summary": (
        "A decade adapting fast across eCommerce, payment processing, WMS, EHR, CRM, "
        "and compliance platforms. I turn ambiguous problems into clear plans that "
        "bridge business strategy and technical execution."
    ),
    "tags": [
        "Problem Solving",
        "Business & Technical Operations",
        "Cross-Functional Strategy",
        "Systems Design",
        "User-Focus",
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
    "title": "Operator. Strategist.",
    "title_emphasis": "Builder.",
    # **double asterisks** mark bold phrases; the frontend renders them safely.
    "paragraphs": [
        "I've spent over a decade inside complex systems, understanding them from root "
        "to surface, fixing what's broken, and designing what's next. My background spans "
        "eCommerce, CRM, EHR, compliance, subscription revenue, and payments.",
        "What sets me apart isn't just knowing how systems work. It's the ability to connect systems "
        "thinking to business strategy and hold the end user at the center of every decision I make.",
        "I'm ready to step into roles where I can own product direction, drive operational "
        "transformation, or shape the systems that power a business. I'm not just a data ops "
        "manager. I'm a force multiplier.",
    ],
    "strengths": [
        {"icon": "gear", "title": "Systems thinking at scale",
         "body": "I understand platforms end to end, from data models to user flows, and identify where leverage lives."},
        {"icon": "target", "title": "Business-first orientation",
         "body": "Every system I touch is measured by business outcomes, not just uptime or clean data."},
        {"icon": "users", "title": "Multi-role user expertise",
         "body": "Deep experience designing for environments with layered user roles, permissions, and workflows."},
        {"icon": "flag", "title": "Agile delivery leadership",
         "body": "Sprint planning, backlog ownership, team mentorship. I run execution with discipline and clarity."},
    ],
}

# The systems map in the hero. connects_to draws the lines between platforms.
PLATFORMS = [
    {"id": "ecom", "name": "eCommerce", "blurb": "Storefronts, catalogs, and order flow from cart to fulfillment.",
     "connects_to": ["pay", "wms", "crm"]},
    {"id": "pay", "name": "Payments", "blurb": "Payment processing, subscription billing, and recurring revenue.",
     "connects_to": ["ecom", "comp"]},
    {"id": "wms", "name": "WMS", "blurb": "Warehouse management: inventory, picking, and shipping operations.",
     "connects_to": ["ecom"]},
    {"id": "ehr", "name": "EHR", "blurb": "Electronic health records with layered clinical and admin roles.",
     "connects_to": ["crm", "comp"]},
    {"id": "crm", "name": "CRM", "blurb": "Customer data, lifecycle workflows, and reporting.",
     "connects_to": ["ecom", "ehr"]},
    {"id": "comp", "name": "Compliance", "blurb": "Audit trails, permissions, and regulatory controls.",
     "connects_to": ["pay", "ehr"]},
]

EXPERTISE = [
    {"icon": "layers", "title": "Technical & Systems Operations",
     "body": "Full lifecycle ownership of complex platforms, from requirements to rollout. I identify failure points others miss and design systems that scale.",
     "platforms": ["ecom", "wms", "ehr"]},
    {"icon": "box", "title": "Product Ownership",
     "body": "Business requirements, stakeholder alignment, sprint planning, and delivery. I translate strategy into executed product roadmaps.",
     "platforms": ["ecom", "crm"]},
    {"icon": "compass", "title": "Business Strategy",
     "body": "I analyze operational inefficiencies, identify growth opportunities, and build the business case for transformation across verticals.",
     "platforms": ["pay", "crm"]},
    {"icon": "link", "title": "Platform Integration",
     "body": "EHR, CRM, eCommerce, payment, and compliance platforms. I've operated in all of them and know how to make them work together.",
     "platforms": ["ecom", "pay", "wms", "ehr", "crm", "comp"]},
    {"icon": "chart", "title": "Data & Reporting Infrastructure",
     "body": "Designing reporting pipelines, ensuring data integrity, and building the visibility teams need to make good decisions quickly.",
     "platforms": ["crm", "pay", "comp"]},
    {"icon": "eye", "title": "End-User Experience",
     "body": "Users aren't a footnote. I embed UX thinking into every operational and product decision across complex, multi-role environments.",
     "platforms": ["ehr", "ecom"]},
]

CONTACT = {
    "title": "Optimize what exists.",
    "title_emphasis": "Build what's next.",
    "body": "Open to roles in technical operations, product management, systems strategy, and business operations. Let's talk.",
}

FOOTER = "Technical Operations · Product Strategy · Systems"
