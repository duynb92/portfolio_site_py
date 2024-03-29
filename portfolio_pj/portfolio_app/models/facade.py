from .project import *
from .skill import *
from .profile import *
from .service import *
from .hobby import *


class Facade:
    @staticmethod
    def getProjects():
        projects = [
            Project(
                name="HubSpot Blog Content Management Toolbox",
                tag="zapier",
                filters="custom-integration",
                description=
                "Streamline content marketing with a Zapier custom app connecting Jira, Confluence, and HubSpot. Effortlessly create and manage marketing materials, empowering companies and individuals to maximize productivity.",
                client="NA",
                roles="Zapier Platform",
                skills="Javascript",
                length="2 weeks",
                categories=[],
                links=[],
                screenshots=0),
            Project(
                name="HubSpot Social Content Management Toolbox",
                tag="zapier",
                filters="custom-integration",
                description=
                "Boost social media marketing efficiency with a Zapier custom app linking Jira, HubSpot. Streamline content creation and management, empowering companies and individuals to maximize their social media presence effortlessly.",
                client="NA",
                roles="Zapier Platform",
                skills="Javascript",
                length="2 weeks",
                categories=[],
                links=[],
                screenshots=0),
            Project(
                name="Timesheet & payroll system",
                tag="zapier",
                filters="custom-integration",
                description=
                "Simplify your payroll management with a custom integration built in Zapier. Effortlessly retrieve timesheets from Upwork, transform and store data in Google Sheets as a powerful database. Seamlessly generate invoices in QuickBooks using the integrated database, streamlining your time tracking and invoicing process.",
                client="NA",
                roles="Zapier Platform",
                skills="Javascript",
                length="1 month",
                categories=[],
                links=[],
                screenshots=0),
            Project(
                name="Jira/JSD/Confluence Administration tasks",
                tag="jarvisanalytics",
                filters="atlassian",
                description=
                "Jira/JSD Cloud cleanup, setting up JSD workflows. Create dashboards and reports on Jira. Create custom templates for meeting notes, client reports.",
                client="United States",
                roles="Jira & Confluence Administator",
                skills="Jira/JSD/Confluence Configuration | Jira REST API | Confluence REST API",
                length="3 months",
                categories=[],
                links=[],
                screenshots=0),
            Project(
                name="JEMH Cloud Configurations",
                tag="casupport",
                filters="atlassian",
                description=
                "Basic and advanced configurations for Enterprise Mail Handler for Jira (JEMH) on Jira Service Desk to customize email template, like adding actions, automate workflows, approve/decline requests.",
                client="United States",
                roles="JSD Administator",
                skills="JSD Configuration | JEMH",
                length="1 months",
                categories=[],
                links=[],
                screenshots=0),
            Project(
                name="JIRA Implementation for B2B & eCommerce business",
                tag="onlineledstore",
                filters="atlassian",
                description=
                "Jira & Confluence server custom complex workflow and integration setup for e-commerce SME. Writing groovy scripts to automate the workflows, syncing data between Jira and Confluence. Using ScriptRunner for automation tasks and customize behaviours.",
                client="United States",
                roles="Jira & Confluence Administator",
                skills="Linux | Jira/Confluence Configuration | Jira REST API | Confluence REST API",
                length="3 months",
                categories=[],
                links=[],
                screenshots=0),
            Project(
                name="Migration from Jira Server to Jira Cloud",
                tag="upmc",
                filters="atlassian",
                description=
                "Perform migration client's self-hosted Jira & Confluence to Cloud, without any data loss. The self-hosted Jira instance have 1000+ users and 120+ projects, Confluence have 160+ spaces with over 15GB of attachments.",
                client="United States",
                roles="Jira Administrator",
                skills="Linux | Jira & Confluence Migration & Troubleshooting",
                length="1 month",
                categories=[],
                links=[],
                screenshots=0),
            Project(
                name="Migration from desk.com to Jira Service Desk Cloud",
                tag="barcodes",
                filters="atlassian",
                description=
                "Moving and transform 30k+ tickets from desk.com to Jira issues. Replicate desk.com workflows and transitions on Jira Service Desk. Apply automate mailbox gateway and automation rules follow clients' requirements.",
                client="United States",
                roles="Jira Administrator",
                skills="Linux | Jira Service Desk Migration & Configuration | Python scripting | Jira CLI",
                length="1 month",
                categories=[],
                links=[],
                screenshots=0),
            Project(
                name="Migration from ConnectWise to Jira Service Desk Server",
                tag="appnovation",
                filters="atlassian",
                description=
                "Moving and transform 20k+ tickets from ConnectWise to Jira issues. Implement customize workflows and transitions for different request types, portal settings and configurations. Setting up and configure Tempo Timesheets integrated with JSD.",
                client="United States",
                roles="Jira Administrator",
                skills="Linux | Jira Service Desk Migration & Configuration | Python scripting | ScriptRunner | Tempo Timesheets",
                length="1 month",
                categories=[],
                links=[],
                screenshots=0),
            Project(
                name="MLQPLUS TRUSTED LEADER",
                tag="mlq",
                filters="native",
                description=
                "A practical and interactive learning program designed to equip users with the skills and tools required for effective leadership. Access leadership content, resources and inspiration. Key features include: Learn: complete the Trusted Leader Program - 5 core modules designed by leadership experts covering a wide range of topics including foundations of effective leadership, coaching and communication, transactional leadership skills, transformational leadership skills and emotional intelligence. Interact: learn through a mix of bite-sized information, engaging visuals and interactive content to get the most of out each module. Access tools: access to worksheets, tip sheets and additional resources that can be downloaded right to your device or shared with others. Test your knowledge: track your progress through leadership quizzes and surveys.",
                client="Australia",
                roles="Developer",
                skills="iOS | Android | Mobile Offline | Subscription IAP",
                length="3 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[
                    Link(
                        "https://play.google.com/store/apps/details?id=com.mlqplus.trustedleader",
                        Platform.ANDROID),
                    Link(
                        "https://itunes.apple.com/us/app/trusted-leader/id1087207561",
                        Platform.IOS),
                ],
                screenshots=11),
            Project(
                name="Okadabooks",
                tag="okadabooks",
                filters="native techlead",
                description=
                "The mobile online bookstore & the marketplace for writer to publish their book onto. Mobile apps are focused on reading experience. System is optimized for high performance & allow publisher controls their books as well.",
                client="Okadabooks",
                roles="Technical Leader",
                skills="iOS Native | Swift | ePub Reader SDK | AES Encryption",
                length="6 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[
                    Link(
                        "https://www.microsoft.com/en-us/store/p/okadabooks/9wzdncrd2dzc",
                        Platform.WINDOWS),
                    Link(
                        "https://play.google.com/store/apps/details?id=com.okadabooks&hl=en",
                        Platform.ANDROID),
                    Link(
                        "https://itunes.apple.com/us/app/okada-books/id1161393771?mt=8",
                        Platform.IOS),
                ],
                screenshots=5),
            Project(
                name="sim library",
                tag="sim",
                filters="native techlead",
                description=
                "Mobile apps facilitate Singapore Institute of Management on room book management, schedule management, loans & requests management, events management (Workshops | Talks | Activities). The apps connect to various end-points (RESTful | SOAP | Legacy) to utilize large set of data through on Single Sign-On securiy mechanism.",
                client="Singapore",
                roles="Technical Leader",
                skills="iOS Native | SOAP | SSO | Javascript | WordPress",
                length="3 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[
                    Link(
                        "https://play.google.com/store/apps/details?id=com.sim.simlibrary",
                        Platform.ANDROID),
                    Link(
                        "https://itunes.apple.com/us/app/sim-library/id1140361058",
                        Platform.IOS),
                ],
                screenshots=8
                ),
            Project(
                name="ovvy",
                tag="ovvy",
                filters="native techlead",
                description=
                "Ovvy is the easiest way to find, compare and engage reliable Service Providers. Merchants can also showcase their skills effectively be notified of jobs they are interested in doing.",
                client="Singapore",
                roles="Technical Leader",
                skills=
                "iOS Native | Chat | Socket.IO | Paypal Mobile SDK | Push Notification",
                length="5 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[
                    Link(
                        "https://play.google.com/store/apps/details?id=com.app.ovvy",
                        Platform.ANDROID),
                    Link(
                        "https://itunes.apple.com/sg/app/ovvy-the-people-marketplace/id1196834481",
                        Platform.IOS),
                ],
                screenshots=9),
            Project(
                name="Billby",
                tag="billby",
                filters="native techlead",
                description=
                "Billby is the world first pocket based bill payment platform, giving you greater control over paying and managing your bills.",
                client="Australia",
                roles="Technical Leader",
                skills=
                "Android | iOS | Amazon | SendGrid Email SDK | QR | PHP/Laravel | MySql",
                length="4 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[Link("http://billby.com.au/", Platform.WEB)],
                screenshots=13),
            Project(
                name="fitaccess",
                tag="fitaccess",
                filters="native techlead",
                description=
                "FitAccess connect clients and trainers to get more traning together instantly. You can be a client who want to be trained and get fit, also be a trainer to provide a class for others.  More than getting in shape, we are connnecting people. Get out of your room and do some training.",
                client="Australia",
                roles="Technical Leader",
                skills=
                "iOS Native | Amazon | Chat XMPP | Stripe SDK | Push Notification",
                length="6 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[],
                screenshots=10),
        ]
        return projects

    @staticmethod
    def getSkills():
        skills = [
            Skill(name="Swift", percent="90%"),
            Skill(name="Obj-C", percent="85%"),
            Skill(name="Scripting (Bash/Ruby/Groovy)", percent="80%"),
            Skill(name="Python", percent="75%"),
            Skill(name="Javascript", percent="60%")
        ]
        return skills

    @staticmethod
    def getProfiles():
        profiles = [
            Profile(
                "education",
                profileItems=[
                    ProfileItem(
                        time="2010-2015",
                        title=
                        "University of Information Technology - Vietnam National University HCMC",
                        subTitle="Bachelor of Engineering",
                        descriptions=[])
                ]),
            Profile(
                "certificates",
                profileItems=[
                    ProfileItem(
                        time="2014 - 2015 - 2016",
                        title="Best Member of the Year | Best Team Leader of the Year | Most Active Support of the Year",
                        subTitle="Beesightsoft",
                        descriptions=[]),
                    ProfileItem(
                        time="2017",
                        title="PSM I | Professional Scrum Master I",
                        subTitle="Scrum.org",
                        descriptions=[
                            "Demonstrated a fundamental level of Scrum mastery, proving an understanding of Scrum as described in the Scrum Guide and the concepts of applying Scrum."
                        ]),
                    ProfileItem(
                        time="2017",
                        title="CSPO | CERTIFIED Scrum Product Owner",
                        subTitle="ScrumAlliance.org",
                        descriptions=[
                            "Learn the foundation of Scrum and the scope of the Certified Scrum Product Owner's role from the best minds in Scrum.",
                            "Demonstrate to employers and peers your attainment of core Scrum knowledge.",
                            "Expand your career opportunities by staying relevant and marketable across all industry sectors adopting Agile practices.",
                            "Engage with a community of recognized Scrum experts who are committed to continuous improvement."
                        ]),
                    ProfileItem(
                        time="2018",
                        title="ACP-JSW | ACP-300 | Atlassian Certified in Agile Development with Jira Software",
                        subTitle="Atlassian.com",
                        descriptions=["The Agile Development with Jira Software (ACP-JSW) credential builds on the professional's existing agile skills, with a focus on optimizing the power of Jira Software for their development teams. This credential is for scrum masters, project leads and board administrators."]),
                    ProfileItem(
                        time="2018",
                        title="AC-JPA | ACP-600 | Atlassian Certified in Jira Project Administration",
                        subTitle="Atlassian.com",
                        descriptions=["Capable Project Administrators are essential to the optimal functioning of Jira Software in large organizations. Certified Jira Project Administrators are the power users who know how to configure projects and boards, customize workflows and manage project permissions in their organization's Jira Server or Data Center instance. They live in Jira day-to-day, and can help scale their instance to meet the demand of their business, so their Jira Administrator and teams can get more work done."]),
                    ProfileItem(
                        time="2019",
                        title="ACP-JSD | ACP-400 | Atlassian Certified Jira Service Desk Administrator",
                        subTitle="Atlassian.com",
                        descriptions=["The Atlassian Certified Professional Jira Service Desk Administrator (ACP-JSD) manages, customizes, and configures Jira Service Desk. Certification in Jira Service Desk Administration covers the skills needed to set up and optimize Jira Service Desk for any service management team."]),
                    ProfileItem(
                        time="2019",
                        title="ACP-JA | ACP-100 | Atlassian Certified Jira Administrator",
                        subTitle="Atlassian.com",
                        descriptions=["The Atlassian Certified Professional Jira Administrator (ACP-JA) manages, customizes, and configures Jira from within the Jira user interface, while ensuring the performance, scalability and day-to-day manageability of the product. The ACP-JA has proven skills needed to optimize Jira for any development or business team."]),
                    ProfileItem(
                        time="2020",
                        title="ACP-MJCP | ACP-620 | Atlassian Certified in Managing Jira Cloud Projects",
                        subTitle="Atlassian.com",
                        descriptions=["The Managing Jira Cloud Projects Certification builds on the professional's existing agile skills, with a focus on optimizing the power of Jira Software for their development teams. This credential is for scrum masters, project administrators, project leads and board administrators who can configure and automate Jira Software Scrum and Kanban projects for classic and next-gen."]),
                    ProfileItem(
                        time="2020",
                        title="ACP-JCA | ACP-120 | Atlassian Certified Jira Administrator for Cloud",
                        subTitle="Atlassian.com",
                        descriptions=["The Atlassian Certified Professional Jira Administrator (ACP-JA) manages, customizes, and configures Jira from within the Jira user interface, while ensuring the performance, scalability and day-to-day manageability of the product. The ACP-JA has proven skills needed to optimize Jira for any development or business team."]),
                    ProfileItem(
                        time="2020",
                        title="JCP | ASB-153 | Atlassian Skills Badge: Configuring and Troubleshooting Permissions in Jira",
                        subTitle="Atlassian.com",
                        descriptions=["The Badge holder has extended their Jira skills by attending an Atlassian Skillbuilder course and passing an online quiz on Configuring and Troubleshooting Permissions in Jira."]),
                    ProfileItem(
                        time="2020",
                        title="ACM | Atlassian Certified Master",
                        subTitle="Atlassian.com",
                        descriptions=["ACM is Atlassian's most prestigious Certification. Atlassian Certified Masters hold at least four Atlassian Certified Professional-level credentials, demonstrating their expertise across multiple Atlassian products."]),
                    ProfileItem(
                        time="2022",
                        title="ACP-MJSP | ACP-420 | Atlassian Certified Jira Service Project Manager",
                        subTitle="Atlassian.com",
                        descriptions=["Certification in Managing Jira Service Projects for Cloud (ACP-MJSP) showcases those who can interpret and translate business requirements into service project configurations. They are experts in features specific to service projects, including request types, queues and SLAs. They manage permissions and notifications for customers and agents, and optimize customer experience through portal configurations and knowledge base design. They streamline the team's work using automation, dashboards and reports."]),
                    ProfileItem(
                        time="2022",
                        title="ITIL 4 ® Foundation",
                        subTitle="Axelos",
                        descriptions=["ITIL® 4 Foundation demonstrates this individual understands the key concepts of IT and digital service delivery including the key concepts, guiding principles and practices of ITIL® 4 for service management. They have a fundamental understanding of the modern organisation’s end-to-end operating model for the creation, delivery and continual improvement of technology-enabled products and services. They have an awareness of how cultural or behavioural principles benefits the wider organisation."]),
                    ProfileItem(
                        time="2022",
                        title="TIL® 4 Specialist - Create, Deliver and Support",
                        subTitle="Axelos",
                        descriptions=["ITIL 4 ® Specialist Create, Deliver and Support demonstrates this individual has an understanding and skills on how to plan, build and integrate different value streams and activities to create, deliver and support IT and digitally-enabled products and services, and relevant practices, methods and tools. They demonstrate sufficient understanding and application of ITIL 4 practices to the creation, delivery and support across support services, the service value systems and value streams."]),
            ]),
        Profile(
            "work experiences",
            profileItems=[
                #ProfileItem(
                #    time="Aug '17 - Present",
                #    title="Upwork",
                #    subTitle="Professional Freelancer",
                #    descriptions=[]),
                #ProfileItem(
                #    time="May '21 - Present",
                #   title="EleganceGroup | Atlassian Gold Solution Partner",
                #   subTitle="Senior Atlassian Architect",
                #   descriptions=[]),
                ProfileItem(
                    time="Jan '21 - Present",
                    title="foodpanda | Delivery Hero APAC Pte. Ltd",
                    subTitle="Senior Software Engineer",
                    descriptions=[]),
                #ProfileItem(
                #    time="May '21 - Sep '21",
                #    title="Appnovation HK | Atlassian Gold Solution Partner",
                #    subTitle="Atlassian Developer",
                #    descriptions=[]),
                ProfileItem(
                    time="Aug '19 - Nov '20",
                    title="DinDinn Corporation Pte. Ltd",
                    subTitle="Software Engineer",
                    descriptions=[]),
                ProfileItem(
                    time="Jul '18 - Jul '19",
                    title="Upwork",
                    subTitle="Professional Freelancer",
                    descriptions=[]),
                ProfileItem(
                    time="Jun '14 - Jul '18",
                    title="Beesightsoft",
                    subTitle="SCRUM Master | iOS Specialist | .NET Ninja",
                    descriptions=[])
            ]),
            Profile(
                "PROFESSIONAL SKILLS",
                profileItems=[
                    ProfileItem(
                        time="Database",
                        title="SQL Server, Postgresql, MySql, Sqlite, Realm",
                        subTitle="",
                        descriptions=[]
                    ),
                    ProfileItem(
                        time="IDE & Tools",
                        title="XCode, Visual Studio Code",
                        subTitle="",
                        descriptions=[]
                    ),
                    ProfileItem(
                        time="VCS / DVCS",
                        title="Bitbucket | GitHub | GitLab",
                        subTitle="",
                        descriptions=[]
                    ),
                    ProfileItem(
                        time="CI & Build Tools",
                        title="Jenkins | Bitrise | TravisCI, Code quality (swiftlint), xcodebuild (iOS), xctest (iOS)",
                        subTitle="",
                        descriptions=[]
                    ),
                    ProfileItem(
                        time="ALM",
                        title="Jira, Confluence, Jira Service Management",
                        subTitle="",
                        descriptions=[]
                    ),
                    ProfileItem(
                        time="Framework & Dependency Manager",
                        title="RxSwift, GoogleMap, GoogleAnalytics, CocoaPods | Carthage",
                        subTitle="",
                        descriptions=[]
                    ),
                    ProfileItem(
                        time="Architecture",
                        title="OOP/SOLID/DRY, Design Patterns, IoC/Dependency Injection, MVC/MVP/MVVM/Clean Architecture, Functional Reactive Programming",
                        subTitle="",
                        descriptions=[]
                    ),
                    ProfileItem(
                        time="Testing",
                        title="TDD | BDD, iOS Testing frameworks (Quick, Nimble)",
                        subTitle="",
                        descriptions=[]
                    ),
                ]
            )
            ]
        return profiles

    @staticmethod
    def getHobbies():
        hobbies = [
            Hobby(
                name="Reading",
                quote="'Books are a uniquely portable magic'",
                author="Stephen King, On Writing: A Memoir of the Craft",
                image="flaticon-open-book"),
            Hobby(
                name="Guitar",
                quote="'I like to be quiet and play guitar and just chill.'",
                author="Post Malone",
                image="flaticon-acoustic-guitar"),
            Hobby(
                name="Travelling",
                quote=
                "'The world is a book, and those who do not travel read only a page.'",
                author="Saint Augustine",
                image="flaticon-aeroplane"),
            Hobby(
                name="Swimming",
                quote=
                "'The man who is swimming against the stream knows the strength of it.'",
                author="Woodrow Wilson",
                image="flaticon-swimmer"),
            Hobby(
                name="Gym",
                quote="'No pain, no gain'",
                author="Ben Franklin",
                image="flaticon-weightlifting"),
            Hobby(
                name="Soccer",
                quote="'Soccer is a magical game'",
                author="David Beckham",
                image="flaticon-soccer-ball-variant")
        ]
        return hobbies

    @staticmethod
    def getServices():
        services = [
            Service(
                name="Atlassian Consultant",
                description=
                "Consult and helping businesses optimize their usage of Atlassian tools",
                image="flaticon-two-thin-arrows-forming-a-circle"),
            Service(
                name="DevOps Consultant",
                description=
                "Architect, design full pipeline of DevOps from ALM (Jira | Git) through CI (Jenkins) to CD (Docker | Configuration Management)",
                image="flaticon-infinite-symbol"),
            Service(
                name="Software Development",
                description=
                "Building clean and robust applications leveraging cutting-edge technologies: Swift, Objective-C, Python, Zapier",
                image="flaticon-computer"),
        ]
        return services