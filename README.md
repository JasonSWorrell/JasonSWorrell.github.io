# JasonSWorrell.github.io<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jason S. Worrell | Resume</title>
    <style>
        /* Color Palette & Variables */
        :root {
            --bg-main: #0d1117;
            --bg-card: #161b22;
            --text-main: #c9d1d9;
            --text-muted: #8b949e;
            --accent-color: #58a6ff;
            --border-color: #30363d;
            --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            --font-mono: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
        }

        body {
            background-color: var(--bg-main);
            color: var(--text-main);
            font-family: var(--font-sans);
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-image: radial-gradient(#30363d 1px, transparent 1px);
            background-size: 30px 30px;
        }

        .container {
            max-width: 900px;
            margin: 40px auto;
            padding: 40px;
            background-color: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.5);
        }

        /* Header Section */
        header {
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 20px;
            margin-bottom: 30px;
        }

        h1 {
            font-size: 2.5em;
            margin: 0 0 5px 0;
            color: #ffffff;
            letter-spacing: -0.5px;
        }

        .subtitle {
            font-size: 1.2em;
            color: var(--accent-color);
            margin: 0 0 15px 0;
            font-family: var(--font-mono);
        }

        .contact-info {
            display: flex;
            gap: 20px;
            font-size: 0.9em;
            color: var(--text-muted);
        }

        .contact-info a {
            color: var(--text-muted);
            text-decoration: none;
            transition: color 0.2s;
        }

        .contact-info a:hover {
            color: var(--accent-color);
        }

        /* Section Styling */
        section {
            margin-bottom: 35px;
        }

        h2 {
            font-size: 1.4em;
            color: #ffffff;
            text-transform: uppercase;
            letter-spacing: 1px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 8px;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
        }

        h2::before {
            content: ">>";
            color: var(--accent-color);
            margin-right: 10px;
            font-family: var(--font-mono);
            font-size: 0.9em;
        }

        /* Experience & Projects Items */
        .item {
            margin-bottom: 25px;
        }

        .item-header {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            margin-bottom: 5px;
        }

        .item-title {
            font-weight: 600;
            font-size: 1.1em;
            color: #ffffff;
        }

        .item-date {
            font-family: var(--font-mono);
            font-size: 0.85em;
            color: var(--text-muted);
        }

        .item-subtitle {
            font-style: italic;
            color: var(--accent-color);
            margin-bottom: 10px;
        }

        .item-details {
            margin: 0;
            padding-left: 20px;
            color: var(--text-main);
        }

        .item-details li {
            margin-bottom: 8px;
        }

        /* Skills Grid */
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }

        .skill-category {
            background: rgba(48, 54, 61, 0.3);
            padding: 15px;
            border-radius: 6px;
            border: 1px solid var(--border-color);
        }

        .skill-category strong {
            display: block;
            margin-bottom: 8px;
            color: var(--accent-color);
            font-family: var(--font-mono);
            font-size: 0.9em;
        }

        @media (max-width: 600px) {
            .container { margin: 10px; padding: 20px; }
            .item-header { flex-direction: column; }
            .contact-info { flex-direction: column; gap: 5px; }
        }
    </style>
</head>
<body>

    <div class="container">
        <header>
            <h1>Jason S. Worrell</h1>
            <div class="subtitle">Senior Technical Leader | Aerospace Systems & AI Integration</div>
            <div class="contact-info">
                <span>📍 Southern California</span>
                <a href="mailto:your.email@example.com">✉️ your.email@example.com</a>
                <a href="https://linkedin.com/in/yourprofile">🔗 LinkedIn</a>
                <a href="https://github.com/yourusername">💻 GitHub</a>
            </div>
        </header>

        <section>
            <h2>Summary</h2>
            <p>Results-driven technical leader with 24 years of experience managing complex aerospace maintenance operations and training programs. Transitioning into defense technology with specialized expertise in integrating autonomous systems, Vision-Language-Action (VLA) models, and UAV simulation frameworks. Proven track record of scaling high-stakes technical projects and leading cross-functional teams in high-tempo environments.</p>
        </section>

        <section>
            <h2>Technical Skills</h2>
            <div class="skills-grid">
                <div class="skill-category">
                    <strong>Software & AI</strong>
                    Python, Rust, VLA Model Workflows, Data Serialization
                </div>
                <div class="skill-category">
                    <strong>Autonomous Systems</strong>
                    PX4-Autopilot, ProjectAirSim, Pixhawk Architecture
                </div>
                <div class="skill-category">
                    <strong>Aerospace Leadership</strong>
                    Maintenance Systems (2A574), Operational Readiness, Technical Training
                </div>
            </div>
        </section>

        <section>
            <h2>Engineering Projects</h2>
            <div class="item">
                <div class="item-header">
                    <span class="item-title">Agentic UAV Simulation Framework</span>
                    <span class="item-date">2026 – Present</span>
                </div>
                <div class="item-subtitle">Lead Developer</div>
                <ul class="item-details">
                    <li>Architected an advanced simulation environment utilizing PX4-Autopilot and ProjectAirSim to test agentic drone behaviors.</li>
                    <li>Integrated hardware-in-the-loop logic using Pixhawk flight controllers to validate AI decision-making.</li>
                    <li>Developed custom Python and Rust scripts to process telemetry data and bridge Vision-Language-Action models with flight controls.</li>
                </ul>
            </div>
        </section>

        <section>
            <h2>Professional Experience</h2>
            <div class="item">
                <div class="item-header">
                    <span class="item-title">United States Air Force</span>
                    <span class="item-date">2002 – Present</span>
                </div>
                <div class="item-subtitle">Senior Maintenance Leader (E7) & Training Director</div>
                <ul class="item-details">
                    <li>Directed comprehensive maintenance, inspection, and repair operations for advanced multi-million dollar aircraft systems.</li>
                    <li>Spearheaded technical training programs, ensuring 100% operational readiness and compliance with stringent aerospace standards.</li>
                    <li>Optimized complex logistics and data tracking across multiple deployment theaters, translating operational requirements into actionable technical solutions.</li>
                </ul>
            </div>
        </section>

        <section>
            <h2>Education & Clearances</h2>
            <div class="item">
                <div class="item-header">
                    <span class="item-title">Security Clearance</span>
                </div>
                <ul class="item-details" style="margin-top: 10px;">
                    <li>Active [Insert Level] Security Clearance</li>
                </ul>
            </div>
            <div class="item">
                <div class="item-header">
                    <span class="item-title">[Degree Name or Relevant Certification]</span>
                    <span class="item-date">[Year]</span>
                </div>
                <div class="item-subtitle">[Institution Name]</div>
            </div>
        </section>
    </div>

</body>
</html>
