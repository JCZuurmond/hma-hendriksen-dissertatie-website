<script>
  import { browser } from '$app/environment';
</script>

<header class="site-header">
  <nav class="nav-bar">
  <button on:click={() => window.scrollTo({top: 0, behavior: 'smooth'})}>Top</button>
  <button on:click={() => document.getElementById('about-section').scrollIntoView({behavior: 'smooth'})}>Over</button>
  <button on:click={() => window.open('https://research.vu.nl/en/publications/improving-information-provision-in-the-memory-clinic-with-a-focus/', '_blank', 'noopener,noreferrer')}>Dissertatie</button>
  </nav>
</header>

<main>
  <section id="header-section" class="header-section">
    <div class="header-background">
    </div>
  </section>
  
  <section id="author-section" class="author-section">
    <div class="author-content">
      <div class="author-image">
        <img src="/hma-hendriksen-dissertatie-website/Heleen.jpg" alt="Heleen" />
        <div class="author-image-note">Foto gemaakt door Hylke Greidanus Photography.</div>
      </div>
      <div class="author-text">
        <p>
          Heleen Hendriksen richt zich in haar onderzoek op de communicatie
          tussen zorgverleners en patiënten op de geheugenpoli. Op basis van
          haar onderzoeksresultaten ontwikkelt ze materialen die zowel patiënten
          als zorgverleners ondersteunen in hun gesprekken. Ze doet dit bij
          Alzheimercentrum Amsterdam binnen het ABOARD-project.  
        </p>
      </div>
    </div>
  </section>

  <section id="about-section" class="about-section">
    <h3>Waar gaat dit onderzoek over</h3>
    <p>
      Het geven van goede en duidelijke informatie op de geheugenpoli is niet
      altijd makkelijk. Er zijn veel verschillende tests, soorten dementie en
      stadia van de ziekte. Vaak is de toekomst onzeker. In dit onderzoek
      beoordeelden 802 patiënten van Alzheimercentrum Amsterdam de hoeveelheid
      en het nut van de ontvangen informatie tijdens hun diagnostisch traject op
      de geheugenpoli. Ook vroegen we of patiënten meer of minder informatie
      hadden gewild, en zo ja, over welke onderwerpen. 
    </p>
  </section>

  <section class="site-footer">
    <div class="footer-content">
      <a href="mailto:contact@heleenhendriksen.nl" class="footer-link">E-mail</a>
      <span class="footer-separator">|</span>
      <a href="https://www.adappt.health/nl/informatie" class="footer-link" target="_blank" rel="noopener noreferrer">Adappt Health</a>
      <span class="footer-separator">|</span>
      <a href="https://www.alzheimer-nederland.nl/" class="footer-link" target="_blank" rel="noopener noreferrer">Alzheimer Nederland</a>
    </div>
  </section>

</main>

<style>
  .site-header {
    width: 100%;
    background: transparent;
    box-shadow: none;
    position: sticky;
    top: 0;
    z-index: 10;
  }
  .nav-bar {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 1.5rem;
    padding: 1rem 0;
    max-width: 800px;
    margin: 0 auto;
  }
  .nav-bar button {
    background: rgb(233, 194, 222);
    color: #222;
    border: none;
    border-radius: 0.5rem;
    padding: 0.5rem 1.25rem;
    font-size: 1rem;
    font-weight: 500;
    cursor: pointer;
    transition: background 0.2s;
    box-shadow: 0 2px 8px rgba(0,0,0,0.12);
  }
  .nav-bar button:hover {
    background: rgb(196, 228, 230);
    color: #111;
  }
  main {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    min-height: 60vh;
    text-align: left;
    padding: 0;
  }
  .header-background {
    width: 100%;
    padding: 35rem 23rem 35rem 23rem;
    background-image: url('/hma-hendriksen-dissertatie-website/background.png');
    background-size: cover;
    background-position: center top;
    background-repeat: no-repeat;
    box-sizing: border-box;
  }
  .header-section {
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
    /* No vertical margin between sections */
  }
  h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    color: #222;
  }
  h2 {
    font-size: 1.5rem;
    color: #444;
    font-weight: normal;
  }
  @media (max-width: 768px) {
    .header-background {
      max-width: 100%;
      padding: 2rem 0.5rem 3.5rem 0.5rem; /* Increased bottom padding for mobile */
    }
    h1 {
      font-size: 2rem;
    }
    h2 {
      font-size: 1.25rem;
    }
  }

  .author-section {
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
    padding: 2.5rem 0rem;
    background-color: rgb(233, 194, 222);
    border-radius: 0;
    box-sizing: border-box;
  }
  .author-content {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    gap: 2rem;
  }
  .author-text {
    flex: 2;
  }
  .author-text h3 {
    margin-top: 0;
    font-size: 1.4rem;
    color: #222;
  }
  .author-text p {
    color: #333;
    font-size: 1rem;
    margin-bottom: 0;
  }
  .author-image {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
  }
  .author-image img {
    max-width: 140px;
    width: 100%;
    height: auto;
    border-radius: 50%;
    object-fit: cover;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  }
  .author-image-note {
    font-size: 0.85rem;
    color: #555;
    margin-top: 0.5rem;
    text-align: center;
  }
  @media (max-width: 768px) {
    .author-content {
      flex-direction: column;
      align-items: flex-start;
      gap: 1.5rem;
    }
    .author-image {
      justify-content: flex-start;
      width: 100%;
    }
    .author-image img {
      max-width: 100px;
    }
  }

  .about-section {
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem 2rem;
    background-color: rgb(233, 194, 222);
    border-radius: 0;
    box-sizing: border-box;
  }
  .about-section h3 {
    margin-top: 0;
    font-size: 1.4rem;
    color: #222;
  }
  .about-section p {
    color: #333;
    font-size: 1rem;
    margin-bottom: 0;
  }

  .site-footer {
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
    padding: 1rem 2rem;
    background-color: rgb(196, 228, 230);
    border-radius: 0;
    box-sizing: border-box;
  }
  .footer-content {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 1.25rem;
    font-size: 1rem;
    color: #222;
    background: transparent;
  }
  .footer-link {
    color: #222;
    text-decoration: none;
    font-weight: 500;
    background: transparent;
    padding: 0.3rem 0.9rem;
    border-radius: 0.5rem;
    transition: background 0.2s;
  }
  .footer-link:hover {
    background: rgb(233, 194, 222);
    color: #111;
  }
  .footer-separator {
    color: #aaa;
    font-size: 1.1rem;
    user-select: none;
  }


  :global(body) {
    margin-bottom: 80px; /* space for footer */
    background: rgb(196, 228, 230);
    font-family: 'Myriad Pro', Arial, Helvetica, sans-serif;
  }

  .site-footer {
  }
  .footer-content {
  }
</style>