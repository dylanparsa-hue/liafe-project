from django.core.management.base import BaseCommand
from core.models import SiteSetting, HomepageSection, ValuePillar, HeroSlide
from services.models import Service, ServiceFeature, CourseCategory, ResearchCategory, ResearchProject
from publications.models import Publication
from messages_app.models import ContactPage


class Command(BaseCommand):
    help = 'Seed the database with initial LIAFE content (idempotent)'

    def handle(self, *args, **options):
        self.seed_site_settings()
        self.seed_hero_slides()
        self.seed_homepage_sections()
        self.seed_value_pillars()
        self.seed_services()
        self.seed_shariah_features()
        self.seed_academy_delivery_modes()
        self.seed_research_values()
        self.seed_course_categories()
        self.seed_research_categories()
        self.seed_research_projects()
        self.seed_publications()
        self.seed_contact_page()
        self.stdout.write(self.style.SUCCESS('✓ Seed complete'))

    # ── Hero Slides ────────────────────────────────────────────
    def seed_hero_slides(self):
        slides = [
            (
                'London International Academy for Excellence',
                'Shariah Advisory · Academy · Research & Development · Publications',
                'A consultancy dedicated to empowering growth through professional training, impactful publications, strategic research, and expert Shariah advisory.',
                'Consult Us', '/contact/', 'Explore Services', '#services', 0,
            ),
            (
                'Expert Shariah Advisory',
                'Independent compliance, structuring, and audit for ethical finance.',
                'We deliver rigorous Shariah advisory services to financial institutions across the UK, MENA, and Asia — grounded in classical scholarship and modern practice.',
                'Learn More', '/services/shariah-advisory/', 'Our Services', '#services', 1,
            ),
            (
                'Executive Education & Training',
                'Programmes built for the modern finance practitioner.',
                'The LIAFE Academy offers structured executive education — from online courses to in-person masterclasses — designed to develop the next generation of Islamic finance professionals.',
                'View Courses', '/services/academy/', 'Contact Us', '/contact/', 2,
            ),
        ]
        for (title, subtitle, desc, b1t, b1l, b2t, b2l, order) in slides:
            obj, created = HeroSlide.objects.update_or_create(
                title=title,
                defaults=dict(subtitle=subtitle, description=desc,
                              button_1_text=b1t, button_1_link=b1l,
                              button_2_text=b2t, button_2_link=b2l,
                              order=order, is_active=True)
            )
            self.stdout.write(f'  {"Created" if created else "Updated"} HeroSlide: {title[:50]}')

    # ── Site Settings ──────────────────────────────────────────
    def seed_site_settings(self):
        obj, created = SiteSetting.objects.get_or_create(pk=1)
        if created:
            obj.company_name  = 'London International Academy for Excellence'
            obj.short_name    = 'LIAFE'
            obj.tagline       = 'Empowering growth through knowledge, innovation and integrity.'
            obj.phone         = '+44 207 354 33 55'
            obj.email         = 'info@ukliafe.com'
            obj.address       = 'London, N4 2DN'
            obj.working_hours = '9 AM – 5 PM'
            obj.footer_text   = 'A consultancy dedicated to empowering growth through Shariah advisory, education, research, and publication.'
            obj.copyright_text = '© 2025 London International Academy for Excellence. All rights reserved.'
            obj.save()
            self.stdout.write('  Created SiteSetting')
        else:
            self.stdout.write('  SiteSetting exists — skipped')

    # ── Homepage Sections ───────────────────────────────────────
    def seed_homepage_sections(self):
        sections = [
            ('hero', 'London International Academy for Excellence',
             'Shariah Advisory – Academy – Research & Development – Publications',
             'The London International Academy for Excellence is a consultancy dedicated to empowering growth through professional training, impactful publications, strategic research, and expert Shariah advisory.',
             'Consult Us', '/contact/'),
            ('about', 'A consultancy where knowledge, innovation and integrity meet.',
             '', 'The London International Academy for Excellence (LIAFE) is a consultancy dedicated to empowering growth through four core services: professional training through the Academy, impactful publications, strategic research, and expert Shariah advisory. We blend knowledge, innovation, and integrity to deliver solutions that matter.', '', ''),
            ('core_services', 'Four practices, one standard of excellence.',
             'Every engagement draws on the full strength of LIAFE — advisory, education, research, and publication working in concert.', '', '', ''),
            ('why_choose_us', 'Six principles that govern everything we deliver.',
             '', 'From Shariah advisory to executive education, our work is shaped by a single set of principles. They are how we hire, how we engage, and how we measure ourselves.', '', ''),
            ('approach', 'Faith. Finance. Evidence. Working together.',
             '', 'We sit at the intersection of classical scholarship and modern finance. Our engagements start with the client\'s commercial and regulatory reality and end with structures that are defensible, transparent, and durable.', 'Start a conversation', '/contact/'),
            ('cta', 'Ready to work with LIAFE?', '', '', 'Contact Us', '/contact/'),
        ]
        for i, (name, title, subtitle, desc, btn_text, btn_link) in enumerate(sections):
            obj, created = HomepageSection.objects.update_or_create(
                section_name=name,
                defaults=dict(title=title, subtitle=subtitle, description=desc,
                              button_text=btn_text, button_link=btn_link,
                              is_active=True, order=i)
            )
            status = 'Created' if created else 'Updated'
            self.stdout.write(f'  {status} HomepageSection: {name}')

    # ── Value Pillars ───────────────────────────────────────────
    def seed_value_pillars(self):
        pillars = [
            ('Knowledge',       'Knowledge',  'A foundation of rigorous scholarship and applied expertise in finance, law, and ethics.'),
            ('Innovation',      'Innovation', 'Modern frameworks for emerging fintech, digital finance, and inclusive economic systems.'),
            ('Integrity',       'Integrity',  'Independent counsel and uncompromising standards across every engagement.'),
            ('Excellence',      'Excellence', 'Delivery measured against the highest professional and academic benchmarks.'),
            ('Ethical Solutions','Ethical',   'Outcomes designed to be transparent, defensible, and aligned with Shariah principles.'),
            ('Global Impact',   'Global',     'A London base, a worldwide reach — partnerships across the UK, MENA, and Asia.'),
        ]
        for i, (title, icon, desc) in enumerate(pillars):
            obj, created = ValuePillar.objects.update_or_create(
                title=title,
                defaults=dict(description=desc, icon_class=icon, is_active=True, order=i)
            )
            self.stdout.write(f'  {"Created" if created else "Updated"} ValuePillar: {title}')

    # ── Services ────────────────────────────────────────────────
    def seed_services(self):
        services = [
            ('shariah-advisory', 'Shariah Advisory', 'Shariah Advisory',
             'Independent Shariah advisory, structuring, and audit for ethical, compliant finance.',
             'Shariah', 'Ensuring Compliance, Building Trust',
             'LIAFE provides expert Shariah advisory services to help businesses grow ethically, transparently, and in harmony with Shariah principles.',
             0),
            ('academy', 'Academy', 'Academy',
             'Executive education, structured training, and online learning for finance professionals.',
             'Academy', 'Professional Training for the Modern Finance Practitioner',
             'The Academy is LIAFE\'s education wing, offering executive and structured professional training both in-person and online.',
             1),
            ('research-house', 'Research House', 'Research House',
             'Dedicated R&D in Islamic finance, social sciences, and fintech.',
             'Research', 'Dedicated R&D in Islamic Finance, Social Sciences, and Fintech',
             'LIAFE Research Centre specialises in research and development for social sciences, fintech, Islamic finance, and Shariah studies.',
             2),
            ('publication', 'Publication', 'Publication',
             'Books, articles, journal papers, and thought leadership that turn insight into impact.',
             'Publication', 'Research, Insights, and Global Perspectives',
             'LIAFE publications turn insight into impact. Our books and articles bring knowledge to life, offering ideas that inspire growth, ethics, and innovation.',
             3),
        ]
        for (slug, title, menu, short, icon, hero_title, hero_desc, order) in services:
            obj, created = Service.objects.update_or_create(
                slug=slug,
                defaults=dict(title=title, menu_title=menu, short_description=short,
                              icon_class=icon, hero_title=hero_title, hero_description=hero_desc,
                              cta_title=f'Ready to learn more about {title}?',
                              cta_button_text='Get in Touch', cta_button_link='/contact/',
                              is_active=True, order=order)
            )
            self.stdout.write(f'  {"Created" if created else "Updated"} Service: {slug}')

    # ── Shariah Features ────────────────────────────────────────
    def seed_shariah_features(self):
        try:
            shariah = Service.objects.get(slug='shariah-advisory')
        except Service.DoesNotExist:
            return

        process = [
            ('Client Consultation',      'Understanding business model, jurisdictional context, and Shariah objectives before scope.'),
            ('Shariah Review',           'Detailed review of contracts, products, and operational flows against AAOIFI standards.'),
            ('Structuring',              'Designing or restructuring products and instruments to achieve Shariah-compliant outcomes.'),
            ('Shariah Endorsement',      'Formal endorsement from qualified scholars supported by reasoned legal opinion.'),
            ('Documentation Review',     'Legal documentation audited for consistency with the endorsed Shariah structure.'),
            ('Implementation Monitoring','Continuous oversight during launch to ensure operational fidelity to the structure.'),
            ('Shariah Audit',            'Periodic independent audit covering products, transactions, and governance.'),
            ('Reporting & Disclosure',   'Board-ready Shariah reports and public disclosures aligned with governance requirements.'),
        ]
        for i, (title, desc) in enumerate(process):
            obj, created = ServiceFeature.objects.update_or_create(
                service=shariah, title=title, item_type='process',
                defaults=dict(description=desc, is_active=True, order=i)
            )

        cards = [
            ('Shariah Structuring',  'Layers',      'End-to-end product and transaction structuring grounded in classical Islamic jurisprudence.'),
            ('Product Development',  'Stack',       'Designing Sukuk, takaful, Murabaha, Ijarah, and bespoke compliant instruments.'),
            ('Shariah Review',       'Eye',         'Independent review of documents, contracts, and processes for compliance.'),
            ('Compliance Screening', 'CheckCircle', 'Equity, asset, and portfolio screening using leading methodologies.'),
            ('Fatwa Issuance',       'Quote',       'Reasoned legal opinions delivered by qualified Shariah scholars.'),
            ('Documentation',        'Edit',        'Drafting and reviewing Shariah governance, policies, and product documentation.'),
            ('Shariah Audit',        'Search',      'Risk-based audit programmes covering products, transactions, and disclosures.'),
            ('Ongoing Compliance',   'Shariah',     'Continuous monitoring and advisory relationships for sustained alignment.'),
        ]
        for i, (title, icon, desc) in enumerate(cards):
            obj, created = ServiceFeature.objects.update_or_create(
                service=shariah, title=title, item_type='card',
                defaults=dict(description=desc, icon_class=icon, is_active=True, order=i)
            )
        self.stdout.write('  Seeded Shariah features')

    # ── Academy Delivery Modes ──────────────────────────────────
    def seed_academy_delivery_modes(self):
        try:
            academy = Service.objects.get(slug='academy')
        except Service.DoesNotExist:
            return
        modes = [
            ('Online Courses',         'Layers',  'Self-paced and cohort-based programmes via our learning platform.', 0),
            ('Face-to-face Training',  'Users',   'Executive masterclasses and structured cohorts delivered in London.', 1),
            ('Webinars',               'Eye',     'Live and recorded webinars with practitioners and visiting scholars.', 2),
            ('Professional Workshops', 'Stack',   'Short-form intensive sessions on focused practitioner topics.', 3),
        ]
        for (title, icon, desc, order) in modes:
            obj, created = ServiceFeature.objects.update_or_create(
                service=academy, title=title, item_type='delivery',
                defaults=dict(description=desc, icon_class=icon, is_active=True, order=order)
            )
            self.stdout.write(f'  {"Created" if created else "Updated"} Delivery Mode: {title}')

    # ── Research Values ─────────────────────────────────────────
    def seed_research_values(self):
        try:
            research = Service.objects.get(slug='research-house')
        except Service.DoesNotExist:
            return
        values = [
            ('Insightful Research',  'Search',     'Rigorous, evidence-led work that addresses the questions practitioners actually face.', 0),
            ('Innovative Solutions', 'Innovation', 'Frameworks and prototypes that translate research into deployable practice.', 1),
            ('Global Impact',        'Global',     'Industry partnerships and policy briefs that shape outcomes across markets.', 2),
        ]
        for (title, icon, desc, order) in values:
            obj, created = ServiceFeature.objects.update_or_create(
                service=research, title=title, item_type='value',
                defaults=dict(description=desc, icon_class=icon, is_active=True, order=order)
            )
            self.stdout.write(f'  {"Created" if created else "Updated"} Research Value: {title}')

    # ── Course Categories ───────────────────────────────────────
    def seed_course_categories(self):
        cats = [
            ('Islamic Finance', 'Shariah', 'Hybrid', '8 weeks', 'Foundation → Advanced',
             'Foundations to advanced practice: contracts, Sukuk, takaful, banking and capital markets.'),
            ('Fintech & Digital Finance', 'Innovation', 'Online', '6 weeks', 'Intermediate',
             'Digital banking, payments, blockchain, RegTech and the regulation of emerging finance.'),
            ('Research & Policy Development', 'Research', 'Workshop', '4 weeks', 'Practitioner',
             'Methodology, evidence-building, and policy translation for industry and government.'),
            ('Leadership & Professional Development', 'Briefcase', 'In-person', '3 days', 'Executive',
             'Executive leadership programmes for senior practitioners across finance and policy.'),
        ]
        for i, (title, icon, delivery, duration, level, desc) in enumerate(cats):
            obj, created = CourseCategory.objects.update_or_create(
                title=title,
                defaults=dict(description=desc, icon_class=icon, delivery_method=delivery,
                              duration=duration, level=level, button_text='Learn More',
                              is_active=True, order=i)
            )
            self.stdout.write(f'  {"Created" if created else "Updated"} CourseCategory: {title}')

    # ── Research Categories ─────────────────────────────────────
    def seed_research_categories(self):
        cats = [
            ('Islamic Finance & Shariah Studies', 'Shariah',
             'Applied scholarship on contracts, governance, instruments, and Maqasid al-Shariah.'),
            ('Fintech & Digital Innovation', 'Innovation',
             'Emerging technologies in finance: payments, tokenisation, AI, and ethical design.'),
            ('Social & Economic Policy', 'Global',
             'Inclusive finance, sustainable development, and evidence-based policy work.'),
        ]
        for i, (title, icon, desc) in enumerate(cats):
            obj, created = ResearchCategory.objects.update_or_create(
                title=title,
                defaults=dict(description=desc, icon_class=icon, is_active=True, order=i)
            )
            self.stdout.write(f'  {"Created" if created else "Updated"} ResearchCategory: {title}')

    # ── Research Projects ───────────────────────────────────────
    def seed_research_projects(self):
        try:
            cat1 = ResearchCategory.objects.get(title__icontains='Islamic Finance')
            cat2 = ResearchCategory.objects.get(title__icontains='Fintech')
            cat3 = ResearchCategory.objects.get(title__icontains='Social')
        except ResearchCategory.DoesNotExist:
            return

        projects = [
            (cat1, 'Maqasid-Based Product Governance Framework',
             'A governance framework for Islamic financial products grounded in higher objectives of Shariah.',
             'published', 'LIAFE Research', 2025, True),
            (cat2, 'Tokenised Sukuk: Regulatory Landscape',
             'Mapping the regulatory and structural considerations for tokenised Sukuk across UK, UAE, and Malaysia.',
             'published', 'LIAFE & Partners', 2025, True),
            (cat3, 'Inclusive Finance Index — UK Muslim Communities',
             'Empirical assessment of financial inclusion metrics across UK Muslim-majority communities.',
             'in_progress', 'LIAFE Research', 2025, False),
            (cat1, 'AAOIFI Standards Adoption Study',
             'Analysis of adoption rates and implementation challenges of AAOIFI standards across GCC institutions.',
             'published', 'LIAFE Research', 2024, True),
        ]
        for i, (cat, title, desc, status, partner, year, featured) in enumerate(projects):
            obj, created = ResearchProject.objects.update_or_create(
                title=title,
                defaults=dict(category=cat, short_description=desc, research_status=status,
                              client_or_partner=partner, year=year, is_featured=featured,
                              is_active=True, order=i)
            )
            self.stdout.write(f'  {"Created" if created else "Updated"} ResearchProject: {title[:40]}')

    # ── Publications ────────────────────────────────────────────
    def seed_publications(self):
        import datetime
        pubs = [
            ('maqasid-in-modern-finance', 'Maqasid in Modern Finance',
             'book', 'Dr. A. Rahman', 'A practitioner-facing treatment of higher objectives of Shariah applied to contemporary instruments.',
             datetime.date(2025, 3, 1), True),
            ('tokenised-sukuk-framework', 'Tokenised Sukuk: A Framework',
             'report', 'LIAFE Research', 'Regulatory and structural considerations for issuance of compliant tokenised Sukuk in the UK and GCC.',
             datetime.date(2025, 1, 15), True),
            ('ethics-in-digital-banking', 'Ethics in Digital Banking',
             'journal', 'Dr. S. Iqbal', 'Empirical study of consumer-facing ethics in challenger banks and Islamic digital institutions.',
             datetime.date(2024, 11, 1), False),
            ('inclusive-finance-quarterly-q2', 'Inclusive Finance Quarterly · Q2',
             'article', 'LIAFE Editorial', 'Editorial roundup on inclusive finance, central bank digital currencies, and policy signals.',
             datetime.date(2025, 6, 1), False),
            ('governance-for-shariah-boards', 'Governance for Shariah Boards',
             'thought', 'Dr. F. Al-Mansouri', 'A practical, governance-first guide to running an effective and independent Shariah supervisory board.',
             datetime.date(2024, 9, 1), True),
            ('climate-finance-and-maqasid', 'Climate Finance & Maqasid',
             'report', 'LIAFE Research', 'Aligning climate finance instruments with Shariah objectives and ESG reporting standards.',
             datetime.date(2025, 2, 1), False),
        ]
        for i, (slug, title, pub_type, author, desc, pub_date, featured) in enumerate(pubs):
            obj, created = Publication.objects.update_or_create(
                slug=slug,
                defaults=dict(title=title, publication_type=pub_type, author=author,
                              short_description=desc, published_date=pub_date,
                              is_featured=featured, is_active=True, order=i)
            )
            self.stdout.write(f'  {"Created" if created else "Updated"} Publication: {title[:40]}')

    # ── Contact Page ────────────────────────────────────────────
    def seed_contact_page(self):
        obj, created = ContactPage.objects.get_or_create(pk=1)
        if created:
            obj.hero_title = 'Speak with our team.'
            obj.hero_subtitle = 'We work with financial institutions, regulators, academics, and organisations seeking expert Shariah and finance advisory.'
            obj.contact_form_intro = 'Fill in the form and a member of our team will respond within one business day.'
            obj.success_message = 'Thank you — we\'ll be in touch shortly.'
            obj.save()
            self.stdout.write('  Created ContactPage')
        else:
            self.stdout.write('  ContactPage exists — skipped')
