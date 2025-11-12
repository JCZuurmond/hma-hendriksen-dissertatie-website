<script>
  import { browser } from '$app/environment';
</script>

<main>
  <div class="header-background">
    <h1>Improving information provision in the memory clinic</h1>
    <h2>with a focus on Subjective Cognitive Decline</h2>
  </div>
  <section class="about-section">
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

  <section class="author-section">
    <div class="author-content">
      <div class="author-image">
        <img src="/hma-hendriksen-dissertatie-website/Heleen.jpg" alt="Heleen" />
        <div class="author-image-note">Foto gemaakt door Hylke Greidanus Photography.</div>
      </div>
      <div class="author-text">
        <h3>Wie is Heleen?</h3>
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
</main>

<style>
  main {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    min-height: 60vh;
    text-align: left;
    padding: 6rem 2rem 2rem 2rem;
  }
  .header-background {
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
    padding: 3.5rem 2.5rem 3.5rem 2.5rem;
    background-image: url('/hma-hendriksen-dissertatie-website/background.jpg');
    background-size: cover;
    background-position: center top;
    background-repeat: no-repeat;
    box-sizing: border-box;
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
      padding: 2rem 0.5rem 2rem 0.5rem;
    }
    h1 {
      font-size: 2rem;
    }
    h2 {
      font-size: 1.25rem;
    }
  }
    .about-section {
      width: 100%;
      max-width: 800px;
      margin: 2rem auto 0 auto;
      padding: 2.5rem 2rem;
      background-color: rgb(219, 171, 194); /* Suggested color */
      border-radius: 1rem;
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
  .author-section {
    width: 100%;
    max-width: 800px;
    margin: 2rem auto 0 auto;
    padding: 2.5rem 2rem;
    background-color: rgb(166, 216, 209); /* Second suggested color */
    border-radius: 1rem;
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
</style>
