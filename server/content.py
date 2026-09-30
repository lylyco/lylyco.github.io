"""All site copy lives here. Edit this file to change what the site says."""

PROFILE = {
    "name": "Lydia Cortez",
    "headline_lead": "Adaptive by nature.",
    "headline_emphasis": "Problem solver by instinct.",
    "summary": (
        "Experience across eCommerce, FinTech, EHR, CRM, and compliance "
        "systems. With a curious mind, I am a natural initiator and proactive "
        "problem solver. I build for real users, spot gaps across data, teams, "
        "processes, and systems, and address them at the root. I lead teams "
        "and collaborate cross-functionally to turn complex challenges into "
        "practical solutions and get things done."
    ),
    "industries_line": (
        "Industries under my belt: retail, distilled spirits, payment processing, "
        "subscription billing, and social and clinical services."
    ),
    "tags": [
        "Systems & Data",
        "Operations Leadership",
        "Process Improvement",
        "Business Acumen",
        "Cross-Functional Collaboration",
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
        "For more than ten years, I have built my career at the intersection of business "
        "operations, data, and technology, earning **five promotions over eight years** "
        "through strong performance, adaptability, and ownership. My experience spans retail, "
        "distilled spirits, payment processing, subscription billing, and social and clinical "
        "services.",
        "I began on the business side of eCommerce before moving into QA for ONEHOPE Wine's "
        "commerce platform, where I learned not only how systems break, but why. That "
        "foundation continues to shape how I approach technical problems.",
        "Most recently, as the first Data Operations Manager at the Alliance for Community "
        "Empowerment, I led three Data Support Specialists and two engineering contractors "
        "supporting an EHR platform across nine social and clinical service programs. I "
        "brought structure and visibility to the team's work, introduced formal scoping and "
        "strategic planning, and addressed gaps that lacked clear ownership.",
        "My approach combines deep systems knowledge, data-driven problem solving, and the "
        "perspective of the people doing the work. I evaluate solutions based on their "
        "impact and cost, communicate the rationale behind decisions, and implement practical "
        "interim solutions when permanent fixes are not immediately possible. I also bring "
        "the right people together to build shared understanding and develop solutions that "
        "are both technically sound and operationally sustainable.",
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
    {"id": "pay", "name": "Fintech", "blurb": "Payment processing, subscription billing, and recurring revenue.",
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
    {"title": "Technical & Systems Operations",
     "body": "I own complex platforms end to end, from requirements through configuration to rollout. I catch failure points early and build systems that hold up as the business grows."},
    {"title": "Product Ownership",
     "body": "I drive business requirements, stakeholder alignment, sprint planning, and delivery for a platform serving nine programs."},
    {"title": "Business Strategy",
     "body": "I find operational inefficiencies, size the opportunity, and build the business case for change."},
    {"title": "Data & Reporting Infrastructure",
     "body": "I design reporting pipelines, protect data integrity, and give teams the visibility to make good decisions quickly."},
    {"title": "End-User Experience",
     "body": "Users aren't a footnote. I bring their perspective into every operational and product decision, especially in multi-role environments."},
    {"title": "People Leadership",
     "body": "I listen first, collaborate openly, and build morale that lasts. Strong teams keep delivering long after a single project ends."},
]

UNDER_THE_HOOD = {
    "title": "This Portfolio is",
    "title_emphasis": "one query.",
    "body": (
        "Every word here comes from a Python GraphQL API (FastAPI and Strawberry), "
        "coded by Claude to my spec. I set the structure, made the calls, and wrote "
        "the copy. The browser sends the query on the right and renders what comes "
        "back."
    ),
}

RECOMMENDATIONS = {
    "title": "In their",
    "title_emphasis": "words.",
    "source": "Source: recommendations on my LinkedIn profile.",
    "source_label": "View on LinkedIn",
    "source_url": "https://www.linkedin.com/in/lydia-cortez",
    "items": [
        {"name": "Rebecca MacLean",
         "title": "Grant Writer + Writing Consultant",
         "relationship": "Worked with Lydia on the same team",
         "date": "January 2025",
         "quote": "Lydia is the powerhouse behind ACE's success.",
         "paragraphs": [
             "Lydia is the powerhouse behind ACE's success. I have seen her tackle challenges that would be daunting to the most talented data managers. She rises to every obstacle and manages to do so while remaining kind, empathetic, and patient. She is truly a pleasure to work with.",
         ]},
        {"name": "Gemma Schrum",
         "title": "Engineering at Onton",
         "relationship": "Managed Lydia directly",
         "date": "December 2023",
         "quote": "Her thoughtful ideas for improvement impacted more than just the tech team.",
         "paragraphs": [
             "Lydia was a cornerstone of the tech team. She mastered the product inside out to where she would identify very obscure edge cases and solve very complex bugs. Her communication and tickets are so clear and descriptive that she saved us precious engineering time\u2013 and oftentimes she had already found the root cause of difficult issues that otherwise would have taken an engineer a lot of time to debug.",
             "Beyond Lydia's testing prowess, she has consistently taken initiative and juggled many tasks and demands beyond her defined role. Her thoughtful ideas for improvement impacted more than just the tech team. Her proactive approach, coupled with a collaborative and kind demeanor, made her a pleasure to work with.",
             "All to say, Lydia's thorough QA work significantly enhanced the quality and stability of their releases. Her ambition and attitude make her an invaluable asset. She will excel in any role she takes on, and I would be honored to work with Lydia again!",
         ]},
        {"name": "Matt Middlesworth",
         "title": "Engineering Leader",
         "relationship": "Managed Lydia directly",
         "date": "December 2023",
         "quote": "She was always a great communicator with our team and when working with frustrated users.",
         "paragraphs": [
             "Lydia and I worked together at OneHope on a custom-built ecommerce platform using ReactJS & Microservices. She was always a great communicator with our team and when working with frustrated users. We started working more closely as she took on additional responsibilities in her role by starting to find issues for the engineering team. Quickly ramping up on QA responsibilities, she joined our engineering team as a dedicated QA engineer, rapidly learning our processes and setting a new QA level of excellence. Lydia has a strong independent drive to learn and drive into more complex scenarios in QA. I hope our paths cross in the future as I would be honored to work together with her.",
         ]},
        {"name": "Carmella Winterbauer",
         "title": "Group Product Manager",
         "relationship": "Managed Lydia directly",
         "date": "January 2024",
         "quote": "She proactively identifies issues and works closely and effectively with engineers toward a resolution.",
         "paragraphs": [
             "I had the pleasure of having Lydia on my team at ONEHOPE for many years. Lydia is a passionate QA leader with a rare curiosity that leads her to understand an application inside and out. She proactively identifies issues and works closely and effectively with engineers toward a resolution.",
             "Her QA plans are thoughtful and thorough. As a product manager, I rested easier at night knowing that Lydia was in charge of QAing a new feature. I believe that a talented QA engineer is worth their weight in gold and I wholeheartedly endorse Lydia as the real deal. Any team would be lucky to have her.",
         ]},
    ],
}

CONTACT = {
    "title": "Optimize what exists.",
    "title_emphasis": "Build what's next.",
    "body": "Open to new opportunities across operations, systems, product, and adjacent functions, as well as select consulting engagements. Let's talk.",
}

FOOTER = "Business Operations · Technical Operations · Systems Strategy"