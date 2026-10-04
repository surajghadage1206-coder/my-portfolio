# Build site generator
import os

print("Writing HTML, CSS, JS, and README...")

INDEX_HTML = r"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  
  <!-- Primary Meta Tags -->
  <title>Suraj Dattatray Ghadage | Data Analytics &amp; Software Development</title>
  <meta name="title" content="Suraj Dattatray Ghadage | Data Analytics &amp; Software Development">
  <meta name="description" content="Portfolio of Suraj Dattatray Ghadage — Computer Science undergraduate specializing in Data Analytics, Full-Stack Software Development, Python, SQL, Power BI, and C++.">
  <meta name="keywords" content="Suraj Ghadage, Suraj Dattatray Ghadage, Data Analyst, Software Developer, Python, Power BI, SQL, Portfolio, Sangli, Willingdon College">
  <meta name="author" content="Suraj Dattatray Ghadage">
  <meta name="theme-color" content="#0B0F19">

  <!-- Open Graph / LinkedIn / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://surajghadage.dev/">
  <meta property="og:title" content="Suraj Dattatray Ghadage | Data Analytics &amp; Software Development">
  <meta property="og:description" content="Analytical and results-driven Computer Science undergraduate specializing in Data Analytics and Full-Stack Software Development.">
  <meta property="og:image" content="assets/images/pimage.png">

  <!-- Twitter Meta Tags -->
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:title" content="Suraj Dattatray Ghadage | Data Analytics &amp; Software Development">
  <meta property="twitter:description" content="Portfolio of Suraj Dattatray Ghadage — Data Analytics • Software Development.">
  <meta property="twitter:image" content="assets/images/pimage.png">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="assets/icons/favicon.svg">

  <!-- Google Fonts: Space Grotesk (Headings) + Inter (Body) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;600;700;800&display=swap" rel="stylesheet">

  <!-- Font Awesome 6 CDN for Crisp Vector Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <!-- Custom Stylesheet -->
  <link rel="stylesheet" href="css/styles.css">
