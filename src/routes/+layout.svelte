
<script lang="ts">
	let { children } = $props();
</script>

<div class="background-wrapper">
	{@render children()}
</div>

<style>
	:global(html), :global(body) {
		margin: 0;
		padding: 0;
		height: 100%;
	}

	.background-wrapper {
		min-height: 100vh;
		background-image: url('/background.jpg');
		background-size: cover;
		background-position: center;
		background-repeat: no-repeat;
	}
</style>
