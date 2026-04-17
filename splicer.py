import sys

html_insert = """    <!-- Services Redesign -->
    <section class="services container" id="services">
        <div class="services-top reveal">
            <div>
                <span class="section-label">02 &middot; Services</span>
                <h2 class="services-title font-tenor">Full-spectrum growth,<br>no compromise.</h2>
            </div>
            <div class="services-desc font-cormorant">
                We don't do fragments.<br>Every service connects.
            </div>
        </div>
        <div class="services-hr reveal"></div>

        <div class="services-split reveal">
            <div class="services-list" id="services-list">
                <!-- Items -->
                <div class="service-row active" data-index="0">
                    <div class="service-row-indicator"></div>
                    <span class="service-row-num">01</span>
                    <span class="service-row-name">Brand Strategy</span>
                    <svg class="service-row-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </div>
                <div class="service-row" data-index="1">
                    <div class="service-row-indicator"></div>
                    <span class="service-row-num">02</span>
                    <span class="service-row-name">Performance Marketing</span>
                    <svg class="service-row-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </div>
                <div class="service-row" data-index="2">
                    <div class="service-row-indicator"></div>
                    <span class="service-row-num">03</span>
                    <span class="service-row-name">Creative & Design</span>
                    <svg class="service-row-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </div>
                <div class="service-row" data-index="3">
                    <div class="service-row-indicator"></div>
                    <span class="service-row-num">04</span>
                    <span class="service-row-name">SEO & Content</span>
                    <svg class="service-row-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </div>
                <div class="service-row" data-index="4">
                    <div class="service-row-indicator"></div>
                    <span class="service-row-num">05</span>
                    <span class="service-row-name">Social Media</span>
                    <svg class="service-row-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </div>
                <div class="service-row" data-index="5">
                    <div class="service-row-indicator"></div>
                    <span class="service-row-num">06</span>
                    <span class="service-row-name">Web & Landing Pages</span>
                    <svg class="service-row-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </div>
            </div>

            <div class="services-panel">
                <div class="service-glass" id="service-glass-card">
                    <!-- Panels inserted by JS or pre-rendered. Let's pre-render them and hide all but first -->
                    <div class="service-panel-content active" data-content="0">
                        <div class="service-icon-wrap">
                            <div class="icon-brand"><div class="icon-brand-inner"></div></div>
                            <span class="service-panel-bg-num">01</span>
                        </div>
                        <h3 class="service-panel-name">Brand Strategy</h3>
                        <p class="service-panel-desc">We define your position, voice, and visual identity with precision. Before the world assigns you a meaning, we give you one that lasts.</p>
                        <div class="service-pills">
                            <span class="service-pill">Positioning</span>
                            <span class="service-pill">Visual Identity</span>
                            <span class="service-pill">Brand Voice</span>
                        </div>
                        <div class="service-timeline">Typical timeline: 3–4 weeks</div>
                    </div>

                    <div class="service-panel-content" data-content="1">
                        <div class="service-icon-wrap">
                            <div class="icon-perf">
                                <div class="perf-bar"></div><div class="perf-bar"></div><div class="perf-bar"></div><div class="perf-bar"></div><div class="perf-bar"></div>
                            </div>
                            <span class="service-panel-bg-num">02</span>
                        </div>
                        <h3 class="service-panel-name">Performance Marketing</h3>
                        <p class="service-panel-desc">ROI isn't a hope — it's a baseline. We engineer campaigns where every dollar is tracked, tested, and scaled with intent.</p>
                        <div class="service-pills">
                            <span class="service-pill">Google Ads</span>
                            <span class="service-pill">Meta Ads</span>
                            <span class="service-pill">Retargeting</span>
                            <span class="service-pill">Analytics</span>
                        </div>
                        <div class="service-timeline">Typical timeline: Ongoing / Sprint-based</div>
                    </div>

                    <div class="service-panel-content" data-content="2">
                        <div class="service-icon-wrap">
                            <div class="icon-creative"></div>
                            <span class="service-panel-bg-num">03</span>
                        </div>
                        <h3 class="service-panel-name">Creative & Design</h3>
                        <p class="service-panel-desc">Visual systems that command attention before a single word is read. We design for emotion first, conversion second.</p>
                        <div class="service-pills">
                            <span class="service-pill">Art Direction</span>
                            <span class="service-pill">UI/UX</span>
                            <span class="service-pill">Motion</span>
                            <span class="service-pill">Photography</span>
                        </div>
                        <div class="service-timeline">Typical timeline: 2–6 weeks</div>
                    </div>

                    <div class="service-panel-content" data-content="3">
                        <div class="service-icon-wrap">
                            <div class="icon-seo"></div>
                            <span class="service-panel-bg-num">04</span>
                        </div>
                        <h3 class="service-panel-name">SEO & Content</h3>
                        <p class="service-panel-desc">Organic traffic that compounds. Content that ranks, educates, and converts — built around search intent and brand authority.</p>
                        <div class="service-pills">
                            <span class="service-pill">Technical SEO</span>
                            <span class="service-pill">Content Strategy</span>
                            <span class="service-pill">Link Building</span>
                            <span class="service-pill">Keyword Research</span>
                        </div>
                        <div class="service-timeline">Typical timeline: 3–6 months to scale</div>
                    </div>

                    <div class="service-panel-content" data-content="4">
                        <div class="service-icon-wrap">
                            <div class="icon-social"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                            <span class="service-panel-bg-num">05</span>
                        </div>
                        <h3 class="service-panel-name">Social Media</h3>
                        <p class="service-panel-desc">We build communities rooted in culture, not just content. Consistent, on-brand, and strategically timed to grow what matters.</p>
                        <div class="service-pills">
                            <span class="service-pill">Content Calendar</span>
                            <span class="service-pill">Community Management</span>
                            <span class="service-pill">Influencer</span>
                            <span class="service-pill">Analytics</span>
                        </div>
                        <div class="service-timeline">Typical timeline: Ongoing monthly</div>
                    </div>

                    <div class="service-panel-content" data-content="5">
                        <div class="service-icon-wrap">
                            <div class="icon-web"></div>
                            <span class="service-panel-bg-num">06</span>
                        </div>
                        <h3 class="service-panel-name">Web & Landing Pages</h3>
                        <p class="service-panel-desc">Conversion-first digital experiences. Every layout decision, every CTA placement, every pixel — built to turn visitors into clients.</p>
                        <div class="service-pills">
                            <span class="service-pill">Landing Pages</span>
                            <span class="service-pill">Full Websites</span>
                            <span class="service-pill">CRO</span>
                            <span class="service-pill">Webflow / HTML</span>
                        </div>
                        <div class="service-timeline">Typical timeline: 2–5 weeks</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="services-cta reveal">
            All services are built around your goals — not our packages.
            <a href="#contact">Start a Project &rarr;</a>
        </div>
    </section>

    <!-- Work Redesign -->
    <section class="work" id="work">
        <div class="container relative z-10">
            <div class="work-head reveal">
                <div>
                    <span class="section-label">03 &middot; Selected Work</span>
                    <h2 class="services-title font-tenor">Results that<br>redefine the<br>benchmark.</h2>
                </div>
                <div class="work-counter">
                    <span class="work-counter-num" id="work-count">01</span> / 06
                </div>
            </div>

            <div class="deck-wrapper reveal">
                <!-- Card 1 -->
                <div class="deck-card dc-1 deck-active" data-slide="0">
                    <div class="deck-shape ds-1"></div><div class="deck-shape ds-2"></div>
                    <div class="dc-overlay">
                        <div class="dc-top">
                            <span class="dc-tag">F&B &middot; Brand Strategy</span>
                            <span class="dc-year">2024</span>
                        </div>
                        <div class="dc-bottom">
                            <h3 class="dc-title">NovaBrew</h3>
                            <div class="dc-metric">+340% ROAS in 60 days</div>
                            <p class="dc-desc">Full-funnel paid media + creative direction.</p>
                            <a href="#" class="dc-link">View Case Study &rarr;</a>
                        </div>
                    </div>
                </div>
                <!-- Card 2 -->
                <div class="deck-card dc-2 deck-behind-1" data-slide="1">
                    <div class="deck-shape ds-1"></div>
                    <div class="dc-overlay">
                        <div class="dc-top"><span class="dc-tag">Real Estate &middot; Performance</span><span class="dc-year">2024</span></div>
                        <div class="dc-bottom">
                            <h3 class="dc-title">UrbanShift</h3>
                            <div class="dc-metric">+210% Qualified Leads</div>
                            <p class="dc-desc">Google & Meta demand gen for luxury properties.</p>
                            <a href="#" class="dc-link">View Case Study &rarr;</a>
                        </div>
                    </div>
                </div>
                <!-- Card 3 -->
                <div class="deck-card dc-3 deck-behind-2" data-slide="2">
                    <div class="deck-shape ds-1"></div><div class="deck-shape ds-2"></div>
                    <div class="dc-overlay">
                        <div class="dc-top"><span class="dc-tag">Healthcare &middot; SEO + Content</span><span class="dc-year">2023</span></div>
                        <div class="dc-bottom">
                            <h3 class="dc-title">Zelta Health</h3>
                            <div class="dc-metric">2.4&times; Organic Traffic in 4 months</div>
                            <p class="dc-desc">Content strategy and technical SEO overhaul.</p>
                            <a href="#" class="dc-link">View Case Study &rarr;</a>
                        </div>
                    </div>
                </div>
                <!-- Card 4 -->
                <div class="deck-card dc-4 deck-behind-3" data-slide="3">
                    <div class="deck-shape ds-1"></div><div class="deck-shape ds-2"></div><div class="deck-shape ds-3"></div>
                    <div class="dc-overlay">
                        <div class="dc-top"><span class="dc-tag">Fashion &middot; Social + Creative</span><span class="dc-year">2024</span></div>
                        <div class="dc-bottom">
                            <h3 class="dc-title">Lumara</h3>
                            <div class="dc-metric">1.8M Impressions in launch week</div>
                            <p class="dc-desc">Social launch strategy and UGC creative system.</p>
                            <a href="#" class="dc-link">View Case Study &rarr;</a>
                        </div>
                    </div>
                </div>
                <!-- Card 5 -->
                <div class="deck-card dc-5 deck-back" data-slide="4">
                    <div class="deck-shape ds-1"></div>
                    <div class="dc-overlay">
                        <div class="dc-top"><span class="dc-tag">D2C &middot; Full-Service</span><span class="dc-year">2023</span></div>
                        <div class="dc-bottom">
                            <h3 class="dc-title">Craft & Co</h3>
                            <div class="dc-metric">$1.2M Revenue in Q1</div>
                            <p class="dc-desc">Brand, performance, and web—built from scratch.</p>
                            <a href="#" class="dc-link">View Case Study &rarr;</a>
                        </div>
                    </div>
                </div>
                <!-- Card 6 -->
                <div class="deck-card dc-6 deck-back" data-slide="5">
                    <div class="deck-shape ds-1"></div><div class="deck-shape ds-2"></div><div class="deck-shape ds-3"></div>
                    <div class="dc-overlay">
                        <div class="dc-top"><span class="dc-tag">SaaS &middot; Brand + Web</span><span class="dc-year">2024</span></div>
                        <div class="dc-bottom">
                            <h3 class="dc-title">Nova Labs</h3>
                            <div class="dc-metric">3&times; Trial-to-Paid Conversion</div>
                            <p class="dc-desc">Repositioning, new site, and onboarding flow.</p>
                            <a href="#" class="dc-link">View Case Study &rarr;</a>
                        </div>
                    </div>
                </div>
            </div>

            <div class="deck-controls reveal">
                <div class="deck-dots">
                    <div class="deck-dot active" data-slide="0"></div><div class="deck-dot" data-slide="1"></div>
                    <div class="deck-dot" data-slide="2"></div><div class="deck-dot" data-slide="3"></div>
                    <div class="deck-dot" data-slide="4"></div><div class="deck-dot" data-slide="5"></div>
                </div>
                <div class="deck-progress-track">
                    <div class="deck-progress-fill" id="deck-progress"></div>
                </div>
            </div>

            <p class="deck-hint reveal">Click the card or use &larr; &rarr; keys to navigate</p>

            <div class="work-all reveal">
                <a href="#" class="work-all-link font-tenor">See all case studies</a>
            </div>
        </div>
    </section>
"""

with open(r'd:\New folder\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if "<!-- Services -->" in line:
        start_idx = i
    if "<!-- Process -->" in line and start_idx != -1:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    with open(r'd:\New folder\index.html', 'w', encoding='utf-8') as f:
        f.writelines(lines[:start_idx])
        f.write(html_insert)
        f.writelines(lines[end_idx:])
    print("Success")
else:
    print("Could not find blocks")