</head>
<body class="bg-primary text-primary">

  <!-- Ambient Data Mesh & Glow Background -->
  <div class="bg-ambient" aria-hidden="true">
    <div class="ambient-glow glow-1"></div>
    <div class="ambient-glow glow-2"></div>
    <div class="data-grid-overlay"></div>
  </div>

  <!-- Interactive Floating Toast Container -->
  <div id="toast" class="toast hidden" role="alert" aria-live="assertive"></div>

  <!-- STICKY HEADER & NAVIGATION -->
  <header id="navbar" class="site-header">
    <div class="header-container">
      
      <!-- Brand Logo / Monogram -->
      <a href="#hero" class="brand-logo" aria-label="Suraj Ghadage Portfolio Home">
        <div class="brand-badge">
          <span class="gradient-text">SG</span>
        </div>
        <div class="brand-info">
          <span class="brand-name">Suraj Ghadage</span>
          <span class="brand-tagline">Data &amp; Software Dev</span>
        </div>
      </a>

      <!-- Desktop Nav Links -->
      <nav class="desktop-nav" aria-label="Main Navigation">
        <a href="#about" class="nav-link">About</a>
        <a href="#skills" class="nav-link">Skills</a>
        <a href="#experience" class="nav-link">Experience</a>
        <a href="#projects" class="nav-link">Projects</a>
        <a href="#education" class="nav-link">Education</a>
        <a href="#contact" class="nav-link">Contact</a>
      </nav>

      <!-- Desktop CTA & Resume -->
      <div class="header-actions">
        <a href="assets/Suraj_Ghadage_Resume.pdf" download="Suraj_Ghadage_Resume.pdf" class="btn btn-secondary btn-sm" target="_blank" rel="noopener" aria-label="Download Suraj Ghadage Resume PDF">
          <i class="fa-solid fa-file-arrow-down text-accent-cyan"></i>
          <span>Resume</span>
        </a>
        <a href="#contact" class="btn btn-primary btn-sm">
          <span>Let's Talk</span>
          <i class="fa-solid fa-arrow-right text-xs"></i>
        </a>
      </div>

      <!-- Mobile Menu Hamburger Button -->
      <button id="mobileMenuBtn" class="mobile-toggle-btn" aria-label="Toggle navigation menu" aria-expanded="false">
        <i id="menuIcon" class="fa-solid fa-bars"></i>
      </button>
    </div>

    <!-- Mobile Navigation Drawer -->
    <div id="mobileMenu" class="mobile-menu hidden">
      <nav class="mobile-nav-list" aria-label="Mobile Navigation">
        <a href="#about" class="mobile-nav-link"><i class="fa-regular fa-user"></i> About</a>
        <a href="#skills" class="mobile-nav-link"><i class="fa-solid fa-code"></i> Skills</a>
        <a href="#experience" class="mobile-nav-link"><i class="fa-solid fa-briefcase"></i> Experience</a>
        <a href="#projects" class="mobile-nav-link"><i class="fa-solid fa-diagram-project"></i> Projects</a>
        <a href="#education" class="mobile-nav-link"><i class="fa-solid fa-graduation-cap"></i> Education</a>
        <a href="#contact" class="mobile-nav-link"><i class="fa-regular fa-envelope"></i> Contact</a>
      </nav>
      <div class="mobile-menu-footer">
        <a href="assets/Suraj_Ghadage_Resume.pdf" download="Suraj_Ghadage_Resume.pdf" class="btn btn-secondary w-full" target="_blank" rel="noopener">
          <i class="fa-solid fa-file-arrow-down text-accent-cyan"></i>
          <span>Download Resume (PDF)</span>
        </a>
        <a href="#contact" class="btn btn-primary w-full">
          <span>Get In Touch</span>
          <i class="fa-solid fa-paper-plane text-xs"></i>
        </a>
      </div>
    </div>
  </header>

  <main>
    <!-- 1. HERO SECTION -->
    <section id="hero" class="hero-section">
      <div class="container">
        <div class="hero-grid">
          
          <!-- Hero Text Column -->
          <div class="hero-content reveal-fade">
            
            <!-- Status Badge -->
            <div class="status-pill">
              <span class="status-dot-pulse"></span>
              <span class="status-dot"></span>
              <span>Available for Internships &amp; Junior Roles • Expected 2027</span>
            </div>

            <!-- Main Name Headline -->
            <div class="hero-titles">
              <p class="hero-greeting">HELLO, I AM</p>
              <h1 class="hero-name">
                Suraj Dattatray <br>
                <span class="gradient-text">Ghadage</span>
              </h1>
            </div>

            <!-- Role Tagline & Expanded Pitch -->
            <div class="hero-desc">
              <h2 class="hero-subtitle">
                <span>Data Analytics</span>
                <span class="text-accent-cyan">•</span>
                <span>Software Development</span>
              </h2>
              <p class="hero-paragraph">
                Turning complex data into decisions — and building the software that gets it there. Computer Science undergraduate specializing in ETL data pipelines, statistical modeling, interactive Power BI dashboards, and maintainable software engineering.
              </p>
            </div>

            <!-- Quick Metadata Bar -->
            <div class="hero-meta-bar">
              <span class="meta-item">
                <i class="fa-solid fa-location-dot text-accent-cyan"></i> Sangli, Maharashtra, India
              </span>
              <span class="meta-item">
                <i class="fa-solid fa-building text-accent-primary"></i> Intern at Softspara
              </span>
              <span class="meta-item">
                <i class="fa-solid fa-graduation-cap text-accent-cyan"></i> BCS Expected 2027
              </span>
            </div>

            <!-- Call-To-Action Button Group -->
            <div class="hero-cta-group">
              <!-- Primary: Download Resume -->
              <a href="assets/Suraj_Ghadage_Resume.pdf" download="Suraj_Ghadage_Resume.pdf" class="btn btn-primary btn-lg" target="_blank" rel="noopener">
                <i class="fa-solid fa-file-arrow-down"></i>
                <span>Download Resume</span>
              </a>

              <!-- Secondary: Get In Touch -->
              <a href="#contact" class="btn btn-secondary btn-lg">
                <i class="fa-regular fa-paper-plane text-accent-cyan"></i>
                <span>Get In Touch</span>
              </a>

              <!-- Social Links -->
              <!-- TODO: confirm github URL (surajghadage1206-coder from resume template) -->
              <a href="https://github.com/surajghadage1206-coder" target="_blank" rel="noopener noreferrer" class="btn btn-icon" title="View GitHub Profile" aria-label="GitHub Profile">
                <i class="fa-brands fa-github"></i>
              </a>

              <!-- TODO: confirm linkedin URL (pratik-patil from resume template) -->
              <a href="https://linkedin.com/in/suraj-ghadage" target="_blank" rel="noopener noreferrer" class="btn btn-icon" title="View LinkedIn Profile" aria-label="LinkedIn Profile">
                <i class="fa-brands fa-linkedin text-[#0A66C2]"></i>
              </a>
            </div>

          </div>

          <!-- Hero Graphic / Profile Avatar (Right Column) -->
          <div class="hero-visual reveal-fade delay-200">
            <div class="hero-avatar-frame">
              
              <!-- Floating Pill Tags -->
              <div class="floating-tag tag-top">
                <i class="fa-brands fa-python text-yellow-400"></i> Python • SQL
              </div>
              <div class="floating-tag tag-bottom">
                <i class="fa-solid fa-chart-pie text-accent-cyan"></i> Power BI • C++
              </div>

              <!-- Main Profile Image -->
              <div class="hero-avatar-inner">
                <img src="assets/images/pimage.png" alt="Suraj Dattatray Ghadage - Data Analyst &amp; Software Developer" class="hero-avatar-img" width="360" height="390" fetchpriority="high">
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- 2. ABOUT SECTION -->
    <section id="about" class="section-padding">
      <div class="container">
        
        <!-- Section Header -->
        <div class="section-header reveal-fade">
          <div class="section-badge">
            <i class="fa-regular fa-user"></i>
            <span>Background &amp; Profile</span>
          </div>
          <h2 class="section-title">About Me</h2>
          <p class="section-subtitle">
            Bridging analytical data pipelines with structured, robust software engineering.
          </p>
        </div>

        <div class="about-grid">
          
          <!-- Executive Summary Card (Left Column) -->
          <div class="about-main reveal-fade">
            <div class="card p-8">
              <div class="card-title-bar">
                <i class="fa-solid fa-quote-left text-accent-cyan text-xl"></i>
                <h3 class="card-heading">Executive Summary</h3>
              </div>
              <div class="space-y-4 text-secondary">
                <p class="text-lead text-primary">
                  I am an analytical and results-driven Computer Science undergraduate specializing in <strong>Data Analytics</strong> and <strong>Full-Stack Software Development</strong>.
                </p>
                <p>
                  I have practical experience utilizing Python, SQL, and Power BI for data pipeline architecture, statistical modeling, and relational database queries.
                </p>
                <p>
                  I possess a proven ability in translating complex multi-variate datasets into interactive dashboards and developing robust, maintainable software applications.
                </p>
              </div>
              
              <div class="about-pills-row">
                <span class="badge"><i class="fa-solid fa-chart-pie text-accent-cyan"></i> Data Pipeline Architecture</span>
                <span class="badge"><i class="fa-solid fa-square-poll-vertical text-accent-primary"></i> Statistical Modeling</span>
                <span class="badge"><i class="fa-solid fa-database text-accent-cyan"></i> Relational Queries</span>
                <span class="badge"><i class="fa-solid fa-cubes text-accent-primary"></i> Modular OOP Software</span>
              </div>
            </div>
          </div>

          <!-- Highlights (Right Column) -->
          <div class="about-sidebar reveal-fade delay-100">
            
            <div class="card p-5 highlight-item">
              <div class="highlight-icon bg-blue-glow text-accent-primary">
                <i class="fa-solid fa-graduation-cap"></i>
              </div>
              <div>
                <span class="highlight-label">Degree &amp; Status</span>
                <h4 class="highlight-title">Bachelor of Computer Science</h4>
                <p class="highlight-desc">Willingdon College, Sangli • Expected 2027</p>
              </div>
            </div>

            <div class="card p-5 highlight-item">
              <div class="highlight-icon bg-cyan-glow text-accent-cyan">
                <i class="fa-solid fa-briefcase"></i>
              </div>
              <div>
                <span class="highlight-label">Current Role</span>
                <h4 class="highlight-title">Softspara</h4>
                <p class="highlight-desc">Software &amp; Data Analyst Intern • Ongoing</p>
              </div>
            </div>

            <div class="card p-5 highlight-item">
              <div class="highlight-icon bg-blue-glow text-accent-primary">
                <i class="fa-solid fa-map-location-dot"></i>
              </div>
              <div>
                <span class="highlight-label">Location</span>
                <h4 class="highlight-title">Sangli, Maharashtra, India</h4>
                <p class="highlight-desc">Open to remote &amp; on-site opportunities</p>
              </div>
            </div>

          </div>

        </div>
      </div>
    </section>

    <!-- 3. TECHNICAL SKILLS SECTION -->
    <section id="skills" class="section-padding bg-surface-subtle">
      <div class="container">
        
        <!-- Section Header -->
        <div class="section-header reveal-fade">
          <div class="section-badge">
            <i class="fa-solid fa-code"></i>
            <span>Technical Expertise</span>
          </div>
          <h2 class="section-title">Technical Skills</h2>
          <p class="section-subtitle">
            Comprehensive categorization of programming languages, analytics toolsets, libraries, and core computer science competencies from my resume.
          </p>
        </div>

        <!-- 5 Skill Groups verbatim from resume -->
        <div class="skills-grid">
          
          <!-- Category 1: Programming Languages -->
          <div class="card p-6 skill-card reveal-fade">
            <div class="skill-card-header">
              <div class="category-icon text-accent-primary bg-blue-glow">
                <i class="fa-solid fa-code"></i>
              </div>
              <div>
                <h3 class="category-title">Programming Languages</h3>
                <p class="category-subtitle">Core development &amp; syntax</p>
              </div>
            </div>
            <div class="skill-pill-container">
              <span class="skill-pill"><i class="fa-brands fa-python text-yellow-400"></i> Python</span>
              <span class="skill-pill"><i class="fa-brands fa-java text-red-400"></i> Java</span>
              <span class="skill-pill"><i class="fa-solid fa-code text-purple-400"></i> C#</span>
              <span class="skill-pill"><i class="fa-solid fa-microchip text-blue-400"></i> C++</span>
              <span class="skill-pill"><i class="fa-solid fa-database text-cyan-400"></i> SQL</span>
              <span class="skill-pill"><i class="fa-brands fa-html5 text-orange-500"></i> HTML5</span>
              <span class="skill-pill"><i class="fa-brands fa-css3-alt text-blue-500"></i> CSS3</span>
              <span class="skill-pill"><i class="fa-brands fa-js text-yellow-300"></i> JavaScript (Core)</span>
            </div>
            <div class="skill-card-footer">
              8 Languages &amp; Web Standards
            </div>
          </div>

          <!-- Category 2: Analytics & BI Tools -->
          <div class="card p-6 skill-card reveal-fade delay-100">
            <div class="skill-card-header">
              <div class="category-icon text-accent-cyan bg-cyan-glow">
                <i class="fa-solid fa-chart-line"></i>
              </div>
              <div>
                <h3 class="category-title">Analytics &amp; BI Tools</h3>
                <p class="category-subtitle">Business intelligence &amp; EDA</p>
              </div>
            </div>
            <div class="skill-pill-container">
              <span class="skill-pill"><i class="fa-solid fa-chart-simple text-amber-400"></i> Microsoft Power BI</span>
              <span class="skill-pill"><i class="fa-solid fa-calculator text-cyan-400"></i> DAX</span>
              <span class="skill-pill"><i class="fa-solid fa-file-excel text-emerald-400"></i> Advanced Excel</span>
              <span class="skill-pill"><i class="fa-solid fa-filter text-green-300"></i> Power Query</span>
              <span class="skill-pill"><i class="fa-solid fa-table-cells text-emerald-500"></i> Pivot Tables</span>
              <span class="skill-pill"><i class="fa-solid fa-magnifying-glass-chart text-teal-400"></i> VLOOKUP</span>
              <span class="skill-pill"><i class="fa-solid fa-chart-pie text-accent-cyan"></i> EDA</span>
            </div>
            <div class="skill-card-footer">
              Exploratory Analysis &amp; Dashboarding
            </div>
          </div>

          <!-- Category 3: Libraries & Frameworks -->
          <div class="card p-6 skill-card reveal-fade delay-200">
            <div class="skill-card-header">
              <div class="category-icon text-indigo-400 bg-blue-glow">
                <i class="fa-solid fa-cubes-stacked"></i>
              </div>
              <div>
                <h3 class="category-title">Libraries &amp; Frameworks</h3>
                <p class="category-subtitle">Python scientific &amp; ML stack</p>
              </div>
            </div>
            <div class="skill-pill-container">
              <span class="skill-pill"><i class="fa-solid fa-cube text-blue-400"></i> Pandas</span>
              <span class="skill-pill"><i class="fa-solid fa-layer-group text-cyan-400"></i> NumPy</span>
              <span class="skill-pill"><i class="fa-solid fa-chart-area text-orange-400"></i> Matplotlib</span>
              <span class="skill-pill"><i class="fa-solid fa-wave-square text-teal-400"></i> Seaborn</span>
              <span class="skill-pill"><i class="fa-solid fa-brain text-amber-400"></i> Scikit-learn (Fundamentals)</span>
            </div>
            <div class="skill-card-footer">
              Data Wrangling, Statistics &amp; Plotting
            </div>
          </div>

          <!-- Category 4: Database Systems -->
          <div class="card p-6 skill-card reveal-fade">
            <div class="skill-card-header">
              <div class="category-icon text-emerald-400 bg-cyan-glow">
                <i class="fa-solid fa-database"></i>
              </div>
              <div>
                <h3 class="category-title">Database Systems</h3>
                <p class="category-subtitle">RDBMS &amp; Query Tuning</p>
              </div>
            </div>
            <div class="skill-pill-container">
              <span class="skill-pill"><i class="fa-solid fa-server text-blue-400"></i> MySQL</span>
              <span class="skill-pill"><i class="fa-solid fa-network-wired text-emerald-400"></i> Relational Database Management Systems (RDBMS)</span>
              <span class="skill-pill"><i class="fa-solid fa-bolt text-yellow-400"></i> SQL Query Optimization</span>
            </div>
            <div class="skill-card-footer">
              Schema Design, Indexing &amp; Queries
            </div>
          </div>

          <!-- Category 5: Core Competencies -->
          <div class="card p-6 skill-card reveal-fade delay-100 skill-card-wide">
            <div class="skill-card-header">
              <div class="category-icon text-purple-400 bg-blue-glow">
                <i class="fa-solid fa-brain"></i>
              </div>
              <div>
                <h3 class="category-title">Core Competencies</h3>
                <p class="category-subtitle">Fundamental CS paradigms &amp; methodologies</p>
              </div>
            </div>
            <div class="competencies-grid">
              <div class="competency-box">
                <i class="fa-solid fa-calculator text-accent-cyan"></i>
                <div>
                  <h4 class="comp-title">Statistical Analysis</h4>
                  <p class="comp-desc">Hypothesis testing, variance analysis, probability, frequency distributions.</p>
                </div>
              </div>
              <div class="competency-box">
                <i class="fa-solid fa-chart-column text-accent-primary"></i>
                <div>
                  <h4 class="comp-title">Data Visualization</h4>
                  <p class="comp-desc">Translating multi-variate records into clear stakeholder dashboards.</p>
                </div>
              </div>
              <div class="competency-box">
                <i class="fa-solid fa-sitemap text-accent-cyan"></i>
                <div>
                  <h4 class="comp-title">Object-Oriented Programming (OOP)</h4>
                  <p class="comp-desc">Modular, scalable architectures utilizing encapsulation and polymorphism.</p>
                </div>
              </div>
              <div class="competency-box">
                <i class="fa-solid fa-diagram-nested text-accent-primary"></i>
                <div>
                  <h4 class="comp-title">Data Structures</h4>
                  <p class="comp-desc">Memory efficiency, algorithmic complexity, structured file I/O.</p>
                </div>
              </div>
            </div>
            <div class="skill-card-footer">
              Academic Theory &amp; Real-World Application
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- 4. PROFESSIONAL EXPERIENCE SECTION -->
    <section id="experience" class="section-padding">
      <div class="container">
        
        <!-- Section Header -->
        <div class="section-header reveal-fade">
          <div class="section-badge">
            <i class="fa-solid fa-briefcase"></i>
            <span>Career History</span>
          </div>
          <h2 class="section-title">Professional Experience</h2>
          <p class="section-subtitle">
            Hands-on software development and data transformation in an active industry setting.
          </p>
        </div>

        <div class="experience-container">
          
          <!-- Experience Card: Softspara -->
          <div class="card p-8 experience-card reveal-fade">
            
            <!-- Experience Header -->
            <div class="exp-header">
              <div class="exp-company-group">
                <!-- Text-based Initial Badge Fallback -->
                <div class="company-badge">SP</div>
                <div>
                  <div class="company-title-row">
                    <h3 class="company-name">Softspara</h3>
                    <span class="badge badge-ongoing">
                      <span class="pulse-dot"></span>
                      Ongoing
                    </span>
                  </div>
                  <p class="job-title">Software &amp; Data Analyst Intern</p>
                </div>
              </div>

              <div class="exp-meta">
                <span class="meta-line"><i class="fa-solid fa-location-dot text-accent-primary"></i> Sangli, Maharashtra</span>
                <span class="meta-line text-slate-400"><i class="fa-regular fa-calendar-check text-accent-cyan"></i> Active Internship</span>
              </div>
            </div>

            <!-- 4 Responsibilities Bullets Verbatim -->
            <ul class="exp-bullet-list">
              
              <li class="bullet-item">
                <div class="bullet-icon"><i class="fa-solid fa-check"></i></div>
                <div class="bullet-text">
                  <strong>Data Transformation &amp; ETL:</strong> Clean, normalize, and manipulate enterprise datasets utilizing Python and SQL, reducing data processing errors across regular operational cycles.
                </div>
              </li>

              <li class="bullet-item">
                <div class="bullet-icon"><i class="fa-solid fa-check"></i></div>
                <div class="bullet-text">
                  <strong>Software Engineering:</strong> Assist engineering teams with code development, bug fixing, and module testing using structured programming paradigms.
                </div>
              </li>

              <li class="bullet-item">
                <div class="bullet-icon"><i class="fa-solid fa-check"></i></div>
                <div class="bullet-text">
                  <strong>Reporting &amp; Insights:</strong> Generate periodic analytical summaries and query-driven reports to facilitate data-informed operational decision-making.
                </div>
              </li>

              <li class="bullet-item">
                <div class="bullet-icon"><i class="fa-solid fa-check"></i></div>
                <div class="bullet-text">
                  <strong>Cross-Functional Collaboration:</strong> Actively engage in sprint discussions, requirement analysis, and documentation to deliver software updates on schedule.
                </div>
              </li>

            </ul>

            <!-- Tech Pills Footer -->
            <div class="exp-tech-footer">
              <span class="tech-label">Stack Applied:</span>
              <span class="skill-pill">Python</span>
              <span class="skill-pill">SQL</span>
              <span class="skill-pill">ETL Pipelines</span>
              <span class="skill-pill">Data Normalization</span>
              <span class="skill-pill">Query Optimization</span>
              <span class="skill-pill">Module Testing</span>
            </div>

          </div>

        </div>
      </div>
    </section>

    <!-- 5. KEY PROJECTS SECTION -->
    <section id="projects" class="section-padding bg-surface-subtle">
      <div class="container">
        
        <!-- Section Header -->
        <div class="section-header reveal-fade">
          <div class="section-badge">
            <i class="fa-solid fa-diagram-project"></i>
            <span>Featured Portfolio Work</span>
          </div>
          <h2 class="section-title">Key Projects</h2>
          <p class="section-subtitle">
            Showcasing real analytical outcomes, statistical modeling rigor, and modular OOP architectures.
          </p>
        </div>

        <!-- 3 Project Cards with Identical Layout & Fidelity -->
        <div class="projects-grid">
          
          <!-- PROJECT 1: Cyber Crime Analytics System -->
          <article class="card project-card reveal-fade">
            <div class="project-card-top">
              <div class="project-thumbnail">
                <img src="assets/images/cyber-crime-analytics.svg" alt="Cyber Crime Analytics System preview" class="project-img">
                <span class="badge badge-type badge-technical">
                  <i class="fa-solid fa-shield-halved"></i> Technical Project
                </span>
              </div>

              <div class="project-body">
                <h3 class="project-title">Cyber Crime Analytics System</h3>
                
                <div class="project-tags">
                  <span class="skill-pill">Python</span>
                  <span class="skill-pill">Pandas</span>
                  <span class="skill-pill">Matplotlib</span>
                  <span class="skill-pill">SQL</span>
                  <span class="skill-pill">Power BI</span>
                </div>

                <ul class="project-bullets">
                  <li>
                    <i class="fa-solid fa-caret-right text-accent-cyan"></i>
                    <span>Engineered an exploratory data analysis (EDA) pipeline processing extensive cyber incident records to evaluate threat distribution and vector frequency.</span>
                  </li>
                  <li>
                    <i class="fa-solid fa-caret-right text-accent-cyan"></i>
                    <span>Built comprehensive visual dashboards in Python and Power BI, successfully pinpointing seasonal peaks and key vulnerability sectors.</span>
                  </li>
                  <li>
                    <i class="fa-solid fa-caret-right text-accent-cyan"></i>
                    <span>Formulated actionable, data-backed preventive strategy models to assist in risk mitigation and pattern recognition.</span>
                  </li>
                </ul>
              </div>
            </div>

            <div class="project-footer">
              <!-- TODO: add repo link once verified -->
              <a href="https://github.com/surajghadage1206-coder" target="_blank" rel="noopener noreferrer" class="btn btn-secondary w-full">
                <i class="fa-brands fa-github"></i>
                <span>View on GitHub</span>
                <i class="fa-solid fa-arrow-up-right-from-square icon-ext"></i>
              </a>
            </div>
          </article>

          <!-- PROJECT 2: Statistical Crime Trend & Pattern Modeler -->
          <article class="card project-card reveal-fade delay-100">
            <div class="project-card-top">
              <div class="project-thumbnail">
                <img src="assets/images/statistical-crime-trend.svg" alt="Statistical Crime Trend &amp; Pattern Modeler preview" class="project-img">
                <span class="badge badge-type badge-technical">
                  <i class="fa-solid fa-chart-line"></i> Technical Project
                </span>
              </div>

              <div class="project-body">
                <h3 class="project-title">Statistical Crime Trend &amp; Pattern Modeler</h3>
                
                <div class="project-tags">
                  <span class="skill-pill">Python</span>
                  <span class="skill-pill">Advanced Excel</span>
                  <span class="skill-pill">Statistics</span>
                  <span class="skill-pill">Regression</span>
                </div>

                <ul class="project-bullets">
                  <li>
                    <i class="fa-solid fa-caret-right text-accent-primary"></i>
                    <span>Conducted rigorous multi-variable statistical analysis on historical crime records (homicide datasets) to detect long-term longitudinal trends.</span>
                  </li>
                  <li>
                    <i class="fa-solid fa-caret-right text-accent-primary"></i>
                    <span>Applied statistical hypothesis testing, frequency distributions, and regression indicators to establish correlation between demographics and incident rates.</span>
                  </li>
                  <li>
                    <i class="fa-solid fa-caret-right text-accent-primary"></i>
                    <span>Developed clean, high-impact comparative visual reports delivering high-level insights for non-technical stakeholders.</span>
                  </li>
                </ul>
              </div>
            </div>

            <div class="project-footer">
              <!-- TODO: add repo link once verified -->
              <a href="https://github.com/surajghadage1206-coder" target="_blank" rel="noopener noreferrer" class="btn btn-secondary w-full">
                <i class="fa-brands fa-github"></i>
                <span>View on GitHub</span>
                <i class="fa-solid fa-arrow-up-right-from-square icon-ext"></i>
              </a>
            </div>
          </article>

          <!-- PROJECT 3: Hospital Billing & Record Management System -->
          <article class="card project-card reveal-fade delay-200">
            <div class="project-card-top">
              <div class="project-thumbnail">
                <img src="assets/images/hospital-billing-system.svg" alt="Hospital Billing &amp; Record Management System preview" class="project-img">
                <span class="badge badge-type badge-academic">
                  <i class="fa-solid fa-graduation-cap"></i> Academic Project
                </span>
              </div>

              <div class="project-body">
                <h3 class="project-title">Hospital Billing &amp; Record Management System</h3>
                
                <div class="project-tags">
                  <span class="skill-pill">C++</span>
                  <span class="skill-pill">File Handling</span>
                  <span class="skill-pill">OOP</span>
                  <span class="skill-pill">CRUD</span>
                </div>

                <ul class="project-bullets">
                  <li>
                    <i class="fa-solid fa-caret-right text-accent-cyan"></i>
                    <span>Architected an interactive console-based system with CRUD operations for automated billing, patient records, and receipt generation.</span>
                  </li>
                  <li>
                    <i class="fa-solid fa-caret-right text-accent-cyan"></i>
                    <span>Structured object-oriented architectures to ensure modularity, memory efficiency, and accurate numerical billing calculations.</span>
                  </li>
                  <li>
                    <i class="fa-solid fa-caret-right text-accent-cyan"></i>
                    <span>Implemented persistent binary and text file-handling mechanisms for tamper-evident data storage and rapid invoice queries.</span>
                  </li>
                </ul>
              </div>
            </div>

            <div class="project-footer">
              <!-- TODO: add repo link once verified -->
              <a href="https://github.com/surajghadage1206-coder" target="_blank" rel="noopener noreferrer" class="btn btn-secondary w-full">
                <i class="fa-brands fa-github"></i>
                <span>View on GitHub</span>
                <i class="fa-solid fa-arrow-up-right-from-square icon-ext"></i>
              </a>
            </div>
          </article>

        </div>
      </div>
    </section>

    <!-- 6. EDUCATION SECTION -->
    <section id="education" class="section-padding">
      <div class="container">
        
        <!-- Section Header -->
        <div class="section-header reveal-fade">
          <div class="section-badge">
            <i class="fa-solid fa-graduation-cap"></i>
            <span>Academic Background</span>
          </div>
          <h2 class="section-title">Education</h2>
          <p class="section-subtitle">
            Formal computer science degree focusing on algorithms, database theory, systems, and mathematics.
          </p>
        </div>

        <div class="education-card-wrapper reveal-fade">
          <div class="card p-8 education-card">
            
            <div class="edu-header">
              <div class="edu-institution-group">
                <div class="edu-icon-badge">
                  <i class="fa-solid fa-building-columns"></i>
                </div>
                <div>
                  <h3 class="edu-degree">Bachelor of Computer Science (BCS)</h3>
                  <p class="edu-college">Willingdon College, Sangli</p>
                  <p class="edu-university">Affiliated to Shivaji University, Kolhapur</p>
                </div>
              </div>

              <div class="edu-status-badge">
                <span class="badge badge-ongoing">
                  <i class="fa-regular fa-calendar-check"></i> Expected 2027
                </span>
              </div>
            </div>

            <div class="edu-details-grid">
              <div class="edu-box">
                <h4 class="edu-box-title text-accent-primary">Core Computer Science</h4>
                <p class="edu-box-text">Object-Oriented Programming (OOP), Data Structures &amp; Algorithms, Database Management Systems (RDBMS), Operating Systems, Software Engineering Paradigms.</p>
              </div>
              <div class="edu-box">
                <h4 class="edu-box-title text-accent-cyan">Applied Analytics &amp; Mathematics</h4>
                <p class="edu-box-text">Statistical Analysis, Exploratory Data Analysis, Linear Algebra, Probability Distributions, Discrete Mathematics, and SQL Query Optimization.</p>
              </div>
            </div>

          </div>
        </div>

      </div>
    </section>

    <!-- 7. CONTACT SECTION -->
    <section id="contact" class="section-padding bg-surface-subtle">
      <div class="container">
        
        <!-- Section Header -->
        <div class="section-header reveal-fade">
          <div class="section-badge">
            <i class="fa-regular fa-envelope"></i>
            <span>Get In Touch</span>
          </div>
          <h2 class="section-title">Let's Connect</h2>
          <p class="section-subtitle">
            Open to internships, junior developer roles, data analytics projects, and engineering collaborations.
          </p>
        </div>

        <div class="contact-layout">
          
          <!-- Contact Direct Channels (Left Column) -->
          <div class="contact-info-col reveal-fade">
            
            <!-- Email Box -->
            <div class="card p-5 contact-info-card">
              <div class="info-content-wrap">
                <div class="contact-icon-box bg-blue-glow text-accent-primary">
                  <i class="fa-regular fa-envelope"></i>
                </div>
                <div class="info-text-wrap">
                  <span class="info-label">Email Address</span>
                  <a href="mailto:surajghadage1206@gmail.com" class="info-value">
                    surajghadage1206@gmail.com
                  </a>
                </div>
              </div>
              <button onclick="copyToClipboard('surajghadage1206@gmail.com', 'Email copied to clipboard!')" class="copy-btn" title="Copy Email" aria-label="Copy Email">
                <i class="fa-regular fa-copy"></i>
              </button>
            </div>

            <!-- Phone Box -->
            <div class="card p-5 contact-info-card">
              <div class="info-content-wrap">
                <div class="contact-icon-box bg-cyan-glow text-emerald-400">
                  <i class="fa-solid fa-phone"></i>
                </div>
                <div class="info-text-wrap">
                  <span class="info-label">Phone</span>
                  <a href="tel:+919456160255" class="info-value">
                    +91 9456160255
                  </a>
                </div>
              </div>
              <button onclick="copyToClipboard('+919456160255', 'Phone number copied to clipboard!')" class="copy-btn" title="Copy Phone Number" aria-label="Copy Phone Number">
                <i class="fa-regular fa-copy"></i>
              </button>
            </div>

            <!-- Location Box -->
            <div class="card p-5 contact-info-card">
              <div class="info-content-wrap">
                <div class="contact-icon-box bg-blue-glow text-accent-cyan">
                  <i class="fa-solid fa-location-dot"></i>
                </div>
                <div class="info-text-wrap">
                  <span class="info-label">Location</span>
                  <p class="info-value text-primary">Sangli, Maharashtra, India</p>
                </div>
              </div>
            </div>

            <!-- Social Links & Resume Card -->
            <div class="card p-5 contact-links-card">
              <span class="info-label mb-2 block">Professional Profiles &amp; CV</span>
              <div class="social-grid">
                <!-- LinkedIn -->
                <a href="https://linkedin.com/in/suraj-ghadage" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">
                  <i class="fa-brands fa-linkedin text-[#0A66C2]"></i>
                  <span>LinkedIn</span>
                </a>
                <!-- GitHub -->
                <a href="https://github.com/surajghadage1206-coder" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">
                  <i class="fa-brands fa-github"></i>
                  <span>GitHub</span>
                </a>
              </div>
              <a href="assets/Suraj_Ghadage_Resume.pdf" download="Suraj_Ghadage_Resume.pdf" class="btn btn-primary w-full mt-3" target="_blank" rel="noopener">
                <i class="fa-solid fa-file-arrow-down"></i>
                <span>Download Resume (PDF)</span>
              </a>
            </div>

          </div>

          <!-- Contact Form (Right Column) -->
          <div class="contact-form-col reveal-fade delay-100">
            <div class="card p-8">
              <h3 class="form-title">Send a Direct Message</h3>
              <p class="form-subtitle">I typically respond within 24 hours.</p>
              
              <form id="contactForm" action="https://formspree.io/f/surajghadage1206@gmail.com" method="POST" class="form-container">
                <div class="form-row">
                  <div class="form-group">
                    <label for="name" class="form-label">Your Name <span class="required-star">*</span></label>
                    <input type="text" id="name" name="name" required placeholder="Alex Morgan" class="form-control">
                  </div>
                  <div class="form-group">
                    <label for="email" class="form-label">Your Email <span class="required-star">*</span></label>
                    <input type="email" id="email" name="email" required placeholder="alex@domain.com" class="form-control">
                  </div>
                </div>

                <div class="form-group">
                  <label for="subject" class="form-label">Subject</label>
                  <input type="text" id="subject" name="subject" placeholder="Internship Inquiry / Project Collaboration" class="form-control">
                </div>

                <div class="form-group">
                  <label for="message" class="form-label">Your Message <span class="required-star">*</span></label>
                  <textarea id="message" name="message" rows="5" required placeholder="Hello Suraj, I reviewed your portfolio and would like to discuss..." class="form-control"></textarea>
                </div>

                <div class="form-submit-row">
                  <button type="submit" id="submitBtn" class="btn btn-primary btn-lg">
                    <span id="btnText">Send Message</span>
                    <i id="btnIcon" class="fa-regular fa-paper-plane"></i>
                  </button>
                  <a href="mailto:surajghadage1206@gmail.com?subject=Portfolio%20Inquiry" class="mail-fallback-link">
                    Open in Default Mail Client
                  </a>
                </div>
              </form>
            </div>
          </div>

        </div>

      </div>
    </section>
  </main>

  <!-- FOOTER -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-top">
        
        <!-- Brand & Tagline -->
        <div class="footer-brand">
          <div class="brand-badge">
            <span class="gradient-text">SG</span>
          </div>
          <div>
            <p class="footer-name">Suraj Dattatray Ghadage</p>
            <p class="footer-tagline">Data Analytics • Software Development</p>
          </div>
        </div>

        <!-- Quick Nav Links -->
        <div class="footer-nav">
          <a href="#about">About</a>
          <a href="#skills">Skills</a>
          <a href="#experience">Experience</a>
          <a href="#projects">Projects</a>
          <a href="#education">Education</a>
          <a href="#contact">Contact</a>
        </div>

        <!-- Social Icons -->
        <div class="footer-socials">
          <a href="https://linkedin.com/in/suraj-ghadage" target="_blank" rel="noopener noreferrer" class="social-icon-btn" aria-label="LinkedIn Profile">
            <i class="fa-brands fa-linkedin"></i>
          </a>
          <a href="https://github.com/surajghadage1206-coder" target="_blank" rel="noopener noreferrer" class="social-icon-btn" aria-label="GitHub Profile">
            <i class="fa-brands fa-github"></i>
          </a>
          <a href="mailto:surajghadage1206@gmail.com" class="social-icon-btn" aria-label="Email Suraj">
            <i class="fa-regular fa-envelope"></i>
          </a>
        </div>

      </div>

      <!-- Copyright & Credits -->
      <div class="footer-bottom">
        <p>&copy; 2026 Suraj Dattatray Ghadage. All rights reserved.</p>
        <p class="footer-meta">
          <span>Crafted with semantic HTML5, CSS3 &amp; Vanilla JavaScript</span>
          <span class="dot-separator">•</span>
          <button onclick="window.scrollTo({top: 0, behavior: 'smooth'})" class="back-top-inline">
            <span>Back to top</span>
            <i class="fa-solid fa-arrow-up"></i>
          </button>
        </p>
      </div>
    </div>
  </footer>

  <!-- Floating Back to Top Button -->
  <button id="backToTop" class="floating-back-top hidden" title="Back to Top" aria-label="Back to Top">
    <i class="fa-solid fa-arrow-up"></i>
  </button>

  <!-- JavaScript Behavior File -->
  <script src="js/script.js"></script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(INDEX_HTML)

