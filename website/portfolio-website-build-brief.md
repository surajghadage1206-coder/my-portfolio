# Portfolio Website — Build Brief for Antigravity

**Subject:** Suraj Dattatray Ghadage — Personal Portfolio Website
**Source of truth:** `Suraj_Ghadage_Resume.pdf` (place this in the same project folder as this file)

---

## ⚠️ Read This Before Building

1. **Contact links mismatch.** The resume's contact block lists `linkedin.com/in/pratik-patil` and `github.com/pratikpat2006-jpg` — these usernames reference a different name ("Pratik Patil") than the resume owner ("Suraj Ghadage"). This is very likely a template leftover or copy-paste error. **Confirm the correct LinkedIn and GitHub URLs before finalizing the Contact/Footer sections** — otherwise the live site will link to what may be someone else's profile. Until corrected, build using the links exactly as given below, and keep them easy to find/replace.
2. **No photo or project screenshots were provided.** Section 10 gives fallback treatments so the build isn't blocked. Swap in real images any time.
3. **No live project demo links or repo URLs were listed.** Never invent a GitHub repo URL. Use the general GitHub profile link for now and mark per-project links with `<!-- TODO: add repo link -->`.

---

## 0. TL;DR for the Agent

Build a single-page, fully responsive, professional portfolio website for **Suraj Dattatray Ghadage**, a Computer Science undergraduate specializing in **Data Analytics & Full-Stack Development**. Use **HTML5 + CSS3 + vanilla JavaScript** — no framework, no build step. Populate **every section in Section 7 with the real content from his resume** — no lorem ipsum, nothing skipped, nothing summarized away. Never invent numbers, percentages, or testimonials that aren't in the resume text. Follow the phased checklist in Section 9, in order, and deploy as a static site.

---

## 1. How to Run This Build in Antigravity

1. Put this file and `Suraj_Ghadage_Resume.pdf` in one project folder, and open that folder in Antigravity.
2. In the **Agent Manager**, start a new task. Set the mode to **Agent-assisted** (recommended) so you can review key decisions as it works — switch to Agent-driven/Autopilot later if you're comfortable letting it run unattended.
3. Because this is a multi-file, multi-section build, ask it to use **Plan Mode** first, e.g.:
   > "Read `portfolio-website-build-brief.md` and `Suraj_Ghadage_Resume.pdf` in this folder. Generate a plan to build the portfolio website described, following the brief exactly."
4. Review the **Plan Artifact** it produces and leave comments on anything you want changed before approving it.
5. Let it execute. Use the **live preview Artifact** to check the site at mobile/tablet/desktop widths as sections come online — leave comments directly on the Artifact to request fixes.
6. Once every box in Section 9 and Section 11 is checked, ask it to prepare the project for deployment (GitHub Pages or Netlify).

---

## 2. Project Objective

Build a **professional, modern, recruiter-ready portfolio website** that:
- Establishes Suraj's credibility as a Data Analytics + Software Development candidate.
- Clearly communicates his technical range across programming, BI tooling, and databases.
- Showcases his three key projects with real outcomes, not just a tech-stack list.
- Makes it effortless for a recruiter or collaborator to view his resume or contact him.


---

## 3. Audience & Goals

**Primary audience:** Recruiters and hiring managers for internships or junior Data Analyst / Software Developer roles. **Secondary audience:** professors, collaborators, potential freelance clients.

**Primary calls-to-action, in priority order:**
1. Download resume (PDF)
2. View GitHub profile
3. Contact via email or contact form

---

## 4. Tech Stack

