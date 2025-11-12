<script module>
// module-level code (if needed)
</script>

<script lang="ts">
	let { children } = $props();
</script>


<div class="page-container">
	<div class="content-wrapper">
		{@render children()}
	</div>
</div>

<style>
	:global(html), :global(body) {
		margin: 0;
		padding: 0;
		height: 100%;
	}

	.page-container {
		width: 100%;
		min-height: 100vh;
		display: flex;
		justify-content: center;
	}

	.content-wrapper {
		width: 100%;
		max-width: 800px; /* Adjust this value to control the width of the image */
		margin: 0 auto;
		background: white;
	}


</style>
