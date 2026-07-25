import json
import uuid
from django.db import migrations


def seed_portfolio_data(apps, schema_editor):
    Skill = apps.get_model('portfolio_app', 'Skill')
    Certification = apps.get_model('portfolio_app', 'Certification')
    Hobby = apps.get_model('portfolio_app', 'Hobby')
    Service = apps.get_model('portfolio_app', 'Service')
    SideProject = apps.get_model('portfolio_app', 'SideProject')
    Profile = apps.get_model('portfolio_app', 'Profile')
    ProfileItem = apps.get_model('portfolio_app', 'ProfileItem')
    Project = apps.get_model('portfolio_app', 'Project')
    Link = apps.get_model('portfolio_app', 'Link')

    # --- Skills ---
    cdn = "https://cdn.jsdelivr.net/gh/glincker/thesvg@main/public/icons/{}/default.svg"
    skills_data = [
        ("Swift", "90%", cdn.format("swift")),
        ("Python", "75%", cdn.format("python")),
        ("Node.js", "60%", cdn.format("nodejs")),
        ("Go", "65%", "https://cdn.jsdelivr.net/gh/glincker/thesvg@main/public/icons/go/light.svg"),
        ("TypeScript", "70%", cdn.format("typescript")),
        ("Bash", "80%", cdn.format("gnu-bash")),
        ("Ruby", "80%", cdn.format("ruby")),
    ]
    for i, (name, percent, icon) in enumerate(skills_data, start=1):
        Skill.objects.create(id=uuid.uuid4(), name=name, percent=percent, icon=icon, order=i)

    # --- Certifications ---
    certifications_data = [
        ("Claude", "https://cdn.jsdelivr.net/gh/glincker/thesvg@main/public/icons/claude/default.svg",
         "https://www.credly.com/users/duy-nguyen.446d7901/badges/credly"),
        ("Google Cloud", "https://cdn.jsdelivr.net/gh/glincker/thesvg@main/public/icons/google-cloud/default.svg",
         "https://www.skills.google/public_profiles/5d7f3359-0912-46b9-b584-2ced13dd36cb"),
        ("Atlassian", "https://cdn.jsdelivr.net/gh/glincker/thesvg@main/public/icons/atlassian/default.svg",
         "https://cp.certmetrics.com/atlassian/en/public/badge/c?id=AT00138007&ccat=62&date=2024-1-18"),
        ("ITIL", "img/cert-icons/itil.png",
         "https://1drv.ms/b/c/383EFE1C5687C4BF/IQBNb2qxx7KORrVlFTDOATBgAYLhzBmiAuJkqhS2yQNqu1c?e=VFWgfs"),
    ]
    for i, (name, icon, link) in enumerate(certifications_data, start=1):
        Certification.objects.create(id=uuid.uuid4(), name=name, icon=icon, link=link, order=i)

    # --- Hobbies ---
    hobbies_data = [
        ("Reading", "'Books are a uniquely portable magic'", "Stephen King, On Writing: A Memoir of the Craft", "flaticon-open-book"),
        ("Guitar", "'I like to be quiet and play guitar and just chill.'", "Post Malone", "flaticon-acoustic-guitar"),
        ("Travelling", "'The world is a book, and those who do not travel read only a page.'", "Saint Augustine", "flaticon-aeroplane"),
        ("Swimming", "'The man who is swimming against the stream knows the strength of it.'", "Woodrow Wilson", "flaticon-swimmer"),
        ("Gym", "'No pain, no gain'", "Ben Franklin", "flaticon-weightlifting"),
        ("Soccer", "'Soccer is a magical game'", "David Beckham", "flaticon-soccer-ball-variant"),
    ]
    for i, (name, quote, author, image) in enumerate(hobbies_data, start=1):
        Hobby.objects.create(id=uuid.uuid4(), name=name, quote=quote, author=author, image=image, order=i)

    # --- Services ---
    services_data = [
        ("Atlassian Consultant",
         "Consult and helping businesses optimize their usage of Atlassian tools",
         "flaticon-two-thin-arrows-forming-a-circle"),
        ("DevOps Consultant",
         "Architect, design full pipeline of DevOps from ALM (Jira | Git) through CI (Jenkins) to CD (Docker | Configuration Management)",
         "flaticon-infinite-symbol"),
        ("Software Development",
         "Building clean and robust applications leveraging cutting-edge technologies: Swift, Objective-C, Python, Zapier",
         "flaticon-computer"),
    ]
    for i, (name, description, image) in enumerate(services_data, start=1):
        Service.objects.create(id=uuid.uuid4(), name=name, description=description, image=image, order=i)

    # --- Side Projects ---
    side_projects_data = [
        ("🟢 Claude Tools Directory", "only-claude.png", ["nextjs", "typescript"], "", "https://only-claude.duynb.com", "", ""),
        ("🟢 AI Status Monitor", "ai-status.png", ["nextjs", "typescript"], "https://github.com/duynb92/all-ai-statuses", "https://ai-status.duynb.com", "", ""),
        ("🟢 Coffee Mate", "coffee-mate.png", ["swiftui", "coredata"], "", "https://coffeemate-lp.duynb.com", "https://apps.apple.com/app/coffee-order-translator/id6757706484", ""),
        ("🚧 Expiry Tracker", "coming-soon.jpg", ["go", "swiftui", "kotlin"], "", "https://expiry-tracker-lp.duynb.com", "", ""),
    ]
    for i, (name, thumbnail, tags, github_url, demo_url, apple_store_url, google_play_url) in enumerate(side_projects_data, start=1):
        SideProject.objects.create(
            id=uuid.uuid4(), name=name, thumbnail=thumbnail,
            tech_tags_raw=json.dumps(tags),
            github_url=github_url, demo_url=demo_url,
            apple_store_url=apple_store_url, google_play_url=google_play_url,
            order=i,
        )

    # --- Profiles ---
    p_certs = Profile.objects.create(id=uuid.uuid4(), header="Certifications", order=1)
    cert_items = [
        (1, "2026", "Claude Certified Architect", "Anthropic.com",
         ["Anthropic's first official certification, designed to verify that engineers can design and ship production-grade Claude AI applications at enterprise scale."],
         "https://www.credly.com/badges/2bfb0239-335f-4ed8-9e01-bf42efb688d7", True),
        (2, "2023", "Certified Zapier Expert", "Zapier",
         ["Officially recognized by Zapier for my advanced automation skills, including building complex workflows, integrating APIs, and optimizing business processes."],
         "https://verify.skilljar.com/c/5nxbf2655e7y", True),
        (3, "2022", "ITIL® 4 Specialist - Create, Deliver and Support", "Axelos",
         ["ITIL 4 ® Specialist Create, Deliver and Support demonstrates this individual has an understanding and skills on how to plan, build and integrate different value streams and activities to create, deliver and support IT and digitally-enabled products and services, and relevant practices, methods and tools. They demonstrate sufficient understanding and application of ITIL 4 practices to the creation, delivery and support across support services, the service value systems and value streams."],
         "https://1drv.ms/b/c/383EFE1C5687C4BF/IQAdYYYJE2T_SqxRqXB06iUEAewtkcmA1gJPScfx_2ue8R8?e=vjdHye", True),
        (4, "2022", "ITIL® 4 Foundation", "Axelos",
         ["ITIL® 4 Foundation demonstrates this individual understands the key concepts of IT and digital service delivery including the key concepts, guiding principles and practices of ITIL® 4 for service management. They have a fundamental understanding of the modern organisation's end-to-end operating model for the creation, delivery and continual improvement of technology-enabled products and services. They have an awareness of how cultural or behavioural principles benefits the wider organisation."],
         "https://1drv.ms/b/c/383EFE1C5687C4BF/IQBNb2qxx7KORrVlFTDOATBgAQiv35t0wlv4tTVD07y1zOM?e=EdMsri", True),
        (5, "2020", "ACE | Atlassian Certified Expert", "Atlassian.com",
         ["ACE is Atlassian's most prestigious Certification. Atlassian Certified Experts hold at least four Atlassian Certified Professional-level credentials, demonstrating their expertise across multiple Atlassian products."],
         "https://cp.certmetrics.com/atlassian/en/public/badge/c?id=AT00138007&ccat=62&date=2024-1-18", True),
        (6, "2017", "CSPO | CERTIFIED Scrum Product Owner", "ScrumAlliance.org",
         ["Learn the foundation of Scrum and the scope of the Certified Scrum Product Owner's role from the best minds in Scrum.",
          "Demonstrate to employers and peers your attainment of core Scrum knowledge.",
          "Expand your career opportunities by staying relevant and marketable across all industry sectors adopting Agile practices.",
          "Engage with a community of recognized Scrum experts who are committed to continuous improvement."],
         "", True),
        (7, "2017", "PSM I | Professional Scrum Master I", "Scrum.org",
         ["Demonstrated a fundamental level of Scrum mastery, proving an understanding of Scrum as described in the Scrum Guide and the concepts of applying Scrum."],
         "", True),
        (8, "2014 - 2015 - 2016", "Best Member of the Year | Best Team Leader of the Year | Most Active Support of the Year", "Beesightsoft",
         [], "", True),
    ]
    for order, time, title, sub_title, descriptions, link, is_active in cert_items:
        ProfileItem.objects.create(
            id=uuid.uuid4(), profile=p_certs, time=time, title=title,
            sub_title=sub_title, descriptions_raw=json.dumps(descriptions),
            link=link, is_active=is_active, order=order,
        )

    p_work = Profile.objects.create(id=uuid.uuid4(), header="work experiences", order=2)
    work_items = [
        # Commented-out items included with is_active=False
        (1, "Aug '17 - Present", "Upwork", "Professional Freelancer", [], "", False),
        (2, "May '21 - Present", "EleganceGroup | Atlassian Gold Solution Partner", "Senior Atlassian Architect", [], "", False),
        (3, "Jan '21 - Present", "foodpanda | Delivery Hero APAC Pte. Ltd", "Senior Software Engineer", [], "", True),
        (4, "July '20 - Dec '24", "AgileOps", "Co-founder | Advisor", [], "", True),
        (5, "Aug '19 - Nov '20", "DinDinn Corporation Pte. Ltd", "Software Engineer", [], "", True),
        (6, "Jul '18 - Jul '19", "Upwork", "Professional Freelancer", [], "", True),
        (7, "Jun '14 - Jul '18", "Beesightsoft", "SCRUM Master | iOS Specialist | .NET Ninja", [], "", True),
    ]
    for order, time, title, sub_title, descriptions, link, is_active in work_items:
        ProfileItem.objects.create(
            id=uuid.uuid4(), profile=p_work, time=time, title=title,
            sub_title=sub_title, descriptions_raw=json.dumps(descriptions),
            link=link, is_active=is_active, order=order,
        )

    p_edu = Profile.objects.create(id=uuid.uuid4(), header="education", order=3)
    ProfileItem.objects.create(
        id=uuid.uuid4(), profile=p_edu,
        time="2010-2015",
        title="University of Information Technology - Vietnam National University HCMC",
        sub_title="Bachelor of Engineering",
        descriptions_raw=json.dumps([]), link="", is_active=True, order=1,
    )

    p_skills = Profile.objects.create(id=uuid.uuid4(), header="PROFESSIONAL SKILLS", order=4)
    skill_items = [
        (1, "Database", "SQL Server, Postgresql, MySql, Sqlite, Realm"),
        (2, "IDE & Tools", "XCode, Visual Studio Code"),
        (3, "VCS / DVCS", "Bitbucket | GitHub | GitLab"),
        (4, "CI & Build Tools", "Jenkins | Bitrise | TravisCI, Code quality (swiftlint), xcodebuild (iOS), xctest (iOS)"),
        (5, "ALM", "Jira, Confluence, Jira Service Management"),
        (6, "Framework & Dependency Manager", "RxSwift, GoogleMap, GoogleAnalytics, CocoaPods | Carthage"),
        (7, "Architecture", "OOP/SOLID/DRY, Design Patterns, IoC/Dependency Injection, MVC/MVP/MVVM/Clean Architecture, Functional Reactive Programming"),
        (8, "Testing", "TDD | BDD, iOS Testing frameworks (Quick, Nimble)"),
    ]
    for order, time, title in skill_items:
        ProfileItem.objects.create(
            id=uuid.uuid4(), profile=p_skills, time=time, title=title,
            sub_title="", descriptions_raw=json.dumps([]), link="", is_active=True, order=order,
        )

    # --- Projects ---
    # ProjectPlatform constants
    IOS, ANDROID, WEB, WINDOWS = 1, 2, 3, 4
    # ProjectCategory constants
    MOBILE, WEB_CAT = 1, 2

    projects_data = [
        # (order, name, tag, filters, description, client, roles, skills, length, categories, screenshots, links)
        (1, "HubSpot Blog Content Management Toolbox", "zapier", "custom-integration",
         "Streamline content marketing with a Zapier custom app connecting Jira, Confluence, and HubSpot. Effortlessly create and manage marketing materials, empowering companies and individuals to maximize productivity.",
         "NA", "Zapier Platform", "Javascript", "2 weeks", [], 0, []),
        (2, "HubSpot Social Content Management Toolbox", "zapier", "custom-integration",
         "Boost social media marketing efficiency with a Zapier custom app linking Jira, HubSpot. Streamline content creation and management, empowering companies and individuals to maximize their social media presence effortlessly.",
         "NA", "Zapier Platform", "Javascript", "2 weeks", [], 0, []),
        (3, "Timesheet & payroll system", "zapier", "custom-integration",
         "Simplify your payroll management with a custom integration built in Zapier. Effortlessly retrieve timesheets from Upwork, transform and store data in Google Sheets as a powerful database. Seamlessly generate invoices in QuickBooks using the integrated database, streamlining your time tracking and invoicing process.",
         "NA", "Zapier Platform", "Javascript", "1 month", [], 0, []),
        (4, "Jira/JSD/Confluence Administration tasks", "jarvisanalytics", "atlassian",
         "Jira/JSD Cloud cleanup, setting up JSD workflows. Create dashboards and reports on Jira. Create custom templates for meeting notes, client reports.",
         "United States", "Jira & Confluence Administator", "Jira/JSD/Confluence Configuration | Jira REST API | Confluence REST API", "3 months", [], 0, []),
        (5, "JEMH Cloud Configurations", "casupport", "atlassian",
         "Basic and advanced configurations for Enterprise Mail Handler for Jira (JEMH) on Jira Service Desk to customize email template, like adding actions, automate workflows, approve/decline requests.",
         "United States", "JSD Administator", "JSD Configuration | JEMH", "1 months", [], 0, []),
        (6, "JIRA Implementation for B2B & eCommerce business", "onlineledstore", "atlassian",
         "Jira & Confluence server custom complex workflow and integration setup for e-commerce SME. Writing groovy scripts to automate the workflows, syncing data between Jira and Confluence. Using ScriptRunner for automation tasks and customize behaviours.",
         "United States", "Jira & Confluence Administator", "Linux | Jira/Confluence Configuration | Jira REST API | Confluence REST API", "3 months", [], 0, []),
        (7, "Migration from Jira Server to Jira Cloud", "upmc", "atlassian",
         "Perform migration client's self-hosted Jira & Confluence to Cloud, without any data loss. The self-hosted Jira instance have 1000+ users and 120+ projects, Confluence have 160+ spaces with over 15GB of attachments.",
         "United States", "Jira Administrator", "Linux | Jira & Confluence Migration & Troubleshooting", "1 month", [], 0, []),
        (8, "Migration from desk.com to Jira Service Desk Cloud", "barcodes", "atlassian",
         "Moving and transform 30k+ tickets from desk.com to Jira issues. Replicate desk.com workflows and transitions on Jira Service Desk. Apply automate mailbox gateway and automation rules follow clients' requirements.",
         "United States", "Jira Administrator", "Linux | Jira Service Desk Migration & Configuration | Python scripting | Jira CLI", "1 month", [], 0, []),
        (9, "Migration from ConnectWise to Jira Service Desk Server", "appnovation", "atlassian",
         "Moving and transform 20k+ tickets from ConnectWise to Jira issues. Implement customize workflows and transitions for different request types, portal settings and configurations. Setting up and configure Tempo Timesheets integrated with JSD.",
         "United States", "Jira Administrator", "Linux | Jira Service Desk Migration & Configuration | Python scripting | ScriptRunner | Tempo Timesheets", "1 month", [], 0, []),
        (10, "MLQPLUS TRUSTED LEADER", "mlq", "native",
         "A practical and interactive learning program designed to equip users with the skills and tools required for effective leadership. Access leadership content, resources and inspiration. Key features include: Learn: complete the Trusted Leader Program - 5 core modules designed by leadership experts covering a wide range of topics including foundations of effective leadership, coaching and communication, transactional leadership skills, transformational leadership skills and emotional intelligence. Interact: learn through a mix of bite-sized information, engaging visuals and interactive content to get the most of out each module. Access tools: access to worksheets, tip sheets and additional resources that can be downloaded right to your device or shared with others. Test your knowledge: track your progress through leadership quizzes and surveys.",
         "Australia", "Developer", "iOS | Android | Mobile Offline | Subscription IAP", "3 months",
         [WEB_CAT, MOBILE], 11,
         [("https://play.google.com/store/apps/details?id=com.mlqplus.trustedleader", ANDROID),
          ("https://itunes.apple.com/us/app/trusted-leader/id1087207561", IOS)]),
        (11, "Okadabooks", "okadabooks", "native techlead",
         "The mobile online bookstore & the marketplace for writer to publish their book onto. Mobile apps are focused on reading experience. System is optimized for high performance & allow publisher controls their books as well.",
         "Okadabooks", "Technical Leader", "iOS Native | Swift | ePub Reader SDK | AES Encryption", "6 months",
         [WEB_CAT, MOBILE], 5,
         [("https://www.microsoft.com/en-us/store/p/okadabooks/9wzdncrd2dzc", WINDOWS),
          ("https://play.google.com/store/apps/details?id=com.okadabooks&hl=en", ANDROID),
          ("https://itunes.apple.com/us/app/okada-books/id1161393771?mt=8", IOS)]),
        (12, "sim library", "sim", "native techlead",
         "Mobile apps facilitate Singapore Institute of Management on room book management, schedule management, loans & requests management, events management (Workshops | Talks | Activities). The apps connect to various end-points (RESTful | SOAP | Legacy) to utilize large set of data through on Single Sign-On securiy mechanism.",
         "Singapore", "Technical Leader", "iOS Native | SOAP | SSO | Javascript | WordPress", "3 months",
         [WEB_CAT, MOBILE], 8,
         [("https://play.google.com/store/apps/details?id=com.sim.simlibrary", ANDROID),
          ("https://itunes.apple.com/us/app/sim-library/id1140361058", IOS)]),
        (13, "ovvy", "ovvy", "native techlead",
         "Ovvy is the easiest way to find, compare and engage reliable Service Providers. Merchants can also showcase their skills effectively be notified of jobs they are interested in doing.",
         "Singapore", "Technical Leader", "iOS Native | Chat | Socket.IO | Paypal Mobile SDK | Push Notification", "5 months",
         [WEB_CAT, MOBILE], 9,
         [("https://play.google.com/store/apps/details?id=com.app.ovvy", ANDROID),
          ("https://itunes.apple.com/sg/app/ovvy-the-people-marketplace/id1196834481", IOS)]),
        (14, "Billby", "billby", "native techlead",
         "Billby is the world first pocket based bill payment platform, giving you greater control over paying and managing your bills.",
         "Australia", "Technical Leader", "Android | iOS | Amazon | SendGrid Email SDK | QR | PHP/Laravel | MySql", "4 months",
         [WEB_CAT, MOBILE], 13,
         [("http://billby.com.au/", WEB)]),
        (15, "fitaccess", "fitaccess", "native techlead",
         "FitAccess connect clients and trainers to get more traning together instantly. You can be a client who want to be trained and get fit, also be a trainer to provide a class for others.  More than getting in shape, we are connnecting people. Get out of your room and do some training.",
         "Australia", "Technical Leader", "iOS Native | Amazon | Chat XMPP | Stripe SDK | Push Notification", "6 months",
         [WEB_CAT, MOBILE], 10, []),
    ]

    for order, name, tag, filters, description, client, roles, skills, length, categories, screenshots, links in projects_data:
        project = Project.objects.create(
            id=uuid.uuid4(), name=name, tag=tag, filters=filters,
            description=description, client=client, roles=roles, skills=skills,
            length=length, categories_raw=json.dumps(categories),
            screenshots=screenshots, order=order,
        )
        for url, platform in links:
            Link.objects.create(id=uuid.uuid4(), project=project, url=url, platform=platform)


def reverse_seed(apps, schema_editor):
    for model_name in ['Skill', 'Certification', 'Hobby', 'Service', 'SideProject', 'Profile', 'Project']:
        apps.get_model('portfolio_app', model_name).objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_auto_20260724_2311'),
    ]

    operations = [
        migrations.RunPython(seed_portfolio_data, reverse_seed),
    ]