| Layer | Choice | Why |
|---|---|---|
| Structure | HTML5 (semantic tags) | No build step, deploys anywhere, matches his own listed skills |
| Styling | CSS3 (custom properties, Grid + Flexbox) | Full control, no framework bloat, fast load |
| Behavior | Vanilla JavaScript | Mobile nav, scroll effects, form handling — no dependency overhead |
| Fonts | Google Fonts — `Space Grotesk` (headings) + `Inter` (body) | Modern, highly legible, common in tech portfolios |
| Icons | Lucide or Font Awesome (CDN) | Skill tags, contact icons, nav |
| Contact form | Formspree (free tier), with a `mailto:` fallback | Working form, zero backend needed |
| Hosting | GitHub Pages (ties directly to his GitHub) or Netlify | Free, simple deploys |

> If a component framework (React/Next.js) is preferred later, the content map in Section 7 still applies — only the execution steps in Section 9 change.

---

## 5. Site Map (single-page, scroll-anchored)

1. Sticky Navigation
2. Hero / Landing
3. About
4. Technical Skills
5. Experience
6. Projects
7. Education
8. Contact
9. Footer

---

## 6. Design System

**Color palette (dark theme):**
```css
:root {
  --bg-primary: #0B0F19;
  --bg-surface: #131826;
  --bg-surface-alt: #1B2233;
  --text-primary: #E8EBF1;
  --text-secondary: #9AA4B8;
  --accent-primary: #3B82F6;    /* blue */
  --accent-secondary: #22D3EE;  /* cyan — data-viz accent */
  --border-subtle: #232B3D;
  --radius-card: 14px;
  --radius-pill: 999px;
}
```

**Typography:** `Space Grotesk` for the hero name and H1–H3 headings; `Inter` for body copy, nav, and buttons.

**Motifs:** a subtle dotted-grid or low-opacity line-chart pattern behind the Hero (nods to "data analytics" without being distracting). Rounded cards, soft shadows, generous whitespace.

**Motion:** fade + slide-up on scroll per section (once, not repeating on every scroll), hover-lift on project/skill cards, animated underline on nav links, smooth-scroll for anchor links.

**Skills as tags/pills**, grouped under the five resume categories (see 7.4) — not a percentage/skill-bar widget, since the resume gives no proficiency numbers and inventing them would misrepresent him.

---

## 7. Content Map — Resume → Website (fill every line below)

> **Content fidelity rule:** every fact, tool, and bullet in this section must appear somewhere on the site. Light rewording for tone (first-person voice, tighter headlines) is fine. Never delete a fact, and never invent a metric, percentage, client name, or testimonial that isn't in the source text.

### 7.1 Identity & Contact → Nav logo, Hero, Footer, Contact section
- **Name:** Suraj Dattatray Ghadage
- **Title / tagline:** Data Analytics • Software Development
- **Location:** Sangli, Maharashtra, India
- **Phone:** +91 9456160255
- **Email:** surajghadage1206@gmail.com
- **LinkedIn:** linkedin.com/in/pratik-patil ⚠️ *(verify — see warning above)*
- **GitHub:** github.com/pratikpat2006-jpg ⚠️ *(verify — see warning above)*

### 7.2 Hero Section
- Headline: his name, large and prominent.
- Subheadline: the tagline above, or a one-line expansion in that same spirit (e.g. *"Turning complex data into decisions — and building the software that gets it there."*) grounded in the Executive Summary below.
- Two buttons: **Download Resume** (links to the PDF copied into `/assets/`) and **Get In Touch** (scrolls to Contact).

### 7.3 About Section
Use this Executive Summary as the source paragraph (may adapt to first person):
> "Analytical and results-driven Computer Science undergraduate specializing in Data Analytics and Full-Stack Software Development. Practical experience utilizing Python, SQL, and Power BI for data pipeline architecture, statistical modeling, and relational database queries. Proven ability in translating complex multi-variate datasets into interactive dashboards and developing robust, maintainable software applications."

Also state: Computer Science undergraduate, expected graduation 2027, based in Sangli, Maharashtra.

### 7.4 Technical Skills Section
Render as five labeled groups of tag pills — include **every** item below, exactly as listed:

