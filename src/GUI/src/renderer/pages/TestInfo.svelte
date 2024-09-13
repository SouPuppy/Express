<script>
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
	<p>function g: {fruits}</p>
	<p>
		This app is using Chrome ({chromeVersion}), Node.js ({nodeVersion}), and Electron ({electronVersion}).
	</p>
</main>
<style>
    p {
        color: rgb(210, 210, 210);
    }
</style>
