<script>

	export let name;
	
	
	let chromeVersion = '';
	let nodeVersion = '';
	let electronVersion = '';
	
	
	let f_result = '';
    let fruits = '';

	import { onMount } from 'svelte';
	onMount( async () => {  console.log("Checking APIs...");
		if (window.versions) {
			chromeVersion   = window.versions.chrome();
			nodeVersion     = window.versions.node();
			electronVersion = window.versions.electron();
		}
		f_result = await window.external_addons.f();
        fruits  = await window.external_addons.g('Apple', 'Banana');
	});

	

</script>


<main>
	<h1>Hello from {f_result}</h1>
	<p>function g: {fruits}</p>
	<p>
		This app is using Chrome ({chromeVersion}), Node.js ({nodeVersion}), and Electron ({electronVersion}).
	</p>
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