- **Programming Languages:** Python, Java, C#, C++, SQL, HTML5, CSS3, JavaScript (Core)
- **Analytics & BI Tools:** Microsoft Power BI, DAX, Advanced Excel (Power Query, Pivot Tables, VLOOKUP), EDA
- **Libraries & Frameworks:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn (Fundamentals)
- **Database Systems:** MySQL, Relational Database Management Systems (RDBMS), SQL Query Optimization
- **Core Competencies:** Statistical Analysis, Data Visualization, Object-Oriented Programming (OOP), Data Structures

### 7.5 Experience Section
**Softspara** — Software & Data Analyst Intern
*Ongoing · Sangli, Maharashtra* — use an "Ongoing" badge instead of an end date.
- Data Transformation & ETL: Clean, normalize, and manipulate enterprise datasets utilizing Python and SQL, reducing data processing errors across regular operational cycles.
- Software Engineering: Assist engineering teams with code development, bug fixing, and module testing using structured programming paradigms.
- Reporting & Insights: Generate periodic analytical summaries and query-driven reports to facilitate data-informed operational decision-making.
- Cross-Functional Collaboration: Actively engage in sprint discussions, requirement analysis, and documentation to deliver software updates on schedule.

### 7.6 Projects Section (3 cards, identical layout, in this order)

**1. Cyber Crime Analytics System** — *Technical Project*
Tags: `Python` `Pandas` `Matplotlib` `SQL`
- Engineered an exploratory data analysis (EDA) pipeline processing extensive cyber incident records to evaluate threat distribution and vector frequency.
- Built comprehensive visual dashboards in Python and Power BI, successfully pinpointing seasonal peaks and key vulnerability sectors.
- Formulated actionable, data-backed preventive strategy models to assist in risk mitigation and pattern recognition.

**2. Statistical Crime Trend & Pattern Modeler** — *Technical Project*
Tags: `Python` `Advanced Excel` `Statistics`
- Conducted rigorous multi-variable statistical analysis on historical crime records (homicide datasets) to detect long-term longitudinal trends.
- Applied statistical hypothesis testing, frequency distributions, and regression indicators to establish correlation between demographics and incident rates.
- Developed clean, high-impact comparative visual reports delivering high-level insights for non-technical stakeholders.

**3. Hospital Billing & Record Management System** — *Academic Project*
Tags: `C++` `File Handling`
- Architected an interactive console-based system with CRUD operations for automated billing, patient records, and receipt generation.
- Structured object-oriented architectures to ensure modularity, memory efficiency, and accurate numerical billing calculations.

Each card needs: title, type badge (Technical/Academic Project), tag pills, full bullet list, and a "View on GitHub" link using `github.com/pratikpat2006-jpg` (pending verification) until real per-repo links are supplied.

### 7.7 Education Section
- **Bachelor of Computer Science (BCS)** — *Expected 2027*
- Willingdon College, Sangli
- Affiliated to Shivaji University, Kolhapur

### 7.8 Contact Section
- Email, phone, and location repeated with icons.
- LinkedIn and GitHub buttons (same verification flag as 7.1).
- Contact form: Name, Email, Message → Formspree endpoint (fallback: `mailto:surajghadage1206@gmail.com`).
- Resume download button again (same file as Hero).

### 7.9 Footer
- Name + tagline, short copyright line (`© 2026 Suraj Dattatray Ghadage`), and repeated social icons (LinkedIn, GitHub, Email).

---

## 8. Functional & Non-Functional Requirements

- [ ] Fully responsive — test at ~375px, ~768px, ~1024px, ~1440px widths
- [ ] Semantic HTML (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) for accessibility & SEO
- [ ] All images have `alt` text; color contrast meets WCAG AA; site is keyboard-navigable
- [ ] `<title>`, meta description, Open Graph tags, and a simple favicon (e.g. an "SG" monogram)
- [ ] Fast load: no heavy frameworks, compressed images, minified CSS/JS for production
- [ ] Sticky nav with mobile hamburger menu; smooth-scroll anchors; active-link highlighting on scroll
- [ ] Verified in latest Chrome, Firefox, Safari, and Edge

