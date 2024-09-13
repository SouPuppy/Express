<script>
    export let Linenumber;
</script>

<main>
    <div class="line-number">{Linenumber}</div>
</main>

<style>
    main {
        background-color: #2d2d2d;
        width: 45px;
        display: flex;
        /* align-items: center; */
        justify-content: flex-end;
    }

    .line-number {
        color: #888;
        margin-right: 5px;
        margin-top: 3px
    }
</style>
