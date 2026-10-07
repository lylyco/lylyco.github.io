"""All site copy lives here. Edit this file to change what the site says."""

PROFILE = {
    "name": "Lydia Cortez",
    "headline_lead": "Adaptive by nature.",
    "headline_emphasis": "Problem solver by instinct.",
    "summary": (
        "Experience across eCommerce, FinTech, EHR, CRM, and compliance "
        "systems. Curious and proactive, I am a natural initiator and problem "
        "solver. I build for real users, spot gaps across data, teams, "
        "processes, and systems, and address them at the root. I lead teams "
        "and collaborate cross-functionally to turn complex challenges into "
        "practical solutions and get things done."
    ),
    "industries_line": (
        "Industries under my belt: retail, distilled spirits, payment processing, "
        "subscription billing, and social and clinical services."
    ),
    "tags": [
        "Business Operations",
        "Process Improvement",
        "Requirements Gathering",
        "Reporting & Analytics",
        "SQL",
        "Systems Strategy",
        "Team Leadership",
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
        "operations, data, and technology, earning **five promotions over eight years**. "
        "My experience spans retail, distilled spirits, payment processing, subscription "
        "billing, and social and clinical services.",
        "I began on the business side of eCommerce, where I was already solving problems, "
        "supporting users and tracking down platform issues. That "
        "work led me into QA for ONEHOPE Wine's commerce platform, where I traced issues to "
        "their root cause and learned not only how systems break, but why. That experience "
        "became the foundation for how I approach technical and operational problems.",
        "Most recently, as ACE's first Data Operations Manager II, I took on product, systems, and technical "
        "operations responsibilities while leading three Data Support Specialists and two "
        "engineering contractors supporting a newly migrated EHR platform across nine social "
        "and clinical service programs. I established formal scoping, strategic planning, and "
        "reporting, strengthened the team's technical capabilities, and resolved organizational "
        "gaps.",
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

# Each project links to its own page at "url". build.py creates that page: the full
# case study if the project has one, otherwise a "coming soon" page. Leave "url" empty to show the card without a link.
PROJECTS = {
    "title": "Problems I've",
    "title_emphasis": "solved.",
    "items": [
        {"title": "Closing the Compliance Gap on Client Assessments",
         "summary": "No program owned the organization's main client assessment. I audited the data, defined ownership, and automated compliance reports for 7 programs, raising completion from under 50% to 90%.",
         "url": "/projects/compliance-reporting/",
         # The full write-up on the project's own page. Projects without "case_study"
         # get a "coming soon" page instead. Wrap words in ** ** to make them bold.
         "case_study": {
             "heading": "Closing the compliance gap",
             "heading_emphasis": "on client assessments.",
             "problem": "The Strengths and Needs Assessment (SANA) is the organization's main assessment requirement for every enrolled client. When a client was enrolled in more than one program, no one knew which program was responsible for completing it. There was no shared workflow, no policy defining ownership, and no one overseeing the data. Visibility depended on occasional manual spot checks by individual program managers, so no one could see the full picture.",
             "steps": [
                 ["Mapped the current process.", "I learned how each program conducted the assessment and confirmed there was no official workflow. I identified the SANA as the core assessment shared across programs, required at enrollment and again every six months. I also flagged edge cases: Behavioral Health and Parenting staff don't conduct these intakes, so they had to be excluded from reporting."],
                 ["Audited the data.", "I compared SANAs recorded in the system against program enrollment. Fewer than 50% of enrolled clients had a SANA on record. Staff were relying on manual side records that leadership could not see or verify."],
                 ["Defined ownership.", "Through collaborative discussions with three directors and the COO, I helped establish a policy for which program is responsible for conducting the SANA when a client is enrolled in more than one."],
                 ["Built the reports.", "I applied my knowledge of the EHR schema to direct AI tools (ChatGPT, Claude) in building compliance reports for 7 programs, including QA and testing, cutting development time from an estimated 3 months to 1 month. Each report shows the staff member responsible for the SANA, even when that responsibility sits with another program, so teams have shared visibility and can coordinate."],
                 ["Automated delivery.", "I rolled the report out to 7 programs and set up automated email delivery, the first time these programs received compliance reports directly. Each report included documentation explaining how it works."],
                 ["Advocated for ending manual tracking.", "Using the audit findings, I made the case to leadership for retiring manual records and making the system the single source of truth. The initiative was not fully adopted, but it put the cost of manual tracking on leadership's radar for the first time and laid the groundwork for future data governance."],
             ],
             "impact": [
                 "Raised SANA completion from under 50% of enrolled clients to 90%",
                 "Gave leadership organization-wide visibility into assessment compliance for the first time, replacing occasional manual spot checks",
                 "Gave managers a clear way to hold case managers accountable to policy: a SANA at enrollment and every six months",
                 "Used the reports as a data quality check, surfacing clients with no enrollment date on record",
             ],
             "next": [
                 "Run ongoing audits to measure adoption and track compliance trends over time",
                 "Continue pushing to fully retire manual tracking so the system becomes the single source of truth",
             ],
             # Shown after What's Next, in this order. Block types: "sql" (a file in the
             # repo), "note", "sheet" (Google Sheets embed), "image" (with "alt" text).
             "sample": {
                 "heading": "Sample Report",
                 "blocks": [
                     {"sql": "samples/sana_report.sql"},
                     {"note": "One program's report, rebuilt with sample data. All names and IDs are fictional."},
                     {"sheet": "https://docs.google.com/spreadsheets/d/1n68s8y_Ww8uzaVTtRuDXVsrUTddvgakzMm5CjWYTkTg/preview",
                      "url": "https://docs.google.com/spreadsheets/d/1n68s8y_Ww8uzaVTtRuDXVsrUTddvgakzMm5CjWYTkTg/edit?usp=sharing"},
                 ],
             },
         }},
        {"title": "Creating Cross-Program Visibility for a New Department",
         "summary": "My team had no shared view of its work across 9 programs. I built a central project board, introduced sprint planning, and automated intake. We delivered 773 stories in 2025.",
         "url": "/projects/cross-program-visibility/",
         "case_study": {
             "heading": "Cross-program visibility",
             "heading_emphasis": "for a new department.",
             "problem": "Our core team had no shared view of who was working on what. Sprint planning had never been used in the organization, so there was no structured way to coordinate work, set priorities, or show leadership and partner teams our actual workload across 9 programs.",
             "steps": [
                 ["Took on a growing scope.", "I joined as a Data Operations Manager, and the role quickly grew to include systems operations and product work across 9 programs."],
                 ["Built a centralized project board.", "To manage that scope, I created one board where all of the team's work lived, so everyone could see what was in progress, what was next, and who owned it."],
                 ["Introduced Agile practices.", "I adapted practices from engineering teams, combining Scrum sprint planning with Kanban workflows."],
                 ["Automated intake.", "I set up work requests and EHR support tickets from across the organization to flow directly onto the board."],
                 ["Iterated until it fit.", "After several rounds of iteration, the process matched how our team actually works."],
             ],
             "impact": [
                 "**Team clarity:** My immediate team gained full visibility into each other's work, priorities, and capacity, along with the structure and rhythm that sprint planning provides.",
                 "**Organization-wide transparency:** Partner teams and leadership could see our work in real time. When we said we were at capacity, the board showed why. At the time, no other team in the organization had a comparable process.",
                 "**Cross-program tracking:** Because our deliverables directly supported or worked alongside all 9 programs, the board gave us a reliable way to track every deliverable and its dependencies.",
                 "**Streamlined intake:** Automating work requests and EHR support tickets into the board removed manual triage and ensured nothing was lost between systems.",
                 "**Measurable output:** We completed 773 stories in 2025 with a team of 3 to 4, and have surpassed 1,000 so far in 2026 with 3 staff and 2 contractors.",
                 "**Clear ownership:** Defined responsibilities made it possible to hold my direct reports accountable to agreed commitments.",
                 "**Reliable upward communication:** I gained a consistent way to report progress and resource needs to my supervisor across all 9 programs.",
             ],
             "next": [
                 "Expand tagging to categorize work by program and type",
                 "Align projects with estimated time and effort",
                 "Introduce story points to estimate and balance workload across the team",
             ],
             "sample": {
                 "heading": "Example",
                 "blocks": [
                     {"note": "I built this dashboard in early 2026 to show leadership everything our team delivered in 2025. I worked on those 773 completed cards alongside my team, not just managed them, and the dashboard gave all of us the recognition we earned."},
                     {"image": "/static/img/projects/dashboard-2025.png",
                      "alt": "Annual Data Team Delivery Dashboard showing 773 completed cards in 2025, with monthly totals rising from 54 in January to 84 in December"},
                 ],
             },
         }},
        {"title": "Project 3",
         "summary": "Coming Soon",
         "url": "/projects/coming-soon-3/"},
    ],
}

RECOMMENDATIONS = {
    "title": "In their",
    "title_emphasis": "words.",
    "source": "Source: recommendations on my LinkedIn profile.",
    "source_label": "View on LinkedIn",
    "source_url": "https://www.linkedin.com/in/lydia-cortez/details/recommendations/",
    "items": [
        {"name": "Rebecca MacLean",
         "photo": "/static/img/recs/rebecca.jpg",
         "title": "Grant Writer + Writing Consultant",
         "relationship": "Worked with Lydia on the same team",
         "date": "January 2025",
         "quote": "Lydia is the powerhouse behind ACE's success.",
         "paragraphs": [
             "Lydia is the powerhouse behind ACE's success. I have seen her tackle challenges that would be daunting to the most talented data managers. She rises to every obstacle and manages to do so while remaining kind, empathetic, and patient. She is truly a pleasure to work with.",
         ]},
        {"name": "Gemma Schrum",
         "photo": "/static/img/recs/gemma.jpg",
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
         "photo": "/static/img/recs/matt.jpg",
         "title": "Engineering Leader",
         "relationship": "Managed Lydia directly",
         "date": "December 2023",
         "quote": "She was always a great communicator with our team and when working with frustrated users.",
         "paragraphs": [
             "Lydia and I worked together at OneHope on a custom-built ecommerce platform using ReactJS & Microservices. She was always a great communicator with our team and when working with frustrated users. We started working more closely as she took on additional responsibilities in her role by starting to find issues for the engineering team. Quickly ramping up on QA responsibilities, she joined our engineering team as a dedicated QA engineer, rapidly learning our processes and setting a new QA level of excellence. Lydia has a strong independent drive to learn and drive into more complex scenarios in QA. I hope our paths cross in the future as I would be honored to work together with her.",
         ]},
        {"name": "Carmella Winterbauer",
         "photo": "/static/img/recs/carmella.jpg",
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

# Shown under your name beside the portrait in About.
TAGLINE = "Business Operations · Process Improvement · Requirements Gathering · Reporting & Analytics · SQL · Systems Strategy · Team Leadership"

FOOTER = {
    "credit": "Written and directed by Lydia Cortez. Built with Claude to my spec using FastAPI and Strawberry GraphQL.",
    "source_label": "View source on GitHub",
    "source_url": "https://github.com/lylyco/lylyco.github.io",
    "legal": "© 2026 Lydia Cortez · Last updated October 2026",
}