---

## 9. Step-by-Step Build Plan (execute in this order)

### Phase 1 — Setup
- [ ] Create the project structure (tree below)
- [ ] Copy `Suraj_Ghadage_Resume.pdf` into `/assets/`
- [ ] Re-read the resume PDF directly and cross-check every fact against Section 7

```
portfolio-website/
├── index.html
├── /css
│   └── styles.css
├── /js
│   └── script.js
├── /assets
│   ├── /images
│   ├── /icons
│   └── Suraj_Ghadage_Resume.pdf
└── README.md
```

### Phase 2 — HTML Structure
- [ ] Build the semantic skeleton for all 9 sections in Section 5
- [ ] Add `<head>` meta tags, favicon link, Google Fonts link

### Phase 3 — CSS / Design System
- [ ] Add the CSS variables from Section 6 to `:root`
- [ ] Mobile-first responsive layout (Grid/Flexbox), then scale up with breakpoints
- [ ] Style every section per Section 6
- [ ] Add scroll-reveal and hover animations

### Phase 4 — JavaScript Behavior
- [ ] Mobile nav toggle (hamburger ↔ close)
- [ ] Smooth scroll + active-section nav highlighting
- [ ] Scroll-triggered reveal animations (IntersectionObserver)
- [ ] Contact form handling (Formspree fetch with success/error state, or mailto fallback)

### Phase 5 — Content Population
- [ ] Populate **every** section using Section 7 — no placeholder or lorem ipsum text anywhere
- [ ] Double-check: all 5 skill categories, all 4 experience bullets, all 3 projects with all their bullets, and education are present and complete

### Phase 6 — Assets
- [ ] Add favicon; add fallback avatar/illustration per Section 10 if no photo is supplied
- [ ] Wire up both "Download Resume" buttons to `/assets/Suraj_Ghadage_Resume.pdf`
- [ ] Write `README.md`: project description, tech stack, how to run locally, live link

### Phase 7 — QA
- [ ] Test all four breakpoints from Section 8
- [ ] Click every link (LinkedIn, GitHub, email, phone, resume download, form submit) — confirm the two ⚠️-flagged links have been corrected or knowingly left as-is
- [ ] Proofread all copy for typos
- [ ] Run a basic accessibility/contrast pass

### Phase 8 — Deploy
- [ ] Initialize git and push to the GitHub account confirmed in Section 7.1
- [ ] Deploy via GitHub Pages (or Netlify/Vercel) and confirm the live URL loads correctly
- [ ] Do a final click-through on the **live** URL, not just localhost

---

## 10. Asset Fallbacks (nothing here should block the build)

| Missing asset | Fallback treatment |
|---|---|
| Profile photo | Circular gradient monogram avatar using the initials "SG" in the accent colors |
| Project screenshots | Icon-based thumbnail per project (e.g. a shield/chart icon for the crime-analytics projects, a receipt/database icon for the billing system) on a subtle gradient card |
| Live project demo links | Omit the "Live Demo" button entirely for that card rather than link to nothing |
| Company logo (Softspara) | Text-based initial badge in the experience card |

---

## 11. Definition of Done

- [ ] Every item in Sections 7.1–7.9 appears on the live site, verbatim or lightly reworded, with nothing omitted
- [ ] Site is fully responsive with no layout breaks at any breakpoint
- [ ] All navigation, social, and download links work
- [ ] No lorem ipsum and no unaddressed placeholder images (fallbacks from Section 10 applied where needed)
- [ ] Passes a basic Lighthouse check for performance and accessibility
- [ ] Deployed to a public URL

---

*This brief is generated from `Suraj_Ghadage_Resume.pdf`. If the resume changes, update Section 7 to match before re-running the build.*