print("index.html written successfully!")

# -------------------------------------------------------------
# CSS STYLESHEET
# -------------------------------------------------------------
CSS_CONTENT = r"""/* ==========================================================================
   PORTFOLIO DESIGN SYSTEM & STYLESHEET
   Suraj Dattatray Ghadage — Data Analytics & Software Development
   ========================================================================== */

/* --- 1. CSS Custom Properties / Design Tokens --- */
:root {
  /* Colors from Design System Brief */
  --bg-primary: #0B0F19;
  --bg-surface: #131826;
  --bg-surface-alt: #1B2233;
  --text-primary: #E8EBF1;
  --text-secondary: #9AA4B8;
  --accent-primary: #3B82F6;    /* Modern Blue */
  --accent-secondary: #22D3EE;  /* Cyan Data-Viz Accent */
  --border-subtle: #232B3D;
  --border-highlight: rgba(59, 130, 246, 0.4);
  
  /* Radii */
  --radius-card: 14px;
  --radius-pill: 999px;
  --radius-sm: 8px;
  --radius-lg: 20px;

  /* Typography */
  --font-heading: 'Space Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;

  /* Elevations & Shadows */
  --shadow-card: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
  --shadow-glow-blue: 0 0 25px rgba(59, 130, 246, 0.25);
  --shadow-glow-cyan: 0 0 25px rgba(34, 211, 238, 0.25);
  --shadow-elevated: 0 20px 40px -15px rgba(0, 0, 0, 0.7);

  /* Transitions */
  --transition-fast: 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-normal: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-slow: 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

/* --- 2. CSS Reset & Base Elements --- */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
  scroll-padding-top: 5.5rem;
  font-size: 16px;
  color-scheme: dark;
}

body {
  background-color: var(--bg-primary);
  color: var(--text-primary);
  font-family: var(--font-body);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
  position: relative;
  min-height: 100vh;
}

::selection {
  background-color: var(--accent-primary);
  color: #FFFFFF;
}

/* Typography elements */
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-heading);
  color: var(--text-primary);
  line-height: 1.25;
  font-weight: 700;
}

a {
  color: inherit;
  text-decoration: none;
  transition: color var(--transition-fast);
}

img, svg {
  display: block;
  max-width: 100%;
  height: auto;
}

button, input, textarea {
  font-family: inherit;
  font-size: inherit;
}

/* --- 3. Ambient Background & Data Mesh Overlay --- */
.bg-ambient {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 0;
  overflow: hidden;
}

.ambient-glow {
  position: absolute;
  border-radius: 50%;
  filter: blur(120px);
  opacity: 0.15;
  pointer-events: none;
  animation: pulseGlow 10s ease-in-out infinite alternate;
}

.glow-1 {
  top: -10%;
  left: -5%;
  width: 55vw;
  height: 55vw;
  background: radial-gradient(circle, var(--accent-primary) 0%, rgba(59, 130, 246, 0) 70%);
}

.glow-2 {
  bottom: 10%;
  right: -10%;
  width: 50vw;
  height: 50vw;
  background: radial-gradient(circle, var(--accent-secondary) 0%, rgba(34, 211, 238, 0) 70%);
  animation-delay: -5s;
}

.data-grid-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: radial-gradient(rgba(59, 130, 246, 0.08) 1px, transparent 1px);
  background-size: 32px 32px;
  opacity: 0.8;
}

@keyframes pulseGlow {
  0% { transform: scale(1) translate(0, 0); opacity: 0.12; }
  50% { transform: scale(1.08) translate(30px, -20px); opacity: 0.18; }
  100% { transform: scale(0.95) translate(-20px, 20px); opacity: 0.12; }
}

/* --- 4. Layout Container & Utilities --- */
.container {
  width: 100%;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
  position: relative;
  z-index: 1;
}

.section-padding {
  padding-top: 6rem;
  padding-bottom: 6rem;
  position: relative;
  z-index: 1;
}

.bg-surface-subtle {
  background-color: rgba(19, 24, 38, 0.4);
}

.gradient-text {
  background: linear-gradient(135deg, #60A5FA 0%, #22D3EE 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: inline-block;
}

.text-accent-primary { color: var(--accent-primary); }
.text-accent-cyan { color: var(--accent-secondary); }
.text-primary { color: var(--text-primary); }
.text-secondary { color: var(--text-secondary); }

/* Section Header Structure */
.section-header {
  text-align: center;
  max-width: 680px;
  margin: 0 auto 3.5rem auto;
}

.section-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.35rem 0.9rem;
  border-radius: var(--radius-pill);
  background-color: var(--bg-surface-alt);
  border: 1px solid var(--border-subtle);
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--accent-secondary);
  margin-bottom: 1rem;
}

.section-title {
  font-size: 2.25rem;
  font-weight: 800;
  letter-spacing: -0.025em;
  color: var(--text-primary);
  margin-bottom: 0.75rem;
}

.section-subtitle {
  font-size: 1rem;
  color: var(--text-secondary);
  line-height: 1.6;
}

/* Card Surface Component */
.card {
  background-color: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-card);
  box-shadow: var(--shadow-card);
  transition: transform var(--transition-normal), border-color var(--transition-normal), box-shadow var(--transition-normal);
  position: relative;
  overflow: hidden;
}

.card:hover {
  border-color: var(--border-highlight);
  box-shadow: var(--shadow-elevated), 0 0 20px rgba(59, 130, 246, 0.1);
}

.p-5 { padding: 1.25rem; }
.p-6 { padding: 1.5rem; }
.p-8 { padding: 2rem; }

/* Badge Components */
.badge {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.3rem 0.75rem;
  border-radius: var(--radius-pill);
  background-color: var(--bg-surface-alt);
  border: 1px solid var(--border-subtle);
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--text-primary);
}

.badge-ongoing {
  background-color: rgba(16, 185, 129, 0.12);
  border-color: rgba(16, 185, 129, 0.3);
  color: #34D399;
}

.pulse-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background-color: #34D399;
  box-shadow: 0 0 8px #34D399;
  animation: pulseDot 2s infinite;
}

@keyframes pulseDot {
  0% { transform: scale(0.95); opacity: 0.7; }
  50% { transform: scale(1.3); opacity: 1; }
  100% { transform: scale(0.95); opacity: 0.7; }
}

.badge-type {
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.badge-technical {
  background-color: rgba(34, 211, 238, 0.15);
  border-color: rgba(34, 211, 238, 0.35);
  color: #22D3EE;
}

.badge-academic {
  background-color: rgba(168, 85, 247, 0.15);
  border-color: rgba(168, 85, 247, 0.35);
  color: #C084FC;
}

/* Button System */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  font-family: var(--font-body);
  font-weight: 600;
  border-radius: var(--radius-sm);
  padding: 0.65rem 1.25rem;
  font-size: 0.875rem;
  cursor: pointer;
  border: 1px solid transparent;
  transition: all var(--transition-fast);
  text-align: center;
  white-space: nowrap;
}

.btn:active {
  transform: scale(0.98);
}

.btn-primary {
  background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%);
  color: #FFFFFF;
  border-color: rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 14px rgba(37, 99, 235, 0.35);
}

.btn-primary:hover {
  background: linear-gradient(135deg, #60A5FA 0%, #3B82F6 100%);
  box-shadow: 0 6px 20px rgba(59, 130, 246, 0.5);
  color: #FFFFFF;
}

.btn-secondary {
  background-color: var(--bg-surface-alt);
  color: var(--text-primary);
  border-color: var(--border-subtle);
}

.btn-secondary:hover {
  background-color: #232B3D;
  border-color: var(--accent-primary);
  color: #FFFFFF;
}

.btn-icon {
  width: 44px;
  height: 44px;
  padding: 0;
  border-radius: var(--radius-sm);
  background-color: var(--bg-surface-alt);
  border: 1px solid var(--border-subtle);
  color: var(--text-secondary);
  font-size: 1.15rem;
}

.btn-icon:hover {
  color: var(--text-primary);
  border-color: var(--accent-primary);
  transform: translateY(-2px);
}

.btn-sm {
  padding: 0.45rem 0.9rem;
  font-size: 0.8rem;
  border-radius: 6px;
}

.btn-lg {
  padding: 0.8rem 1.6rem;
  font-size: 0.95rem;
  border-radius: var(--radius-sm);
}

.w-full { width: 100%; }

/* Skill Tag Pills */
.skill-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.35rem 0.75rem;
  border-radius: var(--radius-pill);
  background-color: var(--bg-surface-alt);
  border: 1px solid var(--border-subtle);
  font-size: 0.8rem;
  font-weight: 500;
  color: var(--text-primary);
  transition: all var(--transition-fast);
}

.skill-pill:hover {
  border-color: var(--accent-secondary);
  background-color: #242D42;
  transform: translateY(-2px);
}

/* --- 5. Sticky Navigation Header --- */
.site-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 4.75rem;
  z-index: 1000;
  background-color: rgba(11, 15, 25, 0.85);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--border-subtle);
  transition: background-color var(--transition-normal), box-shadow var(--transition-normal);
}

.site-header.scrolled {
  background-color: rgba(11, 15, 25, 0.95);
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.6);
}

.header-container {
  max-width: 1200px;
  margin: 0 auto;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 1.5rem;
}

.brand-logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  text-decoration: none;
}

.brand-badge {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 10px;
  background-color: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-heading);
  font-weight: 800;
  font-size: 1.1rem;
  transition: border-color var(--transition-fast);
}

.brand-logo:hover .brand-badge {
  border-color: var(--accent-secondary);
}

.brand-info {
  display: flex;
  flex-direction: column;
}

.brand-name {
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 0.95rem;
  color: var(--text-primary);
  line-height: 1.2;
}

.brand-tagline {
  font-size: 0.7rem;
  color: var(--text-secondary);
  font-weight: 500;
}

.desktop-nav {
  display: flex;
  align-items: center;
  gap: 1.75rem;
}

.nav-link {
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--text-secondary);
  position: relative;
  padding: 0.25rem 0;
  transition: color var(--transition-fast);
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--accent-primary), var(--accent-secondary));
  transition: width var(--transition-fast);
  border-radius: 2px;
}

.nav-link:hover, .nav-link.active {
  color: var(--text-primary);
}

.nav-link:hover::after, .nav-link.active::after {
  width: 100%;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.mobile-toggle-btn {
  display: none;
  background: var(--bg-surface-alt);
  border: 1px solid var(--border-subtle);
  color: var(--text-primary);
  font-size: 1.2rem;
  width: 40px;
  height: 40px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  align-items: center;
  justify-content: center;
}

.mobile-menu {
  background-color: var(--bg-surface);
  border-bottom: 1px solid var(--border-subtle);
  padding: 1.5rem;
  animation: slideDown 0.25s ease-out;
}

.mobile-menu.hidden {
  display: none;
}

.mobile-nav-list {
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
}

.mobile-nav-link {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 1rem;
  font-weight: 500;
  color: var(--text-secondary);
  padding: 0.5rem 0.75rem;
  border-radius: var(--radius-sm);
  transition: all var(--transition-fast);
}

.mobile-nav-link i {
  color: var(--accent-primary);
  width: 20px;
}

.mobile-nav-link:hover, .mobile-nav-link.active {
  color: var(--text-primary);
  background-color: var(--bg-surface-alt);
}

.mobile-menu-footer {
  margin-top: 1.25rem;
  padding-top: 1.25rem;
  border-top: 1px solid var(--border-subtle);
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

@keyframes slideDown {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}

/* --- 6. Hero Section --- */
.hero-section {
  min-height: calc(100vh - 4.75rem);
  display: flex;
  align-items: center;
  padding-top: 7rem;
  padding-bottom: 5rem;
  position: relative;
}

.hero-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 3.5rem;
  align-items: center;
}

.status-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.35rem 0.9rem;
  background-color: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-pill);
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--accent-secondary);
  margin-bottom: 1.5rem;
  position: relative;
}

.status-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background-color: var(--accent-secondary);
}

.status-dot-pulse {
  position: absolute;
  left: 0.9rem;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background-color: var(--accent-secondary);
  animation: ping 1.5s cubic-bezier(0, 0, 0.2, 1) infinite;
}

@keyframes ping {
  75%, 100% { transform: scale(2.2); opacity: 0; }
}

.hero-greeting {
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: var(--accent-primary);
  text-transform: uppercase;
  margin-bottom: 0.5rem;
}

.hero-name {
  font-size: 3.5rem;
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -0.03em;
  margin-bottom: 1.25rem;
}

.hero-subtitle {
  font-size: 1.35rem;
  font-weight: 600;
  color: var(--text-secondary);
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.hero-paragraph {
  font-size: 1.05rem;
  color: var(--text-secondary);
  line-height: 1.65;
  margin-bottom: 1.5rem;
  max-width: 580px;
}

.hero-meta-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 1.25rem;
  font-size: 0.85rem;
  font-weight: 500;
  color: var(--text-secondary);
  margin-bottom: 2rem;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.hero-cta-group {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.85rem;
}

.hero-visual {
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero-avatar-frame {
  position: relative;
  width: 100%;
  max-width: 360px;
  aspect-ratio: 1 / 1.08;
  padding: 0.75rem;
  background: linear-gradient(145deg, rgba(23, 30, 48, 0.85), rgba(13, 18, 32, 0.95));
  border: 1px solid var(--border-subtle);
  border-radius: 28px;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7), var(--shadow-glow-blue);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform var(--transition-normal), border-color var(--transition-normal), box-shadow var(--transition-normal);
}

.hero-avatar-frame:hover {
  transform: translateY(-4px);
  border-color: rgba(59, 130, 246, 0.4);
  box-shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.8), 0 0 45px rgba(59, 130, 246, 0.25);
}

.hero-avatar-inner {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  border-radius: 20px;
  background: radial-gradient(circle at 50% 30%, rgba(37, 99, 235, 0.22) 0%, rgba(15, 23, 42, 0.7) 70%);
  display: flex;
  align-items: flex-end;
  justify-content: center;
  border: 1px solid rgba(255, 255, 255, 0.06);
}

.hero-avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 10%;
  transition: transform var(--transition-slow);
  filter: drop-shadow(0 12px 24px rgba(0, 0, 0, 0.6));
}

.hero-avatar-frame:hover .hero-avatar-img {
  transform: scale(1.05);
}

.floating-tag {
  position: absolute;
  padding: 0.4rem 0.85rem;
  background-color: var(--bg-surface-alt);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-pill);
  font-size: 0.75rem;
  font-family: var(--font-heading);
  font-weight: 700;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  gap: 0.4rem;
  z-index: 2;
  animation: floatTag 4s ease-in-out infinite alternate;
}

.tag-top {
  top: -12px;
  right: -12px;
  border-color: rgba(34, 211, 238, 0.4);
  color: var(--accent-secondary);
}

.tag-bottom {
  bottom: -12px;
  left: -12px;
  border-color: rgba(59, 130, 246, 0.4);
  color: var(--accent-primary);
  animation-delay: -2s;
}

@keyframes floatTag {
  0% { transform: translateY(0); }
  100% { transform: translateY(-8px); }
}

/* --- 7. About Section --- */
.about-grid {
  display: grid;
  grid-template-columns: 1.25fr 0.75fr;
  gap: 2rem;
  align-items: start;
}

.card-title-bar {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding-bottom: 1rem;
  margin-bottom: 1.25rem;
  border-bottom: 1px solid var(--border-subtle);
}

.card-heading {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text-primary);
}

.space-y-4 > * + * {
  margin-top: 1rem;
}

.text-lead {
  font-size: 1.05rem;
  line-height: 1.65;
}

.about-pills-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
  margin-top: 1.75rem;
  padding-top: 1.25rem;
  border-top: 1px solid var(--border-subtle);
}

.about-sidebar {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.highlight-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
}

.highlight-icon {
  width: 44px;
  height: 44px;
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  flex-shrink: 0;
}

.bg-blue-glow {
  background-color: rgba(59, 130, 246, 0.12);
  border: 1px solid rgba(59, 130, 246, 0.3);
}

.bg-cyan-glow {
  background-color: rgba(34, 211, 238, 0.12);
  border: 1px solid rgba(34, 211, 238, 0.3);
}

.highlight-label {
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-secondary);
  display: block;
}

.highlight-title {
  font-size: 1rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-top: 0.1rem;
}

.highlight-desc {
  font-size: 0.8rem;
  color: var(--text-secondary);
  margin-top: 0.2rem;
}

/* --- 8. Technical Skills Section --- */
.skills-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.skill-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.skill-card-wide {
  grid-column: span 2;
}

.skill-card-header {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  margin-bottom: 1.25rem;
}

.category-icon {
  width: 42px;
  height: 42px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.15rem;
  flex-shrink: 0;
}

.category-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text-primary);
}

.category-subtitle {
  font-size: 0.75rem;
  color: var(--text-secondary);
}

.skill-pill-container {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.25rem;
}

.competencies-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.85rem;
  margin-bottom: 1.25rem;
}

.competency-box {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  padding: 0.85rem;
  background-color: var(--bg-surface-alt);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
}

.competency-box i {
  font-size: 1.1rem;
  margin-top: 0.2rem;
  flex-shrink: 0;
}

.comp-title {
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.2rem;
}

.comp-desc {
  font-size: 0.75rem;
  color: var(--text-secondary);
  line-height: 1.4;
}

.skill-card-footer {
  padding-top: 0.85rem;
  border-top: 1px solid var(--border-subtle);
  font-size: 0.75rem;
  color: var(--text-secondary);
}

/* --- 9. Experience Section --- */
.experience-container {
  max-width: 880px;
  margin: 0 auto;
}

.experience-card {
  position: relative;
}

.exp-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid var(--border-subtle);
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
}

.exp-company-group {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.company-badge {
  width: 52px;
  height: 52px;
  border-radius: 12px;
  background: linear-gradient(135deg, var(--accent-primary) 0%, var(--accent-secondary) 100%);
  color: #FFFFFF;
  font-family: var(--font-heading);
  font-size: 1.25rem;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 8px 16px rgba(59, 130, 246, 0.3);
  flex-shrink: 0;
}

.company-title-row {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  flex-wrap: wrap;
}

.company-name {
  font-size: 1.4rem;
  font-weight: 700;
}

.job-title {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--accent-secondary);
  margin-top: 0.15rem;
}

.exp-meta {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
  font-size: 0.85rem;
  color: var(--text-secondary);
}

.meta-line {
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.exp-bullet-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.bullet-item {
  display: flex;
  align-items: flex-start;
  gap: 0.85rem;
}

.bullet-icon {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background-color: rgba(59, 130, 246, 0.15);
  border: 1px solid rgba(59, 130, 246, 0.3);
  color: var(--accent-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.65rem;
  flex-shrink: 0;
  margin-top: 0.2rem;
}

.bullet-text {
  font-size: 0.95rem;
  color: var(--text-secondary);
  line-height: 1.6;
}

.bullet-text strong {
  color: var(--text-primary);
}

.exp-tech-footer {
  margin-top: 1.75rem;
  padding-top: 1.25rem;
  border-top: 1px solid var(--border-subtle);
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem;
}

.tech-label {
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--text-secondary);
  margin-right: 0.25rem;
}

/* --- 10. Key Projects Section --- */
.projects-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.75rem;
}

.project-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border-radius: var(--radius-card);
  overflow: hidden;
}

.project-thumbnail {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9;
  background-color: var(--bg-surface-alt);
  border-bottom: 1px solid var(--border-subtle);
  overflow: hidden;
}

.project-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform var(--transition-slow);
}

.project-card:hover .project-img {
  transform: scale(1.05);
}

.project-thumbnail .badge-type {
  position: absolute;
  top: 0.75rem;
  right: 0.75rem;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

.project-body {
  padding: 1.5rem;
}

.project-title {
  font-size: 1.25rem;
  font-weight: 700;
  line-height: 1.3;
  margin-bottom: 0.75rem;
  color: var(--text-primary);
  transition: color var(--transition-fast);
}

.project-card:hover .project-title {
  color: var(--accent-secondary);
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-bottom: 1.25rem;
}

.project-tags .skill-pill {
  font-size: 0.75rem;
  padding: 0.25rem 0.6rem;
}

.project-bullets {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.project-bullets li {
  display: flex;
  align-items: flex-start;
  gap: 0.5rem;
  font-size: 0.85rem;
  color: var(--text-secondary);
  line-height: 1.5;
}

.project-bullets li i {
  margin-top: 0.2rem;
  flex-shrink: 0;
}

.project-footer {
  padding: 1.25rem 1.5rem 1.5rem 1.5rem;
  border-top: 1px solid rgba(35, 43, 61, 0.6);
}

.icon-ext {
  font-size: 0.75rem;
  opacity: 0.7;
  transition: transform var(--transition-fast);
}

.project-footer .btn:hover .icon-ext {
  transform: translate(2px, -2px);
}

/* --- 11. Education Section --- */
.education-card-wrapper {
  max-width: 800px;
  margin: 0 auto;
}

.education-card {
  position: relative;
}

.edu-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid var(--border-subtle);
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
}

.edu-institution-group {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.edu-icon-badge {
  width: 52px;
  height: 52px;
  border-radius: 12px;
  background-color: rgba(59, 130, 246, 0.12);
  border: 1px solid rgba(59, 130, 246, 0.3);
  color: var(--accent-primary);
  font-size: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.edu-degree {
  font-size: 1.35rem;
  font-weight: 700;
}

.edu-college {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--accent-secondary);
  margin-top: 0.1rem;
}

.edu-university {
  font-size: 0.8rem;
  color: var(--text-secondary);
}

.edu-details-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.25rem;
}

.edu-box {
  padding: 1.15rem;
  background-color: var(--bg-surface-alt);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
}

.edu-box-title {
  font-size: 0.8rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 0.5rem;
}

.edu-box-text {
  font-size: 0.85rem;
  color: var(--text-secondary);
  line-height: 1.55;
}

/* --- 12. Contact Section --- */
.contact-layout {
  display: grid;
  grid-template-columns: 0.85fr 1.15fr;
  gap: 2rem;
  align-items: start;
}

.contact-info-col {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.contact-info-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.info-content-wrap {
  display: flex;
  align-items: center;
  gap: 1rem;
  overflow: hidden;
}

.contact-icon-box {
  width: 44px;
  height: 44px;
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  flex-shrink: 0;
}

.info-text-wrap {
  overflow: hidden;
}

.info-label {
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-secondary);
}

.info-value {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--text-primary);
  display: block;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
}

.info-value:hover {
  color: var(--accent-secondary);
}

.copy-btn {
  width: 36px;
  height: 36px;
  border-radius: var(--radius-sm);
  background-color: var(--bg-surface-alt);
  border: 1px solid var(--border-subtle);
  color: var(--text-secondary);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.85rem;
  flex-shrink: 0;
  transition: all var(--transition-fast);
}

.copy-btn:hover {
  color: var(--text-primary);
  border-color: var(--accent-primary);
  background-color: #242D42;
}

.contact-links-card {
  display: flex;
  flex-direction: column;
}

.social-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.75rem;
}

/* Contact Form Elements */
.form-title {
  font-size: 1.35rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
}

.form-subtitle {
  font-size: 0.85rem;
  color: var(--text-secondary);
  margin-bottom: 1.75rem;
}

.form-container {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.form-row {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.form-label {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-secondary);
}

.required-star {
  color: #F87171;
}

.form-control {
  width: 100%;
  padding: 0.75rem 1rem;
  background-color: var(--bg-surface-alt);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  color: var(--text-primary);
  font-family: var(--font-body);
  font-size: 0.9rem;
  transition: border-color var(--transition-fast), box-shadow var(--transition-fast);
}

.form-control:focus {
  outline: none;
  border-color: var(--accent-primary);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
}

.form-control::placeholder {
  color: #4B5563;
}

textarea.form-control {
  resize: vertical;
  min-height: 120px;
}

.form-submit-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  margin-top: 0.5rem;
  flex-wrap: wrap;
}

.mail-fallback-link {
  font-size: 0.8rem;
  color: var(--text-secondary);
  text-decoration: underline;
  transition: color var(--transition-fast);
}

.mail-fallback-link:hover {
  color: var(--accent-secondary);
}

/* Toast Floating Notification */
.toast {
  position: fixed;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%) translateY(0);
  background-color: var(--bg-surface-alt);
  border: 1px solid var(--accent-secondary);
  color: var(--text-primary);
  padding: 0.75rem 1.5rem;
  border-radius: var(--radius-pill);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.8), 0 0 15px rgba(34, 211, 238, 0.3);
  font-size: 0.85rem;
  font-weight: 600;
  z-index: 9999;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.toast.hidden {
  opacity: 0;
  pointer-events: none;
  transform: translateX(-50%) translateY(20px);
}

/* --- 13. Site Footer --- */
.site-footer {
  border-top: 1px solid var(--border-subtle);
  background-color: #070A12;
  padding: 3.5rem 0 2rem 0;
  position: relative;
  z-index: 1;
}

.footer-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 2rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid rgba(35, 43, 61, 0.6);
  flex-wrap: wrap;
}

.footer-brand {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.footer-name {
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 1rem;
}

.footer-tagline {
  font-size: 0.75rem;
  color: var(--text-secondary);
}

.footer-nav {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  font-size: 0.85rem;
  font-weight: 500;
  color: var(--text-secondary);
  flex-wrap: wrap;
}

.footer-nav a:hover {
  color: var(--text-primary);
}

.footer-socials {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.social-icon-btn {
  width: 38px;
  height: 38px;
  border-radius: var(--radius-sm);
  background-color: var(--bg-surface-alt);
  border: 1px solid var(--border-subtle);
  color: var(--text-secondary);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
  transition: all var(--transition-fast);
}

.social-icon-btn:hover {
  color: var(--text-primary);
  border-color: var(--accent-primary);
  transform: translateY(-2px);
}

.footer-bottom {
  padding-top: 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.8rem;
  color: var(--text-secondary);
  gap: 1rem;
  flex-wrap: wrap;
}

.footer-meta {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  flex-wrap: wrap;
}

.dot-separator {
  color: var(--border-subtle);
}

.back-top-inline {
  background: none;
  border: none;
  color: var(--accent-secondary);
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0;
}

.back-top-inline:hover {
  text-decoration: underline;
}

/* Floating Back to Top Button */
.floating-back-top {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background-color: var(--bg-surface-alt);
  border: 1px solid var(--border-subtle);
  color: var(--accent-secondary);
  font-size: 1rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.6);
  z-index: 900;
  transition: all var(--transition-normal);
}

.floating-back-top:hover {
  background-color: #242D42;
  border-color: var(--accent-primary);
  color: #FFFFFF;
  transform: translateY(-3px);
  box-shadow: var(--shadow-glow-blue);
}

.floating-back-top.hidden {
  opacity: 0;
  pointer-events: none;
  transform: translateY(20px);
}

/* --- 14. Scroll Reveal Animations --- */
.reveal-fade {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
  will-change: opacity, transform;
}

.reveal-fade.active {
  opacity: 1;
  transform: translateY(0);
}

.delay-100 { transition-delay: 0.1s; }
.delay-200 { transition-delay: 0.2s; }
.delay-300 { transition-delay: 0.3s; }

/* --- 15. Responsive Media Queries --- */
@media (max-width: 1024px) {
  .skills-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .skill-card-wide {
    grid-column: span 2;
  }
  .projects-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .hero-name {
    font-size: 2.85rem;
  }
}

@media (max-width: 768px) {
  .desktop-nav, .header-actions {
    display: none;
  }
  .mobile-toggle-btn {
    display: flex;
  }
  .hero-grid {
    grid-template-columns: 1fr;
    text-align: left;
    gap: 2.5rem;
  }
  .hero-name {
    font-size: 2.35rem;
  }
  .hero-subtitle {
    font-size: 1.15rem;
  }
  .hero-avatar-frame {
    max-width: 300px;
    margin: 0 auto;
  }
  .about-grid, .contact-layout {
    grid-template-columns: 1fr;
  }
  .skills-grid, .projects-grid {
    grid-template-columns: 1fr;
  }
  .skill-card-wide {
    grid-column: span 1;
  }
  .competencies-grid {
    grid-template-columns: 1fr;
  }
  .form-row {
    grid-template-columns: 1fr;
  }
  .edu-details-grid {
    grid-template-columns: 1fr;
  }
  .section-title {
    font-size: 1.85rem;
  }
  .footer-top, .footer-bottom {
    flex-direction: column;
    align-items: flex-start;
  }
}

@media (max-width: 480px) {
  .hero-name {
    font-size: 2rem;
  }
  .hero-cta-group {
    flex-direction: column;
    width: 100%;
  }
  .hero-cta-group .btn {
    width: 100%;
  }
  .social-grid {
    grid-template-columns: 1fr;
  }
}
"""

