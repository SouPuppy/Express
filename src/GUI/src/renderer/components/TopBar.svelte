<script>
    function handleMinimize() {
        window.windowControls.minimize();
    }
    function handleMaximize() {
        window.windowControls.maximize();
    }
    function handleClose() {
        window.windowControls.close();
    }
</script>

<main>
    <div class="topBar">
        <div class="titleBar">
            <div class="title">Shitty TopBar</div>
        </div>
        <div class="titleBarBtns">
            <button id="minimizeBtn" class="topBtn minimizeBtn" on:click={handleMinimize}></button>
            <button id="maximizeBtn" class="topBtn maximizeBtn" on:click={handleMaximize}></button>
            <button id="closeBtn"    class="topBtn closeBtn"    on:click={handleClose}></button>
        </div>
    </div>
</main>

<style>
    .topBar {
        display: flex;
        flex-direction: row;
        width: 100%;
        height: 35px;
        background-color: #1B1D23;
        -webkit-user-select: none;
        user-select: none;
    }

    .topBar > .titleBar {
        display: flex;
        flex-direction: row;
        align-items: center;
        width: 100%;
    }
    .titleBar > .title {

		font-size: 10pt;
		color: #949AA7;
        margin-left: 10px;
        width: 100%;
        line-height: 30px;
        margin-top: 2.5px;
        padding-bottom: 2.5px;
        -webkit-app-region: drag;
    }
    .topBar > .titleBarBtns {
        display: flex;
        flex-direction: row;
        width: 150px;
        height: 35px;
    }
    .titleBarBtns > .topBtn {
        width: 50px;
        height: 35px;
        border: none;
        outline: none;
        background-color: transparent;
        background-repeat: no-repeat;
        background-position: center;
        transition: 0.2s;
        font-family: 'Segoe Fluent Icons', Tahoma, Geneva, Verdana, sans-serif;
        color: #d2d2d2;
    }
    .titleBarBtns > .topBtn:hover {
        background-color: #272C36
    }
    .titleBarBtns > .topBtn:active {
        background-color: #464d54
    }
    .titleBarBtns > .closeBtn:hover {
        background-color: #de2339;
    }
    .titleBarBtns > .closeBtn:active {
        background-color: #9e1a29;
    }
</style>