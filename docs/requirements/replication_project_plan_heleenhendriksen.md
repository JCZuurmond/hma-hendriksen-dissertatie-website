# Project Plan: Replicating heleenhendriksen.nl

## Executive Summary

This document outlines the comprehensive plan for replicating the website at https://heleenhendriksen.nl/, which is a Dutch memory clinic information portal ("Informatievoorziening op de Geheugenpoli"). The website features a modern design system with rich text editing capabilities, animation framework, and responsive design.

**Target Website:** https://heleenhendriksen.nl/
**Project Goal:** Create a fully functional, self-hosted replica with all assets and functionality
**Estimated Complexity:** Medium to High (due to interactive features and modern framework)

---

## 1. Website Analysis

### 1.1 Technology Stack
- **Frontend Framework:** Next.js (React-based)
- **Styling System:** Chakra UI with extensive CSS custom properties
- **Rich Text Editor:** ProseMirror integration
- **Typography:** Montserrat (headings, 700 weight) + Roboto (body, 400 weight)
- **Animation System:** Custom JavaScript-based animation framework with PerformanceObserver
- **Build System:** Modern CSS-in-JS approach

### 1.2 Design System
**Color Palette:**
- Primary: Teal/Aqua (`#c4e4e6`, `#acdde0`)
- Accent: Mauve/Purple (`#e9c2de`, `#96367b`)
- Neutral: Grays and whites with carefully crafted shadow system

**Responsive Breakpoints:**
- Mobile: < 30em
- Small tablet: 30em - 46em
- Tablet: 46em - 62em
- Desktop: 62em - 78em
- Large desktop: 78em - 96em
- XL desktop: > 96em

### 1.3 Key Features
1. Card-based layout system
2. Grid/gallery components
3. Rich text blocks (paragraphs, headings, lists, tables)
4. Smart layout cells
5. Animated elements on page load
6. Interactive todo lists with checkboxes
7. Drag-and-drop interfaces
8. Comment/discussion wrapper system
9. Resizable and clippable elements
10. Print-optimized styling
11. Accessibility features (focus indicators, ARIA support)

---

## 2. Project Phases

### Phase 1: Resource Discovery and Mapping

**Objective:** Identify and catalog all website resources

**Tasks:**
1. Parse the main HTML page to extract all resource references
2. Identify and catalog:
   - HTML pages (main + any sub-pages)
   - CSS files (including Next.js generated styles)
   - JavaScript files (Next.js chunks, framework files)
   - Images (PNG, JPG, SVG, WebP)
   - Fonts (Montserrat, Roboto - likely from Google Fonts)
   - Manifest files and build artifacts
   - Any API endpoints or data sources
3. Map the Next.js static file structure (`_next/static/`)
4. Identify dynamically loaded resources
5. Document external dependencies (CDNs, Google Fonts, analytics)

**Deliverables:**
- Complete resource inventory (JSON or CSV format)
- Directory structure map
- List of external dependencies

**Success Criteria:**
- 100% of visible resources identified
- External vs internal resources clearly categorized
- Dynamic loading mechanisms understood

---

### Phase 2: Resource Download and Organization

**Objective:** Download all resources and establish local directory structure

**Tasks:**
1. Create local directory structure matching original site
2. Download all static assets:
   - HTML files
   - CSS files (all chunks and bundles)
   - JavaScript files (framework, polyfills, page bundles)
   - Images and media files
   - Font files (download from Google Fonts or CDN)
3. Download Next.js build manifest files
4. Handle rate limiting and download errors
5. Verify file integrity (checksums if available)
6. Document any resources that failed to download

**Directory Structure:**
```
/
├── index.html
├── _next/
│   ├── static/
│   │   ├── [buildId]/
│   │   │   ├── _buildManifest.js
│   │   │   └── _ssgManifest.js
│   │   ├── chunks/
│   │   │   ├── framework-*.js
│   │   │   ├── main-*.js
│   │   │   ├── pages/
│   │   │   ├── polyfills-*.js
│   │   │   └── webpack-*.js
│   │   └── css/
│   │       └── *.css
├── fonts/
│   ├── montserrat-*.woff2
│   └── roboto-*.woff2
└── images/
    └── [any images used]
```

**Deliverables:**
- Complete local copy of all resources
- Download log with success/failure status
- File integrity verification report

**Success Criteria:**
- All critical resources downloaded successfully
- Directory structure properly maintained
- No broken or corrupted files

---

### Phase 3: Resource Modification and Path Rewriting

**Objective:** Update all resource references to work locally

**Tasks:**
1. **HTML Modifications:**
   - Update all CSS `<link>` tags to local paths
   - Update all JavaScript `<script>` tags to local paths
   - Replace Google Fonts URLs with local font files
   - Update image `src` attributes to local paths
   - Remove external analytics scripts (Google Analytics, etc.)
   - Update meta tags if necessary

2. **CSS Modifications:**
   - Update `@import` statements to local paths
   - Update `url()` references for fonts and images
   - Ensure CSS custom properties are preserved
   - Update any absolute URLs to relative paths

3. **JavaScript Modifications:**
   - Update module imports/requires if necessary
   - Check for hardcoded URLs in JavaScript
   - Update API endpoint references (if any)
   - Ensure chunk loading paths are correct

4. **Font Integration:**
   - Create local `@font-face` declarations
   - Replace Google Fonts with locally hosted fonts
   - Ensure font weights and styles are correct

5. **Remove External Dependencies:**
   - Remove/replace analytics scripts
   - Remove/replace any external tracking
   - Document any functionality that depends on external services

**Deliverables:**
- Modified HTML, CSS, and JavaScript files
- Local font CSS file
- Documentation of all changes made
- List of removed external dependencies

