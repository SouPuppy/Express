<script>
    import TopBar from './components/TopBar.svelte';
	import TestInfo from './TestInfo.svelte';
</script>


<main>
	<TopBar></TopBar>
	<div class="contentArea">
		<TestInfo></TestInfo>
	</div>

</main>

<style>
	.contentArea {
		display: flex;
        flex-direction: row;
        flex-grow: 1; /* Ensure contentArea takes up remaining space */
        overflow: auto; /* Optional: scroll if content overflows */
	}
</style>