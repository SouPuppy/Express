import App from './App.svelte';

const app = new App({
	target: document.body,
	props: {
		word: 'Hello'
	}
});

export default app;