**Success Criteria:**
- No external network requests required
- All resource paths resolve correctly
- Core functionality preserved

---

### Phase 4: Testing and Validation

**Objective:** Ensure the replicated site functions correctly

**Tasks:**
1. **Visual Testing:**
   - Compare visual rendering with original site
   - Test at all responsive breakpoints
   - Verify color schemes match
   - Check typography rendering
   - Validate animations and transitions

2. **Functional Testing:**
   - Test interactive elements (if any remain functional)
   - Verify internal navigation works
   - Test print styles
   - Check keyboard navigation
   - Verify focus indicators work

3. **Technical Validation:**
   - Check browser console for errors
   - Verify all resources load (Network tab)
   - Validate HTML (W3C validator)
   - Test in multiple browsers (Chrome, Firefox, Safari, Edge)
   - Test on mobile devices

4. **Performance Testing:**
   - Measure page load times
   - Check resource sizes
   - Validate animation performance
   - Test on slower connections

5. **Accessibility Testing:**
   - Run automated accessibility checks
   - Test with screen readers
   - Verify keyboard navigation
   - Check color contrast ratios

**Deliverables:**
- Testing report with screenshots
- List of issues and discrepancies
- Browser compatibility matrix
- Accessibility audit report

**Success Criteria:**
- Visual parity with original site (>95%)
- No console errors
- All browsers render correctly
- Accessibility standards met (WCAG 2.1 AA)

---

### Phase 5: Optimization and Documentation

**Objective:** Optimize the replicated site and create comprehensive documentation

**Tasks:**
1. **Optimization:**
   - Minify CSS and JavaScript (if not already)
   - Optimize images (compress without quality loss)
   - Remove unused CSS/JS (if identifiable)
   - Implement caching headers for local server

2. **Documentation:**
   - Create setup instructions
   - Document local hosting options (python -m http.server, nginx, etc.)
   - Write troubleshooting guide
   - Document known limitations
   - Create maintenance guide for future updates

3. **Quality Assurance:**
   - Final review of all files
   - Validate against acceptance criteria
   - Perform end-to-end testing
   - Get stakeholder approval

**Deliverables:**
- Optimized website files
- Comprehensive documentation package
- Setup and deployment guide
- Maintenance and troubleshooting guide

**Success Criteria:**
- Documentation is clear and complete
- Website can be deployed by following instructions
- All known limitations are documented

---

## 3. Technical Requirements

### 3.1 Development Tools
- Web browser with DevTools (Chrome/Firefox)
- Text editor or IDE
- Local web server (Python SimpleHTTPServer, Node.js http-server, nginx, etc.)
- wget or curl for downloading resources
- Image optimization tools (optional: imagemagick, optipng)
- CSS/JS minification tools (optional)

### 3.2 Automation Script Requirements
Reference the existing workflow described in `self_hosting_static_website.md`:
1. Resource listing functionality
2. Batch download capability
3. Path rewriting engine
4. Validation and sanity checking

### 3.3 Hosting Requirements
- Static file server capability
- Support for modern HTML5/CSS3/ES6+
- MIME type configuration for all file types
- (Optional) HTTPS support

---

## 4. Risk Assessment and Mitigation

### 4.1 Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Next.js dynamic features may not work offline | High | High | Document limitations; consider rebuilding with static HTML |
| External dependencies cannot be replaced | Medium | Medium | Identify early in Phase 1; find alternatives |
| Fonts fail to load locally | Low | Medium | Test multiple font hosting approaches |
| Animation framework depends on external API | Low | High | Review JavaScript in Phase 1 |
| Missing resources due to dynamic loading | Medium | High | Use browser DevTools to capture all network requests |
| Legal/licensing issues with content | Low | High | Ensure proper authorization before replication |

### 4.2 Mitigation Strategies
- **Early Detection:** Thoroughly analyze the site in Phase 1
- **Fallback Options:** Prepare alternative approaches for critical features
- **Incremental Testing:** Test after each modification phase
- **Version Control:** Use Git to track all changes
- **Documentation:** Document all workarounds and limitations

---

## 5. Acceptance Criteria

The project will be considered complete when:

1. All visual elements match the original site (>95% accuracy)
2. The site functions without any external network requests
3. The site works in all major modern browsers
4. The site is responsive across all documented breakpoints
5. No critical JavaScript errors in browser console
6. All core functionality is preserved or documented as unavailable
7. Comprehensive documentation is provided
8. The site can be hosted using standard static file servers
9. Accessibility standards are maintained
10. All stakeholders approve the final result

---

## 6. Timeline Considerations

**Phase Duration Estimates:**
- Phase 1: Resource Discovery - 10-15% of total time
- Phase 2: Download and Organization - 15-20% of total time
- Phase 3: Modification - 35-40% of total time
- Phase 4: Testing and Validation - 20-25% of total time
- Phase 5: Optimization and Documentation - 10-15% of total time

**Note:** Timeline will vary based on website complexity and automation level.

---

## 7. Next Steps

1. Review and approve this project plan
2. Set up development environment and tools
3. Begin Phase 1: Resource Discovery
4. Schedule regular checkpoints after each phase
5. Maintain communication with stakeholders throughout

---

## 8. Appendix

### A. Key URLs and Resources
- Target Website: https://heleenhendriksen.nl/
- Related Documentation: `self_hosting_static_website.md`

### B. Contact and Responsibilities
- [To be filled in by stakeholders]

### C. Version History
- v1.0 - 2025-12-10 - Initial project plan created

---

**Document Status:** Draft for Review
**Last Updated:** 2025-12-10
**Next Review Date:** [To be scheduled]
