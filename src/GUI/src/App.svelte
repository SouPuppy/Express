<script>
	export let name;

	let result1 = 0;
	let result2 = 0;
	let errmsg = "";

	import { onMount } from 'svelte';
	onMount(() => {
		if (window.myAPI) {
			result1 = window.myAPI.mytest();
			result2 = window.myAPI.youtest('aaa', 'bbb');
		} else {
			errmsg = "No myAPI in window";
		}
	});

</script>

<main>
	<h1>Hello {name}!</h1>
	
	<p>Result 1: {result1}</p>
	<p>Result 2: {result2}</p>
	<p>Error: {errmsg}</p>


    We are using Node.js <span id="node-version"></span>,
    Chromium <span id="chrome-version"></span>,
    and Electron <span id="electron-version"></span>.
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>