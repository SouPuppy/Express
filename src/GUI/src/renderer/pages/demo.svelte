<script>
    import CodeLine from "../components/Codeline.svelte";

    let lines = [
        {content: "111", altitude: 1},
        {content: `
                int ret=
                <math xmlns="http://www.w3.org/1998/Math/MathML">
                    <mfrac>
                        <mrow>
                            <mi>a</mi>
                            <mo>+</mo>
                            <mi>b</mi>
                        </mrow>
                        <mrow>
                            <mi>c</mi>
                            <mo>-</mo>
                            <mi>d</mi>
                        </mrow>
                    </mfrac>
                </math>
            `, altitude: 2},
        {content: "11311", altitude: 1},
        {content: "412cfsd ", altitude: 1},
        {content: "11aasd1", altitude: 1},
    ];

</script>

<main>
    <div class="code-container">
        {#each lines as line, index}
            <CodeLine start_index={index + 1} {...line} />
        {/each}
    </div>
</main>

<style>
    main {
        height: 100%;
        width: 100%;
        position: relative;
    }

    .code-container {
        max-height: calc(100vh - 35px);
        overflow-y: hidden;
        white-space: nowrap;
    }

    main:hover .code-container {
        overflow-y: auto;
    }

    /* Hide scrollbar */
    .code-container::-webkit-scrollbar {
        width: 16px; /* Width of the scrollbar */
    }

    /* Style the scrollbar track (part that the thumb moves along) */
    .code-container::-webkit-scrollbar-track {
        background: transparent; /* Transparent background */
        background-color: #1e1e1e;
    }

    /* Style the scrollbar thumb (the draggable part) */
    .code-container::-webkit-scrollbar-thumb {
        background: rgba(66, 66, 66, 0.3); /* Semi-transparent thumb */
    }

    /* Optional: Add hover effect for the thumb */
    .code-container::-webkit-scrollbar-thumb:hover {
        background: rgba(66, 66, 66, 0.7); /* Darker on hover */
    }

</style>
