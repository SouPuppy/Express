<script>
    import TopBar from "./components/TopBar.svelte";
	import Demo from "./pages/demo.svelte";
</script>


<main>
	<TopBar/>
	<div class="TextArea">
		<Demo/>
	</div>
</main>

<style>
	.TextArea {
		height: 100%;
		display: flex;
        flex-direction: row;
        flex-grow: 1; 	/* Ensure TextArea takes up remaining space */
        overflow: auto; /* Optional: scroll if content overflows */
	}
</style>