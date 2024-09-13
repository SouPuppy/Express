<script>
    import Gutter from "./Gutter.svelte";
    export let start_index;
    export let content = "";
    export let altitude = 1;
    let line_hight = 14;
</script>

<main style="height: {altitude * (line_hight + 8)}px;">
    <Gutter Linenumber = {start_index}/>
    <div class="content" 
        style="font-size: {4 + 8 * altitude}px;"
    >
        {@html content}
    </div>
</main>

<style>
    main {
        font-family: monospace;
        font-size: 14px;
        color: rgb(210, 210, 210);
        background-color: #1e1e1e;
        display: flex;
        align-items: stretch;
    }
    .content {
        margin-left: 10px;
        display: flex;
        /* align-items: center; */
        margin-top: 3px;
    }
</style>
