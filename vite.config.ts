
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	base: '/hma-hendriksen-dissertatie-website/',
	plugins: [sveltekit()],
	assetsInclude: ['**/*.jp2']
});