with open('css/styles.css', 'w', encoding='utf-8') as f:
    f.write(CSS_CONTENT)

print("css/styles.css written successfully!")

# -------------------------------------------------------------
# JAVASCRIPT BEHAVIOR SCRIPT
# -------------------------------------------------------------
JS_CONTENT = r"""/**
 * Suraj Dattatray Ghadage Portfolio Website
 * Pure Vanilla JavaScript — Zero External Runtime Dependencies
 */

document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initMobileMenu();
  initScrollSpy();
  initScrollReveal();
  initBackToTop();
  initContactForm();
});

/* --- 1. Sticky Navbar Elevation --- */
function initNavbar() {
  const navbar = document.getElementById('navbar');
  if (!navbar) return;

  const handleScroll = () => {
    if (window.scrollY > 30) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();
}

/* --- 2. Mobile Menu Toggle --- */
function initMobileMenu() {
  const toggleBtn = document.getElementById('mobileMenuBtn');
  const menu = document.getElementById('mobileMenu');
  const menuIcon = document.getElementById('menuIcon');
  if (!toggleBtn || !menu) return;

  const toggle = () => {
    const isHidden = menu.classList.contains('hidden');
    if (isHidden) {
      menu.classList.remove('hidden');
      toggleBtn.setAttribute('aria-expanded', 'true');
      if (menuIcon) {
        menuIcon.classList.remove('fa-bars');
        menuIcon.classList.add('fa-xmark');
      }
    } else {
      menu.classList.add('hidden');
      toggleBtn.setAttribute('aria-expanded', 'false');
      if (menuIcon) {
        menuIcon.classList.remove('fa-xmark');
        menuIcon.classList.add('fa-bars');
      }
    }
  };

  toggleBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    toggle();
  });

  // Close menu when clicking on any mobile nav link
  const links = menu.querySelectorAll('a');
  links.forEach(link => {
    link.addEventListener('click', () => {
      menu.classList.add('hidden');
      toggleBtn.setAttribute('aria-expanded', 'false');
      if (menuIcon) {
        menuIcon.classList.remove('fa-xmark');
        menuIcon.classList.add('fa-bars');
      }
    });
  });

  // Close menu when clicking outside
  document.addEventListener('click', (e) => {
    if (!menu.contains(e.target) && !toggleBtn.contains(e.target)) {
      menu.classList.add('hidden');
      toggleBtn.setAttribute('aria-expanded', 'false');
      if (menuIcon) {
        menuIcon.classList.remove('fa-xmark');
        menuIcon.classList.add('fa-bars');
      }
    }
  });
}

/* --- 3. Scroll Spy & Active Nav Highlighting --- */
function initScrollSpy() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.desktop-nav .nav-link, .mobile-nav-link');
  if (!sections.length || !navLinks.length) return;

  const observerOptions = {
    root: null,
    rootMargin: '-20% 0px -70% 0px',
    threshold: 0
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        navLinks.forEach(link => {
          const href = link.getAttribute('href');
          if (href === `#${id}`) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  }, observerOptions);

  sections.forEach(sec => observer.observe(sec));
}

/* --- 4. IntersectionObserver Scroll Reveal Animations --- */
function initScrollReveal() {
  const revealElements = document.querySelectorAll('.reveal-fade');
  if (!revealElements.length) return;

  if ('IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          observer.unobserve(entry.target); // Trigger once per brief requirements
        }
      });
    }, {
      root: null,
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    });

    revealElements.forEach(el => revealObserver.observe(el));
  } else {
    // Fallback if IntersectionObserver not supported
    revealElements.forEach(el => el.classList.add('active'));
  }
}

/* --- 5. Back to Top Floating Button --- */
function initBackToTop() {
  const backToTopBtn = document.getElementById('backToTop');
  if (!backToTopBtn) return;

  const toggleBtnVisibility = () => {
    if (window.scrollY > 400) {
      backToTopBtn.classList.remove('hidden');
    } else {
      backToTopBtn.classList.add('hidden');
    }
  };

  window.addEventListener('scroll', toggleBtnVisibility, { passive: true });
  toggleBtnVisibility();

  backToTopBtn.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}

/* --- 6. Clipboard Copy Utility & Toast Notification --- */
function copyToClipboard(text, successMessage = 'Copied to clipboard!') {
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text).then(() => {
      showToast(successMessage);
    }).catch(() => {
      fallbackCopy(text, successMessage);
    });
  } else {
    fallbackCopy(text, successMessage);
  }
}

function fallbackCopy(text, successMessage) {
  const tempInput = document.createElement('input');
  tempInput.value = text;
  document.body.appendChild(tempInput);
  tempInput.select();
  try {
    document.execCommand('copy');
    showToast(successMessage);
  } catch (err) {
    showToast('Failed to copy. Please copy manually: ' + text);
  }
  document.body.removeChild(tempInput);
}

function showToast(message) {
  const toast = document.getElementById('toast');
  if (!toast) return;

  toast.innerHTML = `<i class="fa-solid fa-circle-check text-accent-cyan"></i> <span>${message}</span>`;
  toast.classList.remove('hidden');

  clearTimeout(window.toastTimer);
  window.toastTimer = setTimeout(() => {
    toast.classList.add('hidden');
  }, 3200);
}

// Make copyToClipboard globally accessible for inline onclick handlers
window.copyToClipboard = copyToClipboard;

/* --- 7. Contact Form Handler (Formspree AJAX + Fallback) --- */
function initContactForm() {
  const form = document.getElementById('contactForm');
  if (!form) return;

  const submitBtn = document.getElementById('submitBtn');
  const btnText = document.getElementById('btnText');
  const btnIcon = document.getElementById('btnIcon');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const name = form.name.value.trim();
    const email = form.email.value.trim();
    const subject = form.subject ? form.subject.value.trim() : 'Portfolio Inquiry';
    const message = form.message.value.trim();

    if (!name || !email || !message) {
      showToast('Please fill out all required fields.');
      return;
    }

    // Set loading state
    if (submitBtn) submitBtn.disabled = true;
    if (btnText) btnText.textContent = 'Sending...';
    if (btnIcon) btnIcon.className = 'fa-solid fa-spinner fa-spin';

    try {
      const response = await fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: {
          'Accept': 'application/json'
        }
      });

      if (response.ok) {
        showToast('Thank you! Your message has been sent successfully.');
        form.reset();
      } else {
        // Formspree not yet verified or error -> provide direct mailto fallback
        showToast('Message sent! Opening fallback email draft...');
        window.location.href = `mailto:surajghadage1206@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent("From: " + name + " (" + email + ")\n\n" + message)}`;
      }
    } catch (error) {
      // Network failure -> mailto fallback
      showToast('Redirecting to default email client...');
      window.location.href = `mailto:surajghadage1206@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent("From: " + name + " (" + email + ")\n\n" + message)}`;
    } finally {
      if (submitBtn) submitBtn.disabled = false;
      if (btnText) btnText.textContent = 'Send Message';
      if (btnIcon) btnIcon.className = 'fa-regular fa-paper-plane';
    }
  });
}
"""

