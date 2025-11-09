import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://svelte.dev/docs/kit/integrations
	// for more information about preprocessors
	preprocess: vitePreprocess(),

		kit: {
			// Using static adapter for static site deployment (e.g., GitHub Pages)
			adapter: adapter(),
			paths: {
				base: '/hma-hendriksen-dissertatie-website'
			}
		}
};

export default config;
