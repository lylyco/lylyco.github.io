"""All site copy lives here. Edit this file to change what the site says."""

PROFILE = {
    "name": "Lydia Cortez",
    "location": "Los Angeles, CA",   # shown under your name in the top bar
    "headline_lead": "Adaptive by nature.",
    "headline_emphasis": "Problem solver by instinct.",
    "summary": (
        "Business systems and operations professional with experience across "
        "eCommerce, payments and subscription billing, EHR, CRM, and compliance "
        "systems. I troubleshoot issues to the root cause, manage the platforms "
        "teams depend on, and spot gaps across data, processes, and systems "
        "before they become problems. I build for real users and work across "
        "teams to turn complex challenges into practical fixes."
    ),
    "industries_line": (
        "Industries under my belt: retail, distilled spirits, payment processing, "
        "subscription billing, and social and clinical services."
    ),
    # Shown as two rows of four on wide screens (split in half, in this order).
    "tags": [
        "Business Systems",
        "Troubleshooting",
        "Systems Administration",
        "Quality Assurance",
        "Process Improvement",
        "Reporting & Analytics",
        "SQL",
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
    "title": "Systems Thinker.",
    "title_emphasis": "Creative Builder.",
    # **double asterisks** mark bold phrases; the frontend renders them safely.
    "paragraphs": [
        "For more than 10 years, I have built my career at the intersection of business "
        "operations, data, and technology, earning **four promotions** along the way. My "
        "experience spans retail, distilled spirits, payment processing, subscription "
        "billing, and social and clinical services.",
        "I began on the business side of eCommerce at Fornia Apparel and Nordstrom Rack | "
        "HauteLook, building product listings, managing samples, and resolving customer issues. "
        "At ONEHOPE Wine, I kept solving problems, supporting users and tracking down platform "
        "issues, which led me into QA for its commerce platform. There I traced issues to their "
        "root cause and learned not only how systems break, but why. That experience became the "
        "foundation for how I approach technical and operational problems.",
        "Most recently, as ACE's first Data Operations Manager, later promoted to Manager II, I took on product, systems, and technical "
        "operations responsibilities while leading an intern, two Data Support Specialists, and two "
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
    {"id": "pay", "name": "Payments", "blurb": "Payment processing, subscription billing, and recurring revenue.",
     "connects_to": ["ecom", "comp"]},
    {"id": "wms", "name": "WMS", "blurb": "Warehouse management and inventory operations.",
     "connects_to": ["ecom","comp"]},
    {"id": "ehr", "name": "EHR", "blurb": "Electronic health records with layered clinical and admin roles.",
     "connects_to": ["comp"]},
    {"id": "crm", "name": "CRM", "blurb": "Customer data, lifecycle workflows, and reporting.",
     "connects_to": ["ecom"]},
    {"id": "comp", "name": "Compliance", "blurb": "Audit trails, permissions, and regulatory controls, including compliance and distribution management software for distilled spirits.",
     "connects_to": ["ecom", "pay", "ehr"]},
]

EXPERTISE = [
    # Top row: the systems. Bottom row: the people and product.
    {"title": "Business Systems",
     "body": "I manage user roles, access, and configuration across platforms, and translate between business teams and engineering."},
    {"title": "Troubleshooting & Root Cause",
     "body": "I identify root causes and resolve what I can on my own. When engineering or vendor support is needed, I hand off clear tickets with reproducible steps."},
    {"title": "Reporting & Analytics",
     "body": "I build SQL reports with data quality checks built in, so teams can trust the numbers and act on them quickly."},
    {"title": "End-User Experience",
     "body": "Users aren’t a footnote. I put myself in their shoes and build for how each role actually works."},
    {"title": "Product Ownership",
     "body": "I drive business requirements, stakeholder alignment, sprint planning, and delivery, then monitor adoption and fix issues after launch."},
    {"title": "People Leadership",
     "body": "I listen first, collaborate openly, and coach where needed. At ACE, I led specialists, an intern, and engineering contractors, and managed our EHR vendor relationship."},
]

# Each project links to its own page at "url". build.py creates that page: the full
# case study if the project has one, otherwise a "coming soon" page. Leave "url" empty to show the card without a link.
PROJECTS = {
    "title": "Problems I've",
    "title_emphasis": "solved.",
    "intro": "I joined as the first Data Operations Manager in a new department. I introduced the tools, processes, and ways of working that helped our teams collaborate and gave everyone clearer visibility into our work.",
    "items": [
        {"title": "Closing the Compliance Gap on Client Assessments",
         "summary": "I audited the data, assigned clear ownership, and automated compliance reports across seven programs, raising assessment completion from under 50% to 90%.",
         "url": "/projects/compliance-reporting/",
         "tools": ["Google Sheets", "Navicat", "SQL"],   # shown at the bottom of the card
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
                 ["Built the reports.", "I applied my knowledge of the EHR schema to direct AI tools (ChatGPT, Claude) in building compliance reports for seven programs, cutting development time from an estimated 3 months to 1 month. Each report shows the staff member responsible for the SANA, even when that responsibility sits with another program, so teams have shared visibility and can coordinate."],
                 ["Quality Assurance.", "I tested each report for accuracy before rollout, checking results against records in the EHR. I built data checks into the queries themselves: excluding test records and flagging issues such as clients marked active with a discharge date or clients with no enrollment date on record."],
                 ["Automated delivery.", "I rolled the report out to seven programs and set up automated email delivery, the first time these programs received compliance reports directly. Each report included documentation explaining how it works."],
                 ["Advocated for ending manual tracking.", "Using the audit findings, I made the case to leadership for retiring manual records and making the system the single source of truth. The initiative was not fully adopted, but it put the cost of manual tracking on leadership's radar for the first time and laid the groundwork for future data governance."],
             ],
             "impact": [
                 "Raised SANA completion from under 50% of enrolled clients to 90%.",
                 "Gave leadership organization-wide visibility into assessment compliance for the first time, replacing occasional manual spot checks.",
                 "Gave managers a clear way to hold case managers accountable to policy: a SANA at enrollment and every six months.",
                 "Used the reports as a data quality check, surfacing clients with no enrollment date on record.",
             ],
             "next": [
                 "Run ongoing audits to measure adoption and track compliance trends over time.",
                 "Continue pushing to fully retire manual tracking so the system becomes the single source of truth.",
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
        {"title": "Redesigning the Care Management Form and the Guidance Behind It",
         "summary": "The form relied on open-ended fields that produced inconsistent, hard-to-report data. I led the redesign with structured answer options and clear staff guidance, raising data accuracy from roughly 25% to 75%.",
         "url": "/projects/care-management-redesign/",
         "tools": ["EHR Configuration", "Google Sheets", "Navicat", "Notion", "SQL"],
         "case_study": {
             "heading": "Redesigning the Care Management form",
             "heading_emphasis": "and the guidance behind it.",
             "problem": "When I joined, the organization was in the middle of moving from Apricot to a new EHR system. Nine programs were operating without a dedicated data manager, which meant no one owned data quality, no audits were taking place, and forms had grown without a clear structure. Staff were not used to entering data into a centralized internal database, and most forms relied on open-ended fields that produced inconsistent, hard-to-report information. Care Management (the organization's equivalent of Case Management) needed a full overhaul, and there was no established process for scoping, planning, or defining requirements. There was also no reference material explaining how the service worked, so staff had little guidance on what to document or why.",
             # A {"group": "..."} entry starts a labeled group; numbering continues across groups.
             "steps": [
                 {"group": "Part 1: Care Management Service Form Redesign"},
                 ["Challenged the initial scope.", "When leadership shared the first outline of desired updates, I pushed back on keeping open-ended responses. Staff needed guidance, and the organization needed data it could measure. I advocated for structured, selectable answer options throughout."],
                 ["Audited the data with SQL.", "I wrote queries to audit legacy records, showing how staff were actually documenting the service and where the data fell short, which guided the research behind the redesign."],
                 ["Led the research and guided the redesign.", "Without a background in social services or clinical behavioral health, I treated that gap as a reason to dig deeper rather than defer, and led the research behind every section of the form. My supervisee carried out most of the hands-on redesign while I supported her through the EHR configuration and handled smaller pieces of the build myself. Together we built answer choices grounded in how the work actually happens."],
                 ["Designed for the end user.", "Every decision was weighed against the staff who would complete the form. I focused on keeping it clear, relevant, and manageable so the added structure would not become a burden."],
                 ["Quality Assurance.", "I wrote SQL queries to QA the redesigned form and confirm it captured data correctly."],
                 {"group": "Part 2: Service Documentation and Guidance"},
                 ["Guided the reference material.", "I guided my supervisee in creating documentation that explains how Care Management works, walks through real-world scenarios, and defines key terms. This gave staff clear direction on what to record and gave the data team the subject knowledge needed to redesign the form."],
                 ["Introduced new tools.", "I brought Notion into the organization as the home for this documentation, creating a central, accessible resource that did not exist before."],
                 {"group": "Across Both"},
                 ["Drove cross-program collaboration.", "I worked closely with the COO and all nine programs to align requirements, gather feedback, and build buy-in."],
                 ["Set a repeatable approach.", "The pairing of a structured form with clear guidance became the model I applied to enhancements across my other projects."],
             ],
             "impact": [
                 "Improved data accuracy from roughly 25% to 75% by auditing legacy records and redesigning the service form with structured, required fields.",
                 "Strengthened the organization's position for grant applications and reporting by making outcomes measurable.",
                 "Gave staff a single source of truth for how to deliver and document the service.",
                 "Made the work of direct service staff visible, which supported recognition, morale, and a culture of celebrating impact.",
             ],
             "next": [
                 "Implement regular data audits and analysis to monitor quality and usage.",
                 "Hold ongoing conversations with programs about how they are adapting and where further refinement is needed.",
             ],
             "sample": {
                 "heading": "Example",
                 "blocks": [
                     {"note": "Screenshots from the Care Management guide in Notion. Each section pairs the redesigned form with plain-language definitions, so staff know what to select and why. Click any image to view it full size."},
                     # A gallery shows the first image full width and the rest side by side.
                     {"gallery": [
                         {"image": "/static/img/projects/care-guide-overview.png",
                          "alt": "Care Management Service Record guide home page in Notion, with a jump-to-section menu, collapsible sections, and a quick reference list",
                          "caption": "The guide's home page: a jump-to-section menu, a section for each part of the form, and a quick reference for common edge cases."},
                         {"image": "/static/img/projects/care-guide-interaction.png",
                          "alt": "Interaction Details section showing the required form fields and a definition for each answer choice",
                          "caption": "Interaction Details: every required field, with a definition for each answer choice."},
                         {"image": "/static/img/projects/care-guide-resources.png",
                          "alt": "Resource Support section showing structured checkboxes for public assistance benefits with examples",
                          "caption": "Resource Support: structured checkboxes in place of open-ended notes, with examples staff can match their work to."},
                     ]},
                 ],
             },
         }},
        {"title": "Creating Cross-Program Visibility for a New Department",
         "summary": "I built a central project board, introduced sprint planning, and automated intake of work requests and EHR tickets, enabling the team to close 773 work items in 2025 and 1,000+ through September 2026.",
         "url": "/projects/cross-program-visibility/",
         "tools": ["Google Sheets", "Trello"],
         "case_study": {
             "heading": "Cross-program visibility",
             "heading_emphasis": "for a new department.",
             "problem": "Our core team had no shared view of who was working on what. Sprint planning had never been used in the organization, so there was no structured way to coordinate work, set priorities, or show leadership and partner teams our actual workload across nine programs.",
             "steps": [
                 ["Took on a growing scope.", "I joined as a Data Operations Manager II, and the role quickly grew to include systems operations and product work across nine programs."],
                 ["Built a centralized project board.", "To manage that scope, I created one board where all of the team's work lived, so everyone could see what was in progress, what was next, and who owned it."],
                 ["Introduced Agile practices.", "I adapted practices from engineering teams, combining Scrum sprint planning with Kanban workflows."],
                 ["Automated workflows.", "I set up work requests and EHR support tickets from across the organization to flow directly onto the board."],
                 ["Iterated until it fit.", "After several rounds of iteration, the process matched how our team actually works."],
             ],
             "impact": [
                 "**Team clarity:** My immediate team gained full visibility into each other's work, priorities, and capacity, along with the structure and rhythm that sprint planning provides.",
                 "**Organization-wide transparency:** Partner teams and leadership could see our work in real time. When we said we were at capacity, the board showed why. At the time, no other team in the organization had a comparable process.",
                 "**Cross-program tracking:** Because our deliverables directly supported or worked alongside all nine programs, the board gave us a reliable way to track every deliverable and its dependencies.",
                 "**Streamlined workflows:** Automating work requests and EHR support tickets into the board removed manual triage and ensured nothing was lost between systems.",
                 "**Measurable output:** We completed 773 work items in 2025 with a team of 3 to 4, and have surpassed 1,000 so far in 2026 with 3 staff and 2 contractors.",
                 "**Clear ownership:** Defined responsibilities made it possible to hold my direct reports accountable to agreed commitments.",
                 "**Reliable upward communication:** I gained a consistent way to report progress and resource needs to my supervisor across all nine programs.",
             ],
             "next": [
                 "Expand tagging to categorize work by program and type.",
                 "Align projects with estimated time and effort.",
                 "Introduce story points to estimate and balance workload across the team.",
             ],
             "sample": {
                 "heading": "Example",
                 "blocks": [
                     {"note": "I built this dashboard in early 2026 to show leadership everything our team delivered in 2025. I worked on those 773 work items alongside my team, not just managed them, and the dashboard gave all of us the recognition we earned."},
                     {"image": "/static/img/projects/dashboard-2025.png",
                      "alt": "Annual Data Team Delivery Dashboard showing 773 completed cards in 2025, with monthly totals rising from 54 in January to 84 in December"},
                 ],
             },
         }},
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
    "body": "Open to roles in Business Systems, Technical Operations, and Product Operations, as well as select consulting engagements focused on systems implementation and workflow improvement.",
}

FOOTER = {
    "credit": "Written and directed by Lydia Cortez. Built with Claude to my spec using FastAPI and Strawberry GraphQL.",
    "source_label": "View source on GitHub",
    "source_url": "https://github.com/lylyco/lylyco.github.io",
    "legal": "© 2026 Lydia Cortez · Last updated October 2026",
}