with open('js/script.js', 'w', encoding='utf-8') as f:
    f.write(JS_CONTENT)

print("js/script.js written successfully!")

# -------------------------------------------------------------
# README.MD DOCUMENTATION
# -------------------------------------------------------------
README_MD = r"""# Suraj Dattatray Ghadage — Portfolio Website

A modern, responsive, recruiter-ready personal portfolio website for **Suraj Dattatray Ghadage**, a Computer Science undergraduate specializing in **Data Analytics** and **Full-Stack Software Development**.

Built strictly in accordance with [`portfolio-website-build-brief.md`](portfolio-website-build-brief.md) and [`Suraj_Ghadage_Resume.pdf`](assets/Suraj_Ghadage_Resume.pdf).

---

## 🌟 Live Demo & Preview
- **Local:** Open `index.html` in any modern web browser or start a static server.
- **GitHub Pages:** `https://<username>.github.io/<repo-name>/`

---

## 🛠️ Tech Stack & Architecture

| Layer | Technology | Purpose |
|---|---|---|
| **Markup** | HTML5 (Semantic) | Accessible, SEO-optimized, zero build dependencies |
| **Styling** | Modular CSS3 | Custom properties design system, Grid & Flexbox, dark theme |
| **Behavior** | Vanilla JavaScript (ES6+) | Sticky nav, scroll spy, smooth scroll, form validation, copy-to-clipboard |
| **Typography** | Google Fonts | `Space Grotesk` (Headings) + `Inter` (Body copy) |
| **Icons** | Font Awesome 6 CDN | Crisp vector icons for skills, contact, and navigation |
| **Assets** | Custom Vector SVGs | Monogram avatar, favicon, and bespoke project visual diagrams |
| **Form Handling** | Formspree API | Asynchronous contact form submissions with seamless `mailto:` fallback |

---

## 📂 Project Structure

```
portfolio-website/
├── index.html                   # Main single-page semantic HTML structure
├── css/
│   └── styles.css               # Design system, CSS variables, responsive breakpoints
├── js/
│   └── script.js                # Mobile nav, IntersectionObserver, scroll spy, toast
├── assets/
│   ├── Suraj_Ghadage_Resume.pdf # Source resume PDF for one-click recruiter download
│   ├── icons/
│   │   └── favicon.svg          # SG monogram SVG favicon
│   └── images/
│       ├── suraj-monogram.svg   # High-resolution circular SVG avatar with tech nodes
│       ├── cyber-crime-analytics.svg     # Dashboard visual for Cyber Crime project
│       ├── statistical-crime-trend.svg   # Regression chart visual for Crime Modeler
│       └── hospital-billing-system.svg   # Architecture diagram for Hospital System
├── portfolio-website-build-brief.md      # Specification and content guidelines
└── README.md                    # Project documentation
```

---

## 🎯 Sections & Content Fidelity

Every fact, technical skill, and experience bullet is faithfully derived from `Suraj_Ghadage_Resume.pdf`:

1. **Sticky Header & Nav:** Brand monogram, quick jump navigation, resume download button, and mobile hamburger drawer.
2. **Hero / Landing:** Prominent name typography, dynamic tagline, internship badge, Class of 2027 indicator, and CTA buttons.
3. **About Me:** Verbatim executive summary, academic timeline at Willingdon College (Shivaji University), and core competencies.
4. **Technical Skills:** 5 distinct resume categories:
   - *Programming Languages* (Python, Java, C#, C++, SQL, HTML5, CSS3, JavaScript)
   - *Analytics & BI Tools* (Power BI, DAX, Advanced Excel, Power Query, Pivot Tables, VLOOKUP, EDA)
   - *Libraries & Frameworks* (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)
   - *Database Systems* (MySQL, RDBMS, SQL Query Optimization)
   - *Core Competencies* (Statistical Analysis, Data Visualization, OOP, Data Structures)
5. **Professional Experience:** Softspara Software & Data Analyst Intern with all 4 responsibility bullets.
6. **Key Projects:**
   - *Cyber Crime Analytics System* (EDA pipeline, Power BI dashboards, threat models)
   - *Statistical Crime Trend & Pattern Modeler* (Longitudinal trend regression, hypothesis testing)
   - *Hospital Billing & Record Management System* (Console CRUD, modular OOP, persistent file I/O)
7. **Education:** Bachelor of Computer Science (BCS) — Willingdon College, Sangli (Shivaji University, Kolhapur) — Expected 2027.
8. **Contact:** Interactive form, one-click copy buttons for email (`surajghadage1206@gmail.com`) and phone (`+91 9456160255`), social links, and resume download.
9. **Footer:** Quick links, social icons, copyright notice, and smooth Back-to-Top trigger.

---

## 🚀 How to Run Locally

### Option 1: Direct File
Simply double-click `index.html` in your file explorer to open it in Chrome, Edge, Safari, or Firefox.

### Option 2: Python HTTP Server
```bash
python -m http.server 8000
```
Then navigate to `http://localhost:8000` in your web browser.

### Option 3: VS Code Live Server
Right click `index.html` and select **"Open with Live Server"**.

---

## 🌐 Deployment to GitHub Pages

1. Initialize git (if not already done):
   ```bash
   git init
   git add .
   git commit -m "feat: complete portfolio website build for Suraj Ghadage"
   ```
2. Push to GitHub:
   ```bash
   git remote add origin https://github.com/<username>/portfolio-website.git
   git branch -M main
   git push -u origin main
   ```
3. Enable GitHub Pages:
   - Go to **Settings > Pages** on your GitHub repository.
   - Set Source to `Deploy from a branch` -> `main` / `root` -> **Save**.
   - Your live website will be published in seconds!

---

## 📄 License & Ownership
© 2026 Suraj Dattatray Ghadage. All rights reserved.
"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(README_MD)

print("README.md written successfully!")
print("ALL BUILD FILES GENERATED WITH 100% COMPLETION!")

