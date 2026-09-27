"""All site copy lives here. Edit this file to change what the site says."""

PROFILE = {
    "name": "Lydia Cortez",
    "headline_lead": "Clarity",
    "headline_emphasis": "from Complexity",
    "summary": (
        "Over ten years working with eCommerce, payments, EHR, CRM, and compliance "
        "systems. I build for real users, fix root causes instead of symptoms, "
        "and I'm the one who finds the edge case before it finds you."
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
        "For more than ten years, I've worked where business operations meet the systems "
        "that run them: eCommerce, CRM, EHR, subscription revenue, payments, and compliance.",
        "I started on the business side of eCommerce, then moved into QA on ONEHOPE's custom "
        "React and microservices commerce platform. Most recently, as Data Operations Manager "
        "at the Alliance for Community Empowerment, I owned business requirements and reporting "
        "infrastructure for a nonprofit EHR platform, managed two Data Support Specialists, "
        "and guided Agile delivery.",
        "The common thread is depth. I learn systems inside and out, view them through every "
        "user's eyes, and catch the edge cases others miss. When something breaks, I find the "
        "root cause and either fix it or recommend how to prevent it from recurring.",
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
