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
                name="Confluence theme customizations",
                tag="respect",
                filters="atlassian",
                description=
                "Building intranet platform using Confluence, using Refined for customize Confluence and add structure, theme, layout and navigation.",
                client="Australia",
                roles="Confluence Administator",
                skills="Confluence Configuration | Refined for Confluence",
                length="2 months",
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
                name="yukitomo",
                tag="yukitomo",
                filters="native",
                description=
                "Skiers and snowboarders, have you ever experienced getting lost or losing your friends in the mountains? Yukitomo helps you to find and locate your friends in realtime. Never get lost !",
                client="Singapore",
                roles="Technical Leader",
                skills=
                "iOS Native | Google Maps API | Firebase Realtime Chat | Realtime Geocoding",
                length="5 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[
                    Link(
                        "https://itunes.apple.com/us/app/yukitomo/id1072053931?mt=8",
                        Platform.IOS),
                ],
                screenshots=0),
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
                name="abakus",
                tag="abakus",
                filters="native techlead",
                description=
                "A pocket-based financial management tool which stored your personal income and tax expenses along with all the receipts and cost based expenses associated with every property you own, allowing you to see your estimated annual tax return and the financial position of your portfolio at any time throughout the year, at just the touch of a button.",
                client="Australia",
                roles="Technical Leader",
                skills=
                "iOS Native | Offline Caching | Cross-platform subscription IAP",
                length="4 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[
                    Link(
                        "https://play.google.com/store/apps/details?id=com.windorwilgainvestments.abakus",
                        Platform.ANDROID),
                    Link(
                        "https://itunes.apple.com/au/app/abakus/id1129055100?ls=1&mt=8",
                        Platform.IOS),
                ],
                screenshots=0),
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
                name="socialoop",
                tag="socialoop",
                filters="native techlead",
                description=
                "Social network apps connect people together, hosting activities, checkin, hobbies, or just update their mood. All in one.",
                client="Singapore",
                roles="Technical Leader",
                skills=
                "iOS Native | Chat | XMPP Framework | Google Maps SDK | Google Maps API | Push Notification",
                length="5 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[
                    
                ],
                screenshots=9),
            Project(
                name="ATOMS",
                tag="atoms",
                filters="native techlead net",
                description=
                "Are you looking for a way you can do more to help those in need? ATOMs is a modern way to spend time and money on other people. Thanks to this app, you can boost your own happiness by improving the lives of other human beings. Research shows this is much more effective than buying more things for yourself.",
                client="Singapore",
                roles="Technical Leader",
                skills=
                "ASP.NET Web API | Azure | SignalR | Android | iOS | AngularJS | Paypal SDK",
                length="4 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[
                    Link("http://atoms.sg", Platform.WEB),
                    Link(
                        "https://play.google.com/store/apps/details?id=com.alpsnetworks.atoms",
                        Platform.ANDROID),
                    Link(
                        "https://itunes.apple.com/us/app/atoms-sg/id1186676679",
                        Platform.IOS),
                ],
                screenshots=5),
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
            Project(
                name="avb",
                tag="avb",
                filters="native techlead sm net",
                description=
                "Searching for clubs/bars/restaurants around you. See who have checked in and getting around with them instantly.",
                client="New Zealand",
                roles="Scrum Master",
                skills=
                "iOS Native | RxSwift MVVM | Android Native | RxJava | ASP.NET Web API | Google Maps API | SignalR | RealmDB",
                length="3 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[],
                screenshots=0),
            Project(
                name="axcro",
                tag="axcro",
                filters="native techlead sm",
                description=
                "Escrow-based shopping platform to gain consumer confidence whe purchasing service packages that are provided in parts over a period. This product will also serve as an additional platform to increase the sales of service provider by providing an alternative payment guaranteed platform.",
                client="Singapore",
                roles="Scrum Master",
                skills=
                "iOS Native | Android Native | Google Maps API | Google Civic Information API | PHP/Laravel | MySql",
                length="3 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[
                    Link(
                        "https://play.google.com/store/apps/details?id=com.app.axcro",
                        Platform.ANDROID),
                    Link(
                        "https://itunes.apple.com/us/app/axcro/id1369884767?ls=1&mt=8",
                        Platform.IOS),],
                screenshots=10),
            Project(
                name="sayswe",
                tag="multiply",
                filters="native techlead sm",
                description=
                "Voting and plege platform for everyone to join and share their own opinions about the election around the world.",
                client="United States",
                roles="Scrum Master",
                skills=
                "iOS Native | Google Maps API | Stripe | PHP/Laravel | MySql",
                length="3 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[Link("https://itunes.apple.com/us/app/sayswe/id1317229517?ls=1&mt=8",Platform.IOS),
                Link("https://play.google.com/store/apps/details?id=org.sayswe.sayswe",Platform.ANDROID)],
                screenshots=9),
            Project(
                name="tacko",
                tag="tacko",
                filters="native techlead",
                description=
                "Love to travel, but want to make money with benefit ? Tacko gives you many chances to buy and sell your items with other peoples when you are travelling around.",
                client="Singapore",
                roles="Scrum Master",
                skills=
                "iOS Native | RxSwift MVVM | Google Maps API | Stripe | Paypal | PHP/Laravel | MySql",
                length="5 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[],
                screenshots=13),
            Project(
                name="sociasta",
                tag="sociasta",
                filters="native techlead sm",
                description=
                "Sociasta aims to connect people who are having the same activity or feeling the same emotions around the world.",
                client="Pakistan",
                roles="Scrum Master",
                skills=
                "iOS Native | Google Maps API | KML Files | PHP/Laravel | MySql",
                length="3 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[],
                screenshots=8),
            Project(
                name="hellomojo",
                tag="hellomojo",
                filters="native techlead sm net",
                description=
                "Capture Everything. Anywhere. Anytime. Hello Mojo's documenting app will give you that extra peace of mind when you need it most.",
                client="New Zealand",
                roles="Scrum Master | Backend Developer",
                skills=
                "iOS Native | Google Maps API | ASP.Net | Microsoft Azure | .NET WebAPI 2",
                length="2 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[Link("https://hellomojo.com/",Platform.WEB)],
                screenshots=11),
        ]
        return projects

    @staticmethod
    def getSkills():
        skills = [
            Skill(name="Swift", percent="90%"),
            Skill(name="Obj-C", percent="85%"),
            Skill(name="Scripts (Bash/Ruby/Groovy)", percent="80%"),
            Skill(name="C#", percent="80%"),
            Skill(name="Python", percent="75%"),
            Skill(name="Dart-Flutter", percent="60%"),
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
                        time="2011",
                        title=
                        "Microsoft Server 2008 System Administrator - MCITP-SA",
                        subTitle="Nhat Nghe Education JSC",
                        descriptions=[]),
                    ProfileItem(
                        time="2014",
                        title="Best Member of the Year",
                        subTitle="Beesightsoft",
                        descriptions=[]),
                    ProfileItem(
                        time="2015",
                        title="Best Team Leader of the Year",
                        subTitle="Beesightsoft",
                        descriptions=[]),
                    ProfileItem(
                        time="2016",
                        title="Most Active Support of the Year",
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
            ]),
        Profile(
            "work experiences",
            profileItems=[
                ProfileItem(
                    time="Aug '17 - Present",
                    title="Upwork",
                    subTitle="Professional Freelancer",
                    descriptions=[]),
                ProfileItem(
                    time="Aug '19 - Present",
                    title="DinDinn Corporation Pte. Ltd.",
                    subTitle="Software Engineer",
                    descriptions=[]),
                ProfileItem(
                    time="Jun '14 - Jul '18",
                    title="Beesightsoft",
                    subTitle="SCRUM Master | iOS Specialist | .NET Ninja",
                    descriptions=[
                        "- Started as a Junior Developer, work across 20+ outsource projects in Elance/Upwork and other clients",
                        "- Depth knowledge on basic and advanced programming techniques: REST APIs, threading, memory management, DI, Clean Architecture ... ",
                        "- Leverage as an iOS Team Leader, training/coaching/mentoring team member from junior level ",
                        "- Growth and scale up team in both size and quality",
                        "- Task management, planning the development path for team member ",
                        "- Join in technical R&D department to get ahead of new technologies and applying/spreading across team: Functional Reactive Programming... ",
                        "- Collaborate to setup CI/CD pipelines ",
                        "- Being trained as a Scrum Master, in charge and responsible to apply a lightweight Agile process, together with ecosystem of tools & frameworks, to help organization shift from traditional Waterfall to Agile to gain maximize productivity",
                        "- Utilizing Atlassian product line: Jira, Confluence to all of departments: engineering, marketing, operation...."
                    ])
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
                        title="Visual Studio, Xamarin Studio, XCode, Visual Studio Code, Sublime Text",
                        subTitle="",
                        descriptions=[]
                    ),
                    ProfileItem(
                        time="VCS / DVCS",
                        title="SVN, Git Bash, Bitbucket | GitHub | GitLab, Git Flow | GitHub Flow | GitLab Flow, Git Submodule | Subtree",
                        subTitle="",
                        descriptions=[]
                    ),
                    ProfileItem(
                        time="CI & Build Tools",
                        title="Jenkins | Code quality (swiftlint, PEP8) | xcodebuild (iOS), xctest (iOS)",
                        subTitle="",
                        descriptions=[]
                    ),
                    ProfileItem(
                        time="ALM",
                        title="Jira, Confluence, Jira Service Desk, ChatOps (HipChat | Slack)",
                        subTitle="",
                        descriptions=[]
                    ),
                    ProfileItem(
                        time="Framework",
                        title="Xamarin | iOS (Objective-C/Swift) | RxSwift | ASP.NET (MVC/Web API/Core) | Flutter",
                        subTitle="",
                        descriptions=[]
                    ),
                    ProfileItem(
                        time="Architecture",
                        title="OOP/SOLID/DRY | Design Patterns | IoC/Dependency Injection | MVC/MVP/MVVM/Clean Architecture | Functional Reactive Programming",
                        subTitle="",
                        descriptions=[]
                    ),
                    ProfileItem(
                        time="Testing",
                        title="TDD | BDD | iOS Testing frameworks (Quick, Nimble)",
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
                name="Agile Consultant",
                description=
                "Consult, coaching how to steer with Agile best practices, tools, processes: Scrum | Kanban | Scrumban | BDD | TDD | XP",
                image="flaticon-two-thin-arrows-forming-a-circle"),
            Service(
                name="DevOps Consultant",
                description=
                "Architect, design full pipeline of DevOps from ALM (Jira | Git) through CI (Jenkins) to CD (Docker | Configuration Management)",
                image="flaticon-infinite-symbol"),
            Service(
                name="Software Development",
                description=
                "Building clean and robust application using various programming languages: Swift, Objective-C, .NET, Python",
                image="flaticon-computer"),
        ]
        return services