<script>
  import { browser } from '$app/environment';
</script>

<main>
  <div class="header-background">
    <h1>Improving information provision in the memory clinic</h1>
    <h2>with a focus on Subjective Cognitive Decline</h2>
  </div>
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
</style>
